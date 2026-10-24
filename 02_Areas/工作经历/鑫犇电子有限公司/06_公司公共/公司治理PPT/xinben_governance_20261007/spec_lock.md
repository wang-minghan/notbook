# PPT Master spec_lock — 鑫犇治理体系 V3

## Locked identity
- canvas: 1280x720
- background: #F7F9FC
- text_primary: #1F2D3D
- text_secondary: #526173
- border: #D7E0EA
- blue: #2F6BFF
- teal: #1C9C8C
- orange: #C56A25
- purple: #7657B8
- red: #D95C5C
- yellow: #A87519
- allowed_derived_colors: #1C9C8C, #1F2D3D, #2F6BFF, #526173, #6B7A90, #7657B8, #805B12, #8091A5, #8190A0, #8A97A8, #9AA9BA, #A87519, #AAB7C6, #B84747, #C56A25, #D5DDE8, #D79A2B, #D7E0EA, #D95C5C, #DCE4EE, #E1E7F0, #E27A21, #E8D39A, #EAF0FF, #EAF7F4, #F2ECFF, #F7F9FC, #F8FCFB, #FBF9FF, #FBFCFE, #FFF0F0, #FFF2E7, #FFF7DF, #FFFBF7, #FFFDF5, #FFFFFF
- font_family: Microsoft YaHei, Arial, sans-serif
- title_size: 36–40px
- subtitle_size: 16px
- body_size: 14–18px
- footer_size: 12px

## colors
- background: #F7F9FC
- text_primary: #1F2D3D
- text_secondary: #526173
- border: #D7E0EA
- blue: #2F6BFF
- teal: #1C9C8C
- orange: #C56A25
- purple: #7657B8
- red: #D95C5C
- yellow: #A87519
- derived_01: #FFFFFF
- derived_02: #8190A0
- derived_03: #E27A21
- derived_04: #8A97A8
- derived_05: #D79A2B
- derived_06: #805B12
- derived_07: #EAF0FF
- derived_08: #EAF7F4
- derived_09: #F2ECFF
- derived_10: #FFF2E7
- derived_11: #FFF7DF
- derived_12: #FFF0F0
- derived_13: #9AA9BA
- derived_14: #8091A5
- derived_15: #B84747
- derived_16: #E8D39A
- derived_17: #D5DDE8
- derived_18: #DCE4EE
- derived_19: #E1E7F0
- derived_20: #F8FCFB
- derived_21: #FBF9FF
- derived_22: #FBFCFE
- derived_23: #FFFBF7
- derived_24: #FFFDF5
- derived_25: #6B7A90
- derived_26: #AAB7C6

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- compact_family: Microsoft YaHei,Arial
- title: 40
- hero: 76
- subtitle: 16
- body: 14
- sub_body: 11
- footer: 12

## Locked semantics
- Blue = customer input / main route / structure
- Teal = collaboration / record / verification / closure
- Orange = authorization / decision / management attention
- Purple = professional judgement / quality / engineering
- Red = abnormality / rejection / escalation
- Yellow = risk / pending confirmation
- Solid line = normal route
- Dashed line = information sync or escalation
- Diamond = decision or approval condition
- Rounded rectangle = activity or controlled output
- Document shape/card = evidence or record
- Do not imply an unconfirmed authority, certification, KPI value, or implemented system as an existing fact.

## Page-level lock
| Page | Rhythm | Layout | Chart grammar | Non-negotiable check |
|---|---|---|---|---|
| 01 | breathing | cover_split | hero image + statement | no process cards |
| 02 | breathing | boundary_split | included/excluded boundary | distinguish governance from SOP |
| 03 | anchor | layered | layered architecture | vertical layers, feedback arrow |
| 04 | breathing | radial | radial principles | center is governance logic |
| 05 | anchor | hierarchy | hierarchy staircase | show control relationship |
| 06 | anchor | tree | top-down org tree | parent-child lines, not process arrows |
| 07 | breathing | split | responsibility split | decision vs execution distinction |
| 08 | dense | map | interface map | inputs/outputs visible |
| 09 | anchor | lifecycle | lifecycle loop | authorization recovery visible |
| 10 | dense | matrix | RACI matrix | one A per row highlighted |
| 11 | dense | matrix | approval matrix | pending confirmation labels |
| 12 | anchor | exception | exception loop | pause and escalation are explicit |
| 13 | anchor | swimlane | swimlane | five lanes, decision, evidence chain |
| 14 | anchor | swimlane | change control | version and re-review loop |
| 15 | dense | decision | decision flow | capacity/resource decision |
| 16 | anchor | swimlane | segregation of duties | requester, buyer, receiver, payer separated |
| 17 | anchor | decision | quality exception | isolate before disposition; release authority pending if unconfirmed |
| 18 | anchor | loop | corrective loop | customer response and effectiveness check |
| 19 | dense | lifecycle | state lifecycle | resource status and history |
| 20 | dense | checklist | handoff checklist | completeness/acceptance gates |
| 21 | anchor | lifecycle | document lifecycle | obsolete version withdrawal |
| 22 | anchor | lifecycle | archive lifecycle | access, retention, disposal |
| 23 | dense | lifecycle | authorization lifecycle | competence before permission |
| 24 | anchor | process | access flow | approval and revocation |
| 25 | anchor | loop | meeting loop | action owner, due date, closure evidence |
| 26 | dense | dashboard | KPI cards | no invented numeric results |
| 27 | dense | risk | heatmap + path | risk level leads to escalation |
| 28 | anchor | loop | emergency loop | report, investigate, verify |
| 29 | anchor | loop | audit loop | process-based, not department-only |
| 30 | anchor | corrective | corrective loop | verification before closure |
| 31 | breathing | cycle | PDCA cycle | Act returns to Plan |
| 32 | dense | matrix | RACI example | example must be labelled example |
| 33 | anchor | pipeline | evidence chain | requirement-to-review chain |
| 34 | breathing | roadmap | timeline | three phases, deliverables and gate |
| 35 | dense | checklist | grouped checklist | all items labelled pending confirmation |
| 36 | breathing | document_map | document map |正文 vs SOP/表单/台账 separated |

## Mandatory executor behavior
- Read this file immediately before authoring every page.
- Author the final SVG one page at a time; do not use a loop or generator to emit final SVGs.
- If a page cannot satisfy its chart grammar, stop and mark it draft; do not substitute a generic card chain.
- Before export, review every page against the non-negotiable check column.
