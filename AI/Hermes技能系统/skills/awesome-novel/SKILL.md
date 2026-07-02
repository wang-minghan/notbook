---
name: awesome-novel
description: 和 AI 协作写小说的工作流系统。7 个 agent 协作完成从设定到归档的完整写作流程。入口检测 → 初始化/迁移 → 交 novel-agent 调度。适用场景：从零写新小说、导入已有小说。
---

# Novel — 小说创作工作流

和 AI 一起写小说。本 skill 负责项目状态检测、新项目初始化、旧版项目自动迁移，完成后将控制权交给 novel-agent。

## 检测流程 — 严格按此执行，禁止跳过

```
检测项目状态
├─ story.yaml 存在 → 旧版 2.x → 执行自动迁移（见下文）
├─ story.md 不存在 → 询问作者是否初始化 → 是则执行 init.py
│   └─ python tools/init.py [project-path] [--genre <编号>] → 完成后 @novel-agent
└─ story.md 存在 → 已有项目
    ├─ 检查同步新鲜度
    │   ├─ python tools/sync-project.py . --check → exit 0 → 已最新，略过
    │   ├─ python tools/sync-project.py . --check → exit 1 → 有更新
    │   │   └─ 展示变更文件，询问作者是否同步
    │   │       ├─ 确认 → 运行 python tools/sync-project.py .
    │   │       └─ 跳过 → 继续
    │   └─ .agent/.sync-fingerprint 不存在（首次）
    │       └─ 静默运行 python tools/sync-project.py . → 写入指纹
    └─ → @novel-agent 继续写作
```

**强制规则：**
- `story.md` 不存在时，**先询问作者**是否要在此目录创建小说项目，确认后再运行 `init.py`
- 禁止未经确认直接执行 `init.py`
- 确认后必须运行 `init.py`，禁止手动创建目录结构替代
- **禁止在 skill 安装目录（含 `skills/awesome-novel` 路径）内运行 `init.py`** — 此目录是技能仓库，不是小说项目
- 如果当前目录是 skill 安装目录，应提示作者切换到目标目录后再执行
- `init.py` 执行完毕后，确认 `.agent/status.md` 和 `.claude/agents/` 已生成，方可进入 `@novel-agent`
- 如果 `init.py` 报错，必须先修复问题重新执行，不允许绕过

## 初始化 — 先询问，确认后执行，不可跳过

全新项目先询问作者是否初始化，确认后运行 `init.py`（项目路径可选，默认当前目录）：
```
python tools/init.py [project-path] [--genre <编号>]
```

**禁止以任何理由跳过 init.py：** 手动创建目录、复制模板、直接调用 agent 都属于违规行为。`init.py` 是初始化入口，必须执行且完整运行。

`init.py` 会：
1. 选题材
2. 创建项目骨架（settings/、volumes/、chapters/、prompts/、archives/）
3. 部署 agent 定义到 `.claude/agents/`
4. 按题材继承反 AI 规则和文风偏好到 `.claude/knowledge/`
5. 按题材继承格式规范、题材案例到 `.claude/knowledge/`
6. 创建空白的写作记忆文件（`.claude/memory/*.md`）
7. 创建永久记忆占位文件（`.claude/knowledge/permanent-memory.md`）
8. 生成 CLAUDE.md
9. 初始化状态文件 `.agent/status.md`

以上 9 步全部由 `init.py` 自动完成，AI 无需也不应手动干预。

**检查：** 运行后确认 `.agent/status.md` 存在且内容正确，方可进入 `@novel-agent`。

## 设定讨论 — novel-agent 与作者讨论后，由 updater 写入

`init.py` 完成后进入 `@novel-agent`，此时 `phase=setup`，按以下流程：

