---
title: Hermes 技能系统
created: 2026-06-27
updated: 2026-07-08
type: overview
tags: [ai, hermes, skill, knowledge-base]
sources: []
confidence: high
contested: false
---

# Hermes 技能系统

这是你知识库里最重要的“工具中枢”之一：它把 Hermes 的外部 skills、管理文档、迁移记录和维护流程组织成一个可持续维护的系统。

## 结构
- `skills/`：Hermes 扫描的外部技能目录
- `docs/`：架构、约定、同步说明
- `reports/`：迁移报告、清单、审计结果
- `concepts/`：编译后的概念页
- `queries/`：可复用的迁移问答与回顾
- `workflows/`：可复用的 prompt / 维护流程

## 运行方式
- 官方 bundled skills 保留在 `C:\Users\32027\AppData\Local\hermes\skills`
- 用户扩展 skills 统一迁移到本目录下
- Hermes 通过 `skills.external_dirs` 加载这里的技能
- 通过 Git 版本管理，避免技能维护失控

## 在知识库中的作用
这个目录不只是技能仓库，它也是：
- Hermes 协作规则的来源
- AI 工作流的说明书
- 可复用方法的沉淀地
- 未来自动化维护的入口

## 相关页面
- [[AI/SCHEMA]]
- [[AI/index]]
- [[AI/log]]
- [[AI知识体系概览]]
- [[AI/Hermes技能系统/concepts/architecture]]
- [[AI/Hermes技能系统/concepts/sync-and-maintenance]]
- [[AI/Hermes技能系统/queries/migration-retrospective]]
- [[AI/Hermes技能系统/docs/workflows/ppt-prompt-node-formula]]
- [[AI/Hermes技能系统/reports/migration-report]]
