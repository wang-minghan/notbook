# 独立 xray systemd 服务模板

当 x-ui 的 config.json 生成器有 bug（clients 字段被置 null）时，使用此方案。

## systemd 服务文件

```ini
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
```

## 部署步骤

```bash
cat > /etc/systemd/system/xray-standalone.service << 'EOF'
... (上方内容)
EOF

systemctl stop x-ui
systemctl daemon-reload
systemctl start xray-standalone
systemctl enable xray-standalone
sleep 3 && ss -tlnp | grep 10086 && echo "✅ OK"
```

## 管理命令

```bash
systemctl restart xray-standalone
systemctl status xray-standalone
journalctl -u xray-standalone -f
```

## vless:// 分享链接

```
vless://<UUID>@<HOST>:443?encryption=none&security=tls&sni=<HOST>&type=ws&path=%2Fwsproxy&host=<HOST>#<别名>
```

示例：
```
vless://4b91e5ac-318d-4d2a-9ad4-c4312a869433@vps.minghan.top:443?encryption=none&security=tls&sni=vps.minghan.top&type=ws&path=%2Fwsproxy&host=vps.minghan.top#VPS-CDN
```

v2rayN 导入：服务器 → 从剪贴板导入批量URL → 粘贴链接。
