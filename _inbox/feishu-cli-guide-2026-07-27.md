# 飞书 CLI 能力全景 & 你的起步建议

> **创建时间**：2026-07-27  
> **创建者**：Hermes Agent (via lark-cli)  
> **关联 Obsidian**：`C:\Users\32027\OneDrive\notebook`  
> **当前配置**：App ID `cli_aad4cd9059f89cdd` | Brand `feishu` | Workspace `hermes` | User `王名涵`

---

## ✅ 权限验证清单（实测通过）

| 能力域 | 验证命令 | 结果 | 关键产出 |
|--------|----------|------|----------|
| **日历-读** | `lark-cli calendar +agenda` | ✅ 通 | 今日日程为空（符合预期） |
| **日历-写** | `lark-cli calendar +create ...` | ✅ 通 | `event_id: 56b45990-853e-4fa8-9ad5-deb870dfe4e9_0` |
| **云文档-写** | `lark-cli docs +create --doc-format markdown` | ✅ 通 | `doc_id: NRfbd91iSolMaHxe07AcHrTtnbD` → [文档链接](https://gwrj1n5umf9.feishu.cn/docx/NRfbd91iSolMaHxe07AcHrTtnbD) |
| **知识库-列表** | `lark-cli wiki spaces list` | ✅ 通 | 2 个空间：`示例知识库`、`亚信公司工作整理个人` |

---

## 📋 飞书 CLI 完整能力矩阵（v1.0.73）

| 大类 | Skill 名称 | 核心能力 | 适用场景 |
|------|-----------|----------|----------|
| **日历** | `lark-calendar` | 增删改查事件、议程视图、会议室、重复规则 | 固定时间块同步、会议自动创建 |
| **云文档** | `lark-doc` | 创建/读取/更新 Docx/Markdown、Block 操作、XML/MD 双格式 | 周报生成、会议纪要、知识沉淀 |
| **知识库** | `lark-wiki` | 空间/节点 CRUD、权限、导入导出 | 团队/个人 Wiki、项目文档库 |
| **多维表格** | `lark-base` | 建表、字段、记录、视图、仪表盘、Workflow | 数据看板、训练/身体/饮食趋势图表 |
| **电子表格** | `lark-sheets` | 读写单元格、区域、图表、数据验证 | 轻量数据处理、导入导出 |
| **幻灯片** | `lark-slides` | 创建/编辑 PPT、母版、动画、导出 | 汇报演示、周复盘 Deck |
| **云盘/文件** | `lark-drive` | 上传/下载/搜索/分享/文件夹 | 素材归档、附件管理 |
| **即时消息** | `lark-im` | 发送消息、富文本/卡片、群管理、Webhook | 微信同款推送、告警通知 |
| **任务** | `lark-task` | 创建/查询/更新任务、子任务、提醒 | 个人待办、协作任务流 |
| **审批** | `lark-approval` | 发起/查询/处理审批实例、定义检索 | 报销、请假、采购流程 |
| **考勤** | `lark-attendance` | 打卡记录查询 | 出勤统计 |
| **妙搭应用** | `lark-apps` | 应用全生命周期、UI 设计、部署、监控 | 低代码业务系统开发 |
| **通讯录** | `lark-contact` | 用户/部门/群组查询 | 组织架构同步、@人 |

> 💡 **查看全部**：`lark-cli skills list`  
> 💡 **读取某 Skill 详细文档**：`lark-cli skills read <skill-name> [references/xxx.md]`

---

## 🎯 基于你的画像：优先起步的 4 个能力

你的工具链：**Obsidian（单一事实源） + 训记（训练/身体/饮食） + 飞书（落地/协作/移动端） + 微信（触达）**  
职业目标：**算法工程师 → 3-5 年转管理** | 训练/工作/恢复/备餐 四大固定块

| 优先级 | 能力 | 为什么选它 | 与现有流的连接点 |
|--------|------|------------|------------------|
| **P0** | **日历** | 固定块（训练/工作同步/恢复/备餐）落地到移动端，系统日历提醒零遗漏 | `daily-feishu-sync` cron → 读 Obsidian 周/日计划 → 写飞书日历（色块区分） |
| **P0** | **云文档** | 周复盘/月复盘沉淀为可协作、可手机阅读、可导出 PDF 的文档 | `weekly-review` cron → 生成 Markdown → `lark-cli docs +create` → 分享链接发微信 |
| **P1** | **多维表格** | 训练/身体/饮食/阅读多维度趋势图表化，比文本更直观 | 训记 API → 定时写 Base 记录 → 仪表盘自动刷新 |
| **P1** | **即时消息** | 早简报/晚复盘/异常告警直接推飞书消息（比微信更适合工作场景） | cron 任务完成后 → `lark-cli im +send` 发给自己或群 |

---

## 🛠 立即可跑的最小闭环（3 步走）

### 步骤 1：恢复 `daily-feishu-sync` cron（已删 google-workspace 版）
```bash
# 新建同步脚本 ~/.hermes/scripts/sync_obsidian_to_feishu_calendar.py
# 逻辑：读 Obsidian daily/weekly 计划 → 解析固定块 → lark-cli calendar +create/+update
# cron: 0 12,19 * * *  (早/晚各一次增量同步)
```

### 步骤 2：周复盘自动发云文档
```bash
# 在 weekly-review cron 末尾追加：
lark-cli docs +create \
  --title "📊 周复盘 $(date '+%Y-W%U')" \
  --doc-format markdown \
  --content "$(cat reviews/weekly/2026-W30.md)"
# 返回 doc_url → 微信推送给自己
```

### 步骤 3：建一个「个人仪表盘」多维表格
```bash
# 手动建一次 Base（或脚本建表）：
# 表 1: 训练记录 (日期, 部位, 动作, 组数, 重量, RPE, 时长, 心率)
# 表 2: 身体指标 (日期, 体重, 体脂, 胸围, 腰围, 臂围, 腿围)
# 表 3: 饮食汇总 (日期, 热量, 蛋白, 碳水, 脂肪, 达标率)
# 表 4: 阅读统计 (日期, 时长, 完成书籍, 新增笔记)
# 然后配置仪表盘：趋势图 + 完成率仪表盘 + 热力图
```

---

## 📐 设计原则（按你的偏好定制）

1. **Obsidian 为单一事实源** — 飞书只做「落地/协作/移动端触达」，不做主存储  
2. **单向写入为主** — Obsidian → 飞书，避免双写冲突  
3. **固定块优先同步** — 训练/工作同步/恢复/备餐这四类固定时间块最先同步  
4. **可视化 > 文本** — 日历用色块，表格用图表，文档用大纲  
5. **极客最小化** — 先跑通最小闭环，再加仪表盘，再加工作流

---

## 🔗 关键资源链接

| 资源 | 链接 |
|------|------|
| 飞书 CLI 官网 | https://www.feishu.cn/feishu-cli |
| GitHub 仓库 | https://github.com/larksuite/cli |
| CLI 内置 Skill 文档 | `lark-cli skills read <skill-name>` |
| 当前配置文件 | `C:\Users\32027\.lark-cli\hermes\config.json` |
| Obsidian Vault | `C:\Users\32027\OneDrive\notebook` |

---

## 🚀 下一步行动清单

| 优先级 | 动作 | 预估工时 | 产出 |
|--------|------|----------|------|
| **P0** | 写 `sync_obsidian_to_feishu_calendar.py` 并接入 cron | 30 min | `daily-feishu-sync` 恢复运行 |
| **P0** | `weekly-review` cron 末尾加云文档创建 + 微信推送 | 15 min | 周复盘自动落云文档 |
| **P1** | 手建「个人仪表盘」多维表格 4 表 + 仪表盘页 | 45 min | 趋势可视化入口 |
| **P1** | 早简报/晚复盘改推飞书消息（或双推） | 10 min | 触达渠道升级 |
| **P2** | 微信读书划线 → 云文档自动追加（知识沉淀） | 30 min | 读书笔记自动化 |

---

> **备注**：飞书 CLI 版本当前 `1.0.73`，最新 `1.0.77`。建议跑 `lark-cli update` 后再正式投产。  
> 所有 `lark-cli` 命令均在 `hermes` profile 下以**用户身份**执行，拥有你在飞书上可见的全部权限。

---

*本文档由 Hermes Agent 自动生成并通过 `lark-cli docs +create` 写入飞书云文档。*  
*源 Markdown 同步保存在 Obsidian：`_inbox/feishu-cli-guide-2026-07-27.md`*