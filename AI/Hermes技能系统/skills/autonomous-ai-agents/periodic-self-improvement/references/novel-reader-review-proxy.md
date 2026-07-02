# Novel Reader Review — Proxy Execution (Cron Context)

When running as a cron-based self-improvement cycle, you may discover that novel reader reviews are **stuck** — the `.agent/status.md` shows uncompleted `[ ]` items for reader review, but no reader agent has been dispatched (because the novel-agent chain was interrupted or the project is waiting on manual progress).

This reference documents how to act as a **proxy reader agent** from within the periodic-self-improvement cycle, without needing the novel-agent dispatch chain.

## Detection

During vault scan (Phase 1), check:

```bash
# Read the novel project's status file
cat <vault>/原创小说/色情小说/<project>/.agent/status.md
```

Look for lines like:
```
- [ ] 第X卷·第Y章「标题」reader 评审
- [ ] 第X卷·第V章「标题」reader 评审
```

If `current_volume` and `current_chapter` indicate the project is paused waiting on reader reviews, you have a stuck review to handle.

## Required Reading (minimum)

To produce a useful reader review, read these files **before** forming any opinion:

| File | Why |
|------|-----|
| `archives/vol-{N}-ch-{M}-{slug}.draft.md` | The actual chapter draft — must read first, no cheating |
| `chapters/vol-{N}-ch-{M}.md` | Chapter outline — to understand the author's intent |
| `settings/genre-setting.md` | Genre/type — sets reader expectations |
| `.agent/task/reader-order-vol-{N}-ch-{M}.md` | Reader order with specific evaluation criteria |
| `settings/writing-style.md` | (optional) Writing style baseline |
| `.claude/knowledge/chapter-quality-checklist.md` | (optional) Quality standards the project uses |

## The Reader Agent Persona

DO NOT produce a "review report" or "audit summary". Adopt the reader agent persona from the project's `.claude/agents/reader.md`:

- **Identity**: A jaded genre-fiction reader who's read thousands of chapters. Hard to impress, but fair. Speaks in plain language, not QA-speak.
- **Tone**: Casual, direct, opinionated. Say "this part slapped" or "this dragged" — not "the pacing requires optimization".
- **Output**: Answer three core questions:
  1. What did it feel like to read?
  2. Do you want to read the next chapter?
  3. Did it hit (be aroused/disturbed/satisfied — depending on genre)?
- **Format**: Start with first reaction → highlight what worked → point out specific problems (with line references) → final verdict (one sentence + will-you-continue).

## What NOT to do

- ❌ Don't write a "评审报告" with numbered dimensions or scores — the reader agent speaks like a person, not QA.
- ❌ Don't proofread for typos — that's not the reader's job.
- ❌ Don't suggest plot changes that span future chapters — evaluate only the current chapter.
- ❌ Don't rewrite anything — reader is read-only, review goes in the final cron message, not into a file.
- ❌ Don't check the outline first and then check if the draft "matches" — read the draft first, form an impression, then consult the outline to understand authorial intent.

## Structured Review Flow

```
Phase 1: Immersive Read
  Read the draft from start to finish without note-taking.
  Let the text do its work. Notice when you speed up, slow down,
  skip, or re-read a passage. That's data.

Phase 2: First Reaction (口语化)
  Write down immediate gut reaction in 2-3 sentences.
  "双龙那章读得我——操，太满了。不是字多，是物理上的满。"

Phase 3: Sharp Analysis
  For each feeling from Phase 2, trace back to specific craft choices:
  - What made a passage hit? (比喻贯穿、白描冷峻、声音细节)
  - What made a passage drag? (多余的环境描写、心理独白泄气)
  - Were there moments of genuine immersion? Why?
  Reference specific lines or paragraphs.

Phase 4: Final Verdict
  - Would you click "next chapter"? (Yes / Yes-but / No)
  - One sentence summary that could sell or kill the chapter.
  - Single biggest issue (if any), with line evidence.

## Where to Put the Review

The review goes into your **final cron message** — not into a file in the novel project directory. The reader agent in the awesome-novel workflow is read-only and doesn't write files. You're performing a proxy read, not persisting an artifact.

In the final report, use a section like:

```
📖 读者评审：第四卷·第4章「双龙」

**第一反应：** [口语化的直观感受]
**好的地方：** [2-3个亮点，有具体依据]
**可以更狠的地方：** [1-2个问题，有原文依据]
**终局判决：** [追读意愿 + 致命伤 + 一句话]
```

## When to Bypass

If the draft files are missing or too short (< 200 words), don't force a review. Note the gap in the cron message and move on. A thin draft means the chapter wasn't actually written yet, and reader review isn't appropriate.
