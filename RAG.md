---
title: RAG
created: 2026-07-08
updated: 2026-07-10
type: concept
tags: [ai, retrieval, concept]
sources:
  - [[工作/工作经历/亚信科技（中国）有限公司]]
  - [[AI知识体系概览]]
confidence: high
contested: false
---

# RAG

RAG（Retrieval-Augmented Generation）是把检索到的可信上下文拼进生成前的推理流程。

## 基本流程
- 文档切片
- 向量化 / 关键词索引
- 检索召回
- 重排
- 拼接 prompt
- LLM 生成

## 在你项目里的位置
- 常和混合检索一起用
- 结合 BM25、RRF、Cross Encoder 提升质量
- 再叠加本体校验抑制幻觉

## 相关页面
- [[混合检索]]
- [[BM25]]
- [[RRF]]
- [[Cross Encoder]]
- [[本体约束]]
- [[Agent编排]]
- [[工作/工作经历/亚信科技（中国）有限公司]]
- [[AI知识体系概览]]
