---
title: Karpathy 式知识库 vs 传统笔记
created: 2026-07-08
updated: 2026-07-08
type: comparison
tags: [ai, knowledge-base, comparison, workflow]
sources:
  - [[AI/SCHEMA]]
  - [[AI/concepts/knowledge-base-lifecycle]]
  - [[AI/index]]
confidence: high
contested: false
---

# Karpathy 式知识库 vs 传统笔记

## 结论
Karpathy 式知识库不是“多记笔记”，而是把知识库当成一个**持续编译的产物**：原始资料进来后，LLM 会把它整理、链接、更新、巡检、再回写。

传统笔记更像是**仓库**，Karpathy 式 wiki 更像是**编译后的代码库**。

## 对比
| 维度   | 传统笔记      | Karpathy 式知识库                    |
| ---- | --------- | -------------------------------- |
| 目标   | 记录        | 维护可复用知识图                         |
| 处理方式 | 看到什么记什么   | ingest → 整理 → 回写                 |
| 知识组织 | 文件堆积、目录分层 | wiki 链接网络 + index + log          |
| 质量控制 | 靠人肉回忆     | lint + 结构巡检 + 持续修复               |
| 问答结果 | 常散落聊天     | 回写成 query / comparison / concept |
| 演化方式 | 低频手动整理    | 高频增量维护                           |

## 对你当前库的启发
- 你已经有了 wiki 骨架，但还需要更强的整理机制
- 现有内容里，工作经历与 AI 概念最适合先进入知识图主干
- 读书笔记和计划页适合逐步升级为 query / comparison / concept

## 相关页面
- [[AI/concepts/knowledge-base-lifecycle]]
- [[SCHEMA]]
- [[index]]
- [[log]]
