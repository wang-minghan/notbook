from pathlib import Path

OUT = Path(r'C:/Users/32027/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/06_公司公共/公司治理PPT/xinben_governance_20261007/svg_prototypes_v01')
OUT.mkdir(exist_ok=True)
W,H=1280,720
BG='#F7F9FC'; INK='#1F2D3D'; SUB='#526173'; BORDER='#D7E0EA'; BLUE='#2F6BFF'; TEAL='#1C9C8C'; ORANGE='#C56A25'; PURPLE='#7657B8'; RED='#D95C5C'; YELLOW='#A87519'; WHITE='#FFFFFF'

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def base(title, subtitle, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <marker id="arrowBlue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{BLUE}"/></marker>
 <marker id="arrowRed" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{RED}"/></marker>
 <marker id="arrowTeal" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{TEAL}"/></marker>
 <style>text{{font-family:'Microsoft YaHei','Arial',sans-serif;fill:{INK}}}.title{{font-size:30px;font-weight:700}}.sub{{font-size:14px;fill:{SUB}}}.label{{font-size:13px;font-weight:700}}.small{{font-size:12px}}.tiny{{font-size:11px}}</style>
</defs><rect width="1280" height="720" fill="{BG}"/>
<text x="52" y="48" class="title">{esc(title)}</text><text x="52" y="75" class="sub">{esc(subtitle)}</text>
{body}
<line x1="52" y1="680" x2="1228" y2="680" stroke="{BORDER}"/><text x="52" y="704" class="tiny" fill="{SUB}">鑫犇电子｜治理体系草案｜图形原型，待正式流程/授权文件确认</text><text x="1190" y="704" class="tiny" fill="{SUB}">DRAFT</text></svg>'''

def box(x,y,w,h,label,fill=WHITE,stroke=BORDER,fs=13):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/><text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle" style="font-size:{fs}px;font-weight:700">{esc(label)}</text>'

def page13():
    lane_x=52; lane_y=120; lane_w=1176; lane_h=82; head_w=126
    names=[('客户', '#EAF0FF'),('营运部','#EAF7F4'),('技术/工程','#F2ECFF'),('生产部','#FFF7DF'),('品质/仓储','#FFF2E7')]
    s='<text x="52" y="105" class="small" fill="'+SUB+'">阅读方向：左→右；泳道表示责任主体，跨泳道连线表示交接</text>'
    for i,(name,fill) in enumerate(names):
        y=lane_y+i*lane_h; s+=f'<rect x="{lane_x}" y="{y}" width="{lane_w}" height="{lane_h}" rx="4" fill="{WHITE}" stroke="{BORDER}"/><rect x="{lane_x}" y="{y}" width="{head_w}" height="{lane_h}" rx="4" fill="{fill}" stroke="{BORDER}"/><text x="{lane_x+head_w/2}" y="{y+47}" text-anchor="middle" class="label">{name}</text>'
    # nodes by lane
    nodes=[(195,137,110,48,'需求/图纸',BLUE,0),(340,219,110,48,'需求确认',TEAL,1),(485,301,110,48,'工程评审',PURPLE,2),(630,383,110,48,'排产/制造',ORANGE,3),(775,465,110,48,'检验/入库',TEAL,4),(920,219,110,48,'交付确认',BLUE,1)]
    for x,y,w,h,t,c,_ in nodes: s+=box(x,y,w,h,t,WHITE,c,12)
    # route arrows
    for (x1,y1,x2,y2,c) in [(305,161,340,243,BLUE),(450,243,485,325,TEAL),(595,325,630,407,PURPLE),(740,407,775,489,ORANGE),(885,489,920,243,TEAL)]:
        s+=f'<path d="M{x1} {y1} C{x1+20} {y1},{x2-20} {y2},{x2} {y2}" fill="none" stroke="{c}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    # decision and exception
    s+=f'<polygon points="1035,382 1070,417 1035,452 1000,417" fill="{WHITE}" stroke="{ORANGE}" stroke-width="2"/><text x="1035" y="414" text-anchor="middle" class="tiny">是否</text><text x="1035" y="428" text-anchor="middle" class="tiny">放行?</text>'
    s+=f'<path d="M1030 243 L1035 382" stroke="{BLUE}" stroke-width="3" fill="none" marker-end="url(#arrowBlue)"/><path d="M1000 417 C950 555,850 600,650 600 C470 600,420 520,520 407" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="760" y="616" class="small" fill="{RED}">异常：隔离/补充资料/升级评审 → 回到工程或制造确认</text>'
    s+=f'<rect x="1080" y="120" width="148" height="132" rx="8" fill="{WHITE}" stroke="{BORDER}"/><text x="1095" y="145" class="label">证据节点</text><text x="1095" y="170" class="tiny">· 订单/图纸版本</text><text x="1095" y="192" class="tiny">· 评审记录</text><text x="1095" y="214" class="tiny">· 检验记录</text><text x="1095" y="236" class="tiny">· 放行/交付记录</text>'
    return base('13｜订单到交付总流程','五泳道端到端流程：责任主体、交接、决策和异常回路分开表达',s)

def page27():
    s=''
    # heatmap
    x0,y0=92,190; cell=54
    s+='<text x="72" y="130" class="label">风险热力图</text><text x="72" y="152" class="tiny" fill="'+SUB+'">横轴：可能性　纵轴：影响</text>'
    colors=['#EAF7F4','#FFF7DF','#FFF2E7','#FFF0F0']
    for r in range(4):
        for c in range(4): s+=f'<rect x="{x0+c*cell}" y="{y0+(3-r)*cell}" width="{cell}" height="{cell}" fill="{colors[min(3,r+c)]}" stroke="{WHITE}"/>'
    s+=f'<text x="{x0+108}" y="430" class="small" text-anchor="middle">可能性 →</text><text x="45" y="300" class="small" transform="rotate(-90 45 300)" text-anchor="middle">影响 ↑</text>'
    risks=[(1,1,'R-01',YELLOW),(2,2,'R-02',ORANGE),(3,3,'R-03',RED)]
    for cx,cy,lab,col in risks:
        x=x0+cx*cell+cell/2;y=y0+(3-cy)*cell+cell/2;s+=f'<circle cx="{x}" cy="{y}" r="17" fill="{col}"/><text x="{x}" y="{y+4}" class="tiny" text-anchor="middle" fill="{WHITE}">{lab}</text>'
    s+=f'<rect x="78" y="455" width="248" height="78" rx="8" fill="{WHITE}" stroke="{BORDER}"/><text x="94" y="478" class="tiny" fill="{SUB}">颜色仅表示风险等级分区；</text><text x="94" y="498" class="tiny" fill="{SUB}">正式阈值、时限和岗位待确认。</text><text x="94" y="518" class="tiny" fill="{SUB}">编号用于右侧责任映射。</text>'
    # explicit mapping table
    s+=f'<rect x="370" y="120" width="850" height="480" rx="10" fill="{WHITE}" stroke="{BORDER}"/><text x="400" y="158" class="label">风险编号 → 触发等级 → 责任层级</text><text x="400" y="184" class="tiny" fill="{SUB}">不使用长曲线推断；每个风险编号直接落到一条责任路径。</text>'
    rows=[('R-01','低/中','业务线自处置','登记、设责任人、按期验证',YELLOW),('R-02','中/高','职能部门复核','评估影响、设期限、必要时升级',ORANGE),('R-03','高','管理层介入','决策资源、确认措施、监督关闭',RED)]
    for i,(rid,level,owner,action,col) in enumerate(rows):
        y=225+i*95
        s+=f'<rect x="400" y="{y}" width="92" height="54" rx="8" fill="{col}"/><text x="446" y="{y+34}" text-anchor="middle" style="font-size:15px;font-weight:700;fill:{WHITE}">{rid}</text>'
        s+=f'<line x1="500" y1="{y+27}" x2="535" y2="{y+27}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
        s+=f'<rect x="545" y="{y}" width="110" height="54" rx="8" fill="#F7F9FC" stroke="{col}" stroke-width="2"/><text x="600" y="{y+34}" text-anchor="middle" class="label">{level}</text>'
        s+=f'<line x1="663" y1="{y+27}" x2="698" y2="{y+27}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
        s+=f'<rect x="708" y="{y}" width="210" height="54" rx="8" fill="{WHITE}" stroke="{col}" stroke-width="2"/><text x="813" y="{y+34}" text-anchor="middle" class="label">{owner}</text>'
        s+=f'<rect x="940" y="{y}" width="245" height="54" rx="8" fill="#EEF3F8" stroke="{BORDER}"/><text x="952" y="{y+23}" class="tiny" fill="{SUB}">{action[:18]}</text><text x="952" y="{y+40}" class="tiny" fill="{SUB}">{action[18:]}</text>'
    s+=f'<path d="M918 510 C850 570,620 570,545 510" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="810" y="590" class="tiny" text-anchor="middle" fill="{RED}">验证失败：返回对应编号重新登记；验证通过：形成关闭证据</text>'
    return base('27｜风险登记与升级','风险点先定位，再按编号直接映射到触发等级和责任层级',s)

def page16():
    s='<text x="52" y="118" class="small" fill="'+SUB+'">同一笔采购至少经过申请、采购、收货、对账/付款的相互核对</text>'
    lanes=[('需求部门','#EAF0FF'),('采购 / 营运部','#EAF7F4'),('仓储 / 收货','#FFF7DF'),('财务 / 授权人','#FFF2E7')]
    lx,ly,lw,lh,hw=52,145,1176,78,142
    for i,(name,fill) in enumerate(lanes):
        y=ly+i*lh; s+=f'<rect x="{lx}" y="{y}" width="{lw}" height="{lh}" rx="4" fill="{WHITE}" stroke="{BORDER}"/><rect x="{lx}" y="{y}" width="{hw}" height="{lh}" rx="4" fill="{fill}" stroke="{BORDER}"/><text x="{lx+hw/2}" y="{y+44}" text-anchor="middle" class="label">{name}</text>'
    nodes=[(220,160,120,'采购申请','需求与规格',BLUE),(390,238,120,'询价 / 下单','供应商与价格',TEAL),(560,316,120,'收货 / 入库','数量与状态',ORANGE),(730,394,120,'对账 / 付款','授权与留痕',PURPLE)]
    for x,y,w,a,b,c in nodes:
        s+=f'<rect x="{x}" y="{y}" width="{w}" height="48" rx="8" fill="{WHITE}" stroke="{c}" stroke-width="2"/><text x="{x+w/2}" y="{y+20}" text-anchor="middle" class="label">{a}</text><text x="{x+w/2}" y="{y+37}" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
    for x1,y1,x2,y2,c in [(340,184,390,262,BLUE),(510,262,560,340,TEAL),(680,340,730,418,ORANGE)]:
        s+=f'<path d="M{x1} {y1} C{x1+24} {y1},{x2-24} {y2},{x2} {y2}" fill="none" stroke="{c}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<rect x="890" y="145" width="338" height="170" rx="8" fill="{WHITE}" stroke="{BORDER}"/><text x="915" y="175" class="label">三类相互核对资料</text><text x="915" y="205" class="small">申请 / 订单资料</text><text x="915" y="233" class="small">收货 / 入库资料</text><text x="915" y="261" class="small">发票 / 付款资料</text><text x="915" y="291" class="tiny" fill="{SUB}">不得由同一角色独立完成全链路</text>'
    s+=f'<path d="M850 418 C820 520,600 570,410 520 C320 495,300 430,410 340" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="700" y="570" class="small" fill="{RED}" text-anchor="middle">数量 / 质量 / 价格不一致：暂停付款并退回核对</text>'
    s+=f'<rect x="90" y="560" width="1080" height="54" rx="6" fill="#FFF7DF" stroke="#E8D39A"/><text x="630" y="585" text-anchor="middle" class="tiny" fill="{YELLOW}">具体金额、审批层级、例外授权：待正式授权文件确认；本页仅表达职责分离原则。</text>'
    return base('16｜采购到付款','职责分离泳道：申请、下单、收货、对账和付款由不同责任主体承接',s)

def page24():
    s='<text x="52" y="118" class="small" fill="'+SUB+'">权限矩阵只回答“谁可以做什么”；申请、批准、留痕和回收另列为控制闭环</text>'
    x0,y0=58,170; cols=[('资料类型',180),('业务/营运',180),('技术/品质',180),('管理层',180),('控制动作',240)]; rows=[('报价 / 订单','可见','需审批','可见','申请→批准→留痕'),('图纸 / 工艺','按项目','可见','可见','项目结束→复核'),('质量 / 客诉','可见','可见','可见','异常→上报→关闭'),('经营 / 人事','不可见','不可见','可见','离岗→立即回收')]
    x=x0
    for i,(h,w) in enumerate(cols):
        fill='#EAF0FF' if i<4 else '#FFF7DF'; s+=f'<rect x="{x}" y="{y0}" width="{w}" height="48" fill="{fill}" stroke="{BORDER}"/><text x="{x+w/2}" y="{y0+30}" text-anchor="middle" class="label">{h}</text>';x+=w
    for r,row in enumerate(rows):
        y=y0+48+r*58;x=x0
        for c,val in enumerate(row):
            fill=WHITE;stroke=BORDER
            if c==0:fill='#F7F9FC'
            elif c==4:fill='#FFF7DF';stroke=ORANGE
            elif '需审批' in val or '按项目' in val:fill='#FFF7DF';stroke=ORANGE
            elif val=='不可见':fill='#FFF0F0';stroke=RED
            elif val=='可见':fill='#EAF7F4';stroke=TEAL
            s+=f'<rect x="{x}" y="{y}" width="{cols[c][1]}" height="58" fill="{fill}" stroke="{stroke}"/><text x="{x+cols[c][1]/2}" y="{y+35}" text-anchor="middle" class="small">{val}</text>';x+=cols[c][1]
    s+=f'<rect x="58" y="475" width="1170" height="118" rx="8" fill="{WHITE}" stroke="{BORDER}"/><text x="82" y="505" class="label">权限控制闭环：四个动作对应矩阵中的每一次权限变化</text>'
    steps=[('1 申请','说明业务需要',BLUE),('2 批准','最小必要权限',ORANGE),('3 使用留痕','访问可追溯',TEAL),('4 复核/回收','岗位变化或异常立即处理',RED)]
    for i,(a,b,col) in enumerate(steps):
        x=82+i*280;s+=f'<rect x="{x}" y="530" width="220" height="42" rx="7" fill="{WHITE}" stroke="{col}" stroke-width="2"/><text x="{x+110}" y="548" text-anchor="middle" class="small">{a}</text><text x="{x+110}" y="565" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
        if i<3:s+=f'<line x1="{x+220}" y1="551" x2="{x+270}" y2="551" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    return base('24｜客户资料与信息权限','权限矩阵与控制闭环：按需批准、使用留痕、变化即回收',s)

def page33():
    s='<text x="52" y="118" class="small" fill="'+SUB+'">证据链不是信息罗列，而是从要求到复盘的可追溯关系</text>'
    stages=[('制度要求',BLUE,'制度/标准'),('责任活动',PURPLE,'岗位/部门'),('执行记录',TEAL,'表单/台账'),('检查结果',ORANGE,'测量/审核'),('整改证据',RED,'问题/措施'),('评审结论',ORANGE,'会议/决定'),('改进证据',TEAL,'验证/更新')]
    x=60; y=250; w=150; gap=18
    for i,(a,c,b) in enumerate(stages):
        s+=f'<rect x="{x}" y="{y}" width="{w}" height="108" rx="10" fill="{WHITE}" stroke="{c}" stroke-width="3"/><text x="{x+w/2}" y="{y+40}" text-anchor="middle" class="label">{a}</text><text x="{x+w/2}" y="{y+68}" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
        if i<len(stages)-1:s+=f'<line x1="{x+w}" y1="{y+54}" x2="{x+w+gap-4}" y2="{y+54}" stroke="{c}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
        x+=w+gap
    # evidence objects under each control stage make the chain auditable
    evidence=['制度条款','责任记录','执行台账','检查报告','整改闭环','会议纪要','版本更新']
    x=60
    for i,ev in enumerate(evidence):
        s+=f'<line x1="{x+w/2}" y1="358" x2="{x+w/2}" y2="390" stroke="{SUB}" stroke-width="2"/><rect x="{x+18}" y="390" width="114" height="34" rx="6" fill="#EEF3F8" stroke="{BORDER}"/><text x="{x+w/2}" y="412" text-anchor="middle" class="tiny" fill="{SUB}">证据：{ev}</text>'
        x+=w+gap
    # traceability bottom
    s+=f'<path d="M135 430 C135 535,1110 535,1110 430" fill="none" stroke="{TEAL}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowTeal)"/><text x="620" y="565" text-anchor="middle" class="small" fill="{TEAL}">复盘反馈：改进结果反向更新制度、责任、表单或检查方式</text>'
    s+=f'<rect x="90" y="150" width="1080" height="48" rx="8" fill="#EAF0FF" stroke="#B7C9FF"/><text x="630" y="180" text-anchor="middle" class="label" fill="{BLUE}">每一段都应能回答：谁负责？留下什么记录？由谁验证？</text>'
    s+=f'<rect x="90" y="590" width="1080" height="42" rx="6" fill="#FFF7DF" stroke="#E8D39A"/><text x="630" y="616" text-anchor="middle" class="tiny" fill="{YELLOW}">待确认：正式表单编号、记录保存期限、评审频次和证据归档位置</text>'
    return base('33｜管理体系证据链','从要求到执行、检查、整改和改进，形成可追溯的治理证据',s)

def page26():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">看板阅读顺序：目标/实际 → 趋势 → 异常风险 → 管理决策；数值与责任人待正式口径确认</text>'
    cards=[('交付','OTD / 准时交付',BLUE,'目标｜实际｜趋势','待确认'),('质量','一次合格率',PURPLE,'目标｜实际｜趋势','待确认'),('采购/库存','交期与库存覆盖',TEAL,'目标｜实际｜趋势','待确认'),('现金/成本','采购成本 / 回款',ORANGE,'目标｜实际｜趋势','待确认'),('能力','关键岗位覆盖率',BLUE,'目标｜实际｜趋势','待确认'),('整改闭环','逾期与复发项',RED,'目标｜实际｜趋势','待确认')]
    for i,(a,b,col,line,val) in enumerate(cards):
        x=52+(i%3)*390;y=150+(i//3)*185
        s+=f'<rect x="{x}" y="{y}" width="350" height="148" rx="10" fill="{WHITE}" stroke="{BORDER}"/><rect x="{x}" y="{y}" width="350" height="10" rx="5" fill="{col}"/><text x="{x+20}" y="{y+39}" class="label">{a}</text><text x="{x+20}" y="{y+64}" class="small" fill="{SUB}">{b}</text><text x="{x+20}" y="{y+100}" class="label" fill="{col}">{val}</text><text x="{x+20}" y="{y+124}" class="tiny" fill="{SUB}">{line}</text>'
        # miniature trend chart, deliberately not implying real values
        s+=f'<polyline points="{x+218},{y+112} {x+244},{y+92} {x+270},{y+104} {x+296},{y+76} {x+322},{y+84}" fill="none" stroke="{col}" stroke-width="3"/><line x1="{x+210}" y1="{y+125}" x2="{x+330}" y2="{y+125}" stroke="{BORDER}"/>'
    s+=f'<rect x="52" y="555" width="560" height="72" rx="8" fill="#FFF0F0" stroke="{RED}"/><text x="76" y="584" class="label" fill="{RED}">异常 / 需要关注</text><text x="76" y="608" class="small" fill="{SUB}">指标偏离目标、逾期或复发项：待确认后列入责任人和期限</text>'
    s+=f'<rect x="640" y="555" width="588" height="72" rx="8" fill="#FFF7DF" stroke="{ORANGE}"/><text x="664" y="584" class="label" fill="{ORANGE}">管理层决策区</text><text x="664" y="608" class="small" fill="{SUB}">本周期需决策事项：资源、优先级、升级或目标调整（待确认）</text>'
    return base('26｜管理指标看板','用目标—实际—趋势—异常—决策组织经营指标，不以普通卡片代替看板',s)

def page20():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">交接只有在完整性闸口通过后才进入下一部门；缺项或版本不一致必须退回</text>'
    stages=[('交出方','输入包','版本 / 数量 / 状态 / 期限',BLUE),('完整性闸口','四项检查','资料齐全｜版本一致｜责任期限｜验收标准',ORANGE),('接收方','验收包','确认 / 差异记录 / 受控任务',TEAL),('受控执行','责任承接','异常升级 / 截止日期 / 输出证据',PURPLE)]
    xs=[70,350,650,950]
    for i,(a,b,c,col) in enumerate(stages):
        x=xs[i];s+=f'<rect x="{x}" y="220" width="230" height="150" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{x+115}" y="255" text-anchor="middle" class="label">{a}</text><text x="{x+115}" y="290" text-anchor="middle" class="small" fill="{col}">{b}</text><text x="{x+115}" y="325" text-anchor="middle" class="tiny" fill="{SUB}">{c}</text>'
        if i<3:s+=f'<line x1="{x+230}" y1="295" x2="{xs[i+1]-16}" y2="295" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M465 370 C430 480,250 500,220 370" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="325" y="500" text-anchor="middle" class="small" fill="{RED}">缺项 / 版本不一致：退回补齐</text>'
    s+=f'<rect x="80" y="145" width="1120" height="48" rx="8" fill="#EAF0FF" stroke="#B7C9FF"/><text x="640" y="175" text-anchor="middle" class="label" fill="{BLUE}">交接证据：清单、版本号、接收确认、差异记录、责任人、截止日期、异常升级记录</text>'
    return base('20｜跨部门交接标准','用输入包—完整性闸口—验收包—受控执行表达责任转移',s)

def page30():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">不符合项不能只记录“已整改”；必须证明原因、措施、验证有效并控制复发</text>'
    stages=[('01 发现登记','事实｜证据｜来源',BLUE),('02 分级升级','风险｜责任｜期限',ORANGE),('03 原因分析','根因｜复发控制',PURPLE),('04 制定措施','责任｜期限｜记录',TEAL),('05 效果验证','证据｜有效性',TEAL),('06 关闭','批准｜留痕',BLUE)]
    x=58
    for i,(a,b,col) in enumerate(stages):
        y=230+(i%2)*170; xx=x+(i//2)*390
        s+=f'<rect x="{xx}" y="{y}" width="300" height="100" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{xx+150}" y="{y+38}" text-anchor="middle" class="label">{a}</text><text x="{xx+150}" y="{y+68}" text-anchor="middle" class="small" fill="{SUB}">{b}</text>'
        if i<5:
            nx=x+((i+1)//2)*390; ny=230+((i+1)%2)*170
            if i%2==0:s+=f'<line x1="{xx+300}" y1="{y+50}" x2="{nx-14}" y2="{ny+50}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
            else:s+=f'<line x1="{xx+150}" y1="{y+100}" x2="{nx+150}" y2="{ny-14}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M1100 400 C1180 430,1180 570,1010 570 C860 570,760 530,760 430" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="1000" y="610" text-anchor="middle" class="small" fill="{RED}">验证失败 / 逾期 / 复发：再升级，不直接关闭</text>'
    s+=f'<rect x="58" y="555" width="650" height="55" rx="7" fill="#FFF7DF" stroke="#E8D39A"/><text x="383" y="588" text-anchor="middle" class="tiny" fill="{YELLOW}">责任岗位、整改期限和关闭权限：待正式授权文件确认</text>'
    return base('30｜不符合项与整改关闭','登记—升级—找根因—措施—验证—关闭，并保留失败回路',s)

def page18():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">客户问题统一入口；内部处置与对外回复分开，验证有效后才关闭</text>'
    stages=[('01 接收分级','入口｜影响判定',BLUE),('02 临时措施','隔离｜遏制风险',RED),('03 原因分析','事实｜根因｜证据',PURPLE),('04 纠正措施','责任｜期限｜记录',ORANGE),('05 效果验证','有效性｜复发控制',TEAL),('06 客户回复','结论｜关闭证据',BLUE)]
    x=58;y=245;w=180;gap=22
    for i,(a,b,col) in enumerate(stages):
        xx=x+i*(w+gap)
        s+=f'<rect x="{xx}" y="{y}" width="{w}" height="116" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{xx+w/2}" y="{y+42}" text-anchor="middle" class="label">{a}</text><text x="{xx+w/2}" y="{y+75}" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
        if i<5:s+=f'<line x1="{xx+w}" y1="{y+58}" x2="{xx+w+gap-5}" y2="{y+58}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M1110 430 C1030 560,520 585,360 430" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="735" y="585" text-anchor="middle" class="small" fill="{RED}">未验证或重复发生：回到原因分析 / 纠正措施</text>'
    s+=f'<rect x="100" y="150" width="1080" height="48" rx="8" fill="#EAF7F4" stroke="#A8DCD4"/><text x="640" y="180" text-anchor="middle" class="label" fill="{TEAL}">对外回复必须引用：事实、处置结论、验证证据和后续防复发安排</text>'
    return base('18｜客诉与纠正措施','从客户入口到临时遏制、根因、纠正、验证和回复的闭环',s)

def page15():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">先确认订单输入和资源能力，再经过开工决策闸口；条件不足不得直接开工</text>'
    items=[('订单输入','产品｜数量｜交期｜版本',BLUE),('能力确认','产能｜物料｜模具｜人员',TEAL),('风险清单','缺口｜责任｜补充期限',YELLOW),('任务发布','受控版本｜责任｜节点',ORANGE)]
    xs=[70,350,630,910]
    for i,(a,b,col) in enumerate(items):
        x=xs[i];s+=f'<rect x="{x}" y="240" width="220" height="120" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{x+110}" y="282" text-anchor="middle" class="label">{a}</text><text x="{x+110}" y="320" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
        if i<3:s+=f'<line x1="{x+220}" y1="300" x2="{xs[i+1]-18}" y2="300" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<polygon points="520,190 570,240 520,290 470,240" fill="{WHITE}" stroke="{ORANGE}" stroke-width="3"/><text x="520" y="237" text-anchor="middle" class="tiny">条件</text><text x="520" y="252" text-anchor="middle" class="tiny">满足？</text>'
    s+=f'<line x1="460" y1="300" x2="470" y2="240" stroke="{TEAL}" stroke-width="3" marker-end="url(#arrowBlue)"/><path d="M520 290 C520 430,700 480,740 360" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="620" y="470" text-anchor="middle" class="small" fill="{RED}">否：形成风险清单，补充资源或升级承诺</text>'
    s+=f'<rect x="95" y="530" width="1090" height="60" rx="8" fill="#FFF7DF" stroke="#E8D39A"/><text x="640" y="566" text-anchor="middle" class="label" fill="{YELLOW}">任务发布前必须完成能力确认；交期承诺不能绕过资源与版本检查</text>'
    return base('15｜生产计划与任务下达','订单输入—能力确认—开工闸口—任务发布，并保留资源不足回路',s)

def page08():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">本页是部门职责地图摘要：看输入、输出和协同接口；不替代岗位SOP或授权文件</text>'
    deps=[('生产部',['订单评审','物料齐套','质量要求'],['生产任务','产量/异常记录'],['品质判定','营运交期协同'],BLUE,['工程技术组','冲压车间','模具维修组','清洗车间']),('品质部',['来料','首件 / 制程','成品待检'],['检验记录','不合格处置','客诉闭环'],['独立质量判断','反馈营运 / 生产'],PURPLE,['制程巡检组','成品出货检验组']),('营运部',['客户订单','产能 / 质量意见','客户需求'],['订单评审','采购订单','出入库 / 交付'],['业务、采购、仓储','分工执行'],TEAL,['业务组','采购组','仓储组']),('行政部',['用工需求','制度事项','后勤事项'],['人事档案','入离职记录','后勤记录'],['人员协同','保障协同'],ORANGE,['人事组','后勤组']),('财务部',['业务单据','费用 / 付款申请','经营数据'],['会计凭证','经营报表','资金 / 付款记录'],['财务审核 / 执行','按授权边界审批'],BLUE,['会计组','出纳组'])]
    x0=52;w=226;gap=12
    for i,(name,ins,outs,ifs,col,subs) in enumerate(deps):
        x=x0+i*(w+gap);s+=f'<rect x="{x}" y="155" width="{w}" height="405" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><rect x="{x}" y="155" width="{w}" height="52" rx="10" fill="{col}"/><text x="{x+w/2}" y="188" text-anchor="middle" style="font-size:16px;font-weight:700;fill:{WHITE}">{name}</text>'
        def lines(label,items,y):
            nonlocal s
            s+=f'<text x="{x+16}" y="{y}" class="label" fill="{col}">{label}</text>'
            for j,t in enumerate(items): s+=f'<text x="{x+16}" y="{y+23+j*17}" class="tiny" fill="{SUB}">· {t}</text>'
        lines('输入',ins,232);s+=f'<line x1="{x+16}" y1="300" x2="{x+w-16}" y2="300" stroke="{BORDER}"/>'
        lines('输出',outs,326);s+=f'<line x1="{x+16}" y1="394" x2="{x+w-16}" y2="394" stroke="{BORDER}"/>'
        lines('协同接口',ifs,405);s+=f'<rect x="{x+12}" y="458" width="{w-24}" height="100" rx="6" fill="#F7F9FC" stroke="{BORDER}"/><text x="{x+20}" y="480" class="tiny" fill="{SUB}">下属组织</text>'
        for j,t in enumerate(subs): s+=f'<text x="{x+20}" y="{500+j*13}" class="tiny" fill="{SUB}">· {t}</text>'
    s+=f'<rect x="80" y="590" width="1120" height="40" rx="7" fill="#FFF7DF" stroke="#E8D39A"/><text x="640" y="615" text-anchor="middle" class="tiny" fill="{YELLOW}">待确认边界：具体时限、金额阈值、岗位替代与例外授权以正式制度/授权文件为准</text>'
    return base('08｜部门职责地图','五个正式一级部门的输入、输出与协同接口；下属组织归属按受控矩阵',s)

def page21():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">主环表示受控文件生命周期；红色分支表示旧版隔离、回收和作废</text>'
    st=[('起草','需求｜版本号',BLUE),('评审','专业意见',PURPLE),('批准发布','受控清单',ORANGE),('执行与培训','使用记录',TEAL),('复审/修订','触发新版本',BLUE)]
    x=65;y=245;w=190;gap=38
    for i,(a,b,col) in enumerate(st):
        xx=x+i*(w+gap);s+=f'<rect x="{xx}" y="{y}" width="{w}" height="110" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{xx+w/2}" y="{y+42}" text-anchor="middle" class="label">{a}</text><text x="{xx+w/2}" y="{y+74}" text-anchor="middle" class="small" fill="{SUB}">{b}</text>'
        if i<4:s+=f'<line x1="{xx+w}" y1="{y+55}" x2="{xx+w+gap-8}" y2="{y+55}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M825 365 C820 500,600 540,350 490" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="590" y="535" class="small" text-anchor="middle" fill="{RED}">旧版本：隔离、回收、标识、留痕，不回流主流程</text>'
    s+=f'<rect x="100" y="150" width="1080" height="48" rx="8" fill="#EAF7F4" stroke="#A8DCD4"/><text x="640" y="180" text-anchor="middle" class="label" fill="{TEAL}">证据：版本清单｜审批记录｜发布通知｜培训记录｜旧版回收记录</text>'
    return base('21｜文件编制与版本控制','让新版本可追溯、可批准、可培训，旧版本可隔离和回收',s)

def page23():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">培训不等于授权：能力确认是权限打开前的闸门，失效时立即暂停或回收</text>'
    for i,(a,b,col) in enumerate([('培训','培训记录',PURPLE),('能力确认','评价结果',PURPLE),('岗位授权','授权批准',ORANGE),('有效维护','复核日期',TEAL)]):
        x=70+i*280;s+=f'<rect x="{x}" y="190" width="220" height="100" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{x+110}" y="230" text-anchor="middle" class="label">{a}</text><text x="{x+110}" y="260" text-anchor="middle" class="small" fill="{SUB}">{b}</text>'
        if i<3:s+=f'<line x1="{x+220}" y1="240" x2="{x+262}" y2="240" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<rect x="70" y="370" width="1090" height="130" rx="10" fill="{WHITE}" stroke="{BORDER}"/><text x="100" y="410" class="label">授权生命周期</text><text x="100" y="450" class="small" fill="{SUB}">维护与复核 → 复训 / 调岗 / 替代 → 失效时暂停 → 离岗或不合格时回收权限</text>'
    s+=f'<path d="M1080 290 C1160 340,1160 470,1010 470" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="1010" y="540" text-anchor="middle" class="small" fill="{RED}">能力失效：暂停 / 回收</text>'
    return base('23｜人员能力与岗位授权','能力确认阶梯 + 授权生命周期：证据齐全后授权，变化触发复核',s)

def page28():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">现场先控制人身与环境风险，再按分级要求上报、调查、整改和验证</text>'
    st=[('01 发现','检查 / 事件',BLUE),('02 现场处置','隔离风险',RED),('03 逐级上报','按级报告',ORANGE),('04 责任调查','事实 / 原因 / 证据',PURPLE),('05 整改','措施 / 责任 / 记录',TEAL),('06 验证关闭','效果 / 防复发',BLUE)]
    x=55;y=245;w=175;gap=25
    for i,(a,b,col) in enumerate(st):
        xx=x+i*(w+gap);s+=f'<rect x="{xx}" y="{y}" width="{w}" height="112" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{xx+w/2}" y="{y+42}" text-anchor="middle" class="label">{a}</text><text x="{xx+w/2}" y="{y+75}" text-anchor="middle" class="tiny" fill="{SUB}">{b}</text>'
        if i<5:s+=f'<line x1="{xx+w}" y1="{y+56}" x2="{xx+w+gap-6}" y2="{y+56}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M1100 410 C1000 560,500 580,350 410" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowRed)"/><text x="720" y="580" text-anchor="middle" class="small" fill="{RED}">未通过 / 复发：再调查或升级</text>'
    s+=f'<rect x="100" y="150" width="1080" height="48" rx="8" fill="#FFF7DF" stroke="#E8D39A"/><text x="640" y="180" text-anchor="middle" class="label" fill="{YELLOW}">响应级别、通知时限和责任岗位：待确认，以正式应急文件为准</text>'
    return base('28｜安全、环保与应急','发现—处置—上报—调查—整改—验证，现场与管理层共同承接',s)

def page29():
    s=f'<text x="52" y="116" class="small" fill="{SUB}">按过程检查证据，再由管理评审形成决策；跟踪结果进入下一轮检查</text>'
    st=[('01 制定计划','范围｜过程｜证据',BLUE),('02 过程检查','现场｜记录｜访谈',TEAL),('03 发现分级','事实｜风险｜整改',ORANGE),('04 管理评审','输入｜决策｜资源',PURPLE),('05 跟踪','关闭证据',TEAL)]
    x=75;y=245;w=205;gap=35
    for i,(a,b,col) in enumerate(st):
        xx=x+i*(w+gap);s+=f'<rect x="{xx}" y="{y}" width="{w}" height="112" rx="10" fill="{WHITE}" stroke="{col}" stroke-width="3"/><text x="{xx+w/2}" y="{y+42}" text-anchor="middle" class="label">{a}</text><text x="{xx+w/2}" y="{y+75}" text-anchor="middle" class="small" fill="{SUB}">{b}</text>'
        if i<4:s+=f'<line x1="{xx+w}" y1="{y+56}" x2="{xx+w+gap-8}" y2="{y+56}" stroke="{col}" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    s+=f'<path d="M1150 410 C1080 550,350 570,220 410" fill="none" stroke="{TEAL}" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrowTeal)"/><text x="690" y="565" text-anchor="middle" class="small" fill="{TEAL}">跟踪结果：进入下一轮检查与评审</text>'
    s+=f'<rect x="100" y="150" width="1080" height="48" rx="8" fill="#FFF7DF" stroke="#E8D39A"/><text x="640" y="180" text-anchor="middle" class="label" fill="{YELLOW}">管理评审输入、输出和频次：待确认，以正式机制为准</text>'
    return base('29｜内部检查与管理评审','计划—检查—分级—评审—跟踪，形成可回到下一轮的管理回路',s)

(OUT/'13_订单到交付总流程.svg').write_text(page13(),encoding='utf-8')
(OUT/'16_采购到付款.svg').write_text(page16(),encoding='utf-8')
(OUT/'24_客户资料与信息权限.svg').write_text(page24(),encoding='utf-8')
(OUT/'27_风险登记与升级.svg').write_text(page27(),encoding='utf-8')
(OUT/'33_管理体系证据链.svg').write_text(page33(),encoding='utf-8')
(OUT/'18_客诉与纠正措施.svg').write_text(page18(),encoding='utf-8')
(OUT/'15_生产计划与任务下达.svg').write_text(page15(),encoding='utf-8')
(OUT/'08_部门职责地图.svg').write_text(page08(),encoding='utf-8')
(OUT/'21_文件编制与版本控制.svg').write_text(page21(),encoding='utf-8')
(OUT/'23_人员能力与岗位授权.svg').write_text(page23(),encoding='utf-8')
(OUT/'28_安全、环保与应急.svg').write_text(page28(),encoding='utf-8')
(OUT/'29_内部检查与管理评审.svg').write_text(page29(),encoding='utf-8')
(OUT/'20_跨部门交接标准.svg').write_text(page20(),encoding='utf-8')
(OUT/'26_管理指标看板.svg').write_text(page26(),encoding='utf-8')
(OUT/'30_不符合项与整改关闭.svg').write_text(page30(),encoding='utf-8')
print('generated',len(list(OUT.glob('*.svg'))),OUT)
