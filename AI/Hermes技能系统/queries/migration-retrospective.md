---
title: Hermes 技能系统迁移回顾
created: 2026-07-08
updated: 2026-07-08
type: query
tags: [hermes, migration, query, skill, docs]
sources:
  - [[reports/MIGRATION_REPORT]]
  - [[docs/README]]
  - [[docs/ARCHITECTURE]]
confidence: high
contested: false
---

# Hermes 技能系统迁移回顾

## 这次迁移解决了什么

最核心的变化是：把用户自定义/扩展技能从官方 bundled skills 中分离出来，放到独立的外部 Git 仓库中维护，并通过 `skills.external_dirs` 让 Hermes 扫描加载。

## 为什么要这么做

- bundled skills 是稳定基线，不该被个人定制污染
- 外部仓库更适合版本控制和回滚
- 迁移后，技能维护与知识整理可以同时进行
- Obsidian 可以作为技能图谱和维护笔记层

## 迁移后的结构收益

- 官方目录更干净
- 用户技能更容易扩展
- 文档、报告、规则、流程可以独立演化
- 未来可通过 cron / git 自动化保持同步

## 结论

这不是“换了一个存放位置”这么简单，而是把 Hermes 的技能维护升级成了一个**可持续治理系统**。

## 相关页面
- [[AI/Hermes技能系统/docs/README]]
- [[AI/Hermes技能系统/docs/ARCHITECTURE]]
- [[AI/Hermes技能系统/concepts/sync-and-maintenance]]
- [[AI/Hermes技能系统/index]]
- [[AI/Hermes技能系统/log]]
