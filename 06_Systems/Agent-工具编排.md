---
title: Agent-工具编排
created: 2026-07-29
updated: 2026-08-01
type: workflow
scope: global
tags:
  - agent
  - automation
  - workflow
confidence: high
contested: false
---

# Agent-工具编排

> 这里定义 Agent 做判断，工具做执行的边界。

## 职责分工
- Agent：读上下文、做决策、拆步骤、判断优先级
- 工具：写文件、同步日程、发消息、查数据、归档
- 流程：输入 → 计划 → 执行 → 复盘 → 沉淀

## 常见链路
- 计划系统生成日计划
- 日计划触发飞书/微信同步
- 复盘系统回收结果
- 结果沉到永久笔记 / 领域页
- 知识库自动整理系统做增量归位、改链、删壳

## 适合放这里的内容
- cron 任务说明
- 自动化脚本说明
- Agent 协作规范
- 外部系统同步规则

## 相关入口
- [[06_Systems/index]]

