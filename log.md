---
title: AI 知识库日志
created: 2026-07-10
updated: 2026-07-19
type: log
scope: global
tags: [ai, knowledge-base, log]
sources:
  - [[index]]
confidence: high
contested: false
---

# AI 知识库日志

> 变更与维护记录。固定纪律写在顶部，下面是增量流水。
> Format: `## [YYYY-MM-DD] action | subject`

## 治理纪律（固定）

- `index.md` 只收 `global` 页；time 页（日/周计划）只进各自 section 索引。
- 目录是存储结构，不自动等于语义结构；是否进全局索引看页面类型和可复用性。
- 自动任务只做增量压缩：只写新增 / 修改 / 删除，不重写全库总结。
- 出现冲突保留并标记 `contested`，不覆盖。
- 优先效果最优（effect-first），不追求最小改动；但"如无必要不增加实体"。

## [2026-07-19] refactor | 融合元文件 + 删桩索引

- 删除 `SCHEMA.md`，其结构约定已并入 `index.md` 顶部「结构约定」。
- 删除 `知识库治理规范.md` 与 `知识库增量摘要.md`，治理纪律并入本页顶部，增量流水就在本页。
- 删除三个单子页桩索引：`个人信息/index-个人信息.md`、`个人提升/健康/index-健康.md`、`个人提升/读书/index-读书.md`；相关引用改指实际页面或父模块 hub（`个人信息/基本信息`、`个人提升/健康/运动身体信息`、`个人提升/index-计划`）。
- 新增预留位 `_inbox/`（含 `.gitkeep`），用于未归类速记，定期归档。
- `个人提升/index-计划.md` 升格为个人提升唯一 hub，`scope` 统为 `global`。
- 面试准备 4 页暂保留（主库 `面试提问内容整理` + 叙事/策略/知识点），重叠问题留待后续内容决策。
- 元文件从 5 个收敛为 2 个（index + log）；桩索引从 3 个清零。

## [2026-07-17] relink | 2026-W30 personal weekly plan

- Added `个人提升/周计划/2026-W30-个人周计划.md` to the weekly plan section index so the new time page is no longer semi-connected.
- Added the weekly section index back-link on the W30 page to keep the local graph bidirectional.
- This was a local graph repair only; `index.md` stayed untouched because time pages still do not belong in the global index.

## [2026-07-15] governance split + scope backfill

- Split governance spec out of SCHEMA; added `知识库增量摘要.md`; clarified directory ≠ semantic structure.
- Backfilled `scope` on key pages; time pages typed `time`, `scope: local`.
- Added module entry pages (`index-<module>.md`) so global index only links module hubs.
