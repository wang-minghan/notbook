---
name: hermes-memory-provider
category: autonomous-ai-agents
description: "Evaluate, switch between, and troubleshoot Hermes Agent external memory providers — provider comparison, migration workflow, and Chinese-network workarounds for heavy ML dependencies."
---

# Hermes Memory Provider Management

Guide to managing Hermes Agent's external memory providers. Hermes ships with 8 providers; only one active at a time (built-in MEMORY.md/USER.md always active alongside).

## Quick Command Reference

```bash
hermes memory setup              # Interactive picker + config wizard
hermes memory status             # Check active provider
hermes memory off                # Disable external provider
hermes config set memory.provider <name>   # Manual switch (set in config.yaml)
```

## Available Free Providers — Dependencies & Best For

| Provider | Dependencies | Free? | Best For |
|----------|-------------|-------|----------|
| **Holographic** | Zero (SQLite + FTS5 only) | ✅ Full local free | Zero-config, stability, constrained networks |
| **Built-in** | Zero (MEMORY.md/USER.md text files) | ✅ Always active | Fallback / no-extra-setup needed |
| **Hindsight (local)** | pg0 (embedded PostgreSQL) + PyTorch (~1GB) + LLM API key | ✅ Local free | Best benchmarks (94.6% LongMemEval) |
| **mem0 OSS** | Embedding API endpoint + qdrant-client | ✅ Free if self-hosted | Teams wanting managed SDK |
| **ByteRover (local)** | CLI install (pip) | ✅ Local free | Multi-hop / temporal reasoning |
| **OpenViking** | Ollama + server | ✅ Self-host free | Air-gapped / on-prem |

## Full Provider Switch — Step-by-Step

### 1. Change Provider
```bash
hermes config set memory.provider <new_provider>
```
This writes `memory.provider: <new>` in `config.yaml`.

### 2. Install Provider Dependencies
The `hermes memory setup` wizard auto-installs via uv. If it fails:
```bash
uv pip install "hindsight-client>=0.6.1"      # For hindsight cloud/external
uv pip install "hindsight-all>=0.6.1"         # For hindsight local_embedded (~1GB!)
```

### 3. Create Provider Config
Each provider reads config from `$HERMES_HOME/<provider>/config.json`:
```json
{
  "mode": "local_embedded",
  "llm_provider": "openai_compatible",
  "llm_base_url": "https://opencode.ai/zen/v1",
  "llm_model": "big-pickle",
  ...
}
```

### 4. Set Environment Variables
Add API keys / mode overrides to `$HERMES_HOME/.env`:
```bash
echo "HINDSIGHT_LLM_API_KEY=sk-xxx" >> $HERMES_HOME/.env
echo "HINDSIGHT_MODE=local_embedded" >> $HERMES_HOME/.env
```

### 5. Uninstall Old Provider
```bash
# Delete config files
rm -f $HERMES_HOME/<old_provider>/*.json
# Uninstall packages (both venv + system)
uv pip uninstall mem0ai qdrant-client
pip uninstall mem0ai qdrant-client -y
# Delete any leftover storage directories
rm -rf $HERMES_HOME/<old_provider>_data
```

### 6. Verify & Restart
```bash
hermes memory status     # Check active
# Close and reopen Hermes desktop app
```

## Provider-Specific Pitfalls

### Hindsight local_embedded
- **Huge download**: `hindsight-all` bundles PostgreSQL (pg0) + PyTorch (~1GB total)
- **Memory**: daemon uses ~1-2GB RAM while running
- **LLM API key required**: even for local mode (fact extraction)
- **Daemon lifecycle**: auto-starts on first use, auto-stops after 5min idle
- **Slim alternative**: `hindsight-api-slim` (no PyTorch, uses hosted embeddings)

### mem0 OSS
- **Needs a real embedding API endpoint**: `opencode.ai/zen/v1` returns 404 on `/embeddings` — won't work
- **Two packages**: `mem0ai` + `qdrant-client` (vector DB)
- **Two config files**: `mem0.json` + optional Qdrant storage dir

### Holographic
- **Zero dependencies**: pure Python + stdlib sqlite3
- **Config in**: `$HERMES_HOME/config.yaml` (no separate config file needed)
- **Storage**: SQLite file at `$HERMES_HOME/memory_store.db`
- **No wizard needed**: just `hermes config set memory.provider holographic`
- **Trust scoring**: facts auto-adjust trust scores based on feedback

## Chinese Network Workarounds

pip has Tsinghua mirror by default; uv does NOT — configure explicitly:

```bash
# Install heavy packages via pip with mirror
pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com <package>

# uv pip install with mirror
UV_DEFAULT_INDEX=https://mirrors.aliyun.com/pypi/simple/ UV_HTTP_TIMEOUT=120 uv pip install <package>

# Or for background installs (long-running):
# Use terminal(background=true, notify_on_complete=true)
```

## Architecture Notes

- **Plugin location**: `$HERMES_HOME/hermes-agent/plugins/memory/<provider>/`
- **Dependencies declared in**: `plugin.yaml` under `pip_dependencies:`
- **Setup wizard in**: `post_setup()` method in `__init__.py`
- **Only ONE external provider active at a time**
- **Built-in MEMORY.md/USER.md always active alongside**

## Verification Flow

After switching providers, confirm:
1. `grep provider $HERMES_HOME/config.yaml` → shows correct provider name
2. `hermes memory status` → `available ✓`
3. Old provider packages not importable: `python -c "import old_provider"` → ModuleNotFoundError
4. New provider config files exist: `ls $HERMES_HOME/<provider>/`
5. `.env` has correct env vars for new provider (no stale vars from old)
