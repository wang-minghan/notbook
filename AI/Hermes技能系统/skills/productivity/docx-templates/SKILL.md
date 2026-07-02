---
name: docx-templates
description: Fill, enhance, and automate Word (.docx) template documents on Windows. Analyze merged-cell layouts, fill government/HR forms, generate filled copies from user data.
platforms: [windows]
tags: [docx, python-docx, form-filling, office, templates]
---

# DOCX Template Filling

Fill structured Word (.docx) template documents programmatically using python-docx. Especially suited for Chinese government/HR registration forms with complex merged-cell layouts.

## Prerequisites

```bash
# On Windows: install to system Python, NOT Hermes venv Python
"/c/Users/<user>/AppData/Local/Programs/Python/Python312/python" -m pip install python-docx
```

> ⚠️ **Windows only**: The Hermes-installed venv Python has no pip (stripped for install size). Always target the **system Python** at `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe`. On this host the system Python is `C:\Users\32027\AppData\Local\Programs\Python\Python312\python.exe`.

On Windows, the reliable execution path: write a `.py` script to disk with `write_file`, then invoke via `terminal` → `subprocess.run` targeting system Python (see Step 4 below).

## Workflow

### 1. Analyze the template structure

Create an analysis script to discover tables, merged-cell regions, and empty input cells.

```python
import docx

doc = docx.Document(r'C:\path\to\template.docx')

# Key structural checks
print(f"Tables: {len(doc.tables)}")
print(f"Paragraphs: {len(doc.paragraphs)}")

# For each table, show row/column structure and non-empty cell content
for i, table in enumerate(doc.tables):
    print(f"\nTable {i}: {len(table.rows)} rows x {len(table.columns)} cols")
    for ri, row in enumerate(table.rows):
        for ci, cell in enumerate(row.cells):
            txt = cell.text.strip()
            if txt:
                print(f"  [{ri},{ci}] {txt[:80]}")
```

**Critical: merged cells.** When cells are merged in the docx, `row.cells[0]` and `row.cells[1]` may share the SAME XML element (`_tc`). Writing to one overwrites both. Detect this:

```python
# Check if cells are the same XML element
print(f"Cell[0] id: {id(row.cells[0]._tc)}")
print(f"Cell[1] id: {id(row.cells[1]._tc)}")
# Same id → merged; only write to one
```

### 2. Identify input cells vs. label cells

In template forms, some cells contain the field **label** (e.g. "姓名", "性别") while adjacent cells are **input** areas. Determine which column indices are the empty input cells:

```python
row = table.rows[1]
for ci in range(len(row.cells)):
    print(f"  [{ci}] txt='{row.cells[ci].text[:30]}' paras={[p.text.strip() for p in row.cells[ci].paragraphs]}")
```

Pattern: consecutive empty cells after a label cell cluster are the input region. For a form with 25 columns and labels in `[0-1]`, the input area starts at `[2]`.

### 3. Write a fill script

