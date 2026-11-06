import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const root='C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司';
const outDir=root+'/outputs/20261106_template_优化';
await fs.mkdir(outDir,{recursive:true});
const font='Arial';
const blue='#1F4E78'; const light='#D9EAF7'; const yellow='#FFF2CC'; const grey='#F3F6F8';
function styleSheet(sh, used, widths=[]){
  sh.showGridLines=false;
  const r=sh.getRange(used); r.format.font={name:font,size:10,color:'#1F2937'}; r.format.verticalAlignment='center';
  if (widths.length) widths.forEach(([col,w])=>sh.getRange(`${col}:${col}`).format.columnWidth=w);
}
function writeUsage(wb, title, rows){
  const sh=wb.worksheets.add('使用说明');
  sh.getRange('A1:F1').merge(); sh.getRange('A1').values=[[title]];
  sh.getRange('A1:F1').format={fill:blue,font:{name:font,size:14,bold:true,color:'#FFFFFF'},rowHeight:28};
  sh.getRange('A3:C3').values=[['主题','规则','责任/关联']];
  sh.getRange(`A4:C${3+rows.length}`).values=rows;
  sh.getRange('A3:C3').format={fill:blue,font:{name:font,size:10,bold:true,color:'#FFFFFF'},wrapText:true};
  sh.getRange(`A4:C${3+rows.length}`).format={fill:'#FFFFFF',font:{name:font,size:10,color:'#1F2937'},wrapText:true};
  sh.getRange(`A3:C${3+rows.length}`).format.borders={preset:'outside',style:'thin',color:'#B7C9D6'};
  sh.getRange(`A3:C${3+rows.length}`).format.borders={insideHorizontal:{style:'thin',color:'#D9E3EA'},insideVertical:{style:'thin',color:'#D9E3EA'},top:{style:'thin',color:'#9FB6C5'},bottom:{style:'thin',color:'#9FB6C5'},left:{style:'thin',color:'#9FB6C5'},right:{style:'thin',color:'#9FB6C5'}};
  sh.getRange('A:A').format.columnWidth=20; sh.getRange('B:B').format.columnWidth=72; sh.getRange('C:C').format.columnWidth=34;
  sh.getRange(`A4:C${3+rows.length}`).format.rowHeight=30;
  sh.freezePanes.freezeRows(3);
  return sh;
}
function header(sh, range){sh.getRange(range).format={fill:blue,font:{name:font,size:10,bold:true,color:'#FFFFFF'},wrapText:true,verticalAlignment:'center'};}
function addTable(sh, range, name){try{sh.tables.add(range,true,name)}catch(e){}}
function getSheet(wb,name){return wb.worksheets.items.find(s=>s.name===name)}
async function load(p){return await SpreadsheetFile.importXlsx(await FileBlob.load(p))}
async function save(wb, outPath){workbookRecalc(wb); const x=await SpreadsheetFile.exportXlsx(wb); await x.save(outPath)}
function workbookRecalc(wb){try{wb.recalculate()}catch(e){}}

