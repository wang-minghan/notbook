import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const files=[
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/生产车间/生产与物料模板.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/模具维修组/模具与维修模板.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/工程技术组/设备台账.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/02_品质部/质量管理与检验模板.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/03_运营部/业务/订单与供应商模板.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/04_行政部/人事/能力与培训模板.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/04_行政部/人事/鑫犇人员主数据.xlsx",
"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/04_行政部/后勤/固定资产模板.xlsx"
];
for (const p of files){const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));const s=await wb.inspect({kind:"sheet,table",maxChars:30000,tableMaxRows:8,tableMaxCols:18,tableMaxCellChars:60});console.log(`FILE ${p}\n${s.ndjson}`)}
