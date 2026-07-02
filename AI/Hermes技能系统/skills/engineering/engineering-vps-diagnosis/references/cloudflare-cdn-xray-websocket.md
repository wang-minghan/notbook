# Cloudflare CDN + xray WebSocket 部署（GFW 限流环境）

## 适用场景

- RackNerd / 其他美国 VPS IP 段被 GFW QoS 限流（TCP 通但 SSH banner 间歇性超时）
- 换 IP 但同网段后问题依旧（整个 /24 段被限流）
- 开 HK/JP 代理时能正常 SSH，但直连不行
- 目标：**从国内直接连接** VPS 上的代理服务

## 架构

```
本地客户端（中国IP）→ Cloudflare CDN (Proxied) → nginx (443/TLS) → xray (127.0.0.1:10086/WS)
```

## 先决条件

- VPS 上已安装 x-ray + x-ui 面板（或任意 xray 管理面板）
- 服务器已安装 nginx
- 有一个域名（如 `example.com`）
- 域名已托管到 Cloudflare DNS（即 NS 指向 Cloudflare）

## 配置步骤

### Step 1: Cloudflare DNS

1. 登录 https://dash.cloudflare.com → 点域名
2. **DNS** → **Add Record**：
   - Type: `A`
   - Name: `vps`（生成 `vps.example.com`）
   - IPv4 address: VPS 真实 IP
   - ☁️ **Proxied（橙色云朵）** ← 必须
3. 点 Save

### Step 2: Cloudflare SSL

1. 左侧 **SSL/TLS** → **Overview** → 选 **Full (strict)**
2. **Origin Server** → **Create Certificate**
   - 保持默认域名
   - 有效期选 **15年**
   - 点 Create
   - **保存弹出窗口的内容：** Origin Certificate 和 Private Key

### Step 3: VPS 上保存证书

```bash
# 创建证书目录
mkdir -p /etc/nginx/certs

# 将证书保存为文件
cat > /etc/nginx/certs/origin.crt << 'EOF'
-----BEGIN CERTIFICATE-----
<粘贴Origin Certificate内容>
-----END CERTIFICATE-----
EOF

cat > /etc/nginx/certs/private.key << 'EOF'
-----BEGIN PRIVATE KEY-----
<粘贴Private Key内容>
-----END PRIVATE KEY-----
EOF

chmod 644 /etc/nginx/certs/origin.crt
chmod 600 /etc/nginx/certs/private.key
```

### Step 4: 配置 nginx 反向代理（WebSocket）

```bash
# 备份旧配置
cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak

# 创建站点配置
cat > /etc/nginx/conf.d/vps.example.com.conf << 'EOF'
server {
    listen 443 ssl http2;
    server_name vps.example.com;

    ssl_certificate /etc/nginx/certs/origin.crt;
    ssl_certificate_key /etc/nginx/certs/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers on;

    location /wsproxy {
        proxy_pass http://127.0.0.1:10086;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
    }

    # Fallback 页面（可选）
    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}

server {
    listen 80;
    server_name vps.example.com;
    return 301 https://$host$request_uri;
}
EOF

# 测试配置并重启
nginx -t && systemctl restart nginx
```

### Step 5: xray 添加 WebSocket 入站

**🚨 重要——x-ui 面板的入站配置方式：**

x-ui 面板的特殊性：
- x-ui 将入站配置存于 **sqlite3 数据库** `/etc/x-ui/x-ui.db`（或 3x-ui 是 `/etc/3x-ui/3x-ui.db`）
- x-ui **重启时会根据数据库重新生成** `config.json`（位于 `/usr/local/x-ui/bin/config.json`）
- **直接修改 config.json 会被面板覆盖！** 必须操作数据库才能持久化。
- xray 实际启动的工作目录：`/usr/local/x-ui/`，二进制文件：`bin/xray-linux-amd64`
- 面板服务文件：`/etc/systemd/system/x-ui.service`

**推荐的方法：通过 sqlite3 操作 x-ui 数据库**

```bash
python3 << 'PYEOF'
import json, uuid, sqlite3

uid = str(uuid.uuid4())
print(f'UUID: {uid}')

# 保存 UUID 到文件（方便后续查看）
with open('/root/vps_uuid.txt', 'w') as f:
    f.write(uid)

# 构造 settings / stream_settings / sniffing JSON
settings = json.dumps({
    "clients": [{
        "id": uid, "flow": "",
        "email": "user@vps", "limitIp": 0,
        "totalGB": 0, "expiryTime": 0, "enable": True
    }],
    "decryption": "none", "fallbacks": []
})

stream_settings = json.dumps({
    "network": "ws", "security": "none",
    "wsSettings": {"path": "/wsproxy", "headers": {}}
})

sniffing = json.dumps({
    "enabled": True, "destOverride": ["http", "tls"]
})

db_path = "/etc/x-ui/x-ui.db"            # x-ui
# db_path = "/etc/3x-ui/3x-ui.db"        # 3x-ui（如果用的是3x-ui）

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 先删除旧记录（防止重复）
cur.execute("DELETE FROM inbounds WHERE tag='vps-ws-inbound'")

# 插入新入站
cur.execute("""
    INSERT INTO inbounds 
    (user_id, up, down, total, remark, enable, expiry_time, port, protocol, 
     settings, stream_settings, tag, sniffing_enabled, sniffing) 
    VALUES (1, 0, 0, 0, 'VPS-CF-WS-TLS', 1, 0, 10086, 'vless', 
            ?, ?, 'vps-ws-inbound', 1, ?)
""", (settings, stream_settings, sniffing))

conn.commit()
conn.close()
print(f'Inbound added. UUID: {uid}')
PYEOF

# 重启 x-ui（从数据库重新生成 config.json → 启动 xray）
systemctl restart x-ui
sleep 4

# 验证
ss -tlnp | grep 10086 && echo "PORT 10086 OPEN" || echo "PORT 10086 NOT OPEN"
```