// Production and materials
const prodPath=root+'/01_生产部/生产车间/生产与物料模板.xlsx';
const prod=await load(prodPath);
const prodRows=[
 ['工作簿定位','生产部业务记录：产品、材料、工单、领料、库存追溯。','生产部维护；跨部门字段按治理层规则引用'],
 ['权威来源','产品主数据：产品编码/图纸版本；材料主数据：材料编码；模具和设备分别由生产部对应台账维护。','不要在业务记录里重新建立同一主数据'],
 ['材料主数据','只记录材料身份与规格：材料编码、牌号、状态/硬度、厚度、宽度、供应商编码、状态、生效日期。','批次、入库、库存重量移至“材料批次”“库存流水/库存余额”'],
 ['材料批次','一批材料一行；批次编码由仓储/采购按受控规则登记，关联材料编码和供应商批次。','营运部采购/仓储维护；品质部负责来料检验结论'],
 ['库存余额','按物料/产品编码+批次+库位汇总库存流水计算；余额表不手填余额。','仓储组维护查询键；由库存流水计算当前余额'],
 ['库存流水','每一笔入库、领料、退料、调拨、报废一行；数量填正数，收发方向区分增减。','营运部仓储组为记录责任；关联工单时填写工单号'],
 ['库存余额','按物料/产品编码+批次+库位汇总库存流水计算；余额表不手填余额。','仓储组维护查询键；不得由质量检查表反向修改'],
 ['生产任务','工单引用订单号、产品编码、图纸版本、材料批次、模具编号、设备编号，减少重复手填。','生产部计划/车间执行；品质部参与三项一致确认'],
 ['领料核对','领料记录必须关联工单号、产品编码、材料批次，并记录标签状态和核对结果。','仓储组与生产车间共同执行，品质部按异常规则介入'],
 ['编号规则','材料编码 MAT + 5位流水号；批次编码 MB + 日期 + 3位流水号；工单 WO + 日期 + 3位流水号；库存流水 STK + 日期 + 4位流水号；领料 MR + 日期 + 4位流水号。','编号确认后固化为值；不依赖排序、插行或删除记录'],
 ['数据状态','EX-示例/虚拟示例不可用于生产；待确认不等于合格。','正式启用前由责任人和治理层确认'],
];
writeUsage(prod,'鑫犇电子｜生产与物料模板使用说明',prodRows);
const mat= getSheet(prod,'材料主数据');
mat.getRange('A1:L2').values=[['材料编码','材料牌号','状态/硬度','厚度(mm)','宽度(mm)','供应商编码','材料类别','状态','生效日期','来源/依据','维护责任人ID','备注'],[null,null,null,null,null,null,null,null,null,null,null,null]];
mat.getRange('A2:L501').format.fill='#FFFFFF'; header(mat,'A1:L1'); mat.getRange('A2:L501').format.fill='#FFFFFF'; mat.getRange('A2:A501').format.fill=yellow;
mat.getRange('I2:I501').format.numberFormat='yyyy-mm-dd'; mat.getRange('A:A').format.columnWidth=16; mat.getRange('B:B').format.columnWidth=18; mat.getRange('C:C').format.columnWidth=14; mat.getRange('D:E').format.columnWidth=12; mat.getRange('F:F').format.columnWidth=15; mat.getRange('G:G').format.columnWidth=14; mat.getRange('H:H').format.columnWidth=12; mat.getRange('I:I').format.columnWidth=13; mat.getRange('J:J').format.columnWidth=26; mat.getRange('K:K').format.columnWidth=15; mat.getRange('L:L').format.columnWidth=24;
const inv= getSheet(prod,'库存与批次'); inv.getRange('A1:N2').values=[['流水编号','日期','物料/产品编码','物料/产品名称（带出）','客户（带出）','批次编码','收发方向','数量','单位','业务类型','库位编码','关联工单号','记录人ID','备注'],[null,null,null,null,null,null,null,null,null,null,null,null,null,null]]; header(inv,'A1:N1'); inv.getRange('B2:B501').format.numberFormat='yyyy-mm-dd'; inv.getRange('H2:H501').format.numberFormat='#,##0.###'; inv.getRange('A:A').format.columnWidth=17; inv.getRange('B:B').format.columnWidth=12; inv.getRange('C:C').format.columnWidth=16; inv.getRange('D:E').format.columnWidth=20; inv.getRange('F:F').format.columnWidth=18; inv.getRange('G:G').format.columnWidth=12; inv.getRange('H:H').format.columnWidth=12; inv.getRange('I:J').format.columnWidth=14; inv.getRange('K:K').format.columnWidth=16; inv.getRange('L:L').format.columnWidth=17; inv.getRange('M:M').format.columnWidth=14; inv.getRange('N:N').format.columnWidth=24;
const batch=prod.worksheets.add('材料批次'); batch.getRange('A1:J1').values=[['材料批次编码','材料编码','供应商编码','供应商批次号','到货日期','来料检验记录编号','入库状态','可用数量','单位','备注']]; header(batch,'A1:J1'); batch.getRange('A:J').format.columnWidth=17; batch.getRange('F:F').format.columnWidth=22; batch.getRange('J:J').format.columnWidth=24; batch.getRange('E:E').format.numberFormat='yyyy-mm-dd'; const bal=prod.worksheets.add('库存余额'); bal.getRange('A1:H1').values=[['物料/产品编码','批次编码','库位编码','单位','期初余额','期间净变动','当前余额（计算）','最近更新日期']]; header(bal,'A1:H1'); bal.getRange('A:H').format.columnWidth=18; bal.getRange('G:G').format.fill=grey; bal.getRange('H:H').format.numberFormat='yyyy-mm-dd'; bal.getRange('G2').formulas=[['=IF(A2=",",E2+F2)']]; bal.getRange('G2:G501').fillDown();const prodTask=getSheet(prod,'生产任务'); prodTask.getRange('A1:U1').values=[['确认单号','生产日期','班次','工单号','订单号','产品编码','图纸版本','材料批次编码','模具编号','设备编号','计划数量','交期','三项一致确认','确认人ID','备注',null,null,null,null,null,null]]; header(prodTask,'A1:O1'); prodTask.getRange('A1:U1').format.fill=blue; prodTask.getRange('A:O').format.columnWidth=16; prodTask.getRange('O:O').format.columnWidth=24; prodTask.getRange('B:B').format.numberFormat='yyyy-mm-dd'; prodTask.getRange('L:L').format.numberFormat='yyyy-mm-dd';
const pick=getSheet(prod,'领料核对'); pick.getRange('A1:N1').values=[['领料记录编号','日期','工单号','产品编码','图纸版本','材料批次编码','材料牌号（带出）','材料厚度(mm)（带出）','材料宽度(mm)（带出）','领料重量(kg)','余料重量(kg)','标签状态','核对结果','核对人ID']]; header(pick,'A1:N1'); pick.getRange('A:N').format.columnWidth=16; pick.getRange('N:N').format.columnWidth=14; pick.getRange('B:B').format.numberFormat='yyyy-mm-dd';
await save(prod,outDir+'/生产与物料模板_优化版.xlsx');

