import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const dir='C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/outputs/20261106_template_优化';
const files=await fs.readdir(dir); for(const f of files.filter(x=>x.endsWith('.xlsx'))){const p=dir+'/'+f; const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p)); console.log('\nFILE',f); console.log((await wb.inspect({kind:'sheet,table',maxChars:12000,tableMaxRows:5,tableMaxCols:15,tableMaxCellChars:80})).ndjson); console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'final formula error scan'})).ndjson)}
