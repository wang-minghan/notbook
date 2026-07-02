# Hermes Release Check

Quick script to check for new Hermes releases and extract notable features.

## One-liner

```bash
curl -sL https://api.github.com/repos/NousResearch/hermes-agent/releases/latest | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(f'Latest: {d[\"tag_name\"]} ({d[\"published_at\"][:10]})')
body = d.get('body','')
# Extract section headings
for line in body.split('\n'):
    if line.startswith('## ') or line.startswith('**'):
        print(line[:120])
"
```

## Check Current Version

```bash
hermes --version
# Returns something like: Hermes Agent v0.17.0 (2026.6.19) · upstream d430684d
```

## What to Look For

When scanning release notes, watch for:
- **New toolsets or platforms** — e.g., iMessage, Raft, WhatsApp Business API
- **Memory/agent improvements** — e.g., batch memory operations, background delegation
- **Cron enhancements** — scheduler changes that affect your jobs
- **Security fixes** — especially if you run in gateway mode

## On Restricted Networks

If GitHub API is blocked (common in China), check the official docs instead:
```bash
curl -sL https://hermes-agent.nousresearch.com/docs/ | head -20
```
The version banner in docs footer usually shows the latest release.