// Quality
const qaPath=root+'/02_品质部/质量管理与检验模板.xlsx'; const qa=await load(qaPath);
const qaRows=[
 ['工作簿定位','品质部质量记录：订单评审、首件、过程巡检、不合格与异常、改善与审核。','品质部维护；订单和工单来源按关联键追溯'],
 ['统一关联键','首件、过程巡检、不合格与异常、改善记录优先使用：工单号 + 产品编码 + 图纸版本。','缺少任一关键键时标记待确认，不用名称猜测'],
 ['订单评审','订单号、产品编码、图纸版本、材料编码/标准、模具编号、设备编号构成评审基础。','订单主数据和客户要求由营运部业务组提供'],
 ['首件/巡检','记录图纸标准、实测值、单位、检具和结果；发现异常要关联异常编号。','生产部执行现场配合；品质部判定和复核边界按RACI'],
 ['不合格与异常','必须记录异常现象、发现时数量、隔离范围、临时处理、处理措施、恢复条件和关闭状态。','不得只填“已处理”，关闭需要证据和确认人'],
 ['改善与审核','来源异常/客户、原因、措施、验证证据和关闭日期完整闭环。','改善记录不替代异常原始记录'],
 ['编码规则','订单评审沿用订单号/评审编号；首件、巡检、异常、改善记录分别使用受控编号；编号确认后固化。','编码规则由治理层统一，品质表提供现场使用提醒'],
 ['部门边界','品质部负责检验判定、隔离/放行授权范围和质量记录；生产部负责执行与现场纠正；模具维修组归生产部。','不在品质表中新增“模具部”或虚构审批岗位'],
];
writeUsage(qa,'鑫犇电子｜质量管理与检验模板使用说明',qaRows);
const review=getSheet(qa,'客户订单评审'); review.getRange('A1:O1').values=[['订单号','日期','客户（营运部提供）','产品编码','图纸版本','数量','交期','材料编码/标准','模具编号','设备编号','质量/包装/标签要求','评审结论','风险与措施','评审人ID','批准人ID']]; header(review,'A1:O1'); review.getRange('A:O').format.columnWidth=17; review.getRange('C:C').format.columnWidth=20; review.getRange('K:M').format.columnWidth=25;
const first=getSheet(qa,'首件检查'); first.getRange('A1:P1').values=[['记录编号','日期','工单号','产品编码','图号','图纸版本','材料批次编码','检查项目','图纸标准','实测值','单位','检具','结果','异常编号','检查人ID','确认人ID']]; header(first,'A1:P1'); first.getRange('A:P').format.columnWidth=15; first.getRange('I:I').format.columnWidth=24; first.getRange('N:N').format.columnWidth=15;
const patrol=getSheet(qa,'过程巡检'); patrol.getRange('A1:O1').values=[['记录编号','日期','工单号','产品编码','图纸版本','检查时间','累计数量','检查项目','图纸标准','实测值','单位','外观结果','异常编号','处理结果','检查人ID']]; header(patrol,'A1:O1'); patrol.getRange('A:O').format.columnWidth=15; patrol.getRange('H:I').format.columnWidth=24;
const nc=getSheet(qa,'不合格与异常'); nc.getRange('A1:S1').values=[['异常编号','发现日期时间','工单号','产品编码','图纸版本','模具编号','工位号','异常类别','异常现象','发现时数量','隔离范围','临时处理','原因分析','处理措施','恢复条件','处理结果','记录人ID','确认人ID','状态']]; header(nc,'A1:S1'); nc.getRange('A:S').format.columnWidth=15; nc.getRange('I:I').format.columnWidth=24; nc.getRange('K:O').format.columnWidth=22;
await save(qa,outDir+'/质量管理与检验模板_优化版.xlsx');

