# 技能迁移报告

本次已将 **非 bundled / 用户扩展 skills** 从 Hermes 官方 skills 目录分离，迁移至外部 Git 管理目录：

`C:\Users\32027\Desktop\tools\notbook\AI\Hermes技能系统\skills`

## 当前原则
- 官方 bundled skills 保留在：`C:\Users\32027\AppData\Local\hermes\skills`
- 用户扩展 skills 转移到外部目录，并由 Hermes `skills.external_dirs` 扫描加载

## 已完成动作
1. 初始化外部 Git 仓库
2. 复制全部非 bundled skills 到外部目录
3. 从官方 skills 目录移除非 bundled skills
4. 更新 `config.yaml` 中的 `skills.external_dirs`

## 产物
- 迁移计划：`reports/migration_plan.json`
- 说明文档：`docs/README.md`
- 架构文档：`docs/ARCHITECTURE.md`

## 后续建议
- 新增用户 skill 时，优先维护到本仓库的 `skills/` 下
- 使用 Git 提交变更
- 通过 cron 定期 `git pull` 保持同步
- 如需在聊天会话中立即生效，建议开启新会话或使用 `/reload-skills`

## 相关页面
- [[AI/Hermes技能系统/index]]
- [[AI/Hermes技能系统/docs/README]]
- [[AI/Hermes技能系统/docs/ARCHITECTURE]]
- [[AI/Hermes技能系统/docs/USAGE_AND_SYNC]]
- [[AI/Hermes技能系统/log]]
