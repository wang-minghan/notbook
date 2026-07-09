---
title: RRF
created: 2026-07-08
updated: 2026-07-10
type: concept
tags: [ai, retrieval, ranking]
sources:
  - [[混合检索]]
  - [[RAG]]
confidence: high
contested: false
---

# RRF

RRF（Reciprocal Rank Fusion）用于融合多路召回结果。

## 公式
- score = Σ 1 / (k + rank_i)
- 常用 k 约 60

## 相关页面
- [[混合检索]]
- [[BM25]]
- [[Cross Encoder]]
- [[RAG]]
- [[AI知识体系概览]]
