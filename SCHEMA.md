---
title: 知识库 Schema 定义
created: 2026-08-03
updated: 2026-08-03
type: schema
scope: global
tags: [knowledge-base, schema, governance]
confidence: high
contested: false
---

# 知识库 Schema 定义

> 统一字段、类型、命名约束，供自动化脚本、模板、校验器共用。

## 通用 Frontmatter 字段

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `title` | string | ✅ | 页面标题，用于显示和搜索 |
| `created` | date (YYYY-MM-DD) | ✅ | 创建日期 |
| `updated` | date (YYYY-MM-DD) | ✅ | 最后修改日期（每次编辑必须更新） |
| `type` | enum | ✅ | 页面类型，见下方类型表 |
| `scope` | enum | ✅ | `global` / `section` / `local` — 决定是否进入全局 index |
| `tags` | string[] | ❌ | 横向筛选标签（状态、主题、来源），不用于结构化导航 |
| `week` | string (YYYY-Www) | ⚠️ | 周计划/日计划必填，格式如 `2026-W32` |
| `date` | date (YYYY-MM-DD) | ⚠️ | 日计划必填 |
| `weekday` | string | ⚠️ | 日计划必填，如 `Monday` |
| `confidence` | enum | ❌ | `high` / `medium` / `low` — 知识可信度 |
| `contested` | boolean | ❌ | 是否有争议/待验证 |
| `sources` | string[] | ❌ | 关键来源页面的 wikilink |

## 页面类型枚举

| type 值 | 含义 | 典型 scope | 示例 |
|---------|------|------------|------|
| `overview` | 索引/入口页 | `global` | `index.md`, `系统索引.md` |
| `hub` | 枢纽页，聚合同主题入口 | `section` | `项目索引`, `资料索引` |
| `entity` | 实体页（人、组织、工具） | `section`/`global` | `基本信息`, `鑫犇电子有限公司` |
| `concept` | 概念/方法/原理页 | `section`/`global` | `计划系统`, `复盘系统` |
| `comparison` | 对比/选型页 | `section` | 工具对比、方案选型 |
| `query` | 问题驱动页（Q&A、排查） | `section` | FAQ、故障排查 |
| `workflow` | 可执行流程/清单 | `section` | 模板、SOP、自动化编排 |
| `time` | 时间页（周/日计划、复盘） | `local` | `个人周计划.md`, `2026-08-03.md` |
| `generated` | 自动生成页（脚本产出） | `local` | 晨间简报、同步产出 |
| `raw` | 原始素材/速记/未整理 | `local` | `_inbox` 里的捕获页 |

## 命名约束

- 目录/文件：kebab-case（如 `06_Systems/plans/weekly/2026-W32/个人周计划.md`）
- wikilink 显示文本：中文自然语言（如 `[[06_Systems/计划系统|计划系统]]`）
- 日期文件：`YYYY-MM-DD.md`，放在周计划同级目录
- 周计划目录：`YYYY-Www`（ISO 周号），如 `2026-W32`

## Scope 判定规则

- `global`：仅 `index.md`、`log.md`、顶层骨架入口（01~09 索引）、核心实体/概念页
- `section`：各子目录的 `index-*.md`、hub 页、稳定 entity/concept
- `local`：所有 `time`、`generated`、`raw` 类型页 —— **绝不进入全局 index.md**

## 链接规范

- 语义关系**只用 wikilink** `[[path/to/page|显示名]]`
- 目录路径、相对链接、URL 不算语义链接，不参与图谱分析
- 反向链接由脚本维护，手动只管正向 wikilink

## 标签规范

- 只做状态/横向筛选：`planning`、`training`、`reading`、`active`、`archived`、`draft`
- 禁用：层级标签（如 `para/projects`）、重复目录结构的标签