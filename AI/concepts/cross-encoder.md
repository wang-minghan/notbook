---
title: Cross Encoder
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, ranking, retrieval]
sources:
  - [[面试提问内容整理]]
  - [[亚信科技（中国）有限公司]]
confidence: high
contested: false
---

# Cross Encoder

Cross Encoder 是你在检索系统中用于精排的模型，输入 query 与候选文档后，对两者做联合建模并输出相关性分数。

## 作用
- 精排召回结果
- 提升最终相关性
- 修正粗召回带来的噪声

## 在你项目里的位置
- 接在 RRF 后面
- 对 BM25 + 向量融合后的候选集做精排
- 是 RAG 质量控制的重要一环

## 相关页面
- [[RAG]]
- [[混合检索]]
- [[RRF]]
- [[亚信科技（中国）有限公司]]
- [[AI知识体系概览]]