1. **novel-agent 检测到 setup 阶段**，与作者逐项讨论设定（世界观/角色/风格/题材）。如果作者需要帮忙取书名，参考 `knowledge/title-craft/index.md` 的方法论给出建议
2. 讨论完毕后，novel-agent **写 order 文件** `.agent/task/setting-update-order.md`
3. novel-agent 通过 **Agent 工具调用 updater**
4. **updater 读取 order**，写入 `settings/world-setting.md`、`settings/genre-setting.md`、`settings/character-setting/*.md` 等设定文件
5. updater 清理 order 文件并结束
6. **novel-agent 确认 order 已清理**，推进 phase → outline，进入卷纲规划

**权限规则：** novel-agent 不得直接写 `settings/` 下的文件，设定写入必须通过 updater 的 setting-update 模式完成。

## 自动迁移（2.x → 3.0）

检测到 `story.yaml` 存在时，按以下流程自动迁移：

### Step 1: 展示迁移计划

扫描项目目录，给作者看三张清单：

**文件清单：**
- 设定文件：story.yaml + settings/ 下所有文件
- 角色文件：settings/character-setting/ 下所有文件
- 卷纲：volumes/ 下所有文件
- 正文：archives/ 下 `.md` 文件数量
- 章纲（已归档）：chapters/ 下 `status: archived` 的章节数量
- 章纲（跳过）：chapters/ 下 `status != archived` 的章节列表
- 提示词：prompts/ 下文件数量

**废弃清理（直接丢弃）：**
- `author-intent.md`、`current-focus.md`
- `drafts/`、`drifts/`、`tmp/`、`temp-*.txt`
- `manuscripts/`、`.vscode/`

**作者确认后继续。**

### Step 2: 备份旧文件

```bash
mkdir -p old
mv story.yaml settings/ volumes/ chapters/ archives/ prompts/ old/
rm -rf drafts/ drifts/ tmp/ manuscripts/ .vscode/ author-intent.md current-focus.md
```

### Step 3: 初始化新骨架

```bash
python tools/init.py [project-path] [--genre <编号>]
```

`init.py` 创建目录结构 + 空模板 + agent 定义 + 记忆/知识库。后续迁移步骤负责填数据。

### Step 4: 迁移设定（逐文件按 templates/migration/ 映射）

对照 `templates/migration/migration-spec.md` 的字段映射表，按优先级逐文件转换：

| 优先级 | 旧文件 → 新文件 | 参考模板 |
|--------|----------------|---------|
| P0 | `old/settings/character-setting/*.yaml` → `settings/character-setting/*.md` | `templates/migration/character.md.template` |
| P1 | `old/story.yaml` + `old/volumes/*.yaml` → `story.md` | `templates/migration/story.md.template` |
| P2 | `old/volumes/*.yaml` → `volumes/volume-{N}.md` | `templates/migration/volume.md.template` |
| P3 | `old/chapters/*.yaml`（archived）→ `chapters/vol-{N}-ch-{M}.md` | `templates/migration/chapter.md.template` |
| P4 | `old/settings/world-setting.yaml` → `settings/world-setting.md` | `templates/migration/world-setting.md.template` |
| P5 | `old/settings/writing-style.yaml` → `settings/writing-style.md` | `templates/migration/writing-style.md.template` |
| P6 | `old/settings/anti-ai.yaml` → `settings/anti-ai.md` | `templates/migration/anti-ai.md.template` |
| P7 | `old/settings/hooks.yaml` → `settings/foreshadowing.md` | `templates/migration/foreshadowing.md.template` |
| P8 | 无旧源 → `settings/genre-setting.md` | `templates/migration/genre-setting.md.template` |

字段映射细节在 `templates/migration/migration-spec.md` 中有完整定义。

### Step 5: 拷贝已归档正文 + 提示词

只拷贝已定稿的正文（非 `.draft.md`），提示词全部复制：

```bash
# 正文：只拷定稿（跳过 draft）
for f in old/archives/*.md; do
  [ -f "$f" ] || continue
  case "$f" in *.draft.md) ;; *) cp "$f" archives/ ;; esac
done
cp old/prompts/*.md prompts/ 2>/dev/null
cp old/prompts/*.txt prompts/ 2>/dev/null
```

