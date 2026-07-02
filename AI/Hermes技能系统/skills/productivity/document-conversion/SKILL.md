---
name: document-conversion
title: Document Format Conversion (EPUB/PDF/HTML/DOCX)
description: Convert between document formats on Windows — EPUB to PDF, EPUB to DOCX, HTML to PDF, and related conversions. Covers the Pandoc + Edge headless pipeline and alternative approaches with Chinese font support.
category: productivity
---

# Document Format Conversion (Windows)

Convert documents between EPUB, PDF, HTML, DOCX, and other common formats, focusing on reliable Windows-native approaches with Chinese font support.

## Tools Available

| Tool | Path | Purpose |
|------|------|---------|
| **Pandoc** | `C:\Program Files\Pandoc\pandoc.exe` | Universal doc converter (EPUB→HTML/MD/DOCX) |
| **Edge (headless)** | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` | HTML→PDF (best Chinese font support) |
| **Python fpdf2** | `pip install fpdf2` | Programmatic PDF creation with custom fonts |
| **Windows Fonts** | `C:\Windows\Fonts\msyh.ttc` (YaHei) | Chinese font for PDF embedding |

## EPUB → PDF (Recommended Workflow)

This is the most reliable path on a standard Windows system without LaTeX.

### Step 1: EPUB → HTML
```bash
"/c/Program Files/Pandoc/pandoc.exe" "input.epub" -t html5 -o "output.html"
```

### Step 2: HTML → PDF via Edge Headless
```bash
"/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
  --headless --disable-gpu \
  --print-to-pdf="output.pdf" \
  "file:///C:/absolute/path/to/output.html"
```

**Result:** Chinese characters render correctly because Edge includes native font rendering. Works without installing any TeX distribution.

### Verify
```bash
ls -la "output.pdf"
# Should be a valid PDF, e.g. 4MB for a full-length book
```

## EPUB → DOCX

```bash
"/c/Program Files/Pandoc/pandoc.exe" "input.epub" -o "output.docx"
```

## EPUB → Markdown (for further processing)

```bash
"/c/Program Files/Pandoc/pandoc.exe" "input.epub" -t markdown -o "output.md"
```

Use this if you need to edit the content before generating PDF, or if you need a plain-text reference.

## HTML → PDF via Python (fpdf2)

For cases where you need more control (custom headers, TOC, formatting):

1. Convert EPUB → Markdown (above)
2. Use fpdf2 with embedded Chinese fonts to build the PDF programmatically
3. Register fonts from `C:\Windows\Fonts\` (e.g. `msyh.ttc` for YaHei)

## Pitfalls

- **pdflatex is NOT available on standard Windows** — requires MiKTeX/TeX Live install. Pandoc's `--pdf-engine=pdflatex` will fail with "pdflatex not found".
- **xhtml2pdf** often fails with exit code 49 on MSYS/Git-Bash (subprocess spawning issue). Avoid it on this shell.
- **Edge headless requires `file:///` prefix** for local HTML files — absolute Windows path like `file:///C:/path/to/file.html`.
- **MSYS path quirks:** Use forward slashes in paths passed to Edge. The binary path itself needs quotes when it has spaces.
- **fpdf2 must register fonts explicitly** — `add_font("yahei", "", "C:/Windows/Fonts/msyh.ttc", uni=True)`.
- **Large EPUBs** (>2000 pages) may cause Edge headless to run slowly or OOM. Consider splitting the HTML first.

## Detection Commands

Check what's available:
```bash
# Check Pandoc
ls "/c/Program Files/Pandoc/pandoc.exe"
# Check Edge
ls "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# Check available Chinese fonts
ls "/c/Windows/Fonts/" | grep -i -E "msyh|simhei|simsun|simkai"
# Check Python packages
pip list 2>/dev/null | grep -i -E "fpdf|reportlab|weasyprint|xhtml2pdf"
```
