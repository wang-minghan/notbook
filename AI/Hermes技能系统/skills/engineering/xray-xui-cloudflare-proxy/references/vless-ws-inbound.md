# VLESS + WebSocket 入站模板

## xray config.json 格式

```json
{
  "tag": "vps-ws-inbound",
  "port": 10086,
  "listen": "127.0.0.1",
  "protocol": "vless",
  "settings": {
    "clients": [
      {
        "id": "<UUID>",
        "flow": "",
        "email": "user@vps",
        "limitIp": 0,
        "totalGB": 0,
        "expiryTime": 0,
        "enable": true
      }
    ],
    "decryption": "none",
    "fallbacks": []
  },
  "streamSettings": {
    "network": "ws",
    "security": "none",
    "wsSettings": {
      "path": "/wsproxy",
      "headers": {}
    }
  },
  "sniffing": {
    "enabled": true,
    "destOverride": ["http", "tls"]
  }
}
```

## SQLite INSERT（新版 x-ui，有 sniffing_enabled 列）

```sql
INSERT INTO inbounds (user_id, up, down, total, remark, enable, expiry_time,
  port, protocol, settings, stream_settings, tag, sniffing_enabled, sniffing)
VALUES (1, 0, 0, 0, 'VPS-CF-WS-TLS', 1, 0, 10086, 'vless',
  '{"clients":[{"id":"<UUID>","flow":"","email":"user@vps","limitIp":0,"totalGB":0,"expiryTime":0,"enable":true}],"decryption":"none","fallbacks":[]}',
  '{"network":"ws","security":"none","wsSettings":{"path":"/wsproxy","headers":{}}}',
  'vps-ws-inbound', 1,
  '{"enabled":true,"destOverride":["http","tls"]}');
```

## SQLite INSERT（旧版 x-ui，无 sniffing_enabled 列）

```sql
INSERT INTO inbounds (user_id, up, down, total, remark, enable, expiry_time,
  port, protocol, settings, stream_settings, tag)
VALUES (1, 0, 0, 0, 'VPS-CF-WS-TLS', 1, 0, 10086, 'vless',
  '{"clients":[{"id":"<UUID>","flow":"","email":"user@vps","limitIp":0,"totalGB":0,"expiryTime":0,"enable":true}],"decryption":"none","fallbacks":[]}',
  '{"network":"ws","security":"none","wsSettings":{"path":"/wsproxy","headers":{}}}',
  'vps-ws-inbound');
```

## SCP 传输 Python 脚本到 VPS 执行（推荐方式）

```bash
# 本地写好脚本后 SCP 传过去执行
scp /local/path/add_inbound.py root@VPS_IP:/root/
ssh root@VPS_IP 'python3 /root/add_inbound.py && systemctl restart x-ui'
```

## 验证命令

```bash
sleep 5 && ss -tlnp | grep 10086 && echo "✅ 端口已开" || echo "❌ 未开"
```
