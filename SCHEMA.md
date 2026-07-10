---
title: AI 知识库 Schema
created: 2026-06-27
updated: 2026-07-10
type: schema
tags: [ai, knowledge-base, schema]
sources:
  - [[index]]
  - [[log]]
  - [[karpathy-llm-wiki-spec]]
confidence: high
contested: false
---

# AI 知识库 Schema

## 领域
这个库是用户的主知识库，服务于：
- Hermes + Obsidian 的知识管理
- AI / 技术 / 工作 / 个人成长 / 读书 / 面试准备
- 可持续累积的知识图谱，而不是一次性笔记堆

## Karpathy 目标
- 把库从“能找”优化成“会长”
- 让 wiki 成为 raw source 和 query 之间的编译层
- 把 index / schema / log 作为真正的系统骨架
- 鼓励重构，只要它让知识网络更强

## 结构原则
- 文件夹负责粗分类，wiki 链接负责语义关系
- 原始资料与整理结论分层管理
- 先建索引，再扩内容；先连接，再扩散
- 优先效果最优，不追求最小改动
- 知识库必须可持续维护：能 ingest、能 query、能 lint、能回写

## 生命周期
- raw：原始资料，尽量只读，不直接改写
- ingest：把新资料编译成实体页/概念页/比较页/查询页
- wiki：持续维护的编译产物，知识应该在这里累积
- query：高质量问答结果要回写进知识库
- workflow：可重复执行的训练路径与行动模板
- lint：周期性检查孤岛、半孤岛、断链、冲突、缺页
- refine：先最小修复，再做重构和合并

## 维护目标
- 每个关键页至少有 2 个相关链接
- 重要枢纽页双向链接
- 原始资料和编译结果分层存放
- 重要结论不要只停留在聊天中
- 出现冲突时保留并标记 `contested`

## 页面类型
### entity
适合：公司、项目、岗位、工具、模型、产品、课程、书籍、人物

### concept
适合：RAG、Agent、知识图谱、LoRA、POD、KAN、图谱维护、面试策略

### comparison
适合：Karpathy wiki vs 传统笔记、Hermes vs 其他 agent、不同模型 / 工具 / 工作流的取舍

### query
适合：高质量问答、面试答题、迁移回顾、问题诊断

### overview
适合：总索引、体系总览、主题地图

### workflow
适合：持续改进流程、可重复执行的训练路径、每日/每周行动模板

### report / log / schema
适合：审计、迁移、规范、结构说明

## Frontmatter
每个核心页都建议使用：
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | overview | log | schema | report | workflow
tags: [ai, knowledge-base]
sources: []
confidence: high | medium | low
contested: false
---
```

## 标签约定
先控制在少量稳定标签，避免 tag 爆炸：


## 链接规则
- 每个新页面尽量至少链接 2 个相关页
- 重要枢纽页要双向链接
- 对照关系优先显式写出来，不靠记忆

## 更新规则
- 新增或修改页面时，更新 `updated`
- 出现冲突时不要覆盖，保留并标记 `contested`
- 重要结论尽量写进 `query` 或 `comparison`，不要只留在聊天记录里

## Hermes 协作规则
Hermes 负责：阅读、归类、提炼、交叉链接、更新索引、维护日志

Obsidian 负责：人工浏览、图谱查看、手工修订、长期沉淀

## 相关页面
- [[index]]
- [[log]]
- [[vault-classification-2026-07-08]]