正文不做任何修改。

### Step 6: 验收

- [ ] story.md 存在，skill_version = 4.0
- [ ] settings/world-setting.md 存在且已填充
- [ ] settings/writing-style.md 存在且已填充
- [ ] settings/genre-setting.md 存在
- [ ] settings/anti-ai.md 存在
- [ ] settings/foreshadowing.md 存在
- [ ] settings/character-setting/ 角色数与旧版一致
- [ ] volumes/ 卷数与旧版一致
- [ ] chapters/ 所有 archived 章节已迁移
- [ ] archives/ 正文全部复制
- [ ] prompts/ 提示词全部复制
- [ ] 旧 .yaml 已移入 old/（无残留）
- [ ] 废弃文件已清理

### Step 7: 交接 novel-agent 评估补充

迁移完成后，调度 `@novel-agent`，由其执行：

1. **项目空间评估** — 扫描全部迁移后的文件，对照验收清单识别缺失项
2. **补充决策** — 判断缺失项该由哪个 agent 处理：
   - 设定缺失（世界观/角色/风格/题材等）→ 调度 updater（setting-update 模式）
   - 其他 → 直接向作者提问
3. **逐项引导补充** — 每次调度一个 agent 完成补充后，再评估下一项，直到项目就绪
4. **汇报就绪** — 全部就绪后向作者展示迁移+补充结果，进入写作循环。确认无误后，作者可手动删除 `old/` 目录。

## 边界条件

| 场景 | 处理 |
|------|------|
| `story.yaml` 存在 → `story.md` 不存在 | 旧版 2.x → 执行自动迁移流程 |
| `story.md` 存在但 `skill_version` < 4.0 | 待升级 → 执行自动迁移流程 |
| `story.md` 存在且版本匹配 | 已有项目 → @novel-agent |
| 两者都不存在 | 全新项目 → init.py → @novel-agent |
| `init.py` 不可用 | 手动创建目录结构 + 复制 `templates/` 文件 |
| 检测到未提交的 git 变更 | 提示作者先提交/stash |

## 项目目录结构

```
{project-name}/
├── story.md              # ★ 项目索引
├── settings/
│   ├── world-setting.md  # 世界观
│   ├── writing-style.md  # 写作风格
│   ├── genre-setting.md  # 题材设定
│   └── character-setting/
│       └── <id>.md       # 每角色一个文件
├── volumes/
│   └── volume-{N}.md     # 卷纲
├── chapters/
│   └── vol-{N}-ch-{M}.md # ★ 章纲（status: outline → draft → archived）
├── prompts/
│   └── vol-{N}-ch-{M}-prompt.md  # 提示词
├── archives/
│   ├── *.draft.md        # 草稿
│   └── *.md              # 定稿
├── .agent/\n│   ├── status.md         # 进度追踪（⚠️ 需对照磁盘实际文件验证，不要凭记忆或推断写"已完成"）\n│   └── task/             # agent 间 order 文件
└── .claude/
    ├── agents/           # Agent 定义
    ├── knowledge/        # 反 AI 规则、文风偏好、永久记忆、格式规范
    └── memory/           # 写作动态记忆
```

## Agent 协作架构

```
novel-agent（总指挥）
  ├─ 新项目 → 调度 volume-planner（规划卷纲）
  ├─ 卷纲就绪 → 调度 chapter-planner（生成章纲）
  │   └─ 章纲较多时（15+章）→ 见「章纲批量调度模式」
  ├─ 章纲就绪 → 调度 prompt-crafter（组装提示词）
  ├─ 提示词就绪 → 调度 writer（写正文）
  ├─ 正文就绪 → 可选调度 reader（深度评审）
  └─ 作者确认 → 调度 updater（归档 + lore-keeping）
```

各 agent 定义在 `agents/`，skill SOP 在 `skills/`。agent 间通过 `.agent/task/*-order.md` 文件通信。

