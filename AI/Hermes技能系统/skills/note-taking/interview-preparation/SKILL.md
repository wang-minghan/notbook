---
name: interview-preparation
description: Organize interview Q&A content into visual, concise, personalized reference notes using tables and mermaid diagrams.
platforms: [linux, macos, windows]
tags: [interview, qna, obsidian, markdown, mermaid]
---

# Interview Preparation

Organize interview preparation notes — turn raw question lists into polished, visual reference documents the user can flip through before an interview.

## When to use

- User asks to "整理面试准备内容" (organize interview prep content)
- User has a folder of raw interview questions and wants them structured
- User wants to prepare Q&A notes for a job interview

## Core Rules

### 1. One-sentence answers — NO digression

Every question gets exactly **one concise sentence** (≤30 words in Chinese). No explanation, no background, no "first of all" — just the answer. The user can ask for follow-up; the document is for quick memorization.

```markdown
| **提问** | **一句话回答** |
|----------|--------------|
| LoRA是什么 | 低秩适配，冻结权重旁路插A×B矩阵(r=8~64)，只训旁路，显存降至1/3。 |
```

### 2. Personalize with the user's actual work experience

Every answer must reference **what the user actually did**. Use the user's job timeline:
- Job 1: topic, technique, project
- Job 2: topic, technique, project

❌ Wrong: "KAN替代了MLP的激活函数，适合可解释场景"
✅ Right: "在CAE降阶项目里用KAN替代DNN做POD系数→物理场插值，小样本拟合更好"

### 3. NEVER fabricate work experience

Only reference experiences **confirmed** by the user or their notes. If the source file lists questions about a topic the user hasn't worked on, label it clearly:

```markdown
> ⚠️ 以下我没有直接项目经验，属于面试覆盖知识，了解原理即可。
```

### 4. Tables are the primary format

Use a two-column table (question | answer) for every module. Compact and scannable.

### 5. Use mermaid diagrams for visual expression

Include at least one mermaid diagram per major section:
- `flowchart` — for system architecture, workflows, multi-step processes
- `timeline` — for career history
- `gantt` — for project timelines
- `mindmap` — for skill/personal overview
- `pie` — for tech stack proportion
- `flowchart LR/TD` with subgraphs — for comparing two approaches

### 6. Deduplicate personal info — use wikilinks, not inline copies

When the interview file lives in `工作/面试准备/` and personal info files exist under `个人信息/` (e.g. `资格证书与技能.md`, `教育经历.md`):

- **Do NOT** copy the full personal info (age, education timeline, cert list, skill mindmap) into the interview file
- **Do** redirect with a brief header:
  ```markdown
  > 个人完整信息见：[[资格证书与技能]] · [[教育经历]]
  ```
- Keep only the **interview-specific narrative** (positioning, talking points, story arc) in the interview file

**Why:** Personal info duplicates between `个人信息/` and `工作/面试准备/` become stale independently. Redirecting keeps single-source-of-truth and the interview file stays focused on what matters for the interview (story line, Q&A).

### 7. Emoji + color for visual hierarchy

- 🏢 / 🏭 for job labels
- ⚡ / ✅ / ❌ for emphasis
- Colored subgraph backgrounds (fill:#d5e8d4 for job 1, #e1d5e7 for job 2)
- 💬 for "interviewer says" oral practice sections

### 7. Narrative arc (故事线)

Connect the user's jobs with a story line showing:
- Problem → Solution → Next Problem → Next Solution
- How skills transferred from one job to the next
- The common thread (e.g., "领域知识嵌入模型推理")

### 9. Modify files directly

When the user says "直接在XX修改", overwrite the existing file. Don't create a parallel file unless asked.

## Structure template

```markdown
# 面试问答整理

> ⚡ [banner with oral practice tip]

---

## [🧬/🧑] 个人画像

> 个人完整信息见：[[资格证书与技能]] · [[教育经历]]
> 下方仅列出面试中需要表达的核心叙事。

| | 面试中要传达的点 |
|--|---------------|
| **🎯 定位** | ... |
| **🧩 差异点** | ... |
| **💡 一句话定位** | ... |

---

## [🗺️] 职业生涯全景图

[gantt timeline + detailed flowchart connecting two jobs]
> 💬 面试说：[oral summary]

---

## [🔗] 主线故事

[problem→solution flowchart]
> 💬 面试说：[oral summary]

---

## 1. [Section Name]

| 提问 | 一句话回答 |
|------|----------|
| ... | ... |

[optional mermaid diagram]

---

...

---

## 📌 面试应答策略

[STAR flowchart + strategy table]
```

## Pitfalls

- **Don't assume job count.** Start from the user's notes. If the file mentions 11 topic sections including topics the user hasn't worked on, don't infer extra jobs. Check with the user if uncertain.
- **Don't write long paragraphs.** The entire value of this skill is conciseness. A paragraph-length answer in the table defeats the purpose.
- **Don't lose the original file's structure.** The user already has categorized questions. Work with their categorization, don't invent new ones.
- **Don't skip the narrative arc.** The story line is what makes the document memorable in an interview.
- **Don't leave placeholder data** (name, education, dates) when you can reasonably infer or ask. If uncertain, use XX and tell the user.