Create a standalone Python script that:
- Opens the template with python-docx
- Fills known cells using a helper function
- Marks unknown fields with `【待补充】` markers
- Saves to a new file (don't overwrite the template)

```python
import docx

SRC = r'C:\path\to\template.docx'
DST = r'C:\path\to\filled-output.docx'

doc = docx.Document(SRC)

def set_cell_text(cell, text):
    """Clear the cell's first paragraph and set its text."""
    cell.paragraphs[0].clear()
    cell.paragraphs[0].add_run(text)

# Fill cells by row/column index
table = doc.tables[0]
set_cell_text(table.rows[1].cells[2], "张三")      # 姓名 (first input after label)
set_cell_text(table.rows[1].cells[8], "男")         # 性别

# Save COPY — never modify the original template
doc.save(DST)
```

### 4. Execute via subprocess (preferred on Windows)

The Hermes `terminal` tool can have issues with python-docx output. Use `execute_code` with subprocess:

```python
import subprocess

script = r'''
import docx
doc = docx.Document(r'C:\path\to\template.docx')
# ... fill logic ...
doc.save(r'C:\path\to\filled-output.docx')
print("Done")
'''

script_path = r'C:\path\to\_temp_fill.py'
with open(script_path, 'w') as f:
    f.write(script)

result = subprocess.run(
    [r'C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe', script_path],
    capture_output=True, text=True, timeout=30
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr[:500])
```

### 5. Verify the output

Rerun the analysis script against the output document to confirm:
- All intended cells have the expected text
- Merged cells show the content only once
- Section headers are preserved
- The signature/declaration area is intact

## Chinese Government/HR Form Special Patterns

These forms (应聘登记表, 入职登记表, 面试登记表, etc.) share common structures:

### Common sections
| Section | Typical content |
|---------|----------------|
| Header row | 应聘部门, 应聘岗位, 预计到岗时间, 面试时间 |
| 一、基本信息 | 姓名, 性别, 出生年月, 籍贯, 民族, 政治面貌, 身高, 婚姻, 身份证, 住址, 电话, 邮箱 |
| 二、教育背景 | Table: 起止年月, 学校名称, 专业, 学历, 学位, 证明人, 电话 |
| 三、工作经历 | Table: 起止年月, 单位名称, 岗位, 月收入, 证明人, 电话, 离职原因 |
| 四、家庭主要成员 | Table: 父亲/母亲/配偶/子女 rows |
| 五-九 | 业绩, 教学, 科研, 奖励, 社会服务 (often blank for new grads) |
| 十、职业规划 | Short/mid/long-term plans |
| 十一 | 对事业/家庭/人际/生活的看法 |
| 十二 | 岗位认识与工作思路 |
| 十四、其他资料 | 犯罪/违纪/病史 checkboxes |

### Merged cell navigation (25-column grid)
Many Chinese forms use a **25-column grid** with `gridSpan` for labels. Common column positions:

| Label region | Input region | Content |
|-------------|-------------|---------|
| [0-1] | [2-4] | 姓名 |
| [5-7] | [8-12] | 性别 |
| [13-16] | [17-23] | 出生年月 |
| [24] | — | 一寸照片 (photo area) |
| Row 8: | [2-6] 户口性质, [8-23] 联系方式 |
| Row 11: | Education header row (起止年月[0-2], 学校名称[3-8], 专业[9-11], 学历[12-15], 学位[16-19], 证明人[20-22], 电话[23-24]) |

### Checkboxes
Chinese forms use □ for unfilled, [✓] or [[☑]] for filled. Fill the blank checkbox with the chosen option:

```python
# Option A: replace the □ before the intended choice
cell_text = cell_text.replace("□城镇", "【✓】城镇")
# Option B: find the "□有    □无" pattern and mark the correct one
cell_text = cell_text.replace("□有", "□有").replace("□无", "【✓】无")
```

### 职业规划 (Career planning) text
For teaching positions at Chinese universities/colleges, use a 3-stage template:
- **短期 (1年)**: 融入团队, 工程经验→教学能力转化, 适应高校教师角色
- **中期 (3-5年)**: 在大模型/知识图谱/AI Agent方向深耕, 争取科研项目, 发表论文, 指导学生竞赛
- **长期 (5-10年)**: 成长为核心骨干, 形成特色研究方向, 推动产学研合作

## Getting data from the user's vault

For forms that require personal info, cross-reference the user's Obsidian vault notes:

| Vault file | Data available |
|-----------|---------------|
| `个人信息/教育经历.md` | 教育背景 (本科/硕士学校, 专业, 时间), 竞赛获奖 |
| `个人信息/资格证书与技能.md` | 证书 (TOPIK, IELTS, 计算机), 技能栈 |
| `工作/工作经历/北京灵易数智-工作经历.md` | 第一份工作详情 |
| `工作/工作经历/亚信科技-工作经历.md` | 第二份工作详情 |
| `工作/面试准备/面试提问内容整理.md` | 职业经历总结, 项目描述 |

Use `read_file` to extract specific fields, then fill programmatically.

## Pitfalls

- **Merged cells**: Writing to one merged cell writes to ALL visually separate cells that share the same `_tc` element. Always check `id(cell._tc)` before assuming cells are independent.
- **`clear()` semantics**: `cell.paragraphs[0].clear()` removes all runs but leaves the paragraph. Adding a run after clear works. Do NOT delete the paragraph.
- **Overwriting template**: Always save to a NEW file path. The template is the source of truth for table structure.
- **Encoding**: python-docx handles Unicode natively, so Chinese text works fine when passed as Python str.
- **table.rows vs merged vertical cells**: Vertically merged rows have fewer actual cells (the merged region counts as one). `len(row.cells)` may vary between rows.
- **Unknown fields**: Always mark with a visible placeholder like `【请填写姓名】` so the user knows exactly what's missing. Never leave a field blank without a marker — blank cells can be mistaken for logical omissions.
- **Checkbox positioning**: Chinese forms often place checkboxes as plain text within a cell, not as form controls. String replacement on `cell.text` works, but you must modify the *inner text*, not just the Python string. Use set_cell_text after replacement.
- **Windows: Hermes venv Python has no pip**: On Windows, the Hermes-installed venv at `~/AppData/Local/hermes/hermes-agent/venv/Scripts/` is stripped for install size — no pip, no pytest. Running `pip install python-docx` inside the Hermes venv will fail with `No module named pip`. **Fix**: use the system Python directly. On this host: `/c/Users/32027/AppData/Local/Programs/Python/Python312/python.exe`. Install python-docx there first:
  ```bash
  "/c/Users/32027/AppData/Local/Programs/Python/Python312/python" -m pip install python-docx
  ```
  Then run your script via subprocess, not from the Hermes venv. The skill's subprocess.run example already handles this — just change the `python.exe` path to the system one.
- **`execute_code` may fail on Windows**: The skill recommends `execute_code` with subprocess, but `execute_code` also runs inside the Hermes venv (no python-docx). On Windows, write a `.py` file to disk with `write_file`, then invoke the system Python via `terminal` → `subprocess.run`. This is the reliable Windows workflow.

## Reference Files

- `references/docx-zipfile-analysis.md` — Quick docx text extraction and gap analysis using stdlib zipfile (no python-docx needed)

## Related skills

- `obsidian` — references/obsidian-local-rest-api.md (extract personal data from vault)
- `powerpoint` — .pptx presentations (different format, similar philosophy)
- `nano-pdf` — PDF text editing (complementary, not overlapping)
- `periodic-self-improvement` — Cron-based self-improvement cycle that may involve form analysis
