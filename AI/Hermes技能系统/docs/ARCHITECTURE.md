---
title: Hermes 技能系统架构
created: 2026-07-08
updated: 2026-07-10
type: concept
tags: [hermes, concept, architecture, skills]
sources:
  - [[AI/Hermes技能系统/docs/README]]
  - [[AI/Hermes技能System/docs/USAGE_AND_SYNC]]
  - [[AI/Hermes技能系统/reports/MIGRATION_REPORT]]
confidence: high
contested: false
---

# Hermes 技能系统架构

这页记录 Hermes 技能系统的运行与管理架构：bundled skills、外部 skills 仓库、Git 管理层与 Obsidian 维护层之间怎么分工。

## 目标状态
- 外部 skills 仓库是唯一编辑入口
- bundled skills 只读，不再手改
- Git 负责版本历史，Obsidian 负责结构解释
- 迁移、同步、维护形成闭环 workflow

## 运行层
- 官方 bundled skills：`C:\Users\32027\AppData\Local\hermes\skills`
- 外部用户 skills：`C:\Users\32027\Desktop\tools\notbook\AI\Hermes技能系统\skills`

## 配置层
Hermes 使用：
```yaml
skills:
  external_dirs:
    - C:\Users\32027\Desktop\tools\notbook\AI\Hermes技能系统\skills
```

## 管理层
- Git：版本管理、回滚、diff、同步
- Obsidian：技能图谱、说明、标签、关系网络
- Cron：周期性检查与同步

## 约束
- 新增自定义 skill 不再直接写入官方 bundled skills 目录
- 优先在外部 skills 仓库维护，再由 Hermes 扫描加载
- 迁移报告和维护说明要回链到总索引

## 相关页面
- [[AI/Hermes技能系统/docs/README]]
- [[AI/Hermes技能系统/docs/USAGE_AND_SYNC]]
- [[AI/Hermes技能系统/reports/MIGRATION_REPORT]]
- [[AI/Hermes技能系统/index]]
- [[AI/index]]
