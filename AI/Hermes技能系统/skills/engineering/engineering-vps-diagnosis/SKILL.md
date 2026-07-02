---
name: engineering-vps-diagnosis
description: 系统化诊断 VPS 不可达、SSH 连接失败、服务器假死等问题。适用场景：SSH 超时/被拒/间歇掉线、服务器失联、面板显示 online 但连不上。
---

# VPS 诊断工程师

系统化诊断 VPS 连接问题。按层递进，每层确认后再进下一层。

## 核心原则

- **逐层排查，不跳层** — 网络层 → TCP 层 → SSH 层 → 系统层
- **用数据说话** — 每种症状对应有限几种根因
- **先确认问题范围** — 是网络问题、服务问题还是服务器本身的问题

## 逐层诊断流程

### Layer 1: 网络可达性

```bash
# 检查服务器是否在线
ping -n 3 <IP>

# 确认从本地到服务器的路由
traceroute <IP>   # Linux/Mac
tracert <IP>      # Windows
```

| 结果 | 含义 | 下一步 |
|------|------|--------|
| Ping 通 | 服务器在线，网络层正常 | 进 Layer 2 |
| Ping 不通 | 服务器关机/网络断开/VPC 防火墙 | 检查面板 VNC/Console |

### Layer 2: 端口可达性

```bash
# 测试 SSH 端口是否开放
nc -zv <IP> 22          # netcat
timeout 5 bash -c "echo >/dev/tcp/<IP>/22" && echo "OPEN" || echo "CLOSED"
```

**用 Python 更精确地检测：**

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
try:
    s.connect(('IP', 22))
    print(f'Port 22: OPEN')
    # 尝试读取 SSH banner
    s.settimeout(5)
    banner = s.recv(1024)
    print(f'Banner received: {banner[:100]}')
except socket.timeout:
    print(f'Port 22: Connected but banner timeout (sshd not responding)')
except Exception as e:
    print(f'Port 22: {e}')
finally:
    s.close()
```

**端口状态诊断表：**

| TCP 状态 | 含义 |
|----------|------|
| 端口开放 + banner 正常 | SSH 服务正常运行 |
| **端口开放 + banner 超时** | **SSH 进程假死 / fail2ban 限流 / iptables connlimit** → 用 VNC 进 |
| 端口关闭（无响应） | SSH 进程挂了 / 防火墙拦截了 22 端口 |
| 端口拒绝（RST） | 服务未启动 / 端口被关闭 |

### Layer 3: SSH 握手诊断

#### 标准场景诊断

**关键症状 — SSH 间歇性 banner 超时（最常见）：**

特征：TCP 连上了但 SSH 不返回 `SSH-2.0-...` banner，或者偶发返回后 KEX 数据为空。

**根因（按概率排序）：**
1. **fail2ban 封禁** — `iptables -L INPUT -n` 确认是否有 DROP 规则
2. **iptables connlimit 限流** — 同一 IP 半开连接数超限
3. **MaxStartups 限制** — `/etc/ssh/sshd_config` 中 MaxStartups 设得太低（默认 10:30:100）
4. **sshd 进程僵死** — 需重启

#### 🇨🇳 中国网络场景诊断（GFW QoS / 国际链路限流）

**何时怀疑是国际链路问题：**
- VPS 面板 Online，Ping 正常（200-300ms），系统健康
- TCP 22 端口开放（socket connect 成功）
- SSH banner **间歇性或持续性超时**
- VNC 进去后服务器完全正常（fail2ban 无封禁、iptables 无规则、sshd 运行正常）
- 服务器自测 OK（`ssh root@127.0.0.1` 秒连）
- 换 IP 但同网段后问题依旧

**诊断方法 — 代理对比测试：**

| 连接方式 | 结果 | 根因分析 |
|---------|------|---------|
| 🔴 国内网络直连 | banner 超时 | GFW QoS / 国际路由限流 |
| 🟢 开 HK/JP/US 代理 | SSH 秒连 | 链路问题确认 |
| 🔴 换 IP 但同网段 | 仍然超时 | 整个 IP 段被限流 |

**关键诊断信号 — 区分 GFW 与服务器问题：**

| 信号 | 含义 |
|------|------|
| 完全收不到 banner（recv 一直阻塞） | 服务器端问题（sshd僵死/fail2ban/connlimit 或 GFW 彻底屏蔽端口） |
| **banner 偶发收到，但 paramiko/OpenSSH 后续 KEX 失败（EOFError）** | **🔥 GFW 检测到 SSH 握手后注入 RST 切断连接 — 服务器端完全正常** |
| 开代理后 10/10 次 banner 成功 | 确认是国际链路限流，非服务器问题 |

**关键区别：** 如果 `socket.connect` 能连上、`socket.sendall` 发版本后 `recv` 有时能收到 `SSH-2.0-...\r\n`（甚至附带后续 KEX 数据），但 paramiko 的 `start_client()` 或 OpenSSH 客户端报 `Error reading SSH protocol banner` / `Connection timed out during banner exchange` — 这实际上是 **连接在 banner 发送后就被切断了**，而不是 "收不到 banner"。这是 GFW 对 SSH 流量的特征识别行为。

**预发版本字符串诊断法（确认服务器能响应）：**

当 paramiko 反复报 banner 超时时，用此方法验证服务器是否在正常响应：

```python
import socket, time
host = 'YOUR_VPS_IP'
# 短间隔多次探测，发版本字符串后等响应
for attempt in range(10):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(8)
    try:
        sock.connect((host, 22))
        sock.sendall(b'SSH-2.0-Diag\\r\\n')
        time.sleep(1.5)
        try:
            data = sock.recv(4096)
            if data:
                idx = data.find(b'\\r\\n')
                if idx >= 0:
                    banner = data[:idx].decode()
                    kex = data[idx+2:]
                    print(f'✓ #{attempt+1}: Banner={banner}, KEX data={len(kex)}bytes')
                else:
                    print(f'✓ #{attempt+1}: Got data (no CRLF): {len(data)}bytes')
            else:
                print(f'✗ #{attempt+1}: Empty response')
        except socket.timeout:
            print(f'✗ #{attempt+1}: Connected but no banner (timeout)')
    except Exception as e:
        print(f'✗ #{attempt+1}: {e}')
    finally:
        sock.close()
    time.sleep(1)
