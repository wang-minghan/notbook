---
title: LoRA微调
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, training, ai]
sources:
  - [[亚信科技（中国）有限公司]]
confidence: high
contested: false
---

# LoRA微调

LoRA 是你在亚信项目里用于领域适配的核心微调方法，用低秩旁路参数来高效适配 Qwen 等基础模型。

## 核心特点
- 冻结原模型参数
- 训练低秩旁路矩阵
- 显著降低显存和训练成本
- 适合领域小样本微调

## 你项目中的作用
- 领域知识对齐
- 改善业务术语与回答风格
- 配合 RAG / 本体约束增强落地效果

## 相关页面
- [[Qwen]]
- [[亚信科技（中国）有限公司]]
- [[Agent编排]]
- [[AI知识体系概览]]
