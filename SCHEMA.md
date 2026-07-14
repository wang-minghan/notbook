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
- Obsidian 的知识管理与长期沉淀
- 工作 / 个人成长 / 面试准备 / 个人信息
- 可持续累积的知识图谱，而不是一次性笔记堆

## Karpathy 目标
- 把库从“能找”优化成“会长”
- 让 wiki 成为 raw source 和 query 之间的编译层
- 把 index / schema / log 作为真正的系统骨架（只应该是目录规范而不是具体实现）
- 鼓励重构，只要它让知识网络更强

## 当前主干
- `工作任务/`：工作经历、面试准备与工作相关知识
- `个人信息/`：稳定个人资料与基础背景
- `个人提升/`：长期成长、计划、读书与方法论

## 处理原则
- 默认建立引用，只有在语义足够强时，才升级为组合
- 只有在严格满足 "is-a" 时，才允许继承
- 删除了的页面，不再继续在总目录里挂死链
- 目录只做粗分类，入口页负责把最常用的内容串起来
- 参考层、技能层、实现层如果不是知识内容本身，就不要塞进主目录索引

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
- 避免或者减少信息孤岛

## 治理规则
- 先看 `index`，再看 `SCHEMA`，最后看 `log`
- 每次结构性改动都要回写 `log`
- 周期性检查孤岛、重复概念、空壳页、断链和缺页
- 先列清单，再决定删除、合并或补全
- 索引页负责主入口，治理页负责执行细则
- 治理规则是结构规则的一部分，不是附录

## 页面类型
### entity
适合：公司、项目、岗位、工具、人物、经历承载页

### concept
适合：方法、机制、模型、策略、流程、原则

### comparison
适合：取舍、对照、优缺点分析

### query
适合：高质量问答、面试答题、迁移回顾、问题诊断

### overview
适合：总索引、体系总览、主题地图

### workflow
适合：持续改进流程、可重复执行的训练路径、行动模板

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
