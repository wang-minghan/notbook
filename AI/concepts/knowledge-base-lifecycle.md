---
title: Knowledge Base Lifecycle
created: 2026-07-08
updated: 2026-07-08
type: concept
tags: [ai, knowledge-base, workflow, maintenance]
sources:
  - [[AI/SCHEMA]]
  - [[AI/index]]
  - [[AI/log]]
confidence: high
contested: false
---

# Knowledge Base Lifecycle

这页定义这套知识库的实际工作流：**raw → ingest → wiki → query → lint → refine**。

## 1) Raw
原始资料是不可轻易改写的输入层：
- 文章、PDF、截图、聊天记录、网页摘录
- 只负责保留来源，不负责总结结论

## 2) Ingest
把新资料编译进知识库，而不是只堆进笔记：
- 提取实体、概念、比较、问题结论
- 归类到对应页面类型
- 更新相关索引页
- 记录变更到 log

## 3) Wiki
Wiki 是持续维护的编译产物：
- 实体页：人、公司、项目、工具、书、课程
- 概念页：方法、机制、框架、原则
- 比较页：选型、权衡、A vs B
- 查询页：一次问题的高质量答案

## 4) Query
好的回答要能回写：
- 重要结论写进 `query`
- 可复用判断写进 `comparison`
- 新发现的关系写进实体/概念页

## 5) Lint
周期性巡检知识图：
- 孤岛页
- 半孤岛页
- 断链/错链
- 重复页
- 过时结论
- 缺失概念
- 冲突与 `contested` 标记

## 6) Refine
修复与整理的原则：
- 先连起来，再追求美观
- 先保留，再合并
- 先最小修复，再大重构
- 重要内容优先成为可链接页面

## 维护约定
- 每个关键页至少有 2 个相关链接
- 重要枢纽页双向链接
- 原始资料与编译结果分层放置
- 新知识尽量不要只留在聊天中

## 适用场景
- 个人成长
- AI / 技术知识积累
- 工作经历与面试材料
- 读书与研究
- Hermes 协作维护
