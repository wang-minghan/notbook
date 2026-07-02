# Hermes 技能系统

这个目录用于将用户自定义/扩展的 Hermes skills 与 Hermes 官方 bundled skills 分离管理。

## 结构
- `skills/`：Hermes 通过 `skills.external_dirs` 扫描的外部技能目录
- `docs/`：管理文档、约定、同步说明
- `reports/`：迁移报告、清单、审计结果

## 原则
1. Hermes 官方 bundled skills 保留在 `C:\Users\32027\AppData\Local\hermes\skills`
2. 用户自定义/扩展 skills 统一迁移到本目录的 `skills/`
3. 通过 Git 进行版本管理
4. 通过 Hermes `skills.external_dirs` 让 Hermes 加载本目录技能

## 后续同步
- 可通过 cron 定期执行 `git pull`
- 可在 Obsidian 中为本目录建立技能图谱、索引和维护笔记
