# SSH Banner Timeout 诊断案例

## 症状

- VPS 面板显示 Online
- Ping 正常（~226ms，无丢包）
- TCP 端口 22 开放（socket connect 成功）
- SSH banner 间歇性接收：约 40% 的连接收到 `SSH-2.0-OpenSSH_7.6p1 Ubuntu-4\r\n`
- 收不到 banner 时 paramiko 报 `Error reading SSH protocol banner`
- 偶尔能连上后执行命令就超时（`Timeout opening channel`）
- 多次重试（〜第5次）后成功连接一次，系统一切正常（内存 985MB/仅用182MB，磁盘 24GB/用1.9GB）

## 诊断过程

```
Layer 1: ping → 通 ✅
Layer 2: port 22 TCP → 通 ✅
Layer 2.5: SSH banner → 间歇超时 ⚠️  <-- 关键发现
Layer 3: paramiko 重试 → 第5次成功 ✅
Layer 4: 系统健康检查 → 一切正常 ✅
```

## 关键发现

**"TCP 通但 banner 不到" 这个组合症候群指向：**

1. **fail2ban 限流** — 最可能。服务器 OpenSSH 7.6p1 + Ubuntu 18.04，这是默认装 fail2ban 的经典组合
2. **iptables connlimit** — `-m connlimit --connlimit-above N` 限制了同一 IP 的半开连接数
3. **MaxStartups 太紧** — 默认 `10:30:100`（开始拒绝 10 个并发连接，30:100 是概率参数）
4. **国际链路不稳定** — 从国内到美国机房的 TCP 在 banner 交换段丢包
5. **GFW QoS / 限流** — 中国到特定美国 IP 段的整段限流，换 IP 但同网段无效

## 检测命令（VNC 进去后执行）

```bash
# 查看 fail2ban 是否封了本机
fail2ban-client status sshd

# 查看 iptables 规则
iptables -L INPUT -n --line-numbers
iptables -L INPUT -n -v  # 带统计，看有没有大量 match 某条规则

# 检查 sshd 的 MaxStartups
cat /etc/ssh/sshd_config | grep MaxStartups

# 重启 sshd
systemctl restart sshd

# 看日志
journalctl -u sshd --no-pager | tail -30
cat /var/log/auth.log | grep -i 'Failed\|Invalid' | tail -20
```

## 对 Windows 客户端的特殊考虑

- 本地环境为 Git Bash (MSYS2) on Windows 10
- `sshpass` / `expect` 均不可用
- `paramiko` 安装在 Python 3.12 下（`$LOCALAPPDATA/Programs/Python/Python312/python.exe`）
- Hermes 虚拟环境的 `python` 是 3.11 且无 pip → 不能用 Hermes 自带的 python 跑 paramiko
- OpenSSH 客户端 9.9 默认不兼容 `diffie-hellman-group14-sha1` 等旧算法，需手动 `-oKexAlgorithms=+...` 参数

## 服务器信息（第一次案例）

- 提供商: RackNerd (DC03LA182KVM)
- 节点: 洛杉矶
- 系统: Ubuntu 18.04 with Docker
- 配置: 1C/1G/25GB/1.95TB
- SSH: OpenSSH 7.6p1 Ubuntu-4
- 原来装了什么: 未明（Docker 无容器运行）

---

## 补充案例：中国 GFW QoS / 国际链路限流（2026-06-26）

### 症状

- RackNerd LA 节点，Ubuntu 18.04，IP: 155.94.133.37 → 换到 155.94.133.41（同网段）
- 面板 Online，服务器健康，资源充足
- Ping 通（226ms），TCP 22 开放
- **SSH banner 间歇性超时**（约 30-40% 概率 banner，其余超时）
- 有 banner 时附带 ~1080 bytes KEX 数据（参服务器正常发了完整握手包）
- VNC 进去检查：fail2ban 封禁数=0，iptables 全 ACCEPT 无规则，sshd 正常运行
- 服务器自测 `ssh root@127.0.0.1` 秒连

### 关键发现 — GFW 干扰特征

**最关键信号：原始 socket 能拿到 banner + KEX 数据，但 paramiko / OpenSSH 报错**

```
原始 socket:
  connect → send version → recv → ✅ 收到 "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4\r\n" + 1080 bytes KEX
                                   ✅ 服务器完整发送了握手数据包

paramiko 同一 socket:
  start_client() → ❌ EOFError: Error reading SSH protocol banner
                   ❌ No existing session

OpenSSH 客户端:
  ssh → ❌ Connection timed out during banner exchange
```

**解读：** 这不是 "收不到 banner"，而是服务器发完了 banner + 完整的 KEX 握手包，但连接在握手过程中被**外部切断**。GFW 识别出 SSH 协议特征后注入 RST 包中断连接。

### 关键诊断步骤

1. **VNC 进去验证服务器健康** — 发现 fail2ban/iptables/sshd 全部正常
2. **代理对比测试** — 开 HK 代理后 SSH 秒连（8/8 次 banner 成功）；关掉代理 banner 间歇性超时
3. **换 IP** — 付费换成 155.94.133.41（同网段），问题依旧 → 确认是整个 IP 段被 GFW 限流，而非单个 IP
4. **10 次快速探测** — 开代理时 8/8 成功；关代理时约 3/10 成功，其余为 "banner timeout"（TCP 通但无响应）

### 根因

**GFW / 国际出口针对 SSH 协议特征的 QoS 限流**，对 RackNerd 的 155.94.133.x 网段进行传输层干预。不是服务器问题，不是 fail2ban，不是 SSH 配置。

### 诊断确认流程图

```
Ping 通? → TCP:22 通? → banner 收到?
  ├─ 从来收不到 → 服务器端问题（sshd/fail2ban/防火墙）
  └─ 间歇性收到，有 KEX 数据 → GFW 干扰 ⚠️
      └─ 开代理后 100% 成功？ → ✅ 确认 GFW 限流
          └─ 换 IP 但同网段仍不行？ → ✅ 整个 IP 段被限流
```

### 当前状态

| 方案 | 效果 | 说明 |
|------|------|------|
| 🟢 **通过 HK 代理 SSH** | ✅ 秒连 | 当前有效（需要代理） |
| 🟡 **Cloudflare Tunnel** | 待实施（需域名 + Cloudflare） | 推荐永久方案，不走直连不受 GFW 限流 |
| 🔴 **提工单换 IP** | ❌ 同网段无效（155.94.133.x） | 已尝试失败 |
| 🔴 **直连 SSH** | ❌ 间歇性 banner 超时（~30%成功率） | 不可靠