// Operations
const opsPath=root+'/03_营运部/业务/订单与供应商模板.xlsx'; const ops=await load(opsPath);
const opsRows=[
 ['工作簿定位','营运部订单、客户、供应商、采购与来料、出货放行记录。','营运部业务组、采购组、仓储组分别维护本职责内记录'],
 ['客户主数据','客户编码、名称、类型、状态和联系人信息只在“客户主数据”维护。','订单台账引用客户编码；客户名称作为带出/核对字段'],
 ['供应商主数据','“供应商管理”作为供应商唯一主数据来源，供应商编码不得在采购记录中重新定义。','营运部采购组维护，品质部参与评价'],
 ['订单记录','订单号可对应多个订单行，使用“订单行ID”区分产品；订单评审编号连接品质部评审。','业务组维护；变更必须保留版本和传递记录'],
 ['采购与来料','关联供应商编码、材料编码、材料批次编码；检验状态由品质部提供，入库状态由仓储组记录。','不得把入库数量当作库存余额'],
 ['出货放行','关联订单号、订单行ID、产品编码、成品批次和检验记录编号；放行结论由受控职责执行。','业务组协调，品质部负责质量放行边界，仓储组负责出库记录'],
 ['统一编码','客户 CUS + 4位；供应商 SUP + 4位；订单/评审/采购/出货使用受控业务编号；正式编码确认后固化。','不使用行号自动生成永久编码'],
 ['部门边界','营运部是正式部门名称，下设业务组、采购组、仓储组；模具维修组属于生产部，不能作为营运部或独立部门填写。','组织名称以治理层组织单元表为准'],
];
writeUsage(ops,'鑫犇电子｜营运部订单与供应商模板使用说明',opsRows);
const order=getSheet(ops,'客户订单台账'); order.getRange('A1:M1').values=[['订单号','订单行ID','接收日期','客户编码','客户名称（带出）','产品编码','数量','交期','客户特殊要求','订单状态','评审编号','业务负责人ID','交付风险/备注']]; header(order,'A1:M1'); order.getRange('A:M').format.columnWidth=16; order.getRange('I:I').format.columnWidth=28; order.getRange('M:M').format.columnWidth=24; order.getRange('C:C').format.numberFormat='yyyy-mm-dd'; order.getRange('H:H').format.numberFormat='yyyy-mm-dd';
const pur=getSheet(ops,'采购与来料'); pur.getRange('A1:L1').values=[['记录编号','日期','供应商编码','材料编码','材料批次编码','采购数量','到货数量','检验状态（品质部）','入库状态（仓储组）','关联工单号','责任人ID','备注']]; header(pur,'A1:L1'); pur.getRange('A:L').format.columnWidth=17; pur.getRange('L:L').format.columnWidth=24; pur.getRange('B:B').format.numberFormat='yyyy-mm-dd';
const ship=getSheet(ops,'出货放行'); ship.getRange('A1:M1').values=[['放行编号','日期','订单号','订单行ID','客户编码','产品编码','成品批次编码','数量','包装/标签确认','检验记录编号','放行结论','放行人ID','备注']]; header(ship,'A1:M1'); ship.getRange('A:M').format.columnWidth=16; ship.getRange('I:I').format.columnWidth=24; ship.getRange('M:M').format.columnWidth=24; ship.getRange('B:B').format.numberFormat='yyyy-mm-dd';
const cust=ops.worksheets.add('客户主数据'); cust.getRange('A1:I1').values=[['客户编码','客户名称','客户简称','客户类型','联系人','联系电话（受控）','地址（受控）','状态','备注']]; header(cust,'A1:I1'); cust.getRange('A:I').format.columnWidth=18; cust.getRange('E:G').format.columnWidth=24;
await save(ops,outDir+'/订单与供应商模板_优化版.xlsx');

