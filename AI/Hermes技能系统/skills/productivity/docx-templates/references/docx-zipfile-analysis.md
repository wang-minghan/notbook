# DOCX Gap Analysis via Zipfile (stdlib)

When `python-docx` is not installed or you just need a quick text dump to find empty/missing fields in a Word form, use Python stdlib `zipfile` + `xml.etree.ElementTree`.

## Quick Text Dump

```python
import zipfile, xml.etree.ElementTree as ET

z = zipfile.ZipFile(r'C:\path\to\document.docx')
xml = z.read('word/document.xml')
tree = ET.fromstring(xml)

texts = [t.text for t in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
full_text = ' '.join(texts)
print(full_text)
```

## Find Pending Fields

Search for markers commonly found in Chinese HR/government forms:

```python
import re

pending_markers = ['请填写', '请补充', '待填', '未填写', '____', '______']
for marker in pending_markers:
    for m in re.finditer(marker, full_text):
        start = max(0, m.start() - 40)
        end = min(len(full_text), m.end() + 60)
        ctx = full_text[start:end]
        print(f'Found \"{marker}\" at pos {m.start()}:')
        print(f'  ...{ctx}...')
```

## When to Use This vs. python-docx

| Approach | Best for |
|----------|----------|
| **zipfile + ElementTree** | Quick gap analysis, finding empty fields, extracting all text. No pip install needed. |
| **python-docx** | Actually filling fields, table navigation, merged-cell handling, saving modified documents. |

Use both in sequence: zipfile to discover what's missing, then python-docx to fill it.
