# DOCX Form Field Audit (Cron Context)

When running a self-improvement cycle and checking for pending documents (e.g. 应聘登记表, 入职登记表), you may need to audit a DOCX form for **missing or blank fields** without python-docx installed or when the terminal tool has output-capture issues with Python zipfile/stdlib.

## Detection

During vault or Desktop scan, look for files matching patterns:
- `*应聘登记表*.docx`
- `*入职登记表*.docx`
- `*面试登记表*.docx`
- `*王名涵*.docx` (filled version of a named template)

## Prerequisites

Two options, pick one:

**Option A (recommended): `python-docx` via system Python** — preserves table structure, merged cells, and cell layout. Install:
```bash
"/c/Users/32027/AppData/Local/Programs/Python/Python312/python" -m pip install python-docx
```
Then extract text with a script written via `write_file` and run via subprocess. This is the preferred approach for detailed form analysis.

**Option B (fallback): `pandoc`** — faster for a quick text dump but loses table structure (merged cells, column spans). Installed on this Windows host at `/c/Program Files/Pandoc/pandoc`. Falls back cleanly if absent.

> ⚠️ The Hermes venv Python (`~/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe`) has no pip and no python-docx on Windows. Always use the **system Python** path above.

## Workflow

### 1. Extract text from the DOCX

**Option A (recommended — preserves table structure):** Write a python-docx analysis script and run it via system Python:

```bash
# Write an analysis script
cat > /tmp/analyze_form.py << 'PYEOF'
import docx
doc = docx.Document(r"C:\Users\<user>\Desktop\<filename>.docx")
for ti, table in enumerate(doc.tables):
    for ri, row in enumerate(table.rows):
        for ci, cell in enumerate(row.cells):
            txt = cell.text.strip()
            if txt:
                print(f"[T{ti},R{ri},C{ci}] {txt[:120]}")
PYEOF

# Run via system Python (NOT Hermes venv Python!)
"/c/Users/<user>/AppData/Local/Programs/Python/Python312/python" /tmp/analyze_form.py
```

Key: each cell prints with its table/row/col coordinates, making blank fields obvious (they simply don't appear). This is how the detailed form audit in this session was done.

**Option B (fallback — fast text dump, loses table structure):**
```bash
pandoc "/c/Users/<user>/Desktop/<filename>.docx" -t plain --wrap=none
```

### 2. Identify blank sections

If using Option A (python-docx), blank sections show up as **tables or rows with no non-empty cells**. Use the coordinates to locate them:

| Section | Table index | What to look for |
|---------|-------------|------------------|
| 八、所获奖励荣誉 | Table 4 (typical) | Header row has content; data rows are completely empty |
| 十一、事业家庭三观 | Table 7 (typical) | 15 rows × 3 cols; columns 0-1 have labels, column 2 is all empty → 15 blank fields |
| 五、工作业绩 | Table 1 (typical) | Single-cell table with sparse text, no quantification |

If using Option B (pandoc), scan for:
- **Empty table cells** — consecutive `---` rows with blank content between them
- **Section headers with no content** — e.g. "八、近五年所获奖励" followed by blank table rows
- **Fields with nothing after the colon** — e.g. "对事业的态度 |" with empty space after pipe
- **Checkbox areas** — cluster of □ symbols where none are filled with ✓

### 3. Cross-reference with vault content

After identifying blank fields, check the vault for existing content to fill them:

| Blank section | Vault files to read |
|---------------|-------------------|
| Section 八 (奖励荣誉) | `个人信息/教育经历.md` — lists 数学建模省一等奖, 数据科学国家三等奖, ACM省二等奖, 奖学金×2 |
| Section 十一 (三观) | `个人提升/应聘登记表补全指南.md` — has draft text for each sub-field |
| Section 十 (职业规划) | `个人提升/高校教师岗面试准备路线图.md` — contains career plan template |

### 4. Generate a vault note with fillable content (when data exists but form is blank)

When vault content has the answers (like the draft text in `应聘登记表补全指南.md`) but the DOCX is still empty, **write a guidance note** to the vault with paste-ready content, cross-referenced to the exact section numbers.

### 5. Actually fill the DOCX (advanced — when python-docx is ready)

If you have python-docx installed on the system Python and the form structure is well-understood, write a fill script and invoke via subprocess:

```python
import subprocess

script = r'''
import docx
doc = docx.Document(r"C:\Users\<user>\Desktop\<template>.docx")

def set_cell(cell, text):
    cell.paragraphs[0].clear()
    cell.paragraphs[0].add_run(text)

# Fill Section 八: Table 4, Row 1 (first data row)
table = doc.tables[4]
set_cell(table.rows[1].cells[0], "全国数学建模竞赛")

doc.save(r"C:\Users\<user>\Desktop\<output>.docx")
print("Done")
'''

with open(r"C:\Users\<user>\Desktop\_temp_fill.py", 'w') as f:
    f.write(script)

result = subprocess.run([
    r"C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe",
    r"C:\Users\<user>\Desktop\_temp_fill.py"
], capture_output=True, text=True, timeout=30)
print(result.stdout)
```

> ⚠️ On Windows, the Hermes venv Python has no pip. Always target the **system Python** at `C:\Users\<user>\AppData\Local\Programs\Python\Python312\python.exe`.

```markdown
# 应聘登记表 — 待填字段内容草稿

---

## Section 八：近五年所获奖励

| 所获荣誉项目名称 | 类别和等级 | 授予单位 | 时间 | 排名 | 等级 |
|---|---|---|---|---|---|
| 全国数学建模竞赛 | 学科竞赛/省级 | 全国组委会 | 2024 | 1/3 | 一等奖 |
```

### 5. Git-stage the new file

```bash
cd <vault_dir> && git add -A
```

## When NOT to use this

- If the user has explicitly marked a field as "待面试后填写" or similar, skip it
- If the DOCX is password-protected or encrypted, pandoc will fail — report the blocker
- If the form was already fully filled and signed (no empty cells), skip the audit
- If pandoc is not installed, fall back to `python3 -c "import zipfile; ..."` to read the XML directly (less reliable on Windows terminal)

## See also

- `docx-templates` skill — for programmatic *filling* of DOCX forms (python-docx approach)
- `references/vault-scan-patterns.md` — Environment scan patterns for the vault
