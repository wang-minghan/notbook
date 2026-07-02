# Vault Scan Patterns

Quick-reference for scanning an Obsidian vault (or any markdown-based knowledge base) before executing a self-improvement cycle.

## Baseline Scan

```bash
# 1. Git status — are there uncommitted changes?
cd <vault_path>
git status

# 2. Recent commits — how active has the vault been?
git log --oneline -10

# 3. Top-level directory structure
ls -la <vault_path>/

# 4. Subdirectory contents for focus areas
ls -la <vault_path>/个人提升/
ls -la <vault_path>/工作/面试准备/
ls -la <vault_path>/原创小说/色情小说/<project>/.agent/status.md
```

## Key Status Files to Watch

| File | What it tells you |
|------|------------------|
| `项目/.agent/status.md` | Novel/writing project progress, current chapter, blocked tasks |
| `工作/面试准备/*.md` | Interview prep status, Q&A bank |
| `工作/工作经历/*.md` | Work history details for job applications |
| `个人信息/*.md` | User profile data |
| `个人提升/*.md` | Previously created plans and guides |

## Document Scanning

For `.docx` forms (应聘登记表, contracts, etc.):

```bash
python -c "
import zipfile, xml.etree.ElementTree as ET, re, sys

z = zipfile.ZipFile('path/to/form.docx')
xml = z.read('word/document.xml')
tree = ET.fromstring(xml)

texts = [t.text for t in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
full = ' '.join(texts)

# Find all text — useful for understanding structure
print(full)

# Search for pending markers
for marker in ['请填写', '请补充', '待填', '未填写', '____']:
    for m in re.finditer(marker, full):
        start = max(0, m.start()-40)
        end = min(len(full), m.end()+60)
        print(f'Marker \"{marker}\" at {m.start()}: ...{full[start:end]}...')
"
```

This approach works without python-docx (stdlib only) and is good for quick gap analysis.
