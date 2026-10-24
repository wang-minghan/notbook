from pathlib import Path
from html import escape
import shutil, textwrap
ROOT=Path(r'C:/Users/32027/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/06_公司公共/公司治理PPT/xinben_governance_20261007')
SVG=ROOT/'svg_output'; NOTES=ROOT/'notes'; IMG=ROOT/'images'
for p in [SVG,NOTES,IMG]: p.mkdir(parents=True,exist_ok=True)
# copy existing images
src=Path('C:/Users/32027/ppt-master/projects/xinben_pqcdsm_ppt169_20261007/images')
for f in ['FULL_DIE_CONCEPT_DEMO_ISOMETRIC.png','FULL_DIE_CONCEPT_DEMO_OPEN_SECTION.png','Mold_Base_3VIEW.png']:
 if (src/f).exists(): shutil.copy2(src/f,IMG/f)
BG='#F7F9FC'; SUR='#FFFFFF'; SUR2='#EEF3F8'; WHITE='#1F2D3D'; MUTED='#526173'; DIM='#8190A0'; BLUE='#2F6BFF'; ORANGE='#E27A21'; TEAL='#1C9C8C'; RED='#D9534F'; LINE='#D7E0EA'
slides=[
('01', '公司治理与部门协同管理体系', '以权责、流程、记录和改进支撑稳定经营', '惠州市鑫犇电子有限公司｜V2.0重构蓝图（待确认）', 'cover'),
('02', '文件定位与适用范围', '本文件规定治理边界和跨部门协同，不替代部门SOP', '公司层治理｜部门接口｜流程控制｜执行文件另册', 'framework'),
('03', '管理体系三层架构', '把治理要求逐层落到部门责任、流程和证据', '治理层：方向、权责、授权、风险｜协同层：订单、采购、品质、交付｜执行层：制度、SOP、表单、台账', 'framework'),
('04', '管理原则', '权责清晰、授权经营、过程受控、异常升级、记录可追溯', '权责清晰｜授权经营｜过程受控｜异常必升级｜记录可追溯｜持续改进', 'five'),
('05', '制度文件层级', '不同问题由不同层级文件解决', '治理原则｜管理制度｜流程程序｜SOP/表单/记录', 'lifecycle'),
('06', '组织架构与决策边界', '组织图必须表达责任传递，不只是岗位名单', '最高管理层｜总经理/经营负责人｜职能部门｜现场执行单元', 'org'),
('07', '决策与经营职责', '战略监督与日常经营衔接，但不混淆', '重大方向和风险｜经营目标和资源｜跨部门裁决｜部门结果责任', 'split'),
('08', '部门职责地图', '每个部门统一写清定位、输入、输出、权限和接口', '定位｜主要责任｜关键输入｜关键输出｜权限边界｜升级对象', 'cards'),
('09', '岗位责任与替代机制', '岗位变更、兼岗和离岗必须保持责任连续', '岗位目的｜核心职责｜关键权限｜能力确认｜替代岗位｜权限回收', 'cards'),
('10', 'RACI责任规则', '一项事项只能有一个A，不能用“大家负责”替代授权', 'A：批准/结果负责｜R：执行｜C：事前咨询｜I：结果知会｜冲突时升级', 'raci'),
('11', '授权审批矩阵', '审批权必须与风险、金额、专业判断相匹配', '合同/订单｜采购/付款｜质量放行｜文件发布｜异常处置｜重大资源', 'matrix'),
('12', '越权与职责冲突处理', '先暂停、再升级、后决定、留痕关闭', '发现冲突｜暂停越权动作｜提交授权人｜形成决定｜更新责任和记录', 'cycle'),
('13', '订单到交付总流程', '客户承诺必须建立在跨部门共同确认上', '客户/业务｜营运｜生产｜技术/品质｜采购/仓储｜授权管理层', 'swimlane'),
('14', '订单与变更控制', '口头变化必须转化为受控的评审、批准和版本更新', '需求登记｜影响评估｜批准/拒绝｜更新版本｜旧版隔离｜验证关闭', 'swimlane'),
('15', '生产计划与任务下达', '开工前确认产品、资源、交期和受控版本', '订单输入｜产能确认｜材料/模具/设备确认｜任务发布｜进度反馈｜交付风险升级', 'process'),
('16', '采购到付款', '需求、验收、入库、对账和付款形成相互制约', '需求部门｜采购｜品质/技术｜仓储｜财务｜授权批准人', 'swimlane'),
('17', '质量异常与放行', '异常先隔离和判断，不能以交期压力代替质量授权', '发现｜隔离｜分级｜调查与临时措施｜授权处置｜验证关闭', 'quality'),
('18', '客诉与纠正措施', '客户问题必须有统一入口、责任人、时限和验证', '接收分级｜临时措施｜事实调查｜原因分析｜改善｜效果验证｜客户回复', 'cycle'),
('19', '模具、设备与关键资源', '治理层规定状态、责任、批准和履历，不规定维修动作', '需��/异常｜状态评估｜方案与资源｜完成后验证｜恢复使用批准｜履历更新', 'process'),
('20', '跨部门交接标准', '部门协同的最小单元是完整输入和可验证输出', '输入完整｜责任明确｜期限清楚｜状态可见｜输出可验证｜异常可升级', 'process'),
('21', '文件编制与版本控制', '承诺、图纸、制度和流程必须对应到受控版本', '起草｜评审｜批准｜发布培训｜执行记录｜复审修订/作废', 'lifecycle'),
('22', '记录与档案生命周期', '记录证明谁在何时依据什么作出什么结果', '形成｜审核｜编码归档｜权限保存｜检索借阅｜到期处置', 'lifecycle'),
('23', '人员能力与岗位授权', '治理只规定能力、授权、替代和离岗回收，不展开招聘SOP', '培训｜能力确认｜上岗授权｜权限维护｜复训/调岗｜离职交接', 'lifecycle'),
('24', '客户资料与信息权限', '最小权限、使用留痕和离岗回收保护客户与公司资料', '资料分级｜权限申请｜审批｜使用留痕｜回收｜泄露上报与复盘', 'security'),
('25', '经营会议与管理闭环', '会议以决定、责任、期限和关闭证据为完成标准', '数据输入｜议题筛选｜管理决策｜责任/期限｜跟踪验证｜升级归档', 'meeting'),
('26', '管理指标看板', '管理层看趋势、风险和需要决策的事项', '交付｜质量｜采购/库存｜现金/成本｜能力｜整改闭环', 'dashboard'),
('27', '风险登记与升级', '风险管理嵌入经营决策，不是单独罗列问题', '识别｜评价｜责任人｜预警阈值｜应对措施｜升级与关闭', 'risk'),
('28', '安全、环保与应急', '责任不能全部转移给行政，现场和管理层都要承接', '日常检查｜风险发现｜现场处置｜逐级上报｜责任调查｜整改验证', 'cycle'),
('29', '内部检查与管理评审', '按过程检查治理是否有效，不只按部门检查', '过程目标｜责任权限｜记录证据｜指标趋势｜风险与整改｜管理评审', 'framework'),
('30', '不符合项与整改关闭', '整改必须有原因、措施、期限、验证和复发控制', '发现｜分级｜责任人｜措施｜效果验证｜关闭/再升级', 'cycle'),
('31', 'PDCA持续改进', '文件的价值是减少重复问题并提升过程能力', 'Plan：目标风险｜Do：执行记录｜Check：数据审核｜Act：纠正标准化', 'pdca'),
('32', '部门协同RACI示例', '先用关键事项校准责任，再扩展到完整矩阵', '订单评审｜技术变更｜采购验收｜质量放行｜客诉关闭｜付款批准', 'matrix'),
('33', '管理体系证据链', '制度、流程、表单和记录必须形成可追溯链条', '要求｜责任｜执行｜记录｜复核｜改进', 'framework'),
('34', '90天落地路线', '先跑通关键责任、授权和记录，再扩展到全公司', '0—30天：确认主数据｜31—60天：试运行流程｜61—90天：复盘内审固化', 'roadmap'),
('35', '待确认事项清单', '未确认的岗位、权限、时限和保存期限不能写成现行事实', '组织与岗位｜放行与付款权限｜兼岗控制｜记录期限｜异常时限｜会议机制', 'cards'),
('36', '附件与另册文件', '治理PPT不替代部门制度、SOP和表单体系', '部门管理制度｜流程程序文件｜SOP｜表单与台账｜记录清单｜修订记录', 'framework'),
]

