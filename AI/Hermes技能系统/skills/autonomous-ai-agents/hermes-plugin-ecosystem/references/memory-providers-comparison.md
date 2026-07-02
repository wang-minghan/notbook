# Hermes Memory Providers Comparison

Research gathered 2026-06-27. Benchmarks are directional, not directly comparable (different tasks/datasets).

## At a Glance (Free/Local Options Only)

| Provider | Free tier | Benchmark | Storage | Deps footprint | Daemon? |
|----------|----------|-----------|---------|---------------|---------|
| **mem0 OSS** | Full local free | LongMemEval-S 67.6% | Qdrant vector DB | `mem0ai` + `qdrant-client` (~50MB) | No — in-process |
| **Hindsight** | Full local free | LongMemEval 91.4-94.6% | PostgreSQL + pgvector | `hindsight-all` **~800MB** (Torch, pg0, ONNX) | Yes — pg0 emb. PostgreSQL |
| **Holographic** | Full local free | N/A | SQLite FTS5 | **Zero** (stdlib only) | No |
| **OpenViking** | Self-host free | N/A | Configurable | Requires Ollama + server | Yes |
| **ByteRover** | Local CLI free | LoCoMo 92.2% | Local | pip install | No |
| **Built-in** | Always free | N/A | Text files in config dir | Zero | No |

## Hindsight Architecture Details

- **TEMPR** = 4 parallel retrieval strategies: Temporal, Entity, Metadata, BM25
- **3-stage pipeline**: Retain (ingest) → Recall (retrieve) → Reflect (synthesize across stored knowledge)
- Published paper: arXiv 2512.12818 (Virginia Tech)
- License: MIT
- GitHub: vectorize-io/hindsight (2.4K stars)

### Config Keys (local_embedded mode)

| Key | Default | Description |
|-----|---------|-------------|
| `mode` | — | `cloud`, `local_embedded`, or `local_external` |
| `llm_provider` | — | `openai`, `anthropic`, `gemini`, `groq`, `openrouter`, `minimax`, `ollama`, `lmstudio`, `openai_compatible` |
| `llm_base_url` | — | Required for `openai_compatible` — full URL to /v1 endpoint |
| `llm_model` | provider default | Model name for extraction/synthesis |
| `bank_id` | `hermes` | Memory bank name/identifier |
| `recall_budget` | `mid` | `low`/`mid`/`high` — controls recall aggressiveness |
| `timeout` | 120s | API request timeout |
| `idle_timeout` | 300s | Daemon idle shutdown (0 = never) |

### Environment Variables

| Env Var | Required For | Notes |
|---------|-------------|-------|
| `HINDSIGHT_MODE` | Any | `local_embedded` or `cloud` |
| `HINDSIGHT_LLM_API_KEY` | local_embedded | Used for extraction/synthesis, NOT user Q&A |
| `HINDSIGHT_API_KEY` | cloud | From ui.hindsight.vectorize.io |
| `HINDSIGHT_BANK_ID` | Optional | Overrides config.json bank_id |
| `HINDSIGHT_TIMEOUT` | Optional | Overrides config.json timeout |
| `HINDSIGHT_IDLE_TIMEOUT` | local_embedded | Daemon idle timeout in seconds |

### LLM Provider Notes

- The LLM is used ONLY for memory extraction/entity resolution/synthesis — NOT for answering user queries
- A small/cheap model works fine (the extraction task is much simpler than full Q&A)
- For `openai_compatible`: any OpenAI-API-compatible endpoint works (llama.cpp, vLLM, LM Studio, opencode.ai)
- OpenRouter auto-sets `llm_base_url` to `https://openrouter.ai/api/v1`

### Daemon Behavior

- Auto-started by Hermes on first memory operation
- Idle timeout: defaults to 300s (5 min), configurable via `idle_timeout` or `HINDSIGHT_IDLE_TIMEOUT`
- Set `idle_timeout: 0` to keep daemon running permanently
- Startup logs: `$HERMES_HOME/logs/hindsight-embed.log`
- Runtime logs: `~/.hindsight/profiles/<profile>.log`
- First startup may take 10-30s (pg0 initializes + downloads base models)

### Daemon Port

Default: `http://localhost:8888`