**调度规则：** novel-agent 是唯一调度者，只写 order 文件 + 调用子 agent。所有内容创作（卷纲/章纲/提示词/正文）、设定维护、归档更新均由子 agent 完成，novel-agent 不得越权代劳。子 agent 完成任务后清理 order 文件，novel-agent 检测到清理即确认完成。

**重要：novel-agent 是顶层入口，禁止将 novel-agent 作为 subagent 调度——它将失去子 agent 调度能力，导致调度链断裂。** 加载方式取决于运行环境：

- **Claude Code：** 通过 `@novel-agent` 加载。使用 Agent 工具调用子 agent，子 agent 自动读取 `.claude/agents/` 定义和 `.agent/task/*-order.md` 文件
- **Hermes：** 通过 `skill_view(name='awesome-novel')` 加载。使用 `delegate_task` 调度子 agent，通过 `context` 参数传递 order 文件内容。子 agent 完成后仍需清理 `.agent/task/*.md` 文件作为完成信号

主 agent 加载 novel-agent 定义后即扮演总指挥角色，拥有完整的子 agent 调度权限。

## 章纲批量调度模式

当项目有大量章节（15+章）需要规划章纲时，采用以下批量模式提升效率。

### 作者偏好确认

进入 outline 阶段后，首先与作者确认规划策略：

- **方案A：一卷一卷推进** — 完成一卷的全部章纲→提示词→正文→归档，再进入下一卷。适合长篇连载/需频繁交付
- **方案B：先全部章纲再正文（推荐中短篇）** — 一次性完成所有卷的章纲后，统一进入提示词/写作阶段。适合中短篇/作者希望先看清全貌

### 批量执行流程（方案B）

1. **全局读档** — 读取所有卷纲（volumes/volume-{N}.md）和所有涉及的角色设定（settings/character-setting/），确保对全局有完整把握
2. **评估 order 文件状态** — 检查 `.agent/task/` 下哪些章已有 order 文件（可能来自上次中断）、哪些需要新建
3. **准备/增强 order 文件** — 对缺失的章创建 order 文件，以卷纲描述为基准，补充方向性约束（肉戏标记、情绪基调、硬约束）。⚠️ **关键缺陷：** 如果 order 文件仅引用卷纲文本而没有章节专属的方向说明，子 agent 产出的章纲可能流于泛泛。每份 order 至少应包含：章节专属的方向指引、硬约束、以及区别于同一卷其他章的核心冲突/情绪特化点。卷纲描述足够详细的 order 可直接 dispatch；描述过于简略（一句话概括一章）的应先与作者讨论方向
4. **分批 dispatch** — 每批并行调度 2-4 个 chapter-planner subagent。不同章节互不依赖，可同时进行
5. **等待 + 验证** — 子 agent 完成任务后清理 order 文件。novel-agent 检查每个文件是否创建、格式是否正确、内容非空
6. **准备下一批** — 在当前批次运行时，提前写好下一批的 order 文件，减少串行等待
7. **按卷按序推进** — 优先完成一卷内的所有章纲再换卷，保持剧情连贯性（不跨卷交叉调度）

### 适用前提

- 每章的卷纲描述足够详细（含肉戏标记、情绪基调、硬约束）→ 可以直接 dispatch，不需额外讨论
- 角色设定已完备 → subagent 可自行参考，不需 novel-agent 在 order 中逐项罗列设定细节
- 如果某卷的卷纲过于简略（仅一句话概括一章），应先与作者确认方向，再写 order 文件

## 工具契约

| 工具 | 用途 | 谁用 |
|------|------|------|
| **Bash** | 执行 init.py；迁移备份/拷贝命令；版本检测 | skill 入口（非 agent） |
| **Read** | 检测项目文件、读取设定/状态 | 所有 agent |
| **Write** | 写 order 文件（novel-agent）；写设定/记忆/知识（子 agent） | 各 agent 按权限 |
| **Agent** | novel-agent 调用子 agent | novel-agent 专用 |
| **Edit** | 写 settings/、.claude/ 下的内容文件 | 子 agent（非 novel-agent） |
| **Glob** | 扫描文件 | 所有 agent |
| **Grep** | 搜索内容 | 所有 agent |

