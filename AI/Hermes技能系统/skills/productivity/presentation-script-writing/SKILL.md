---
name: presentation-script-writing
description: Write TED-style presentation scripts (逐字稿) for Chinese audiences. Convert technical/academic content into natural conversational delivery with Chinese annotations for English terms. Creates both the manuscript and coordinated PPT.
version: 1.0.0
author: hermes-agent
license: MIT
metadata:
  hermes:
    tags: [presentation, script-writing, academic, public-speaking]
---

# Presentation Script Writing (逐字稿写作)

Write a full presentation script that sounds natural when spoken aloud — not like reading bullet points off a slide. Designed for Chinese audiences who need English term annotations.

## Core Principles

### 1. TED Style = Spoken, Not Written

TED talks sound conversational because speakers use techniques that feel like talking, not reading:

| Technique | Example | Effect |
|-----------|---------|--------|
| **Rhetorical question** | "你们用AI查过资料吗？" | Engages audience immediately |
| **Story hook** | "我给大家看一个具体的例子" | Creates anticipation |
| **Short punchy sentences** | "用过的人都懂" | Feels natural and familiar |
| **Metaphor / Analogy** | "大模型本质上是个猜词游戏" | Makes abstract concrete |
| **Contrast** | "RAG给AI材料 — 本体约束给AI画路" | Clarifies difference |
| **Number emphasis** | "51%存在严重问题" | Data lands harder spoken |
| **Self-questioning** | "等等——那是不是问题就解决了？" | Leads audience through reasoning |

### 2. Chinese Audience — English Term Rules

**ALWAYS annotate English terms on first appearance:**

| First Use | Later Use |
|-----------|-----------|
| "幻觉（Hallucination）" | "Hallucination" or "幻觉" |
| "检索增强生成（RAG）" | "RAG" |
| "本体约束（Ontology-Constrained Reasoning）" | "本体约束" |
| "语义检索（Dense Retrieval）" | "语义检索" |

Never assume English terms are understood. Every acronym gets a Chinese expansion + plain-language explanation on first use.

### 3. Five-Paragraph Rhythm per Major Point

1. **Hook** — question or relatable scenario (5-10 sec)
2. **Context** — why this matters (10-15 sec)
3. **Core idea** — the key point, with metaphor if possible (15-20 sec)
4. **Evidence** — data, example, or citation (10-15 sec)
5. **Bridge** — transition to next point (5 sec)

Total per slide: ~45-90 sec spoken = fits a 10-min talk (12 slides).

## Workflow

### Step 1: Read the source material
Load the source outline/manuscript. Identify:
- Core message (one sentence that summarizes everything)
- 3-5 key takeaways the audience must remember
- All English terms that need Chinese annotations

### Step 2: Research reference TED talks
Before writing, study 2-3 TED transcripts in a similar domain:
- Note opening hooks (how they draw you in)
- Track how they handle technical concepts (metaphors, analogies)
- Observe sentence length and rhythm
- Extract 3-5 specific techniques to imitate

### Step 3: Rewrite — Script First, Slides Second
Write the spoken script first. The slides serve the script, not vice versa.

**Script structure:**
```
## [Slide N] — [Title] ~[time]

> [Brief reminder of what the slide shows]

[Script text — written to be spoken aloud]
```

**Anti-patterns to avoid:**
- ✗ "现在翻到第X页" (audience doesn't need navigation cues)
- ✗ Reading bullet points verbatim
- ✗ Long 50+ word sentences (impossible to speak naturally)
- ✗ English without Chinese explanation
- ✗ "本指南介绍……"/"本报告旨在……" (too formal for spoken)
- ✗ Academic paper tone in spoken delivery

### Step 4: Add delivery annotations
Include speaker notes at the end:
- Timing per section
- Where to slow down or emphasize
- Pronunciation hints for English terms
- Body language cues for key numbers

### Step 5: Update the PPT
After rewriting the script, update the PPT to match:
- Slide titles should be conversational questions/statements, not technical labels
- English terms on slides must have Chinese subtitles
- Remove any text that's only useful as a reading script (shorten slides)
- Add visual emphasis where the script has emphasis

## Sample Script Segment (Before/After)

**Before (stiff, resembles bullet points):**
> "RAG即检索增强生成技术，通过检索外部知识库来增强大模型的生成能力。该技术由Lewis等人于2020年提出。检索过程分为三步……"

**After (TED style, conversational):**
> "RAG的逻辑特别简单，我打个比方——你不该让学生裸考，你应该给他一本参考书，告诉他答案都在书里，你翻到相关内容再回答。概念上就是三步——第一步，先翻书找答案；第二步，把找的内容摆在桌上；第三步，看着材料回答问题。就这么简单。"

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Paragraphs too long when written | Break after every 2-3 sentences. Breathe. |
| Too many English terms in one slide | Limit to 3-4 new terms per slide; all get Chinese annotation |
| Data without context | Every data point needs a "so what" follow-up |
| No transition between slides | Each slide ends with a bridge ("那问题来了——……") |
| Script reads like an essay | Read aloud and cut any sentence that doesn't sound like you |
| Overusing the same technique | Don't open 3 slides in a row with questions — vary hooks |
