# Community Plugins for Hermes Agent

> Last surveyed: 2026-06-27
> Source: GitHub API search for `hermes plugin` + `topic:hermes` + awesome lists

## 🧠 Memory & Context Enhancement

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-lcm** | 792 | `git clone → plugins/` (see note ⚠) | Lossless Context Management — DAG-based context engine that never loses a message |
| **ClawMem** | 188 | `plugins install yoloshii/ClawMem` | On-device memory layer + hybrid RAG search. Hooks + MCP server |
| **scope-recall-hermes** | 142 | `plugins install 410979729/scope-recall-hermes` | Scope-aware recall, LanceDB semantic search, SQLite truth store |
| **icarus-plugin** | 137 | `plugins install esaradev/icarus-plugin` | Self-memory and replacement models — remember your work, train your replacement |
| **hermes-membase** | 12 | `plugins install aristoapp/hermes-membase` | Persistent AI memory for Hermes |

## 🔍 Search Enhancement

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-web-search-plus** | 315 | `plugins install robbyczgw-cla/hermes-web-search-plus` | Multi-provider web search + extraction with intelligent routing and quality reports |

## 📊 Observability & Analytics

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-labyrinth** | 291 | `plugins install stainlu/hermes-labyrinth` | Read-only observability: journeys, crossings, guideposts, reports |
| **cronalytics** | 95 | `plugins install 8bit64k/cronalytics` | Cron job analytics dashboard for agentic automations |
| **sigil-hermes** | 5 | `plugins install alexander-akhmetov/sigil-hermes` | Grafana AI observability integration |

## 🚀 Productivity & Dev Tools

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-skill-factory** | 406 | `plugins install Romanescu11/hermes-skill-factory` | Auto-watches workflows and generates reusable skills |
| **hermes-kanban** | 254 | `plugins install GumbyEnder/hermes-kanban` | Obsidian Kanban + Hermes autonomous project executor |
| **42-evey/hermes-plugins** | 249 | `plugins install 42-evey/hermes-plugins` | Bundle: goal management, inter-agent bridge, model selection, cost control |
| **rtk-hermes** | 188 | `plugins install ogallotti/rtk-hermes` | Rewrites shell commands for 60-90% LLM token savings |
| **planforge-hermes** | 9 | `plugins install AxDSan/planforge-hermes` | Spec-driven development planning, GSD-inspired |
| **agentplane-hermes-plugin** | 5 | `plugins install basilisk-labs/agentplane-hermes-plugin` | Spawn AgentPlane as external worker lane |

## 🌐 Social & Platform Integration

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-tweet** | 15 | `plugins install Xquik-dev/hermes-tweet` | X/Twitter automation through Xquik |
| **clawsocial-hermes-plugin** | 6 | `plugins install mrpeter2025/clawsocial-hermes-plugin` | Social discovery for AI agents |
| **hermes-meshtastic-adapter** | 4 | `plugins install amscotti/hermes-meshtastic-adapter` | Connects Hermes to a Meshtastic LoRa mesh |
| **Heimdall-SL-Hermes-Agent** | 4 | `plugins install hrabanazviking/Heimdall-SL-Hermes-Agent` | Autonomous Second Life Agent |

## 🤖 Reasoning & LLM Routing

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **hermes-reasoning-router-plugin** | 6 | `plugins install Team-Volt/hermes-reasoning-router-plugin` | Automatic Discord/Telegram reasoning-effort routing |
| **Sibyl-Memory** | 88 | `plugins install Sibyl-Labs/Sibyl-Memory` | Long time-horizon persistent memory with relational context |

## 🔧 Network & Connectivity

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **ClawRouter-Hermes** | 15 | `plugins install BlockRunAI/ClawRouter-Hermes` | 55+ LLMs, x402 USDC micropayments on Base & Solana |
| **Seidr-Smidja** | 12 | `plugins install hrabanazviking/Seidr-Smidja` | VRM (anime avatar) control for AI agents |
| **watchline-hermes-plugin** | 3 | `plugins install qordinate-ai/watchline-hermes-plugin` | Register Watchline event watches |

## 🧪 Research & Specialized

| Plugin | Stars | Install | Description |
|--------|-------|---------|-------------|
| **proofrail-hermes** | 21 | `plugins install 410979729/proofrail-hermes` | LoopCraft runtime harness with evidence-first execution |

## 📋 Install Method Notes

⚠️ **hermes-lcm** — `hermes plugins install stephenschoettler/hermes-lcm` may not work on all setups (depends on plugin.yaml metadata). Reliable fallback:

```bash
cd ~/AppData/Local/hermes/plugins/
git clone https://github.com/stephenschoettler/hermes-lcm
hermes plugins enable hermes-lcm
hermes config set context.engine lcm
```

Requires `context.engine: lcm` in config.yaml — this replaces the built-in compressor engine, enabled via `hermes config set context.engine lcm`. Takes effect on next session.

## 📚 Awesome Lists (Discovery Starting Points)

| Name | Stars | URL |
|------|-------|-----|
| **0xNyk/awesome-hermes-agent** | 4,232 | https://github.com/0xNyk/awesome-hermes-agent |
| **SamurAIGPT/awesome-hermes-agent** | 1,779 | https://github.com/SamurAIGPT/awesome-hermes-agent |
| **aliaihub/awesome-hermes-usecases** | 124 | https://github.com/aliaihub/awesome-hermes-usecases |
| **ZeroPointRepo/awesome-hermes-skills** | 68 | https://github.com/ZeroPointRepo/awesome-hermes-skills |
| **ChuckSRQ/awesome-hermes-skills** | 67 | https://github.com/ChuckSRQ/awesome-hermes-skills |

## Finding New Plugins

To refresh this list, run from terminal:

```bash
# Search by topic
curl -s "https://api.github.com/search/repositories?q=topic:hermes&sort=stars&per_page=30" | \
  python -c "import json,sys; [print(f'⭐{r[\"stargazers_count\"]:5d} | {r[\"full_name\"]}') for r in json.load(sys.stdin)['items']]"

# Search by keyword
curl -s "https://api.github.com/search/repositories?q=hermes+plugin&sort=stars&per_page=30" | \
  python -c "import json,sys; [print(f'⭐{r[\"stargazers_count\"]:5d} | {r[\"full_name\"]} | {r.get(\"description\",\"\")[:80]}') for r in json.load(sys.stdin)['items']]"
```
