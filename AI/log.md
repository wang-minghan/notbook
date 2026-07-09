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