### 运行环境工具映射

| 操作 | Claude Code | Hermes |
|------|------------|--------|
| **加载 novel-agent** | `@novel-agent` | `skill_view(name='awesome-novel')` |
| **调度子 agent** | Agent 工具（@-mention） | `delegate_task(tasks=[...], toolsets=[...])` |
| **传递上下文** | 子 agent 自动读 `.agent/task/*-order.md` | 通过 delegate_task 的 `context` 参数直接嵌入 |
| **子 agent 完成信号** | 子 agent 清理 order 文件 | 子 agent 清理 order 文件 + delegate_task 返回摘要 |

**Hermes 环境注意事项：**
- delegate_task 最多并行 3 个子 agent（受 `max_concurrent_children` 限制）
- 子 agent 的 `toolsets` 参数需显式指定（如 `["terminal", "file"]`），不给默认无工具
- 子 agent 完成后需验证文件实际写入（delegate_task 返回的是子 agent 自述摘要，不是验证报告）
- order 文件依然推荐写入 `.agent/task/` 作为调度记录——即使 delegate_task 已传递上下文，order 文件作为持久化痕迹和完成信号仍有价值

---

## 附：双模型推荐工作流

对于需要生成**大尺度/黄暴/硬核肉文**内容（如 BL 题材），推荐以下角色切分：

| 角色 | 模型 | 职责 |
|------|------|------|
| **架构师** | Claude（本会话） | 设定、卷纲、章纲、提示词、项目管理 |
| **写手** | 本地千问 / Qwen | 正文生成（黄暴/露骨内容） |

### 给写手的提示词结构（7段式）

当 prompt-crafter 组装写手提示词时，使用以下分段：

1. **角色** — writing-style 的 role/core_principles/possible_mistakes/depiction_techniques 四字段
2. **任务指示** — 目标字数、叙事目标×3（悬念/情绪/爽点）、本章在全卷角色
3. **背景信息** — 前情提要 + 角色初始状态 + 微习惯
4. **写作案例** — 1个场景示范（感官分层取舍、焦点冲突法）
5. **输入** — 每个场景的原材料（权重、核心事件、情绪拐点、信息差、衔接）
6. **不可违反规则** — 红线约束（不可删减）、边界禁止（不涉及）、角色禁区、写作风格基线、段落精度分层
7. **字数/情绪目标** — 从章纲读取，**不**在提示词中重新定义

参考文件 `references/male-erotica-style-checklist.md` 提供了一个具体的男同硬核肉文风格场景分布锚点模板，可直接在提示词组装修复中复制使用。

## 风格类追加指令的执行落地问题

经验教训：当提示词中包含风格类追加指令（粗俗比喻、骚话分布、生理失控等需要分布到多个场景的约束）时，**仅写"至少出现X次"不够**——writer 会集中在同一段落/场景全部兑现，导致分布不均匀。

### 追加指令需要 scene-level 锚点

**反例（不够）：**
```
- 受方至少有4处不同场景的骚话
- 翻白眼/舌头外伸/口水失禁——至少出现2次
- 粗俗比喻（矿水瓶/驴屌等）——至少3处不同的鸡巴比喻
```

writer 会把4句骚话堆在 Scene 5、3个比喻挤在 Scene 4 同一页、所有生理失控集中在同一段。reader 会识别这个问题，但浪费一轮修正。

