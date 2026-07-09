---
title: Karpathy LLM Wiki 规范
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [ai, knowledge-base, karpathy, wiki]
sources:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - [[knowledge-base-lifecycle]]
  - [[SCHEMA]]
confidence: high
contested: false
---

# Karpathy LLM Wiki 规范

这是把当前知识库重构成 Karpathy 式 compounding wiki 的目标说明，不是对现状的描述。

## 目标
- 把原始资料变成可持续编译的 wiki
- 让知识不是“查出来”，而是“累积出来”
- 把页面分成 entity / concept / comparison / query / overview / log / schema
- 让 index、schema、log 成为真正的骨架，而不是摆设

## 核心要求
- **raw sources 只读**：原始资料尽量不直接改写
- **wiki 持续维护**：LLM 负责整理、链接、更新、冲突标记
- **schema 先于内容**：先定义规则，再扩展内容
- **cross-reference 优先**：每个核心页都要能回链到枢纽
- **query / comparison 要回写**：高质量问答不能只停留在聊天里
- **知识要 compounding**：每次 ingest 都让图谱更强，而不是更乱

## 推荐结构
- `raw/`：原始来源，只读
- `indexes/`：总览、导航、枢纽
- `entities/`：人、组织、项目、工具、作品
- `concepts/`：方法、机制、框架、原则
- `comparisons/`：A vs B、选型、取舍
- `queries/`：一次问题的高质量答案
- `logs/`：迁移、审计、重构记录

## 维护动作
1. ingest 新资料
2. 抽实体、概念、比较、查询
3. 更新相关页面
4. 补双向链接
5. 记录日志
6. 做 lint
7. 继续 refine

## 这套库的优化目标
不是“最小改动”，而是：
- 更清晰的页面类型
- 更高的枢纽中心性
- 更少的隐性知识
- 更强的可持续维护性
- 更像一个能越用越值钱的知识引擎

## 相关页面
- [[AI知识体系概览]]
- [[knowledge-base-lifecycle]]
- [[karpathy-wiki-vs-traditional-notes]]
- [[AI/index]]
- [[SCHEMA]]
- [[log]]
