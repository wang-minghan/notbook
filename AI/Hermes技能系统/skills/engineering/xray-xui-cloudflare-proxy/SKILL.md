---
name: xray-xui-cloudflare-proxy
description: Deploy xray/x-ui behind Cloudflare CDN with WebSocket+TLS. Covers panel API quirks, SQLite DB config, Nginx WS reverse proxy, and Origin CA cert setup.
---

# xray/x-ui 代理部署（Cloudflare CDN + WebSocket + TLS）

适用于 x-ui / 3x-ui 面板 v1.8.8+，将 xray 代理隐藏到 Cloudflare CDN 后端，中国大陆可直接连接。

## 架构

```
Client → Cloudflare CDN (vps.yourdomain.com) → Nginx (TLS+WS反代) → xray (WS入站)
```

- Cloudflare 终结 TLS，回源到 Nginx（使用 Cloudflare Origin CA 证书）
- Nginx 代理 WebSocket 到 xray 本地端口
- xray 监听 127.0.0.1，不对外暴露

## 前提

- 域名已托管到 Cloudflare（NS 切换完成）
- VPS 上已有 x-ui 面板运行中
- Nginx 已安装

## 配置步骤

### 1. Cloudflare 端

- **DNS**: 添加 A 记录 `vps` → `你的VPS-IP`，Proxy 状态设为 **Proxied**（橙色云朵）
- **SSL/TLS**: 设为 **Full**（**不是** Full strict）— 见下方陷阱说明
- **Origin Certificate**: Cloudflare Dashboard → SSL/TLS → Origin Server → 创建证书（有效期15年）

### 2. VPS 证书

保存 Origin CA 证书：
```bash
mkdir -p /etc/nginx/certs
# 将证书内容写入 /etc/nginx/certs/origin.crt
# 将私钥写入 /etc/nginx/certs/origin.key
```

### 3. Nginx 配置

```nginx
server {
    listen 443 ssl http2;
    server_name vps.yourdomain.com;

    ssl_certificate /etc/nginx/certs/origin.crt;
    ssl_certificate_key /etc/nginx/certs/origin.key;
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

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}

# HTTP → HTTPS redirect
server {
    listen 80;
    server_name vps.yourdomain.com;
    return 301 https://$host$request_uri;
}
```

### 4. xray 入站配置

> 📄 完整模板和 SCP 一键部署脚本见 [references/vless-ws-inbound.md](references/vless-ws-inbound.md)
> 📄 独立 xray systemd 服务模板 + vless:// 分享链接见 [references/standalone-xray-service.md](references/standalone-xray-service.md)

#### ⚠️ 关键陷阱：x-ui 的配置存储

**x-ui 面板将入站配置存储在 SQLite 数据库** (`/etc/x-ui/x-ui.db`) 的 `inbounds` 表中。重启 x-ui 时从 DB 重新生成 `/usr/local/x-ui/bin/config.json`。

**直接编辑 config.json 无效** — 重启后被 DB 内容覆盖。

#### 方式 A：通过 x-ui 面板 Web UI 添加（推荐）

浏览器访问 `https://<VPS-IP>:<PORT>/<webBasePath>/` 登录后手动添加入站。

#### 方式 B：通过 x-ui 面板 API 添加

**API 要点：**
- CSRF token 从 HTML meta 标签获取：`<meta name="csrf-token" content="...">`
- 登录使用 `application/x-www-form-urlencoded` 格式（**不是** JSON）
- 所有 API 请求需携带 `X-CSRF-Token` 和 `X-Requested-With: XMLHttpRequest` 头

