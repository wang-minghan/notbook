---
title: RRF
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, retrieval, ranking]
sources:
  - [[面试提问内容整理]]
  - [[亚信科技（中国）有限公司]]
confidence: high
contested: false
---

# RRF

RRF（Reciprocal Rank Fusion）是你在混合检索里用来融合多路召回结果的排名融合方法。

## 公式
- score = Σ 1 / (k + rank_i)
- k 常用 60 左右

## 价值
- 不依赖分数尺度统一
- 对多路检索结果融合稳定
- 适合 BM25 + 向量召回的融合

## 在你项目里的位置
- 融合 BM25 和 BGE 召回结果
- 再交给 Cross Encoder 精排
- 提升最终召回质量

## 相关页面
- [[混合检索]]
- [[RAG]]
- [[亚信科技（中国）有限公司]]
- [[AI知识体系概览]]
