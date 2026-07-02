---
name: hermes-plugin-ecosystem
description: "Discover, evaluate, install, and manage community plugins for Hermes Agent."
version: 1.0.0
author: Hermes Agent (auto-generated)
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, plugins, community, ecosystem, installation]
    related_skills: [hermes-agent]
---

# Hermes Plugin Ecosystem

Hermes Agent has a plugin system for adding custom tools, hooks, and integrations. Beyond the bundled plugins that ship with Hermes, there's a growing community ecosystem of third-party plugins on GitHub.

This skill covers **how to find, evaluate, install, and manage** community plugins.

## Quick Reference

```bash
# List all plugins (bundled + installed)
hermes plugins list

# Compact view (bundled only)
hermes plugins list --plain --no-bundled

# Interactive toggle UI
hermes plugins

# Install a community plugin from GitHub
hermes plugins install owner/repo
# Or full Git URL
hermes plugins install https://github.com/owner/repo

# After install, enable the plugin
hermes plugins enable <name>

# Disable without removing
hermes plugins disable <name>

# Uninstall
hermes plugins remove <name>

# Update an installed plugin
hermes plugins update <name>
```

## How Plugins Work

### Plugin States

| State | Meaning |
|-------|---------|
| **enabled** | Loaded on next session — in `plugins.enabled` in config.yaml |
| **disabled** | Explicitly off — in `plugins.disabled` (always wins if in both lists) |
| **not enabled** | Discovered but never opted in — default for new/bundled plugins |

### After Install

Plugins install as **not enabled** by default. You must explicitly enable:
```bash
hermes plugins enable <name>
```
Or use the `--enable` flag during install:
```bash
hermes plugins install owner/repo --enable
```

Changes take effect on **next session** (`/reset` or restart Hermes).

### Config Location

Plugin enable/disable state is stored in `~/.hermes/config.yaml`:
```yaml
plugins:
  enabled:
    - my-plugin
    - disk-cleanup
  disabled:
    - noisy-plugin
```

## Finding Community Plugins

### 1. GitHub Search (Recommended)

Search GitHub with these topic tags:
- `topic:hermes`
- `topic:hermes-agent`
- `topic:hermes-plugin`

Raw API queries (fastest):
```
https://api.github.com/search/repositories?q=hermes+plugin&sort=stars
https://api.github.com/search/repositories?q=topic:hermes&sort=stars
```

### 2. Awesome Lists (Curated)

These community-maintained lists aggregate the best resources:

| Awesome List | Stars | URL |
|---|---|---|
| **0xNyk/awesome-hermes-agent** | 4,200+ | `github.com/0xNyk/awesome-hermes-agent` |
| **SamurAIGPT/awesome-hermes-agent** | 1,700+ | `github.com/SamurAIGPT/awesome-hermes-agent` |
| **ZeroPointRepo/awesome-hermes-skills** | 68 | `github.com/ZeroPointRepo/awesome-hermes-skills` |
| **aliaihub/awesome-hermes-usecases** | 124 | `github.com/aliaihub/awesome-hermes-usecases` |

### 3. Hermes Docs

The official docs describe plugin authoring but don't maintain a community plugin registry:
https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins/

## Evaluating a Plugin

Check before installing:
1. **Stars & recency** — actively maintained? Recent commits?
2. **Description** — does it do what you need?
3. **License** — compatible with your use?
4. **README** — clear install/setup instructions?
5. **Code quality** — is the Python clean?
6. **Config requirements** — does it need API keys or env vars?

## Categories of Community Plugins

See `references/community-plugins.md` for a detailed categorized list with descriptions, stars, and install commands.

Popular categories:
- **Memory & Context** — enhanced memory providers, context compression, scope-aware recall
- **Search** — multi-provider web search with intelligent routing
- **Observability** — dashboards, analytics, cron monitoring, Grafana integration
- **Productivity** — skill factories, kanban boards, goal management, token optimization
- **Social** — Twitter/X automation, Second Life integration, Meshtastic LoRa adapter
- **Reasoning & Routing** — automatic reasoning-effort routing per platform

## Common Pitfalls

- **Plugins are opt-in by default** — installing does NOT enable them. Always run `hermes plugins enable <name>` after install.
- **Bundled plugins** (browser, image_gen, web, platforms, etc.) show as "not enabled" — they auto-load when their config is active, so don't manually enable them.
- **Restart required** — plugin changes only take effect on a new session (`/reset`).
- **Check `hermes plugins list` first** — avoids confusion about what's installed vs enabled.
- **API keys matter** — many plugins have `requires_env` in their manifest. Install prompts for missing keys.
- **Third-party risk** — community plugins run with Hermes's full system access. Review the code before installing untrusted plugins.

