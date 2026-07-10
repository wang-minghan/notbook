# 日常使用与同步说明

## 当前位置
- 外部 skills 仓库：`C:\Users\32027\Desktop\tools\notbook\AI\Hermes技能系统`
- 实际被 Hermes 扫描的外部 skills 目录：`C:\Users\32027\Desktop\tools\notbook\AI\Hermes技能系统\skills`

## 日常维护原则
1. **不要**再把自定义 skill 直接放回 `C:\Users\32027\AppData\Local\hermes\skills`
2. 新 skill / patch / references / templates / scripts，优先维护在本仓库的 `skills/` 下
3. 每次修改后建议执行 Git 提交

## 推荐 Git 流程
```bash
cd /c/Users/32027/Desktop/tools/notbook/AI/Hermes技能系统
git status
git add .
git commit -m "feat: update Hermes skills"
```

## 定期同步（未来可接 cron）
如果该仓库有远端：
```bash
cd /c/Users/32027/Desktop/tools/notbook/AI/Hermes技能系统
git pull --ff-only
```

## Hermes 生效说明
- `skills.external_dirs` 已指向本仓库 `skills/`
- 新会话中会自动加载扫描结果
- 若当前会话看不到更新，可：
  - 开新会话 `/new`
  - 或使用 `/reload-skills`

## Obsidian 图谱建议
可在同仓库的 `docs/` 或单独的 Obsidian 笔记里维护：
- 技能索引
- 技能关系图
- 类别导航页
- 变更记录
- 高价值 skill 清单

## 风险提示
- 避免与 builtin skill 同名
- skill 不只是 `SKILL.md`，相关 `references/`、`templates/`、`scripts/` 也要一起提交
- 如果从远端拉取大改动，建议先 `git status` 检查工作区是否干净

## 相关页面
- [[AI助理/Hermes技能系统/index]]
- [[AI助理/Hermes技能系统/docs/ARCHITECTURE]]
- [[AI助理/Hermes技能系统/docs/README]]
- [[MIGRATION_REPORT]]
- [[AI助理/Hermes技能系统/log]]
