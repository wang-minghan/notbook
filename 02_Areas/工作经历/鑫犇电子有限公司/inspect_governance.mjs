import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load("C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/00_公司治理/鑫犇电子_公司组织架构与职责矩阵模板.xlsx"));
console.log((await wb.inspect({kind:"workbook,sheet,table",maxChars:30000,tableMaxRows:20,tableMaxCols:20,tableMaxCellChars:100})).ndjson);
