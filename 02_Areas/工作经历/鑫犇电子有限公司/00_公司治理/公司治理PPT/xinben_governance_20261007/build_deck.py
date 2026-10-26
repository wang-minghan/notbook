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
('01','公司治理与管理方法','让客户看见一家制造企业如何被可靠地管理','惠州市鑫犇电子有限公司｜客户与公司介绍版','cover'),
('02','这不是“部门介绍”','治理的核心，是把承诺变成可验证的责任、流程和证据','客户关心的不是组织名称，而是：谁负责、如何决策、出了问题如何闭环。','quote'),
('03','鑫犇是谁','以制造为基础，以治理为保障，以长期合作为目标','电子零件与金属件制造场景｜冲压、清洗、模具维护及配套管理','intro'),
('04','客户为什么要看治理','稳定交付背后，必须有稳定的组织与决策机制','四个客户判断点：承诺是否有依据｜变更是否受控｜异常是否有人负责｜记录是否能够追溯','four'),
('05','我们的治理观','把“说得清楚”变成“做得到、查得到、改得动”','客户承诺 · 责任边界 · 过程控制 · 证据留存 · 持续改进','quote'),
('06','治理模型总览','一个公司治理系统，至少回答五个问题','方向由谁定｜权责如何分｜事项如何决｜结果如何看｜问题如何改','five'),
('07','组织架构：公司—部门—班组','组织架构不是名单，而是责任传递的路径','公司层：董事长、总经理｜部门层：生产、品质、营运、行政、财务｜班组层：执行与反馈','org'),
('08','董事长与总经理的边界','战略监督与日常经营，必须既衔接又不混淆','董事长：战略、重大事项、重大风险与授权监督｜总经理：经营目标、日常管理、跨部门协调与结果负责','split'),
('09','一级部门如何承接治理','部门负责人不是“信息中转站”，而是结果责任人','每个部门明确：定位｜主要输出物｜月度汇报对象｜汇报周期｜关键权限','cards'),
('10','生产部的治理职责','把计划、调度、记录和现场问题统一到一条责任线上','管理输出：生产任务单、日产量报表、设备点检汇总、生产异常记录','dept'),
('11','品质部的治理职责','质量不是末端检验，而是独立的判断与放行机制','管理输出：来料检验、制程/终检、不合格处置、客诉闭环、量具校准、受控文件','dept'),
('12','营运部的治理职责','订单、客户、采购、仓储必须在同一个承诺链上','管理输出：订单评审、采购申购、仓储盘点、出货检测报告','dept'),
('13','行政部与财务部的治理职责','后台职能的价值，是把规则、资源和风险管住','行政：制度、人事、培训、安全台账｜财务：核算、资金、税务、成本和付款审批','split'),
('14','岗位字典：让岗位成为管理单元','岗位不是一个称呼，而是目的、职责、权限和能力的组合','每个岗位至少写清：岗位目的｜核心职责｜关键权限｜任职能力｜替代岗位','cards'),
('15','RACI：一项事项只能有一个A','RACI让“大家负责”变成“责任可定位”','A 最终负责/批准｜R 执行责任｜C 事前咨询｜I 结果知会｜每行只能1个A，至少1个R','raci'),
('16','客户订单评审如何治理','先确认能不能承诺，再确认谁来承诺','输入：订单、图纸、交期、材料、客户要求｜输出：订单评审记录｜A：营运部｜R：业务、生产、品质、技术、采购、仓储','process'),
('17','生产任务下达如何治理','开工前把产品、材料、模具、设备和交期说清楚','关键动作：确认版本｜确认材料｜确认模具｜确认设备｜确认交期｜形成生产任务确认单','process'),
('18','首件与异常放行','异常发生时，最重要的不是“先做完”，而是“先判断”','品质部承担最终判断｜生产与技术提供事实｜不合格隔离｜恢复生产必须留下批准依据','quality'),
('19','来料检验如何治理','供应商来料是否可用，要有标准、有记录、有处置','到料 → 检验 → 合格入库/异常隔离 → 反馈与处置 → 记录归档','process'),
('20','客户投诉如何闭环','客户问题进入公司后，要有统一入口和明确时限','接收与分级｜止血与隔离｜事实调查｜原因分析｜改善措施｜效果验证｜客户回复','cycle'),
('21','模具管理如何治理','模具是制造能力的一部分，必须有台账、有履历、有责任','新模/改模评审｜模具编号｜维修保养｜上机状态｜异常记录｜技术文件归档','tool'),
('22','文件和版本控制','客户拿到的承诺，必须对应到受控版本','文件编码｜版本号｜审批人｜生效日期｜发放范围｜旧版回收｜变更原因｜变更记录','doc'),
('23','记录管理：没有证据就没有完成','记录不是为了填表，而是为了证明过程真实发生','记录要能回答：谁做的｜何时做的｜依据是什么｜结果怎样｜异常怎么处理','quote'),
('24','经营会议如何做成治理机制','会议不以“开过”为完成，而以事项关闭为完成','输入：部门月度结果｜讨论：偏差与风险｜决定：责任人与期限｜输出：会议纪要、重点事项跟踪表','meeting'),
('25','管理层看什么','管理层要看趋势、风险和需要决策的事项','组织：架构与岗位｜经营：目标与重点事项｜质量：异常与客诉｜资源：资金与关键能力｜整改：逾期事项','dashboard'),
('26','授权与审批边界','权限不写清楚，组织就会靠经验运行','重大事项：董事长监督/审批｜日常经营：总经理统筹｜专业判断：部门负责人在授权范围内负责｜超边界事项升级','authority'),
('27','风险管理：先识别，再控制','治理不是等问题发生，而是提前定义触发条件和升级路径','风险登记｜责任人｜预警阈值｜应对措施｜升级对象｜关闭证据','risk'),
('28','利益相关方沟通','客户、员工、供应商和管理层，都需要可预期的沟通方式','客户：承诺与变化｜员工：职责与反馈｜供应商：要求与异常｜管理层：数据与决策','stake'),
('29','治理成熟度：从人治到机制','成熟不是文件越多，而是关键事项越来越不依赖个人记忆','1 口头约定 → 2 有表单 → 3 有责任 → 4 有复核 → 5 有数据闭环','maturity'),
('30','制度体系总图：从原则到证据','成熟制度不是文件堆，而是从治理原则落到岗位动作和记录证据','治理层：战略、权责、授权、风险｜管理制度层：人事、合同、采购、生产、品质、财务、安全、信息｜作业与证据层：SOP、表单、台账、报告、会议纪要','framework'),
('31','制度文件生命周期','每一份制度都要经历受控的产生、执行、修订和归档过程','需求提出 → 起草 → 跨部门评审 → 权限批准 → 发布培训 → 执行记录 → 定期复审 → 修订/作废/归档','lifecycle'),
('32','客户/合同/订单变更流程','客户承诺不能只停留在业务口头沟通，必须进入评审和变更控制','客户需求 → 合同/订单评审 → 图纸与版本确认 → 产能/材料/交期确认 → 变更批准 → 任务更新 → 客户回传与留痕','swimlane'),
('33','采购—供应商—入库—付款','采购制度的核心，是把质量、交付、价格和付款放进同一条控制链','需求提出 → 供应商选择/评价 → 采购审批 → 到货验收 → 合格入库 → 对账 → 付款审批 → 供应商复盘','swimlane'),
('34','人员全生命周期管理','人员制度不仅是招聘，还包括能力确认、授权、替代和离职交接','需求与招聘 → 入职建档 → 岗位培训 → 能力确认 → 权限/上岗授权 → 绩效与复训 → 调岗/替代 → 离职交接','lifecycle'),
('35','关键授权与审批矩阵','制度是否有效，最终要落到谁可以决定、谁必须复核、谁只能知会','事项：战略/重大投资/高层任免｜经营目标/跨部门调度/一般人事｜专业放行/质量判定/文件受控｜付款/费用/合同/印章｜矩阵字段：申请、审核、批准、执行、归档','matrix'),
('36','保密与信息权限控制','客户图纸、报价、工艺、质量和员工资料，都需要按角色控制访问','资料分级 → 权限申请 → 负责人审批 → 最小权限 → 使用留痕 → 离岗回收 → 泄露上报 → 事件复盘','security'),
('37','安全、环保与应急响应','客户看到的不只是效率，也包括企业对人员、设备和环境风险的责任','日常检查 → 风险发现 → 现场处置 → 逐级上报 → 应急预案 → 责任调查 → 整改验证 → 复盘培训','cycle'),
('38','记录与档案生命周期','没有保存规则，记录就不能稳定支持追溯、审查和客户沟通','形成记录 → 审核确认 → 编码归档 → 权限保存 → 检索借阅 → 到期复核 → 续存/销毁审批 → 销毁留痕','lifecycle'),
('39','风险热力图：先识别再排序','风险管理不是罗列问题，而是按影响和发生可能性排序控制','高影响/高可能：立即升级｜高影响/低可能：预案与监控｜低影响/高可能：标准化控制｜低影响/低可能：持续观察','heatmap'),
('40','PDCA持续改进闭环','管理体系的价值，不是文件齐全，而是能持续减少重复问题','Plan：目标与风险｜Do：执行与记录｜Check：指标、审核、客诉与复盘｜Act：纠正、预防、标准化与再验证','pdca'),
('41','90天治理落地路线','先把最关键的责任、授权和记录跑通，再扩展到全公司','0—30天：主数据、架构、岗位、RACI｜31—60天：确认清单、会议机制、版本控制｜61—90天：复盘、内审、持续改进','roadmap'),
('42','客户可见的治理证据包','把“我们有管理”变成客户看得懂的资料包','公司介绍与组织边界｜订单/变更评审｜质量与异常闭环｜模具与版本履历｜会议与改善记录','evidence'),
('43','给客户的承诺','我们不承诺零变化，但承诺变化可沟通、责任可定位、过程可追溯、问题可闭环','鑫犇电子｜以受控的管理方法，支撑长期、透明、可验证的合作','close'),
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
  s+=rect(0,0,740,720,BG,rx=0,op=0.92)+txt(70,100,'XINBEN ELECTRONICS',18,TEAL,'bold')+txt(70,245,'公司治理',76,WHITE,'bold')+txt(70,330,'与管理方法',76,ORANGE,'bold')+txt(70,400,'让客户看见一家制造企业如何被可靠地管理',30,MUTED)+line(70,460,470,460,ORANGE,5)+txt(70,520,'客户与公司介绍版',22,WHITE)+txt(70,575,'惠州市鑫犇电子有限公司',20,MUTED)+txt(70,650,'2026',18,DIM)
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
  a,b=body.split('｜'); yy=330
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