**正例（有效）：**
```
- 骚话分布（scene-level锚点）：
  - Scene 2（第一根入嘴前后）：含含糊糊的一声"操……好胀……"
  - Scene 3（轮换间隙）："骚逼被撑满了……"（换人时的低声漏出）
  - Scene 4（最粗插入后）："操死我……"（20cm顶入极限时含混喊出）
  - Scene 5（持续轮换中段）："贱狗让干烂……"（翻白眼之后瘫软低吟）
  - Scene 6-7：不需要（嘴巴合不拢/被操失语状态）

- 生理失控分布：
  - Scene 3（第一次射精冲击）：嘴角口水拉丝
  - Scene 5（最粗插入+双洞同步）：翻白眼 + 舌头外伸 + 口水淌落
  - Scene 5（前列腺高潮）：无碰触射精

- 粗俗比喻分散：
  - Scene 2（第一根入嘴）："狗鸡巴捅进嗓子眼"
  - Scene 3（换嘴时）："龟头像剥了壳的鸡蛋"
  - Scene 4（20cm插入）："擀面杖从中间劈开"
  - Scene 5（外翻描写）："屁眼像小孩嘴巴"
```

### 原则

1. **宁缺不堆** — 如果某个场景本身就1行过渡，不要硬塞比喻进去。跳过这个场景，换下一个
2. **先定场景再定元素** — 每类风格元素（骚话/比喻/失控）先列"适合出现的场景"，再决定具体内容和形式
3. **章末场景（Scene 6-7）通常不需要** — 这时受方被操失语/瘫软了，再加骚话会破坏章末麻木感
4. **reader 是验证者** — 写完追加指令后，可以模拟 reader 视角问自己：这些约束能让 writer 产出均匀分布的内容吗？如果不能，加 scene-level 锚点

### 追加指令结构模板

当给提示词追加风格类约束时，用以下模板：

```
### ★ [风格名]追加指令（强制覆盖，优先级高于上方所有同级规则）

#### 1. [元素类型1]（强制）
- 总量要求：至少X处
- 场景分布：Scene A（具体描述）→ [具体内容] / Scene B → [具体内容] / Scene C → [具体内容]
- 禁区：Scene D 禁止出现（理由）

#### 2. [元素类型2]（强制）
- 同上

#### 3. [元素类型3]（强制）
- 同上

[场景分布矩阵]（可选）
| 场景 | 骚话 | 生理失控 | 比喻 | 攻方台词 |
|------|------|----------|------|----------|
| 1 | - | - | - | - |
| 2 | ✓ | ✓ | ✓ | ✓ |
| 3 | ✓ | ✓ | - | ✓ |
...

*强制检查清单：*
- [ ] 每项有 scene-level 锚点
- [ ] 没有两个元素堆在同一段
- [ ] 章末场景没有硬塞元素破坏麻木感
- [ ] 每个元素有"什么场景/什么时机/什么内容"三重约束
```

### 应用场景

- 性爱场景的风格约束（男同硬核肉文、BDSM、粗暴系等）
- 战斗场景的节奏约束（拳拳到肉、慢动作特写等）
- 恐怖场景的氛围约束（视觉限制、声音主导等）
- 任何需要"均匀分布"而非"集中在某一段"的风格要求

## 修复循环 — reader 评审后的定向修正

当 reader 评审识别出正文存在风格/元素分布/执行落地问题时，采用以下修复循环代替全文重写。

### 适用场景

一轮 writer 输出经 reader 评审后，被指出以下类型的问题（非方向性推翻）：
- 某类风格元素（骚话/比喻/失控等）集中堆叠在同一段落
- 特定元素完全缺失（如攻方全员无台词）
- 某场景段节奏单一缺乏变化（50+行同一强度）
- 男同硬核肉文风格检查清单项未通过且差距可定向修复

### 修复流程

```
reader评审 → 识别具体问题项 → 写 revision order → dispatch 修订写手 →
定向手术 → 验证检查清单 → 可选 reader 复评审 → 归档/继续写作
```

### Revision Order 格式

每份 revision order 包含：