```python
import urllib.request, urllib.error, urllib.parse, ssl, json, http.cookiejar, http.client, uuid, re

# 1. Get CSRF
ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(
    type('H', (urllib.request.HTTPSHandler,), {'https_open': lambda s,r: s.do_open(http.client.HTTPSConnection, r, context=ctx)})(),
    urllib.request.HTTPCookieProcessor(cj))
resp = opener.open(f'https://{HOST}:{PORT}{BASE}/', timeout=10)
csrf = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', resp.read().decode()).group(1)

# 2. Login (form-urlencoded!)
data = urllib.parse.urlencode({'username': 'root', 'password': PASSWORD}).encode()
req = urllib.request.Request(f'https://{HOST}:{PORT}{BASE}/login', data=data,
    headers={'X-Requested-With':'XMLHttpRequest','X-CSRF-Token':csrf,
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}, method='POST')
resp = json.loads(opener.open(req, timeout=10).read().decode())
# resp['success'] == True means logged in

# 3. Add inbound
new_inbound = {
    "remark": "VPS-CF-WS-TLS", "port": 10086, "protocol": "vless",
    "settings": json.dumps({"clients": [{"id":"UUID","flow":"","email":"user@vps",
        "limitIp":0,"totalGB":0,"expiryTime":0,"enable":True}],
        "decryption":"none","fallbacks":[]}),
    "streamSettings": json.dumps({"network":"ws","security":"none",
        "wsSettings":{"path":"/wsproxy","headers":{}}}),
    "sniffing": json.dumps({"enabled":True,"destOverride":["http","tls"]}),
    "enable": True
}
req = urllib.request.Request(f'https://{HOST}:{PORT}{BASE}/panel/api/inbounds/add',
    data=json.dumps(new_inbound).encode(),
    headers={'X-Requested-With':'XMLHttpRequest','X-CSRF-Token':csrf,
             'Content-Type':'application/json'}, method='POST')
```

#### 方式 C：直接操作 SQLite 数据库（SSH 有 shell 时可用）

> ⚠️ **x-ui 版本差异**：部分旧版 x-ui 的 `inbounds` 表**没有** `sniffing_enabled` 和 `sniffing` 列。插入时去掉这两个字段即可：
> ```sql
> INSERT INTO inbounds (user_id,up,down,total,remark,enable,expiry_time,port,protocol,settings,stream_settings,tag)
> VALUES (...);
> ```
> 如果报错 `no such column: sniffing_enabled`，说明你的 x-ui 是旧版。

```bash
sqlite3 /etc/x-ui/x-ui.db << 'SQL'
INSERT INTO inbounds (user_id,up,down,total,remark,enable,expiry_time,port,protocol,settings,stream_settings,tag,sniffing_enabled,sniffing)
VALUES (1,0,0,0,'VPS-CF-WS-TLS',1,0,10086,'vless',
  '{"clients":[{"id":"<UUID>","flow":"","email":"user@vps","limitIp":0,"totalGB":0,"expiryTime":0,"enable":true}],"decryption":"none","fallbacks":[]}',
  '{"network":"ws","security":"none","wsSettings":{"path":"/wsproxy","headers":{}}}',
  'vps-ws-inbound',1,
  '{"enabled":true,"destOverride":["http","tls"]}');
SQL
systemctl restart x-ui
```

### 5. 重启与验证

```bash
# 先检查 nginx 配置语法
nginx -t

# reload nginx
nginx -s reload

# 重启 x-ui（使新建入站生效）
systemctl restart x-ui

# ⚠️ 重启后等 4-5 秒再检查端口（xray 启动需要时间）
sleep 5
ss -tlnp | grep -E "10086|443" && echo "✅ 端口已开"
```

## 客户端连接参数

| 参数 | 值 |
|---|---|
| 协议 | VLESS |
| 地址 | vps.yourdomain.com |
| 端口 | 443 |
| 传输 | WebSocket |
| 路径 | /wsproxy |
| TLS | ✅ 开启（SNI: vps.yourdomain.com） |

#### 方式 D：独立 xray systemd 服务（绕过 x-ui config.json 生成问题）

> ⚠️ **已知 bug**：某些 x-ui 版本在从 SQLite DB 生成 config.json 时会把 `clients` 字段写成 `null`，导致 xray 不接受任何连接。表现为端口在监听但 WebSocket 握手无响应。
>
> **解决方案**：手动写 config.json，用独立 systemd 服务运行 xray，不经过 x-ui。

```bash
# 1. 手动写入正确的 config.json（见上方模板）
scp config.json root@VPS:/usr/local/x-ui/bin/config.json

# 2. 创建 systemd 服务
cat > /etc/systemd/system/xray-standalone.service << 'EOF'
[Unit]
Description=Xray Proxy Server (Standalone)
After=network.target

[Service]
Type=simple
WorkingDirectory=/usr/local/x-ui/bin
ExecStart=/usr/local/x-ui/bin/xray-linux-amd64 -c /usr/local/x-ui/bin/config.json
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# 3. 停 x-ui，启动独立 xray
systemctl stop x-ui
systemctl daemon-reload
systemctl start xray-standalone
systemctl enable xray-standalone

# 4. 验证
ss -tlnp | grep 10086 && echo "✅ 独立 xray 运行中"
```

> 使用此方式后 x-ui 面板的入站列表可能为空或不准确，但代理功能完全正常。管理入站需直接编辑 config.json + `systemctl restart xray-standalone`。

