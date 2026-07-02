---
name: hermes-skills-management
description: "Manage Hermes skills directory structure — deduplicate, merge, clean up config, and maintain skills across installs and leftover directories."
---

# Hermes Skills Management

Managing where skills live, detecting duplicate/legacy skill directories, merging them safely, and cleaning up configuration references.

## When to Use

- The user asks why `skills_list` shows fewer skills than the files on disk
- You find skills in two places (e.g. `$HERMES_HOME/skills/` **and** `~/.hermes/skills/`)
- A user reports "too many" / "duplicate" skills after installing, migrating, or restoring a backup
- Config references a path that no longer exists or points to an external directory that overlaps with the main skills dir

## Key Concepts

### Where Skills Actually Live

Hermes uses `$HERMES_HOME/skills/` as the **single source of truth** for installed skills:

| Path | What it is |
|------|------------|
| `$HERMES_HOME/skills/` | **Official skills directory** — all builtin, hub, and local skills coexist here |
| `~/.hermes/skills/` | NOT used by default — it's a **legacy or leftover directory** from a different installation or manual copy |
| `skills.external_dirs` (config) | An **opt-in** list of extra directories to scan; each must be a valid path |

### How to Check Where Skills Are

```bash
echo "$HERMES_HOME"                         # e.g. C:\Users\<user>\AppData\Local\hermes
hermes config path                          # config.yaml location
hermes config set skills.external_dirs []   # read current external dirs
```

Scan each candidate directory:

```python
from agent.skill_utils import iter_skill_index_files, get_all_skills_dirs
for d in get_all_skills_dirs():
    count = sum(1 for _ in iter_skill_index_files(d, "SKILL.md"))
    print(f"{d}: {count} skills")
```

### The Two-Directory Problem

This happens when:
- A previous Hermes installation used `~/.hermes/skills/` before the `$HERMES_HOME` convention changed
- A user manually copied skills to `~/.hermes/skills/` as a backup or migration artifact
- A profile's skills directory survived after the main install moved

**Result:** `skills_list` shows fewer entries than `find . -name "SKILL.md" | wc -l` on `~/.hermes/skills/` — because Hermes is looking at `$HERMES_HOME/skills/`, not the legacy path.

## Workflow: Consolidate Duplicate Skills Directories

### 0. Prerequisites

Ensure you have a working Hermes CLI:

```bash
hermes --version
hermes skills list
```

### 1. Count Skills in Each Directory

```bash
# Official dir
find "$HERMES_HOME/skills" -name "SKILL.md" | wc -l

# Legacy dir
find ~/.hermes/skills -name "SKILL.md" | wc -l 2>/dev/null || echo "does not exist"
```

### 2. Check for Name Collisions

Use Python to scan both directories and compare names:

```python
def collect_skill_names(base_dir):
    """Return {skill_name: (category, relative_path)} for all SKILL.md files."""
    result = {}
    for sk in base_dir.rglob("SKILL.md"):
        # Parse frontmatter for the 'name:' field
        content = sk.read_text(encoding="utf-8")
        if content.startswith("---"):
            end = content.find("---", 3)
            if end > 0:
                for line in content[3:end].splitlines():
                    if line.startswith("name:"):
                        name = line.split(":", 1)[1].strip().strip("\"'")
                        result[name] = sk
    return result

official = collect_skill_names(Path($HERMES_HOME/skills))
legacy = collect_skill_names(Path("~/.hermes/skills").expanduser())
overlap = set(official) & set(legacy)
print(f"Overlap: {len(overlap)}")  # Should be 0 for a clean merge
```

**Note:** `iter_skill_index_files` from `agent.skill_utils` respects platform filtering and disabled-list checking — use it for a semantic scan. Raw `rglob` is faster for counting but may count platform-incompatible skills.

### 3. Merge

With zero collisions, simply copy:

```bash
cp -rv ~/.hermes/skills/* "$HERMES_HOME/skills/"
```

If collisions exist:
- **Same name, same content** → skip (deduplicate)
- **Same name, different content** → pick a winner or rename one; never overwrite blindly