// Governance coding and relation rules
const govPath=root+'/00_公司治理/鑫犇电子_公司组织架构与职责矩阵模板.xlsx'; const gov=await load(govPath);
const gRows=[
 ['治理定位','本表是组织单元、岗位、RACI和编码规则的受控来源，不替代部门业务记录。','公司治理层维护；变更需确认人、日期和依据'],
 ['正式部门名称','营运部为正式组织名称，下设业务组、采购组、仓储组。','所有新表和新文件使用“营运部”，不再使用“运营部”'],
 ['组织层级','模具维修组是生产部下属班组/组织单元，不是独立部门。','业务表的责任部门写“生产部”，责任班组可写“模具维修组”'],
 ['主数据顺序','先维护客户、供应商、产品/图纸、材料、模具、设备、库位，再建立订单、工单、采购、库存、质量记录。','各业务工作簿的“使用说明”同步提醒'],
 ['共享关联键','订单号、订单行ID、产品编码、图纸版本、材料编码、材料批次编码、工单号、模具编号、设备编号、员工ID。','关系未确认前保留“待确认”，不能据字段存在推断授权'],
 ['编码规则','CUS/SUP + 流水号；MAT材料；MB材料批次；WO工单；STK库存流水；MR领料；异常/检验/改善编号由各域按治理层规则登记。','编号确认后固化为值；禁止依赖排序生成永久编码'],
 ['RACI边界','A=最终负责/批准；R=执行；每项只能一个A且至少一个R。','模具维修组的RACI角色不能替代生产部的部门A'],
 ['变更控制','新增字段、改主外键、改编码、改责任部门或拆分表前，先更新数据模型与确认清单。','批准后同步业务工作簿使用说明'],
];
const gs=gov.worksheets.add('07_编码与关系规则'); gs.getRange('A1:C1').values=[['主题','规则','执行提醒']]; gs.getRange('A2:C9').values=gRows; header(gs,'A1:C1'); gs.getRange('A2:C9').format.wrapText=true; gs.getRange('A:A').format.columnWidth=20; gs.getRange('B:B').format.columnWidth=76; gs.getRange('C:C').format.columnWidth=38; gs.getRange('A1:C9').format.borders={preset:'all',style:'thin',color:'#D9E3EA'}; gs.freezePanes.freezeRows(1);
const cover=gov.worksheets.getItem('00_总览与说明'); cover.getRange('A31:C31').values=[['本次架构补充','正式组织名称统一为“营运部”；模具维修组明确为生产部下属组织单元。编码与跨表关系见“07_编码与关系规则”。',null]]; cover.getRange('A31:C31').format.wrapText=true;
await save(gov,outDir+'/鑫犇电子_公司组织架构与职责矩阵模板_优化版.xlsx');

// Human master data terminology correction
const empPath=root+'/04_行政部/人事/鑫犇人员主数据.xlsx'; const emp=await load(empPath); for(const sh of emp.worksheets.items){const u=sh.getUsedRange(); if(!u) continue; const v=u.values; for(let i=0;i<v.length;i++)for(let j=0;j<v[i].length;j++)if(typeof v[i][j]==='string')v[i][j]=v[i][j].replaceAll('运营部','营运部'); u.values=v;} await save(emp,outDir+'/鑫犇人员主数据_名称统一版.xlsx');

console.log('DONE',outDir);



