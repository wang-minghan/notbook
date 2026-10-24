from pathlib import Path
from xml.sax.saxutils import escape

ROOT=Path(r'C:/Users/32027/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司/06_公司公共/公司治理PPT/xinben_governance_20261007')
OUT=ROOT/'drawio_assets'; IMG=ROOT/'images'
OUT.mkdir(exist_ok=True); IMG.mkdir(exist_ok=True)

DIAGS={
'01_governance_framework':('制度体系｜从原则到证据',['治理原则\n战略｜权责｜授权｜风险','管理制度\n人事｜合同｜采购｜生产｜品质｜财务｜安全｜信息','作业与证据\nSOP｜表单｜台账｜报告｜会议纪要']),
'02_order_change':('客户/合同/订单变更流程',['客户需求','订单评审','图纸与版本确认','产能/材料/交期确认','变更批准','任务更新','客户回传与留痕']),
'03_procurement_payment':('采购—供应商—入库—付款',['需求提出','供应商选择/评价','采购审批','到货验收','合格入库','对账','付款审批','供应商复盘']),
'04_personnel_lifecycle':('人员全生命周期',['需求与招聘','入职建档','岗位培训','能力确认','上岗授权','绩效与复训','调岗/替代','离职交接']),
'05_document_lifecycle':('制度文件生命周期',['需求提出','起草','跨部门评审','权限批准','发布培训','执行记录','定期复审','修订/作废/归档']),
'06_pdca':('PDCA持续改进闭环',['PLAN\n目标与风险','DO\n执行与记录','CHECK\n指标/审核/客诉','ACT\n纠正/预防/标准化']),
}
COLORS=['#2F6BFF','#1C9C8C','#E27A21','#6F7BF7','#9B59B6','#D9534F','#3CA37A','#A4772E']

def svg(title, items):
    w,h=1280,600
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', '<rect width="1280" height="600" fill="#F7F9FC"/>']
    parts.append(f'<text x="60" y="55" fill="#1F2D3D" font-family="Microsoft YaHei,Arial" font-size="28" font-weight="700">{escape(title)}</text>')
    n=len(items)
    if title.startswith('制度体系'):
        ys=[145,285,425]
        for i,it in enumerate(items):
            parts.append(f'<rect x="150" y="{ys[i]}" width="980" height="90" rx="14" fill="#FFFFFF" stroke="{COLORS[i]}" stroke-width="3"/>')
            parts.append(f'<text x="190" y="{ys[i]+38}" fill="{COLORS[i]}" font-family="Microsoft YaHei,Arial" font-size="22" font-weight="700">{escape(it.split(chr(10))[0])}</text>')
            parts.append(f'<text x="480" y="{ys[i]+38}" fill="#1F2D3D" font-family="Microsoft YaHei,Arial" font-size="20">{escape(it.split(chr(10))[1])}</text>')
            if i<2: parts.append(f'<path d="M640 {ys[i]+92} L640 {ys[i+1]-10}" stroke="#74859B" stroke-width="4" marker-end="url(#a)"/>')
    else:
        gap=24; x0=55; bw=(1170-gap*(n-1))/n
        for i,it in enumerate(items):
            x=x0+i*(bw+gap); y=235 if n<=4 else 215
            if i<n-1: parts.append(f'<path d="M{x+bw+5} {y+58} L{x+bw+gap-5} {y+58}" stroke="#74859B" stroke-width="4" marker-end="url(#a)"/>')
            parts.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="116" rx="14" fill="#FFFFFF" stroke="{COLORS[i%len(COLORS)]}" stroke-width="3"/>')
            lines=it.split('\\n')
            for j,line in enumerate(lines):
                parts.append(f'<text x="{x+bw/2:.1f}" y="{y+48+j*28}" text-anchor="middle" fill="#1F2D3D" font-family="Microsoft YaHei,Arial" font-size="18" font-weight="700">{escape(line)}</text>')
    parts.append('<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#74859B"/></marker></defs></svg>')
    return ''.join(parts)

def drawio(title, items):
    cells=['<mxCell id="0"/>','<mxCell id="1" parent="0"/>']
    n=len(items); y=120
    for i,it in enumerate(items):
        x=80+i*170
        if title.startswith('制度体系'): x=180; y=120+i*140
        cells.append(f'<mxCell id="n{i}" value="{escape(it)}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor={COLORS[i%len(COLORS)]};fontColor=#1F2D3D;fontSize=16;fontStyle=1;" vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="150" height="90" as="geometry"/></mxCell>')
        if i<n-1:
            x2=180 if title.startswith('制度体系') else x+170
            y2=y+140 if title.startswith('制度体系') else y
            cells.append(f'<mxCell id="e{i}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#74859B;" edge="1" parent="1" source="n{i}" target="n{i+1}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    return '<?xml version="1.0" encoding="UTF-8"?><mxfile host="app.diagrams.net"><diagram name="'+escape(title)+'"><mxGraphModel grid="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900"><root>'+''.join(cells)+'</root></mxGraphModel></diagram></mxfile>'

for stem,(title,items) in DIAGS.items():
    (OUT/(stem+'.drawio')).write_text(drawio(title,items),encoding='utf-8')
    (OUT/(stem+'.svg')).write_text(svg(title,items),encoding='utf-8')
    (IMG/(stem+'.svg')).write_text(svg(title,items),encoding='utf-8')
print('generated',len(DIAGS),'drawio diagrams and SVG previews')
