---

title: AI 知识体系概览
created: 2026-06-27
updated: 2026-07-08
type: overview
tags: [ai, knowledge-base, overview]
sources: []
confidence: high
contested: false
---

# AI 知识体系概览

这是 `AI/` 目录的总览页，也是你主知识库向 Karpathy 式 LLM Wiki 迁移的起点。

## 核心定位

你当前的 AI 知识体系有两条主线：
- **物理仿真领域**：北京灵易数智相关经验，包含 POD、代理模型、小样本预测
- **业务智能领域**：亚信科技相关经验，包含 RAG、本体约束、Agent、LoRA、部署

## 技术地图

```text
领域知识嵌入模型推理
├── 物理仿真领域（北京灵易数智）
│   ├── POD 降维
│   ├── 代理模型（KAN / RBF / DNN / Kriging）
│   └── 小样本预测
│
└── 业务智能领域（亚信科技）
    ├── RAG（BM25 + 向量 + 重排）
    ├── 本体约束（Neo4j / 路径裁剪 / 关系校验）
    ├── Agent 架构
    ├── 模型微调（Qwen + LoRA）
    └── 推理部署（vLLM + Kubernetes）
```

## 差异化定位

- 工业界实战链路完整
- 跨领域能力强，能从仿真迁移到 LLM
- 方法论统一，适合抽象成可复用概念页
- 很适合和 Hermes 技能系统一起打通，形成“知识 + 工具 + 工作流”的闭环

## 当前优先补齐的主题

- [[AI/Hermes技能系统/docs/README|Hermes 技能系统]] — AI 工具与技能中枢
- [[AI/concepts/pod-reduction]]
- [[AI/concepts/small-sample-surrogate]]
- [[AI/concepts/model-serving]]
- [[AI/concepts/kan]]
- [[AI/concepts/rag]]
- [[AI/concepts/hybrid-retrieval]]
- [[AI/concepts/ontology-constraint]]
- [[AI/concepts/agent-orchestration]]
- [[AI/concepts/lora-finetuning]]
- [[AI/concepts/qwen]]
- [[AI/concepts/python]]
- [[AI/concepts/transformer]]
- [[AI/concepts/bm25]]
- [[AI/concepts/rrf]]
- [[AI/concepts/cross-encoder]]
- [[AI/concepts/neo4j]]
- [[AI/concepts/vllm]]
- 知识图谱基础（RDF / OWL / Neo4j / SPARQL）
- 模型量化与部署（vLLM / TensorRT / ONNX）
- 面试高频算法题整理

## 相关入口

- [[SCHEMA]] — 知识库规则
- [[index]] — 总索引
- [[log]] — 变更日志
- [[工作/工作经历/北京灵易数智-工作经历]]
- [[工作/工作经历/北京灵易数智科技有限公司]]
- [[工作/面试准备/面试提问内容整理]]
- [[个人信息/教育经历总览]]