1. **现状描述** — reader 指出的具体问题，可附原文依据
2. **修复要求** — 不重写的定向指令，明确声明"只修改以下 N 处，不改其他任何内容"
3. **具体手术项** — 每项含：位置（哪个场景/段落）、替换/插入内容（具体文本或描述）、插入时机（前置条件）
4. **硬约束** — 保留轮换结构、场景划分、字数规模不变
5. **验证清单** — 完成后逐项打勾

### 定向手术分类

| 手术 | 名称 | 触发条件 | 典型修复方式 |
|------|------|----------|-------------|
| ① | **攻方台词加脏** | 参与者零台词或台词太文明 | 在每轮轮换间隙插入带脏字台词（"操""骚逼""干烂"等） |
| ② | **阴茎崇拜语态贯穿** | 全文仅1-2处接近崇拜语态 | 在4处关键节点插入身体诚实反应（"满了"不想退/舌头追/还能这么满/终于满了） |
| ③ | **粗俗比喻分散** | 3+个比喻集中在一段 | 删掉堆叠的1-2个，移到前面的场景替换原有泛泛描写 |
| ④ | **场景段节奏变化** | 某场景段50+行同一强度 | 插入假结尾（空5秒以为结束+再填满）/ 意外动作（巴掌/拉扯）/ 频率突变 |
| ⑤ | **生理失控分布** | 所有失控描写堆在同一段 | 按场景分散（口水/S2, 翻白眼/S4, 无碰射/S5 等） |

### 执行要点

1. **定向操作，不重写全文** — 用 patch 工具做精准的 find-and-replace
2. **每个手术独立可验证** — 完成后对照检查清单逐项确认
3. **字数控制** — 修改后字数变化应在 ±10% 以内
4. **保持场景结构** — 不合并/拆分/重排段落顺序；不增删场景
5. **手术间独立** — 各手术互不依赖，可在同一轮 dispatch 中并行执行
6. **revision order 和 writing order 分开** — 不要混用 writer 流程
7. **手术5项中，①-④是reader常见问题，①（攻方台词）最常被漏掉** — writer 容易专注于受方视角而忽略攻方声音维度

### 与正文写作的关系

- writer → reader → revision → re-review 是一个完整子循环
- 对于**严重但定向可修复的问题**（攻方台词缺失、比喻堆叠、节奏平、语态不足等），用 revision 循环代替全文重写
- 对于**方向性错误**（基调不对、角色崩了、主线偏离等），应回到 prompt-crafter 修改提示词后重新 writer
| revision 循环完成后，reader 可选择做复评审确认修复效果

### Git 备份节奏

| 里程碑 | 提交时机 |
|--------|---------|
| 设定填充完成 | `git commit -m "设定：填充世界观/角色/风格/题材"` |
| 卷纲完成 | `git commit -m "卷纲：卷N《标题》规划完成"` |
| 章纲完成 | `git commit -m "章纲：第N章《标题》"` |
| 提示词就绪 | `git commit -m "提示词：第N章《标题》——就绪"` |
| 正文归档 | `git commit -m "正文：第N章《标题》归档"` |

### 批量生产模式 — 多章并行写作与评审

当作者要求**全部写完再审**（如"全部完成后让我审核"）时，采用批量生产模式代替逐章推进。本质是从「垂直串行」（一章走完所有阶段再下一章）变为「水平流水线」（所有章先过阶段A，再一起过阶段B）。

#### 适用前提

- 所有卷纲和章纲已就绪
- 角色设定完整
- 前一卷（如有）已归档
- 作者明确表示不要中途评审，要一次性全写完

#### 全局规划

1. **盘点全部剩余工作量** — 列出所有需要产出提示词→正文→评审的章节，按卷分组
2. **一次性准备全部 order 文件** — 在启动任何 dispatch 之前，把**所有阶段**的 order 文件写好：
   - 全部 prompt-order（提示词调度）
   - 全部 writer-order（正文调度，先写但先不 dispatch）
   - 全部 reader-order（评审调度，最后）
3. **分阶段、分批 dispatch**

#### 阶段与批次

