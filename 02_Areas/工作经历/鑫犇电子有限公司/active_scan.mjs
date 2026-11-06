import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const files=[
'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/01_生产部/生产车间/生产与物料模板.xlsx',
'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/02_品质部/质量管理与检验模板.xlsx',
'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/03_营运部/业务/订单与供应商模板.xlsx',
'C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/00_公司治理/鑫犇电子_公司组织架构与职责矩阵模板.xlsx'];
for(const p of files){const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));const e=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},summary:'active scan'}); console.log(p.split('/').at(-1),e.ndjson); const names=wb.worksheets.items.map(s=>s.name); console.log('sheets',names.join('|'));}
