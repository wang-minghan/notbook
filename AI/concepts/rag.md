---
title: RAG
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, ai, retrieval]
sources:
  - [[亚信科技（中国）有限公司]]
  - [[亚信科技-工作经历]]
confidence: high
contested: false
---

# RAG

RAG（Retrieval-Augmented Generation）是你第二段工作里的核心底座之一，目标是让大模型在生成前先检索到可信上下文。

## 基本流程
- 文档切片
- 向量化 / 关键词索引
- 检索召回
- 重排
- 拼接 prompt
- LLM 生成

## 你项目里的特点
- 不是单一路径检索，而是混合检索
- 结合 BM25 和向量召回
- 通过 RRF 融合与 Cross Encoder 重排提高质量
- 再叠加本体校验抑制幻觉

## 相关页面
- [[亚信科技（中国）有限公司]]
- [[混合检索]]
- [[本体约束]]
- [[Agent编排]]
- [[AI知识体系概览]]