```

**结果解读：** 
- 0次banner=屏蔽级别(GFW限流)
- 3-7次banner=路由抖动/QoS（GFW 间歇性识别并切断）
- 10/10次banner=服务器正常，可能本地网络问题或端口被封
- 开代理10/10次=确认是国际链路问题
- **如果原始 socket 能拿到 banner + KEX 数据但 paramiko/OpenSSH 还是超时** → 这是 GFW 检测到 SSH 协议签名后主动干预的特征，比纯 banner 超时更明确地指向 GFW，而非服务器故障

**另一个有效信号 — 有 KEX 数据但 paramiko 报 EOFError：**

```python
# 如果原始 socket 收到绑止的 banner 后附带 >1000 字节 KEX 数据
# 但 paramiko.start_client() 报 EOFError / No existing session
# 表示服务器完整发完了握手包，但连接在握手过程中被外部切断
print(f'KEX data present: {len(kex)} bytes -> GFW INTERFERENCE CONFIRMED')
```

**永久解决方案：**

**永久解决方案：**\n\n| 方案 | 说明 | 复杂度 |\n|------|------|--------|\n| 🅰 **HK 代理中转 SSH** | 本地走代理再 SSH，最简单 | ⭐ |\n| 🅱 **Cloudflare CDN + xray WebSocket** | **推荐**。域名+Cloudflare Proxied + WS+TLS，不走直连，不受 GFW 限流影响 | ⭐⭐⭐ |\n| 🅲 **Cloudflare Tunnel (cloudflared)** | 装 cloudflared 走 CF 网络，不需要开端口（安全），但需要域名 | ⭐⭐⭐ |\n| 🅳 **WireGuard/frp 中转** | 在亚洲线路好的跳板机上搭隧道 | ⭐⭐⭐⭐ |\n| 🅴 **提工单换节点** | 要求换到亚洲优化线路的机房，不一定成功 | ⭐ |\n\n#### 🅱 Cloudflare CDN + xray WebSocket 方案详解\n\n**适用场景：** VPS 已有 xray/x-ui 面板，需要通过 Cloudflare CDN 中转代理流量\n\n**架构：**\n```\n用户本地 ---Cloudflare CDN(Proxied)--- nginx(443/TLS) --- xray(10086/WS) --- 目标\n                              ↑\n                      域名 vps.example.com\n```\n\n**步骤：**\n\n1. **Cloudflare 添加域名** → DNS → 添加 A 记录：子域名 → VPS IP → 开启 ☁️ Proxied（橙色云朵）\n2. **Cloudflare SSL/TLS** → 设为 **Full**（**不是** Full strict — Origin CA 证书 CN 是 "Cloudflare" 不含域名 SAN，Full strict 会报 526）\n3. **Cloudflare Origin Server** → **Create Certificate**（Origin CA，有效期选最长）→ 保存 certificate + private key\n4. **VPS 上配置 nginx**（反向代理 + WebSocket）：\n\n```nginx\n# /etc/nginx/conf.d/vps.example.com.conf\nserver {\n    listen 443 ssl http2;\n    server_name vps.example.com;\n\n    ssl_certificate /etc/nginx/certs/origin.crt;\n    ssl_certificate_key /etc/nginx/certs/private.key;\n    ssl_protocols TLSv1.2 TLSv1.3;\n\n    location /wsproxy {\n        proxy_pass http://127.0.0.1:10086;\n        proxy_http_version 1.1;\n        proxy_set_header Upgrade $http_upgrade;\n        proxy_set_header Connection \"upgrade\";\n        proxy_set_header Host $host;\n        proxy_read_timeout 300s;\n        proxy_send_timeout 300s;\n    }\n}\n```\n\n5. **xray 添加 WebSocket 入站**（监听 127.0.0.1:10086、路径 `/wsproxy`、security=none）：\n   - 协议: VLESS\n   - 端口: 10086, 监听: 127.0.0.1\n   - 传输: WebSocket, 路径: /wsproxy\n   - 安全: none（TLS 由 nginx 处理）\n\n6. **xray 添加入站（⚠️ x-ui 面板用户注意！）：**
   - x-ui 面板将配置存于 **sqlite3 DB**（`/etc/x-ui/x-ui.db`），重启时会 **重新生成 config.json**
   - **不要直接编辑 config.json** — 面板会覆盖你的修改！
   - 必须通过 **sqlite3 操作数据库** 来新增/修改入站
   - 参见参考文件 `references/cloudflare-cdn-xray-websocket.md` Step 5 的详细 SQL 代码
   - 重启 x-ui 的命令：`systemctl restart x-ui`