**方法 B — 直接修改 config.json（仅适用于纯 xray 无面板的场景）：**

如果 VPS 上用的不是 x-ui 面板而是纯 xray 或 sing-box，可直接编辑配置文件：

```bash
python3 << 'PYEOF'
import json, uuid

with open('/usr/local/etc/xray/config.json', 'r') as f:
    config = json.load(f)

uid = str(uuid.uuid4())
print(f'UUID: {uid}')

new_inbound = {
    "tag": "vps-ws-inbound",
    "port": 10086,
    "listen": "127.0.0.1",
    "protocol": "vless",
    "settings": {
        "clients": [{
            "id": uid, "flow": "",
            "email": "user@vps", "limitIp": 0,
            "totalGB": 0, "expiryTime": 0, "enable": True
        }],
        "decryption": "none", "fallbacks": []
    },
    "streamSettings": {
        "network": "ws", "security": "none",
        "wsSettings": {"path": "/wsproxy", "headers": {}}
    },
    "sniffing": {"enabled": True, "destOverride": ["http", "tls"]}
}

config['inbounds'].append(new_inbound)

with open('/usr/local/etc/xray/config.json', 'w') as f:
    json.dump(config, f, indent=2)

print('Config OK')
PYEOF

# 重启 xray
kill -HUP $(pidof xray-linux-amd64) 2>/dev/null || systemctl restart xray
sleep 3
```

**关键点：**
- 端口 10086 只监听 `127.0.0.1`（不对外暴露，由 nginx 代理外部请求）
- `security: "none"`（TLS 由 nginx 在 443 端上处理，避免 xray 双重加密）
- WebSocket 路径 `/wsproxy` 需要与 nginx 配置中的 `location` 一致
- **有 x-ui 面板 → 必须用方法 A (DB)** | **纯 xray/sing-box → 用方法 B (config.json)**

### Step 6: 验证

```bash
# 检查监听
ss -tlnp | grep -E '443|10086'

# 检查进程
ps aux | grep xray | grep -v grep

# 本地 curl 测试（从 VPS 内部）
curl -k -o /dev/null -s -w "%{http_code}" https://127.0.0.1/wsproxy
curl -k -o /dev/null -s -w "%{http_code}" https://vps.example.com/wsproxy
```

### Step 7: 客户端配置

| 参数 | 值 |
|------|-----|
| 协议 | VLESS |
| 地址 | `vps.example.com`（**域名，不是 IP**） |
| 端口 | 443 |
| UUID | (上一步生成的) |
| 传输 | WebSocket |
| 路径 | `/wsproxy` |
| TLS | 开启 |
| SNI | `vps.example.com` |
| 底层传输 | TCP |

**v2rayN 客户端示例：**
- 添加 → VLESS → 服务器地址: `vps.example.com` → 端口: `443`
- 用户ID: 粘贴 UUID
- 传输方式: `ws` → 路径: `/wsproxy`
- 底层传输安全: `tls` → 伪装域名: `vps.example.com`

## 常见问题

### Q: 客户端连上但无法上网（或特定网站打不开）
- 检查 xray 路由规则（`domainStrategy`、`geosite`）
- 确认 xray 出站 `outbounds` 包含 freedom 协议
- 检查 Cloudflare 的 Proxied 模式是否开启（橙色云朵）

### Q: 域名解析到 Cloudflare IP 但连不上
- Cloudflare DNS 未生效（等待几分钟到几小时）
- SSL/TLS 设成了 Off 或 Flexible（需要 Full strict）
- 证书未正确安装（检查 nginx -t）

### Q: 已有 sing-box REALITY 配置，会冲突吗？
不会冲突。xray + nginx WebSocket 入站和 sing-box REALITY 入站使用不同的端口和不同的进程，互不干扰。

### Q: 为什么不开 Full(strict) 会报 526 错误？
Cloudflare 需要验证源站证书。Origin CA 证书是 Cloudflare 签发的，设置 Full(strict) 后 Cloudflare 会用自签的 CA 验证源站，确保流量加密。

## 常用命令速查

```bash
# nginx 排查
nginx -t                              # 测试配置
systemctl restart nginx                # 重启
journalctl -u nginx -n 30 --no-pager  # 看日志

# x-ui 面板
/usr/local/x-ui/x-ui setting -show    # 查看面板信息
systemctl restart x-ui                 # 重启面板（xray会随面板重启）

# xray 排查
ps aux | grep xray                    # 确认进程存在
ss -tlnp | grep xray                  # 确认端口监听
# 查看 config.json 中的 inbounds
cat /usr/local/x-ui/bin/config.json | python3 -c "import sys,json; d=json.load(sys.stdin); [print(i['tag'],i['port'],i['protocol']) for i in d['inbounds']]"

# Cloudflare DNS 检查
nslookup vps.example.com 8.8.8.8      # 应该看到 Cloudflare IP（104.21.x.x / 172.67.x.x）
```