```
阶段1：生成提示词
├─ 第1批：卷A ch1-3 → dispatch 3 prompt-crafter
├─ 第2批：卷A ch4-6 → dispatch 3 prompt-crafter（趁上批运行时先写order）
├─ 第3批：卷A ch7-8 + 卷B ch1 → dispatch 3 prompt-crafter
└─ ...
  全部完成 → 进入阶段2

阶段2：写正文
├─ 第1批：卷A ch1-3 → dispatch 3 writer
├─ 第2批：卷A ch4-6 → dispatch 3 writer
└─ ...
  全部完成 → 进入阶段3

阶段3：读者评审（可选）
├─ 每批 dispatch 2-3 reader（每章1个独立reader）
└─ 全部完成 → 作者统一审核

阶段4：二次修正（如需）
├─ 识别共有问题 → 批量 dispatch revision-writer
└─ 作者最终确认 → 归档全卷
```

#### 注意事项

1. **order 文件优先原则** — 在 dispatch 阶段1之前，先写好全部阶段的 order 文件（至少到阶段2）。这让你在等待子 agent 完成时可以继续准备后续 order，而不是每批之间都串行写文件
2. **提交即dispatch** — order 文件写好立即 dispatch 当前批次，不必等负责人检查。利用每批 2-3 分钟的运算时间准备下一批 order
3. **跨卷可混合批次** — 不必按卷切割批次。卷A第4章和卷B第1章在同一个阶段中互不依赖，可以放在同一批 dispatch
4. **子 agent 自述不可信** — writer 声称"通过了全部检查"不代表真的通过。归档前至少抽检每卷最具代表性的一章核对
5. **连续写作时的风格一致性** — 当多个 writer 在不同章节工作时，注意保持受方角色的说话方式、身体习惯、系统面板格式等跨卷一致的设定。如有 drift，归档前需修正
6. **受委托批量写作与逐章写作的重大区别**：逐章写作时，每章的核心驱动力来自章纲和前章结尾；批量写作时，**每一章必须同时感知前章结尾和下一章开头**，确保跨章的衔接自然（如第3章结尾受方被灌了一肚子精→第4章续写时不能突然跳到精神饱满的状态）

#### 与逐章推进的对比

| 维度 | 逐章推进（默认） | 批量生产 | 
|------|-----------------|---------|
| 总时间 | 较长（每章含评审+修改） | 较短（并行利用最大） |
| 质量反馈 | 每章可调整方向 | 全部写完后一次性调整 |
| 适合场景 | 连载/需要频繁交付 | 先全本再精修 |
| 子 agent 调用量 | 分散 | 集中爆发 |
| 跨章一致性 | 易保持（每章可对照前章） | 需额外关注 |

### 关联 skill

本 skill 的 **anti-ai 系统**（`knowledge/anti-ai/` + `skills/anti-ai.md` + `agents/anti-ai.md`）即专为中文小说场景的「去 AI 味道」设计——比英文 humanizer 更适合本创作场景。加载本 skill 时自动可用。

## Pitfalls

- ❌ **参考文件不得绑定具体角色名** — `references/` 下的风格检查清单、修复示例等文件是**跨故事通用模板**，必须使用角色类型占位符（受方、攻方、控场者、参与者），不得出现任何具体角色名（如张野、王队）。使用时由 prompt-crafter 替换为当前故事的角色名
- ❌ **文件名不得绑定具体故事/风格名** — 风格参考文件应以目标受众/类型命名（如 `male-erotica-style-checklist.md`），不得以某个具体故事的缩写命名（如 `gv-style-*.md`）
- ❌ **追加指令不得笼统写"至少出现X次"** — 必须为每个元素指定 scene-level 锚点（哪个场景/什么时机/什么内容），否则 writer 会集中在同一段落兑现
- ❌ **novel-agent 不得作为 subagent 调用** — 它是顶层入口，作为 subagent 调用会丢失子 agent 调度能力
- ❌ **不得跳过 init.py 手动创建目录** — init.py 是唯一初始化入口
