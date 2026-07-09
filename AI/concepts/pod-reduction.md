---
title: POD降维
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, work, ai]
sources:
  - [[北京灵易数智科技有限公司]]
confidence: high
contested: false
---

# POD降维

POD（Proper Orthogonal Decomposition）是你第一段工作里最关键的降维方法之一，核心是把高维工程场映射到低维模态空间，再在低维空间中做建模和预测。

## 核心思路

- 对样本矩阵做 SVD
- 取前 k 个主模态作为基底
- 用能量阈值控制模态数量
- 把高维场投影到低维系数上建模
- 最后再反投影恢复物理场

## 价值

- 显著降低训练和推理复杂度
- 让小样本条件下的建模更稳
- 提升模型泛化能力
- 非常适合工程场 / CAE 数据

## 相关页面
- [[北京灵易数智科技有限公司]]
- [[小样本代理建模]]
- [[模型服务化]]
- [[AI知识体系概览]]
