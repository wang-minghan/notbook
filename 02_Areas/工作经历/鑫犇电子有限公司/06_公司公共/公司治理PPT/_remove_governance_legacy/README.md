# 鑫犇电子公司治理与部门协同管理体系 V3

36页治理体系PPT，按公司治理、部门协同、管理运行、内控监督和持续改进组织，不替代部门SOP。

## 当前交付

- V3页面源文件：`svg_output/`
- V3逐页设计合同：`design_spec.md`
- V3视觉锁定文件：`spec_lock.md`
- 当前可编辑PPTX基线：`exports/xinben_governance_20261008_115048.pptx`（36页，封面版本已统一为V3.0，营运部名称已统一为“营运部”，第13页标题已与设计合同统一为“订单到交付总流程”，已包含第12、14、15、19页视觉重绘）
- 本轮视觉重绘总规划：`visual_rework_plan_v4.md`（第20—25页及第32页的逐页图示方案、执行顺序和验收标准）
- V1历史版：`archive/v1_43slides/xinben_company_management_manual_43slides.pptx`
- draw.io源文件：`drawio_assets/*.drawio`

## V3执行约束

- 最终SVG必须逐页手写，不能由 `build_deck.py`、`build_deck_v2.py` 或其他批量生成器直接作为最终路径。
- 每页必须符合 `design_spec.md` 的页面角色和图示语法，并在生成前重读 `spec_lock.md`。
- 导出前必须运行：
  `python C:/Users/32027/ppt-master/skills/ppt-master/scripts/workflow_gate.py <project_path>`
- `svg_quality_checker.py` 只代表技术兼容性通过，不代表视觉验收完成。

## 内容边界

正文聚焦公司治理、部门协同、授权、记录、风险、会议和持续改进；生产、品质、营运部、行政、财务仅作为责任和接口单元说明。设备操作、检验步骤、模具维修、财务记账、招聘培训和表单填写说明进入另册制度、程序文件、SOP、表单和台账。

## 事实成熟度

尚未由公司正式确认的组织名称、岗位权限、质量放行权、金额授权、时限和保存期限统一标记为“待确认、拟建立、建议机制或以正式授权文件为准”。