def txt(x,y,s,size=24,fill=WHITE,weight='normal',anchor='start',opacity=1):
 return f'<text x="{x}" y="{y}" font-family="Microsoft YaHei,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" opacity="{opacity}">{escape(s)}</text>'
def rect(x,y,w,h,fill=SUR,stroke='none',sw=1,rx=14,op=1): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
def line(x1,y1,x2,y2,stroke=LINE,sw=2,dash=''): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def wrap(s,n=20):
 out=[]
 while len(s)>n: out.append(s[:n]); s=s[n:]
 if s: out.append(s)
 return out

def base(num,title,sub):
 return f'<rect width="1280" height="720" fill="{BG}"/>{rect(0,0,1280,8,BLUE,rx=0)}'+txt(60,68,f'{num} / GOVERNANCE',14,TEAL,'bold')+txt(60,112,title,40,WHITE,'bold')+txt(60,145,sub,19,MUTED)+line(60,166,1220,166,LINE,1)

def bullets(items,x=90,y=230,w=520,accent=ORANGE):
 s=''
 for i,it in enumerate(items):
  yy=y+i*78; s+=rect(x,yy-28,10,10,accent,rx=5)+txt(x+28,yy,it,25,WHITE,'bold')
  # optional second line
 return s

def slide_svg(num,title,sub,body,kind):
 s='<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">'
 if kind=='cover':
  s+=f'<image href="../images/FULL_DIE_CONCEPT_DEMO_ISOMETRIC.png" x="650" y="0" width="630" height="720" preserveAspectRatio="xMidYMid slice"/>'+rect(650,0,630,720,BG,rx=0,op=0.55)
  s+=rect(0,0,740,720,BG,rx=0,op=0.92)+txt(70,100,'XINBEN ELECTRONICS',18,TEAL,'bold')+txt(70,245,'公司治理',76,WHITE,'bold')+txt(70,330,'与管理方法',76,ORANGE,'bold')+txt(70,400,'让客户看见一家制造企业如何被可靠地管理',30,MUTED)+line(70,460,470,460,ORANGE,5)+txt(70,520,'公司治理与部门协同管理体系｜V2.0',22,WHITE)+txt(70,575,'惠州市鑫犇电子有限公司',20,MUTED)+txt(70,650,'2026',18,DIM)
 elif kind=='quote':
  s+=base(num,title,sub)+rect(90,230,1100,250,SUR2,stroke=LINE)+txt(130,305,'“',88,ORANGE,'bold')+txt(210,325,body,38,WHITE,'bold')+txt(210,390,'把管理方法变成客户可以验证的合作能力。',24,TEAL)
 elif kind in ('intro','four','five','cards','dept','dashboard','evidence','authority','risk','stake'):
  s+=base(num,title,sub)
  items=body.split('｜')
  cols=2 if len(items)>4 else len(items)
  if len(items)<=4:
   w=250; start=90; gap=28
   for i,it in enumerate(items):
    x=start+i*(w+gap); s+=rect(x,235,w,230,SUR,stroke=LINE)+txt(x+24,280,f'{i+1:02d}',20,ORANGE,'bold')
    yy=325
    for z in wrap(it,10): s+=txt(x+24,yy,z,24,WHITE,'bold'); yy+=35
  else:
   for i,it in enumerate(items):
    col=i%2; row=i//2; x=90+col*560; y=220+row*100
    s+=rect(x,y,520,76,SUR,stroke=LINE)+rect(x,y,8,76,TEAL if i%2==0 else ORANGE,rx=4)+txt(x+28,y+32,f'{i+1:02d}',18,DIM,'bold')+txt(x+75,y+36,it,24,WHITE,'bold')
 elif kind in ('heatmap','pdca'):
  s+=base(num,title,sub)
  items=body.split('｜')
  if kind=='heatmap':
   s+=txt(665,225,'影响程度 ↑',18,MUTED,'bold','middle')+txt(150,570,'发生可能性 →',18,MUTED,'bold')
   for r in range(3):
    for c in range(3):
     fill=[['#244A48','#8A6D3B','#7A3F45'],['#1F514D','#946A2F','#A13E45'],['#2A5B52','#A4772E','#C23E45']][r][c]
     s+=rect(250+c*180,260+r*90,160,70,fill,stroke=LINE)
   for i,it in enumerate(items): s+=txt(790,275+i*62,it,24,WHITE,'bold')
  else:
   pts=[(200,340),(520,240),(840,340),(520,470)]
   for i,(x,y) in enumerate(pts):
    nx,ny=pts[(i+1)%4]; s+=line(x,y,nx,ny,TEAL,5)
    s+=rect(x-100,y-45,200,90,SUR,stroke=TEAL)+txt(x,y-5,it if False else items[i][:18],20,WHITE,'bold','middle')
   s+=txt(520,350,'持续改进',30,ORANGE,'bold','middle')
 elif kind in ('org','raci','process','quality','cycle','tool','doc','meeting','roadmap','maturity','framework','lifecycle','swimlane','matrix','security'):
  s+=base(num,title,sub)
  items=body.split('｜')
  y=240
  for i,it in enumerate(items):
   x=85+i*int(1110/max(1,len(items)))
   if i<len(items)-1: s+=line(x+90,y+24,x+int(1110/max(1,len(items)))+10,y+24,LINE,4)
   s+=rect(x,y,170,105,SUR,stroke=BLUE if i%2==0 else TEAL)+txt(x+85,y+34,f'{i+1:02d}',18,ORANGE,'bold','middle')
   yy=y+66
   for z in wrap(it,8)[:2]: s+=txt(x+85,yy,z,20,WHITE,'bold','middle'); yy+=26
  s+=txt(90,470,'规范字段：目的｜适用范围｜责任｜输入｜步骤｜输出｜记录｜控制点',24,MUTED,'normal')
  diagram_map={'framework':'01_governance_framework.svg','swimlane':'02_order_change.svg','lifecycle':'05_document_lifecycle.svg','matrix':'03_procurement_payment.svg','security':'04_personnel_lifecycle.svg','cycle':'06_pdca.svg','roadmap':'02_order_change.svg','org':'01_governance_framework.svg','process':'02_order_change.svg','quality':'06_pdca.svg','tool':'05_document_lifecycle.svg','doc':'05_document_lifecycle.svg','meeting':'06_pdca.svg','maturity':'01_governance_framework.svg'}
  if kind in diagram_map:
   s+=rect(45,185,1190,430,BG,stroke=LINE,rx=12)+f'<image href="../images/{diagram_map[kind]}" x="55" y="195" width="1170" height="410" preserveAspectRatio="xMidYMid meet"/>'

 elif kind=='split':
  s+=base(num,title,sub)+rect(80,225,520,300,SUR,stroke=BLUE)+rect(680,225,520,300,SUR,stroke=ORANGE)+txt(120,275,'左侧：治理定位',22,TEAL,'bold')+txt(720,275,'右侧：客户感知',22,ORANGE,'bold')
  a,b=(body.split('｜',1)+[''])[:2]; yy=330
  for z in wrap(a,15): s+=txt(120,yy,z,26,WHITE,'bold'); yy+=40
  yy=330
  for z in wrap(b,15): s+=txt(720,yy,z,26,WHITE,'bold'); yy+=40
 elif kind=='close':
  s+=f'<image href="../images/FULL_DIE_CONCEPT_DEMO_OPEN_SECTION.png" x="700" y="80" width="520" height="520" preserveAspectRatio="xMidYMid meet"/>'+rect(700,80,520,520,BG,rx=0,op=0.45)+rect(0,0,820,720,BG,rx=0,op=0.94)+txt(70,100,'CUSTOMER PROMISE',18,TEAL,'bold')+txt(70,230,'给客户的',64,WHITE,'bold')+txt(70,310,'承诺',78,ORANGE,'bold')+txt(70,405,body,28,WHITE,'bold')+txt(70,560,'鑫犇电子有限公司',24,MUTED)
 else:
  s+=base(num,title,sub)+bullets(body.split('｜'))
  s+=rect(760,230,380,330,SUR2,stroke=LINE)+txt(800,280,'MANAGEMENT METHOD',18,TEAL,'bold')+txt(800,345,'责任',36,WHITE,'bold')+txt(800,405,'流程',36,WHITE,'bold')+txt(800,465,'证据',36,WHITE,'bold')+txt(800,525,'复盘',36,WHITE,'bold')
 s+=txt(60,690,'鑫犇电子有限公司｜公司治理与管理方法',14,DIM)+txt(1220,690,num,14,DIM,'normal','end')+'</svg>'
 return s
for num,title,sub,body,kind in slides:
 name=f'{num}_{title.replace("/","_").replace("：","")}'
 (SVG/f'{name}.svg').write_text(slide_svg(num,title,sub,body,kind),encoding='utf-8')
 note=f'本页围绕“{title}”展开。重点不是介绍概念本身，而是说明鑫犇如何把责任、流程和证据组织起来，让客户能够理解并验证我们的管理方式。下一页将继续把这一方法落到具体治理场景。'
 (NOTES/f'{name}.md').write_text(note,encoding='utf-8')
print('generated',len(slides))