## 已知陷阱

1. **x-ui 面板密码 ≠ SSH 密码** — 面板密码是面板内部设置的，即使 SSH 密码改了也不会同步
2. **x-ui 面板 API 使用 CSRF token** — 每个 POST 请求都需要从 HTML meta 标签获取最新的 CSRF token
3. **x-ui 面板登录用 form-urlencoded** — 不是 JSON 格式
4. **x-ui 重启时从 DB 重新生成 config.json** — 直接改 config.json 不生效
5. **Cloudflare SSL/TLS 必须设为 Full（不是 Full strict）** — Cloudflare Origin CA 证书的 CN 是 `Cloudflare`，不包含域名 SAN。Full strict 模式会因主机名不匹配返回 526 (Invalid SSL Certificate)。Full 模式仍全程加密，只是不验证源站证书的主机名
6. **RackNerd LA 155.94.133.x 网段被 GFW QoS** — 中国大陆直连 SSH 不稳定，需 HK 代理中转或走 CDN
7. **x-ui 数据库路径可能是 /etc/x-ui/x-ui.db 或 /usr/local/x-ui/bin/database/ 下的 db 文件** — 发行版不同
8. **旧版 x-ui 的 inbounds 表没有 sniffing_enabled/sniffing 列** — 插入时去掉这两个字段即可
9. **Cloudflare DNS A 记录（Proxied）必须手动创建** — VPS 配置完成后，客户端要靠 `vps.yourdomain.com` 解析到 Cloudflare 边缘 IP 才能连，不是自动生效的。DNS 记录需要在 Cloudflare Dashboard 手动添加
10. **重启 x-ui 后 xray 需要几秒启动** — 立即检查端口会漏报。插 `sleep 5; ss -tlnp | grep 10086`
11. **Windows/MSYS 下 SSH heredoc 的引号会被吃掉** — 从 Windows 的 git-bash/MSYS 通过 SSH heredoc 传递 Python 脚本时，单引号会被 shell 吞掉导致语法错误。**用 SCP 传脚本文件**比 heredoc 可靠 10 倍：`scp script.py root@VPS:/root/ && ssh root@VPS 'python3 /root/script.py'`
12. **x-ui 面板 API 登录返回 403** — 不是密码错误，是缺少 CSRF token。必须先 GET 主页提取 `<meta name="csrf-token" content="...">` 中的 token，然后在 POST 请求头中带 `X-CSRF-Token`
13. **SSH 不稳定时优先用 SCP 传文件** — GFW QoS 环境下 SSH 连接随时会断，长命令容易半途失败。短 SSH 命令 + SCP 分步操作更可靠
14. **x-ui DB 写入 clients 后 config.json 仍为 null** — 部分 x-ui 版本的 config 生成器有 bug：即使 SQLite `inbounds.settings` JSON 中有正确的 `clients`，生成的 `config.json` 仍输出 `"clients": null`。症状：端口 10086 在监听，但 WebSocket 握手无响应（curl -v 显示连接成功后挂起）。**解决**：用方式 D（独立 systemd 服务）绕过
15. **vless:// 分享链接格式** — 导入客户端用：`vless://<UUID>@<HOST>:443?encryption=none&security=tls&sni=<HOST>&type=ws&path=%2Fwsproxy&host=<HOST>#<别名>`
16. **Cloudflare 免费版 gRPC 传输不可靠** — 尝试将 WebSocket 换成 gRPC（xray 配置 `network: grpc`, `grpcSettings: {serviceName: "proxy"}` + nginx `grpc_pass`）时，Cloudflare 会剥离/修改 `Content-Type` 头，导致 xray 返回 `Grpc-Status: 3, invalid gRPC request content-type ""`。症状：nginx 返回 HTTP 405 或 415。**解决：保持 WebSocket 传输**。gRPC 在 Cloudflare Pro/Business/Enterprise 计划上可能正常工作，但免费版不保证。
17. **Cloudflare 免费版 + 廉价 VPS = 速度慢** — 如果用户反馈代理能用但很卡，根因通常是：① Cloudflare 免费版对中国线路无优化（走普通国际带宽）；② VPS 本身带宽低（如 RackNerd LA）。优化方向：Cloudflare Dashboard → Network → 开启 HTTP/3 (QUIC)；或考虑换 CDN（AWS CloudFront / Bunny CDN）；或换 CN2 GIA 线路 VPS（搬瓦工/DMIT）。不建议在免费版上折腾 gRPC/XHTTP 等新协议，稳定性不如 WebSocket。