### 4. Clean Up Config

Remove any `external_dirs` entry pointing to the legacy path:

```bash
hermes config set skills.external_dirs []
```

⚠️ **Pitfall:** `hermes config set` serializes list values **as a YAML string**, not a YAML list. If you pass `'["path"]'`, it stores the literal string `'["path"]'`, which Hermes' YAML parser will treat as a string (not a list), and `external_dirs` resolution will silently return zero directories.

**Watch for this output:**
```yaml
# WRONG — stored as string
external_dirs: '["C:\\Users\\user\\.hermes\\skills"]'

# CORRECT — stored as YAML list
external_dirs:
  - C:\Users\user\.hermes\skills
```

**Fix:** use `hermes config edit` to open the file in an editor, or replace the line via Python/patch tool:

```python
old = """  external_dirs: '["C:\\\\path\\\\to\\\\skills"]'"""
new = """  external_dirs: []"""
# Replace in config.yaml
```

### 5. Remove Legacy Directory

```bash
rm -rf ~/.hermes  # only if profiles/ there is known unused
```

Check before deleting: `ls -la ~/.hermes/profiles/` — if it contains profiles you still use, keep them or migrate them.

### 6. Verify

```bash
hermes skills list
# Expected: 0 hub-installed, N builtin, M local — X enabled, 0 disabled
```

The total should match the sum of unique skills across both directories (minus any collisions). Count displayed rows (the list footer shows the exact total).

Also verify `config.yaml` no longer references the old path:

```bash
grep external_dirs "$(hermes config path)"
# Should show empty list, never a string path
```

## Workflow: Supplement URL-Installed Skills With Supporting Files

When you install a skill from a direct GitHub URL (`hermes skills install https://raw.githubusercontent.com/.../SKILL.md --name <name> --yes`), **only the SKILL.md is downloaded**. If the GitHub repo has a `references/`, `templates/`, or `scripts/` directory, those files are **not included** — you must fetch them manually.

### Detection

After installing, check whether supporting files are missing:

```bash
# Has the skill been installed?
ls "$HERMES_HOME/skills/<name>/"

# Check the GitHub repo for a references/ directory
curl -sL "https://api.github.com/repos/<owner>/<repo>/contents/references" \
  | python -c "import sys,json; data=json.load(sys.stdin); \
  [print(f['name']) for f in (data if isinstance(data,list) else [])]" \
  2>/dev/null || echo "No references/ directory on the repo"
```

A JSON list response means files exist; an `"error"` response with `"Not Found"` means there are none.

### Fetch

For each file in the repo's `references/` (or `templates/`, `scripts/`) directory:

```bash
SKILL_DIR="$HERMES_HOME/skills/<name>"
mkdir -p "$SKILL_DIR/references"

curl -sL "https://raw.githubusercontent.com/<owner>/<repo>/main/references/<file>.md" \
  -o "$SKILL_DIR/references/<file>.md"
```

### Verify

```bash
ls -la "$HERMES_HOME/skills/<name>/references/"
# Expected: each file matches the repo listing
```

After adding files, `skill_view(name)` will show the new files in `linked_files`.

## Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| `config set` stores list as YAML string | `external_dirs: '[...]'` instead of `external_dirs:\n  - ...` | Manually edit config.yaml |
| Legacy dir has skill names that collide with builtins | `hermes skills list` shows fewer than expected after merge | Check overlap before merge |
| `~/.hermes/` contains active profiles (`profiles/<name>/`) | Deleting it removes those profiles' sessions/config | Move or merge profiles first |
| Platform-incompatible skills in legacy dir (e.g. `apple/*` skills on Windows) | They exist on disk but don't show in `skills_list` | That's correct behaviour — skip them |

## Verification

After consolidation, confirm:

```bash
hermes skills list               # shows expected count
hermes skills list --source local | head -10  # shows imported skills from each category
find "$HERMES_HOME/skills" -maxdepth 2 -name "SKILL.md" | wc -l  # matches total
```

Session-independent health check:

```bash
hermes doctor
```