7. **客户端连接信息：**\n   - 地址: `vps.example.com`（**域名，不是 IP**）\n   - 端口: 443\n   - TLS: 开启，SNI: `vps.example.com`\n   - 传输: WebSocket, 路径: `/wsproxy`\n\n**注意事项：**\n- 确认域名已通过 Cloudflare 解析（NS 已切换到 Cloudflare）\n- SSL/TLS 必须设为 **Full**（不是 Full strict），用 Origin CA 证书\n- Cloudflare 免费版不支持 WebSocket over非标准端口 → 必须用 443 或 80\n- Proxied 模式下 Cloudflare 会缓存/优化流量，对 VMESS/SS 等协议不友好 → 推荐 VLESS+WS+TLS\n- 如果已有 sing-box/xray 其他入站（如 VLESS-REALITY），保留原配置，新增 WebSocket 入站互不冲突\n\n**关键优势：** 从国内直接访问 Cloudflare CDN IP（104.21.x.x / 172.67.x.x）通常不受 GFW 限流，VPS 真实 IP（155.94.133.x）被完全隐藏。\n

**Windows 环境下的 SSH 工具链注意事项：**
- `sshpass` 不可用（Chocolatey 无包）
- `expect` 不可用
- **推荐用 paramiko**（需确认 Python 3.x 中已安装，且路径正确）
- Windows 上 `python` vs `python3` 可能是不同版本 — paramiko 可能装在其中一个

**用 paramiko + 重试诊断：**

```python
import socket, paramiko, time

host = 'IP'
for attempt in range(10):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(8)
        sock.connect((host, 22))
        # Pre-send SSH version for better compatibility with older servers
        sock.sendall(b'SSH-2.0-DiagClient\r\n')
        time.sleep(1.5)
        data = sock.recv(4096)
        if data:
            print(f'✓ Attempt {attempt+1}: Got SSH banner')
            break
    except socket.timeout:
        print(f'✗ Attempt {attempt+1}: Connected but no banner')
    except Exception as e:
        print(f'✗ Attempt {attempt+1}: {e}')
    finally:
        sock.close()
    time.sleep(1.5)
```