## Windows-Specific Installation

On Windows (Hermes Desktop), `HERMES_HOME` is at `~/AppData/Local/hermes/` — NOT `~/.hermes/`. This affects every path.

### Git clone fallback (when `hermes plugins install` fails)

Some GitHub repos lack proper `plugin.yaml` metadata or an install entry point, causing `hermes plugins install owner/repo` to fail silently. Use `git clone` directly:

```bash
cd ~/AppData/Local/hermes/plugins/
git clone https://github.com/owner/repo
hermes plugins enable <name>
```

Then configure via the safe command (direct config.yaml editing is blocked by Hermes's config-write guard):

```bash
hermes config set plugins.enabled '["my-plugin"]'
hermes config set context.engine lcm
```

### `hermes config set` is the safe path

The `patch` tool cannot write to `config.yaml` — it's blocked by Hermes's config-write guard. Always use `hermes config set <key> <value>`.

### Proxy / VPN on Windows

If GitHub clone hangs, unset any stale proxy env vars first:
```bash
unset https_proxy http_proxy all_proxy HTTP_PROXY HTTPS_PROXY
git clone https://github.com/owner/repo
```

If the system-wide VPN is already active (e.g. TUN mode), the clone succeeds without proxy variables.

## Memory Provider Configuration

Hermes ships with several built-in memory providers under `~/AppData/Local/hermes/hermes-agent/plugins/memory/`:
- `mem0` — Mem0 Platform API or OSS self-hosted
- `hindsight`, `holographic`, `honcho`, `openviking`, `retaindb`, `supermemory`, `byterover`

### mem0 OSS (Self-Hosted) Setup

The interactive CLI setup (`hermes memory setup mem0`) works in a TTY, but the OSS flags (`--mode oss --oss-llm ...`) are **intercepted by the main `hermes` CLI parser** before they reach the setup code. Running:

```bash
hermes memory setup mem0 --mode oss --oss-llm openai ...
# → ERROR: unrecognized arguments
```

This is a known limitation of the CLI flag forwarding. **Workaround: write `mem0.json` directly.**

Create `~/AppData/Local/hermes/mem0.json`:

```json
{
  "mode": "oss",
  "user_id": "hermes-user",
  "agent_id": "hermes",
  "oss": {
    "llm": {
      "provider": "openai",
      "config": {
        "model": "gpt-5-mini",
        "base_url": "https://your-llm-endpoint/v1"
      }
    },
    "embedder": {
      "provider": "openai",
      "config": {
        "model": "text-embedding-3-small",
        "base_url": "https://your-llm-endpoint/v1",
        "dims": 1536
      }
    },
    "vector_store": {
      "provider": "qdrant",
      "config": {
        "path": "C:/Users/<user>/AppData/Local/hermes/mem0_qdrant"
      }
    }
  }
}
```

Then ensure the vector store dependency is installed:
```bash
pip install qdrant-client
```

Verify with:
```bash
hermes memory status
# → Provider: mem0, Status: available ✓
```

### Switching between memory providers

**Clean switching procedure** (not just changing the config key):

```bash
# 1. Set the new provider
hermes config set memory.provider <name>

# 2. Run the interactive setup wizard
hermes memory setup
```

When the interactive wizard cannot run (non-TTY session), configure manually:

```bash
# 3a. Create provider-specific config (see subsections below)
# 3b. Add required env vars to $HERMES_HOME/.env
# 3c. Install required Python dependencies
uv pip install <provider-package>
```

**Cleanup when switching AWAY from a provider:**

```bash
# 1. Remove provider-specific config files
rm -f $HERMES_HOME/mem0.json
rm -rf $HERMES_HOME/hindsight/
rm -rf $HERMES_HOME/mem0_qdrant/        # local Qdrant vector store

# 2. Uninstall provider packages (both venv and system pip)
uv pip uninstall mem0ai qdrant-client
pip uninstall mem0ai qdrant-client -y

# 3. Verify no residue
python -c "import mem0" 2>&1 || echo "gone ✓"
```

The `uv pip uninstall` targets the Hermes venv; the system `pip uninstall` catches system-level installs.

---

### mem0 OSS (Self-Hosted) Setup

See subsection above — full `mem0.json` structure and known pitfalls.

### mem0 OSS provider options

| Component | Supported providers |
|-----------|-------------------|
| LLM | `openai` (compatible API), `ollama` (local) |
| Embedder | `openai`, `ollama` (e.g. `nomic-embed-text`) |
| Vector store | `qdrant` (local file or server), `pgvector` |

**Ollama path** (avoids external API key): install Ollama, pull `nomic-embed-text`, then in `mem0.json` set `"ollama_base_url": "http://localhost:11434"` and provider to `"ollama"` for both llm and embedder.

---

### Hindsight (Local Embedded) Setup

Hindsight uses a TEMPR architecture with 4 parallel retrieval strategies (temporal, entity, metadata, BM25). Best LongMemEval benchmarks of any provider (91.4-94.6%). MIT license, free for local use.

**Quick comparison:**

| Aspect | Local Embedded | Cloud |
|--------|---------------|-------|
| Dependencies | `hindsight-all` (~800MB: PyTorch, pg0, ONNX models) | `hindsight-client` (lightweight) |
| LLM needed | Yes - for fact extraction + entity resolution | Yes - cloud handles infrastructure |
| Data stays local | Yes | No |
| Persistent daemon | Auto-started by Hermes, idles after 5min | No daemon needed |

**Manual config (when `hermes memory setup` can't run interactively):**

```bash
# Create config directory
mkdir -p $HERMES_HOME/hindsight
```

Write `$HERMES_HOME/hindsight/config.json`:
```json
{
  "mode": "local_embedded",
  "llm_provider": "openai_compatible",
  "llm_base_url": "https://your-llm-endpoint/v1",
  "llm_model": "your-model-name",
  "recall_budget": "mid",
  "bank_id": "hermes",
  "timeout": 120,
  "idle_timeout": 300
}
```

Add env vars to `$HERMES_HOME/.env`:
```bash
HINDSIGHT_MODE=local_embedded
HINDSIGHT_LLM_API_KEY=<your-llm-api-key>
```

Then set the provider:
```bash
hermes config set memory.provider hindsight
```

**Installation - network considerations:**

On mainland China, `hindsight-all` regularly fails because it downloads PyTorch (~117MB), scikit-learn, ONNX models, and pg0 (embedded PostgreSQL). Total ~800MB. Use a domestic PyPI mirror:

```bash
UV_DEFAULT_INDEX=https://mirrors.aliyun.com/pypi/simple/ UV_HTTP_TIMEOUT=120 uv pip install "hindsight-all>=0.6.1"
```

Other mirrors: `https://pypi.tuna.tsinghua.edu.cn/simple/`

If the download still fails (common on unstable connections), background the install and proceed with config - the heavy download keeps retrying in the background.

**Supported LLM providers for local_embedded mode:**

| Provider | `llm_provider` | Notes |
|----------|---------------|-------|
| OpenAI | `openai` | Uses GPT-4o-mini by default |
| Anthropic | `anthropic` | Uses claude-haiku-4-5 by default |
| Any OpenAI-compatible | `openai_compatible` | Set `llm_base_url` to your endpoint |
| Ollama (local) | `ollama` | Uses gemma3:12b by default |
| OpenRouter | `openrouter` | Uses qwen/qwen3.5-9b by default |

The LLM key is used ONLY for fact extraction/entity resolution/synthesis - not for answering user queries. So a cheap/small model works fine here.

**When to use the slim client instead of the full package:**

If you have your own LLM endpoint (like opencode.ai, a local llama.cpp, vLLM), `hindsight-client` suffices for cloud and local_external modes. For **local_embedded** mode (daemon + embedded PostgreSQL), you MUST use `hindsight-all`.

```bash
# Cloud or local_external only:
uv pip install "hindsight-client>=0.6.1"

# Local embedded (includes daemon + DB + models):
UV_DEFAULT_INDEX=https://mirrors.aliyun.com/pypi/simple/ uv pip install "hindsight-all>=0.6.1"
```

**Verification:**

```bash
hermes memory status
# Expected: Provider: hindsight, Status: available ✓
```

When the daemon starts for the first time, it may take 10-30s. Logs at:
- Daemon startup: `$HERMES_HOME/logs/hindsight-embed.log`
- Runtime logs: `~/.hindsight/profiles/<profile>.log`

---

### Holographic (Lightweight Alternative)

If Hindsight's dependency footprint is too heavy, **Holographic** is the zero-dependency fallback:

- SQLite FTS5 store - no external DB, no API keys, no background daemon
- HRR algebra-based retrieval with trust scoring
- Tools: `fact_store` (9 actions) + `fact_feedback`
- Simply set `memory.provider: holographic` - nothing else to install

```bash
hermes config set memory.provider holographic
```

Best for: users who want reliable persistence without any infrastructure overhead.
