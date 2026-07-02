---
title: Find Skill
name: find-skill
description: >
  Search, filter, and recommend Hermes skills by keyword, category, or task description.
  Use this whenever you need to find the right skill for a job, or when the user asks
  "is there a skill for X" / "哪个 skill 能做 Y".
---

## When to use

- User asks "有没有 find skill 的 skill" / "哪个 skill 能做 X"
- User asks for a capability and you need to check if a skill exists
- You want to discover related skills you didn't know about
- Before starting a complex task, check if relevant skills exist

## Workflow

### 1. List all skills

```tool
skills_list()
```

Returns all skills with `name` and `description`.

### 2. Search by keyword / category

Filter the result set mentally (or use `skills_list(category=...)`) to narrow:

**Categories available**: `autonomous-ai-agents`, `creative`, `data-science`, `email`, `github`, `media`, `mlops`, `note-taking`, `productivity`, `research`, `smart-home`, `software-development`

Use category filter when the domain is obvious:

```tool
skills_list(category="github")
```

### 3. Inspect matches

For any promising match, load the full content:

```tool
skill_view(name="<skill-name>")
```

### 4. Report to user

Present: skill name, description, key capabilities, load status.

If user wants to use it, load with `skill_view(name)`.

### 5. If nothing matches → offer to create

Tell the user no existing skill covers the need, and ask if they want to create one.
Use `skill_manage(action='create', name='<name>', content='...')`.

## Example flow

```
User: 有没有 pdf 相关的 skill？
Agent: 用了 find-skill 搜索 → 发现 nano-pdf skill → 加载给用户看
```

## Tips

- `skills_list()` output is already sorted by category → easy to scan
- Description field is the fastest signal — read it, don't load every skill
- Err on the side of listing the category; the user may spot something you miss
- When the user asks "有没有装 xxx 的 skill", run this skill's workflow first
