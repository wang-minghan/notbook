import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const files={
  gov:'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/00_公司治理/鑫犇电子_公司组织架构与职责矩阵模板.xlsx',
  erd:'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/00_公司治理/鑫犇电子_数据模型与ERD总入口.md',
  prod:'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/生产车间/生产与物料模板.xlsx',
  mold:'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/模具维修组/模具与维修模板.xlsx'
};
for (const [k,p] of Object.entries(files)) {
 if(!p.endsWith('.xlsx')) continue;
 const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));
 console.log('FILE',k);
 console.log((await wb.inspect({kind:'sheet,table,formula',maxChars:30000,tableMaxRows:6,tableMaxCols:25,tableMaxCellChars:100,options:{maxResults:100}})).ndjson);
}
