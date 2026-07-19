---
title: AI 知识库日志
created: 2026-07-10
updated: 2026-07-19
type: log
scope: global
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
- Removed the obsolete `管理岗转型-4周实操计划.md` workflow from the personal planning stack and removed its references from the plan overview.
- Normalized `时间计划日程.md` plus the weekly and daily templates to use the same canonical management-workflow name.
- Added explicit links between the planning templates and the management workflow so the personal planning stack behaves like a reusable graph instead of isolated forms.

## [2026-07-10] refine | personal planning loop wiring
- Created `个人提升/周计划/2026-W28-个人周计划.md` and `个人提升/日计划/2026-07-10.md` as the first concrete execution pages copied from the templates.
- Reframed the planning flow so cron jobs should write to running pages under `周计划/` and `日计划/`, not overwrite the templates.
- Kept the templates as canonical blueprints and the dated pages as the live working copies.

## [2026-07-10] weekly plan | 2026-W28 personal planning
- Wrote back `个人提升/周计划/2026-W28-个人周计划.md` from the weekly template, health profile, and current plan shell.
- Filled training, work, reading, and diet sections; added next-week menu and a de-duplicated shopping list.
- Kept the existing page structure intact and only completed the empty sections.

2026-07-11 / notebook graph cleanup / index, 个人计划总览, 周计划, 日计划, 运动身体信息, 精英的傲慢-笔记, 被讨厌的勇气-笔记, log / 串起个人计划、健康和阅读页，压掉重复入口并补回主入口链接。

2026-07-10 / 每日健康做菜提醒 / 个人提升/日计划/2026-07-10.md, log.md / 按周计划写入今天的上肢容量训练、增肌饮食、采购提醒和复盘框架。

2026-07-10 / 每日健康做菜提醒 / 个人提升/日计划/2026-07-10.md, log.md / 按周计划写入今天的上肢容量训练、增肌饮食、采购提醒和复盘框架。

## [2026-07-11] refine | knowledge-base governance spec
- Added `个人提升/知识库治理规范.md` to define the maintenance order, lint flow, and output standards.
- Linked the governance page from `index.md` so it sits in the main navigation.
- This adds the missing governance layer between schema and weekly maintenance.
2026-07-13 / 每日健康做菜提醒 / 个人提升/日计划/2026-07-13.md, log.md / 按周计划写入今天的 Push 训练、当天菜单、采购提醒和复盘框架。
## [2026-07-13] weekly plan + shopping list | 2026-W29 personal planning
- Wrote the next-week page `个人提升/周计划/2026-W29-个人周计划.md` instead of extending W28.
- Rebased the week on current fitness baselines, kept the 4–5 training cadence, and compressed the shopping list to reduce duplicates.
- Kept the output focused on next week’s training, food, recovery, and purchase planning.

## [2026-07-14] daily health reminder | 个人提升/日计划/2026-07-14.md, log.md
- Based on `2026-W28` weekly plan, today is Pull 背部二头 day.
- Wrote the daily page with the pull session, the划船 progression note, and today’s meal menu.
- Kept the reminder aligned to the weekly menu: 黑椒牛肉饭 + 生菜 / 鸡蛋豆腐盖饭 + 青菜.

2026-07-15 / notebook graph cleanup / index.md, 个人提升/index-计划.md, 个人提升/周计划/2026-W29-个人周计划.md, 个人提升/日计划/2026-07-13.md, 个人提升/日计划/2026-07-14.md, log.md / 串起当前周计划和两天日计划，补回主入口并压掉半孤岛。
2026-07-15 / notebook graph cleanup / index.md, 个人提升/index-计划.md, log.md / 合并个人计划主入口，补回索引与计划总览的双向链接。

2026-07-15 / knowledge-base governance split / SCHEMA.md, index.md, 知识库治理规范.md, 知识库增量摘要.md / 把时间页从全局索引里剥离，新增增量压缩摘要页，明确目录只是存储结构不是语义结构。
2026-07-15 / scope backfill + template hardening / @模板/个人计划模板（日）.md, @模板/个人计划模板（周）.md, 工作任务/工作经历/北京灵易数智科技有限公司.md, 工作任务/工作经历/亚信科技（中国）有限公司.md, 工作任务/面试准备/面试提问内容整理.md, 工作任务/面试准备/面试应答策略.md, 工作任务/面试准备/面试叙事主线.md, 工作任务/面试准备/面试知识点.md, 个人信息/基本信息.md, 个人提升/健康/运动身体信息.md, 个人提升/index-计划.md, 个人提升/周计划/2026-W29-个人周计划.md, 个人提升/日计划/2026-07-14.md / 给关键页补上 scope，模板默认 local，避免自动任务继续把时间页抬进全局索引。
2026-07-15 / time-page retype / @模板/个人计划模板（日）.md, @模板/个人计划模板（周）.md, 个人提升/周计划/2026-W28-个人周计划.md, 个人提升/周计划/2026-W29-个人周计划.md, 个人提升/日计划/2026-07-10.md, 个人提升/日计划/2026-07-11.md, 个人提升/日计划/2026-07-12.md, 个人提升/日计划/2026-07-13.md, 个人提升/日计划/2026-07-14.md / 把日周计划从 workflow 改成 time，并补齐 scope: local，避免自动任务再把时间页当成全局知识页。
2026-07-15 / local section hubs / 个人提升/周计划/index-周计划.md, 个人提升/日计划/index-日计划.md, 个人提升/index-计划.md / 新增周计划与日计划的局部入口，避免时间页继续混进全局索引。
2026-07-15 / module entry pages / 个人信息/index-个人信息.md, 个人提升/index-计划.md, 个人提升/健康/index-健康.md, 个人提升/周计划/index-周计划.md, 个人提升/日计划/index-日计划.md, 工作任务/index-工作任务.md, 工作任务/工作经历/index-工作经历.md, 工作任务/面试准备/index-面试准备.md, @模板/index-模板.md / 给每个稳定模块补了自己的入口页，并把全局索引改成只挂模块入口。
2026-07-15 / personal growth index merge / index.md, 个人提升/index-计划.md, 个人提升/健康/index-健康.md, log.md / 合并个人提升的入口页，保留 index-计划 为唯一入口并更新相关链接。

## [2026-07-17] relink | 2026-07-16 daily plan
- Added `个人提升/日计划/2026-07-16.md` to `个人提升/日计划/index-日计划.md` so the new time page is no longer semi-connected.
- Kept the fix local to the day-plan section index; no global index reshuffle was needed.

## [2026-07-17] weekly plan | 2026-W30 personal planning
- Wrote the next-week page `个人提升/周计划/2026-W30-个人周计划.md` from the current week plan, today’s daily plan, the body baseline note, and the weekly template.
- Kept the focus on training cadence, reading continuity, food / purchase planning, and recovery rhythm.
- Recommended `龙族Ⅲ：黑月之潮（下）` so next week can continue the current reading thread without switching books.

## [2026-07-19] relink | 2026-W30 personal weekly plan
- Added `个人提升/周计划/2026-W30-个人周计划.md` to the weekly plan section index so the new time page is no longer semi-connected.
- Added the weekly section index back-link on the W30 page to keep the local graph bidirectional.
- This was a local graph repair only; `index.md` stayed untouched because time pages still do not belong in the global index.
