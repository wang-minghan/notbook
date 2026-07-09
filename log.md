---
title: AI 知识库日志
created: 2026-07-10
updated: 2026-07-10
type: log
tags: [ai, knowledge-base, log]
sources:
  - [[SCHEMA]]
  - [[index]]
confidence: high
contested: false
---

# AI 知识库日志

> 记录知识库的结构迁移、索引维护与重要重构。
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-07-08] create | AI wiki skeleton
- Created `SCHEMA.md` for knowledge-base conventions.
- Created `index.md` as the AI knowledge entry point.
- Created `log.md` for structural change tracking.
- Began mapping existing vault content into wiki-style pages.

## [2026-07-08] add | knowledge-base lifecycle
- Added `AI/concepts/knowledge-base-lifecycle.md` to formalize raw → ingest → wiki → query → lint → refine.
- Extended `AI/SCHEMA.md` with lifecycle and maintenance rules.
- Linked the lifecycle page from `AI/index.md`.
- Scheduled weekly graph lint for orphan/semi-orphan detection.

## [2026-07-08] add | query page classification
- Reclassified `工作/面试准备/面试提问内容整理.md` as a query page.
- Added a query-page frontmatter/header so it can be maintained as a reusable interview answer bank.
- Linked the interview query page from `AI/index.md`.

## [2026-07-08] refine | daily fitness-meal reminder
- Upgraded the daily fitness cron into a weekday-rotating training + meal reminder.
- Added a direct mapping from weekdays to training splits and recovery days.
- Tightened the output to微信-friendly training + meal + checklist format.
- Added a default common-food pantry plus purchase-backlog handoff into the weekly plan template.

## [2026-07-10] refine | Hermes skill-system graph cleanup
- Added `AI/Hermes技能系统/docs/workflows/ppt-prompt-node-formula.md` to the main AI index.
- Added the same page to the Hermes sub-wiki index so it has a natural hub.
- Upgraded the note to typed `concept` frontmatter and linked it back to `AI/index` and the Hermes sub-wiki.
- This was a minimal graph fix: no content rewrite, just structure and bidirectional links.

## [2026-07-10] refine | Hermes skills subwiki relink
- Added frontmatter and explicit cross-links to `AI/Hermes技能系统/docs/workflows/ppt-prompt-node-formula.md` so it reads as a reusable workflow instead of a dangling note.
- Switched the Hermes subwiki index and migration query to explicit `AI/Hermes技能系统/...` links to remove path ambiguity around `SCHEMA` and `log`.
- Added the PPT prompt workflow into the Hermes subindex and the top-level AI index so it sits back under the main navigation instead of floating off alone.
- Recorded the maintenance path in the Hermes subwiki docs and kept the change scope intentionally tiny: no raw sources rewritten, no large refactor.

## [2026-07-10] refine | graph hub back-links
- Grouped the obvious hub pages into `AI/index`, `AI/Hermes技能系统/index`, `AI/SCHEMA`, and `AI/log`.
- Added explicit related-page back-links on the schema and log pages so they stop reading like isolated rule stubs.
- Kept the pass minimal: hub links first, leaf pages later.

## [2026-07-10] refine | AI concept relink pass
- Tightened `AI/AI知识体系概览.md` so it explicitly links back to `AI/index`, `AI/SCHEMA`, `AI/log`, and the Hermes sub-wiki.
- Rewrote the related-page blocks on core AI concept pages (`RAG`, `混合检索`, `BM25`, `RRF`, `Cross Encoder`, `本体约束`, `Agent编排`) to use explicit canonical links.
- This pass focused on true concept nodes, not skills/references leaf assets.

## [2026-07-10] refine | Karpathy-style wiki optimization pass
- Reframed the AI wiki toward Karpathy-style compounding wiki goals: persistent compilation, explicit schema, overview/comparison/query pages, and bidirectional hubs.
- Added and normalized the Karpathy target/spec page plus the comparison page so the knowledge base points at a clearer end state.
- Upgraded core concept pages into canonical nodes with typed frontmatter and backlinks so they can function as reusable graph anchors.
- This pass intentionally optimized the end-state graph, not the edit count.

## [2026-07-10] refine | management-workflow graph cleanup
- Promoted `个人提升/管理岗转型-4周实操计划.md` into a typed workflow page and linked it from the weekly/daily planning stack.
- Normalized `时间计划日程.md` plus the weekly and daily templates to use the same canonical management-workflow name.
- Added explicit links between the planning templates and the management workflow so the personal planning stack behaves like a reusable graph instead of isolated forms.
