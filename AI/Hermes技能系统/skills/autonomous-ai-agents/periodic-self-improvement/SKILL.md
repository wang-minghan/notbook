---
name: periodic-self-improvement
description: "Run periodic self-improvement cycles as a cron job — understand the user, arm yourself, improve the user, and create unexpected value. A framework for recurring agent growth across multiple dimensions."
version: 1.1.0
author: Hermes Agent
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [cron, self-improvement, maintenance, vault, personal-growth]
---

# Periodic Self-Improvement Cycle

A framework for running recurring self-improvement/maintenance tasks as cron jobs. Use this when Hermes fires as a scheduled cron job with a mandate to improve itself, understand the user more deeply, and create lasting value — not just answer a single query.

## Trigger Conditions

Use this skill when all of the following are true:
- You are running as a **cron job** (no interactive user present; final response auto-delivered)
- The mandate includes **self-improvement** or **maintenance** — not a specific one-shot task
- You have access to the user's vault/workspace to read current state and write output

## Core Framework: Four Dimensions

Rotate through these each run. Pick **1-3** per cycle — never all four in one run. Vary your selection; don't repeat the same pattern every time.

### Dimension ① — Understand the User (了解用户)

**Purpose**: Build a richer user profile over time. Ask systematic questions that fill in the picture, one aspect per cycle.

**Example directions** (pick 1-2 per cycle, don't repeat the same question):
- Family background, upbringing
- Current city and why they chose it
- Career history and pivot points (e.g., why economics → data science)
- Life vision for 5 years out
- Personality self-assessment (strengths, weaknesses)
- Creative drivers (e.g., what drives their novel writing)
- What fitness/health means to them

**Method**: Ask the question in your final report. Store any new answers in **memory** (user profile) using the memory tool with `action="add"` and target `user`.

### Dimension ② — Arm Yourself (武装自己)

**Purpose**: Acquire real external knowledge to make yourself more capable.

**Actions** (pick 1-2):
- Check for Hermes releases/features: `curl` the GitHub API for the latest release, parse notable features
- Visit authoritative sources if accessible (Hermes docs, GitHub, etc.)
- Skill library maintenance: check for outdated skills, patch gaps
- Learn new tool-usage patterns and record them
- Improve communication style — review past sessions for improvement areas

**Fallback**: Network may be restricted (China). If a direct call fails, try an alternative source or skip. Never fabricate results from failed calls.

### Dimension ③ — Improve the User (提升用户)

**Purpose**: Create tangible value for the user based on your growing understanding of them.

**Actions**:
- Scan the user's current work focus (job search, fitness, creative writing, skill building)
- Create personalized plans and write them to the vault as notes
- Identify gaps: missing documents, empty form fields, outdated plans
- Each output must be **actionable** — specific steps, not general advice

**Output location**: Write files to the vault directory. Create a sensible directory structure (`个人提升/`, `工作/`, etc.) if needed.

### Dimension ④ — Creative Divergence (发散创造)

**Purpose**: Surprise the user with unexpected insights.

**Ideas** (vary each cycle):
- Analyze vault note connectivity — suggest reorganization or missing cross-links
- Check git status — alert on uncommitted changes
- **Check progress on pending tasks (novel status, job application forms)**
  - **Novel reader reviews**: If reader reviews are stuck in `.agent/status.md` as uncompleted, run the proxy reader workflow (see `references/novel-reader-review-proxy.md`) to unblock the project. When **multiple** chapters are pending simultaneously (e.g. ch4 + ch5), read them in narrative order and evaluate their relationship — a quiet chapter that follows an intense one may be structurally deliberate (contrast, comedown, setup).
  - **Job application forms**: Check Desktop and vault for `*应聘登记表*.docx` files. Extract text with pandoc to identify blank sections (see `references/docx-form-field-audit.md`). Cross-reference with vault content to generate fillable guidance notes.
- Recommend a high-quality resource (tool, article, course)
- Compare industry demand vs. user's current skills — find gaps
- Organize the user's skill tree
- Review your own recent answers — find ways to improve quality

## Workflow: Step by Step

### Phase 1: Scan Environment (always do this first)

```yaml
1. Check git status in the vault directory
2. List vault top-level directories
3. List subdirectories relevant to the user's current focus areas
4. Read key status files (project status, interview prep, novel progress)
5. Check for pending documents — both explicit markers (`【请填写】`) and **completely blank sections** in DOCX forms (e.g. 应聘登记表 sections 八/十一). See `references/docx-form-field-audit.md` for the audit workflow.
6. Check novel `.agent/status.md` for stuck reader reviews
```

### Phase 2: Choose Dimensions

```yaml
1. Recall which dimensions were done in recent sessions (rotate!)
2. Pick 1-3 dimensions, preferring ones not done recently
3. Consider the user's current state and what would be most valuable
```

### Phase 3: Execute

```yaml
For each dimension:
  - Do real work (write files, check resources, make changes)
  - If dimension ① produced new info, save to memory immediately
  - If dimension ② involved external resources, note what you found
  - If dimension ③ or ④, actually write files — don't just plan
```

### Phase 4: Report

Final message (auto-delivered by cron system — do NOT use send_message):

```
Structure:
  - One sentence summarizing what was done this cycle
  - Key findings/outputs
  - Any question from dimension ①
  - Tone: warm, friend-like, concise
```

## User Preferences (Tone & Style)

These are the user's explicit preferences. Embed them in every interaction.

| Preference | Rule |
|-----------|------|
| **Address** | Use "你" — never "您", "亲", "哈喽", or other formal/overly familiar address |
| **Tone** | Chat like a friend, not a system notification or report |
| **Language** | Chinese (Mandarin) |
| **Format** | Concise, no bullet-spam. Prefer flowing sentences with occasional line breaks |
| **Variety** | Don't do the same thing every cycle. Keep it fresh |
| **Scope** | 1-3 dimensions per cycle, never all four |
| **Execution** | Actually produce output (write files, make changes) — never stop at planning |
| **Honesty** | If a network call fails, say so. Never fabricate results |

## Pitfalls / Anti-Patterns

- **❌ Recurse**: Never create additional cron jobs from within a cron job. Manage only the current job.
- **❌ Repetition**: Don't ask the same questions or do the same analysis every cycle.
- **❌ Over-scope**: Don't do all 4 dimensions in one run. It burns too much context and feels robotic.
- **❌ Plan-only**: If you said you'd write a file, write it. Plans without execution are wasted cycles.
- **❌ Fabrication**: If a network call fails or a tool is blocked, report the blocker. Don't supply plausible-sounding but fake data.
- **❌ System-report tone**: Don't start with "已完成以下任务" or close with "汇报完毕". Talk like a person.
- **❌ Unstaged work**: After writing files, git add them so the user can push with one commit.

## Reference Files

- `references/vault-scan-patterns.md` — Common vault scanning workflows
- `references/hermes-release-check.md` — How to check for new Hermes releases and features
- `references/novel-reader-review-proxy.md` — How to perform a novel reader review from cron context when the awesome-novel dispatch chain didn't run it
- `references/docx-form-field-audit.md` — How to audit DOCX forms (应聘登记表, etc.) for blank/missing fields using pandoc, cross-reference with vault content, and generate fillable guidance notes

## Related Skills

- `obsidian` — Reading/writing vault notes
- `docx-templates` — DOCX form filling and analysis
- `hermes-agent` — Cron CLI commands, memory management
- `awesome-novel` — Novel writing workflow (for users who write)
