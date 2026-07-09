---
title: 小样本代理建模
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [concept, work, ai]
sources:
  - [[北京灵易数智科技有限公司]]
confidence: high
contested: false
---

# 小样本代理建模

这是一条贯穿你工程经历的核心能力：在样本不多、计算昂贵、物理约束强的情况下，用代理模型逼近真实系统。

## 常见方法
- RBF
- Kriging
- DNN
- KAN

## 选型逻辑
- 样本很少：优先考虑更稳的插值/代理方法
- 非线性强：考虑更灵活的模型
- 需要可解释：倾向 KAN
- 需要不确定性：考虑 Kriging

## 价值
- 降低昂贵仿真的调用频率
- 提升工程迭代速度
- 把科研式方法变成可落地工程系统

## 相关页面
- [[北京灵易数智科技有限公司]]
- [[POD降维]]
- [[KAN]]
- [[RBF]]
- [[Kriging]]
- [[DNN]]
