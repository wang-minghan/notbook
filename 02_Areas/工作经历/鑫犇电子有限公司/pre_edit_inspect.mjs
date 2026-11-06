import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const files={
prod:"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/生产车间/生产与物料模板.xlsx",
qa:"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/02_品质部/质量管理与检验模板.xlsx",
ops:"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/03_营运部/业务/订单与供应商模板.xlsx",
gov:"C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/00_公司治理/鑫犇电子_公司组织架构与职责矩阵模板.xlsx"
};
for (const [k,p] of Object.entries(files)){const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));console.log('FILE',k);console.log((await wb.inspect({kind:'sheet,table',maxChars:25000,tableMaxRows:5,tableMaxCols:25,tableMaxCellChars:80})).ndjson);const sh=wb.worksheets.items[0];const prev=await wb.render({sheetName:sh.name,autoCrop:'all',scale:1,format:'png'});await (await import('node:fs/promises')).writeFile(`./pre_${k}.png`,new Uint8Array(await prev.arrayBuffer()));}
