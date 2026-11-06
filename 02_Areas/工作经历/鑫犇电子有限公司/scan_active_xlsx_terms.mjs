import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
import fs from 'node:fs/promises';
const root='C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司';
async function walk(dir){let out=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){if(e.name==='99_归档'||e.name==='archive'||e.name==='node_modules')continue;const p=dir+'/'+e.name;if(e.isDirectory())out.push(...await walk(p));else if(e.name.toLowerCase().endsWith('.xlsx'))out.push(p)}return out}
for(const p of await walk(root)){try{const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(p));for(const sh of wb.worksheets.items){const used=sh.getUsedRange();if(!used)continue;const vals=used.values;for(let i=0;i<vals.length;i++)for(let j=0;j<(vals[i]||[]).length;j++){const v=vals[i][j];if(typeof v==='string'&&(v.includes('运营部')||v.includes('模具部')||v.includes('模具维修组'))){console.log(JSON.stringify({file:p,sheet:sh.name,cell:sh.getCell(i,j).address,value:v}))}}}}catch(e){console.error('ERR',p,String(e))}}
