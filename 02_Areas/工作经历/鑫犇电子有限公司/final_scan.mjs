import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
import fs from 'node:fs/promises';
const dir='C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/outputs/20261106_template_优化';
for(const f of (await fs.readdir(dir)).filter(x=>x.endsWith('.xlsx'))){const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(dir+'/'+f)); const e=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:50},summary:'formula scan'}); console.log(f, e.ndjson)}