### Layer 4: 进入系统后排查

**一旦 SSH 连接成功，立即检查：**

```bash
# 系统负载
uptime                      # 运行时间 + 平均负载
free -h                     # 内存 + swap
df -h /                     # 磁盘使用率
dmesg | tail -30            # 内核日志（OOM killer、磁盘错误等）

# SSH 配置
cat /etc/ssh/sshd_config | grep -E '^(Port|PermitRootLogin|PasswordAuthentication|MaxStartups)'

# fail2ban 状态
fail2ban-client status sshd 2>/dev/null || echo "fail2ban not installed"

# iptables 规则（排查限流）
iptables -L INPUT -n --line-numbers 2>/dev/null || echo "no iptables"

# 最近登录失败记录
cat /var/log/auth.log* 2>/dev/null | grep -i "Failed\\|Invalid" | tail -20
last -10

# 进程按内存排序
ps aux --sort=-%mem | head -20

# 重启 SSH 服务（如果进程僵死）
systemctl restart sshd
```

## 症状 → 根因速查表

| 症状 | 最可能根因 | 处理方式 |
|------|-----------|----------|
| Ping 通, 22 端口开放, banner 间歇性超时 | fail2ban / iptables connlimit / MaxStartups | VNC 进去看规则后调整 |
| Ping 通, 22 端口开放, banner 正常, 密码正确但连不上 | 密码错误 / sshd 配置禁止密码登录 / PAM 配置问题 | 检查 PermitRootLogin 和 PasswordAuthentication |
| Ping 通, 22 端口开放, 能 SSH 但执行命令超时 | 内存耗尽（OOM）/ CPU 满载 | 内存检查, 看 dmesg 有无 oom_killer |
| Ping 通, 22 端口开, 收到 Connection refused | SSH 服务没启动 | VNC 进去 systemctl start sshd |
| Ping 通, 22 端口关（无响应） | 防火墙 / iptables 规则 / 端口被封 | VNC 进去检查 iptables |
| Ping 不通 | VPS 关机 / 网络断开 / 底层故障 | 面板重启 + VNC Console |
| 间歇性断连 + 高延迟 | 国际链路不稳定 / 运营商QoS / GFW限流 | 保活参数 + 代理中转；服务端配 `ClientAliveInterval 15`；本地配 `-o ServerAliveInterval=15 -o ConnectionAttempts=5` |
| **同一密码有时能连有时报 Permission denied** | **⚠️ 链路不稳导致 SSH auth 握手中途被切断，并非密码错误** — 表现为同一密码在同一链路上有时成功有时失败，VNC 确认密码正确 | **重试循环（10+次）+ sleep间隔。如果开代理后稳定连上，确认是链路问题。不要假设密码错了** |\n| **换IP但同网段后问题依旧** | **整个IP段被GFW限流（如RackNerd 155.94.133.x）** | **Cloudflare CDN + WebSocket 或 HK 代理中转** |\n| Docker 容器占用全部端口 | docker network 抢占了宿主机端口 | 检查 docker network ls 和端口映射 |

## 最后手段

如果 SSH 完全连不上，**始终先用面板的 VNC Console / Serial Console**。这是等同于在机房面前操作，不经过网络层，可以绕过所有网络级故障。

VNC 进去后优先跑：
```bash
systemctl status sshd
systemctl restart sshd
journalctl -u sshd --no-pager | tail -30
fail2ban-client status sshd
iptables -L INPUT -n
```

## Windows 平台特有约束

- **无 sshpass** — 不要尝试安装，Chocolatey 无此包
- **无 expect** — 同上
- **用 paramiko** — 安装位置在 Python 3.x 的 pip 下
- **多 Python 版本** — `python --version` 可能是 Hermes 虚拟环境（无 pip），真实 Python 可能在 `$LOCALAPPDATA/Programs/Python/Python312/`
- **查 paramiko 位置** — `pip show paramiko` 查看安装路径，确认与目标 Python 一致
