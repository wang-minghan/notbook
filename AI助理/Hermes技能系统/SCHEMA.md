# Hermes 技能系统 Schema

## 领域
本子库专注于 Hermes Agent 的技能、工作流、文档、迁移与维护。

## 结构原则
- `skills/`：可执行/可维护的技能内容
- `docs/`：架构、使用、同步、约定
- `reports/`：迁移、审计、清单
- `references/`：可复用参考资料
- `templates/`：模板与标准化骨架
- `scripts/`：辅助脚本

## 页面类型
- `overview`：总览页
- `schema`：规则页
- `index`：索引页
- `log`：日志页
- `entity`：具体 skill、文档、工具、流程
- `concept`：技能设计、维护策略、协作方式
- `comparison`：不同方案/插件/策略对比
- `query`：某次分析或决策结果

## 标签
- `hermes`
- `skill`
- `workflow`
- `docs`
- `migration`
- `maintenance`
- `index`
- `log`
- `comparison`
- `query`

## 协作规则
- 新技能优先维护在外部仓库
- 文档和索引必须同步更新
- 重要改动写入 log
- 能复用的经验沉淀为 references 或 concept 页

## 迁移优先级
1. docs 与索引
2. 高价值 skills
3. references 与 templates
4. 迁移报告与审计结果

## 相关页面
- [[AI助理/Hermes技能系统/index]]
- [[AI助理/Hermes技能系统/docs/README]]
- [[AI助理/Hermes技能系统/log]]
- [[index]]
- [[SCHEMA]]
