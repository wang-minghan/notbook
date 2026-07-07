---
name: ppt-visual-system
description: "Use when a PPT task needs visual quality, cover images, layout polish, image generation, or style consistency across slides. For real deck production, route through ppt-master first and use this skill as a supplemental visual orchestration layer."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ppt, powerpoint, visual-design, image-generation, comfyui, prompt-engineering, layout, aesthetics]
    related_skills: [powerpoint, comfyui, design-image-prompt-engineer, design-ui-designer, design-visual-storyteller, presentation-script-writing]
---

# PPT Visual System

## Overview

This skill is the **visual orchestration layer** for PPT work. It does not replace `ppt-master`; it sits above or beside it.

Use this skill when the user is not merely asking to edit a `.pptx`, but is implicitly asking for a **better-looking presentation**: stronger cover slides, higher-quality images, better style consistency, more intentional layout, or a more premium feel.

The core idea is simple:

- `ppt-master` owns the primary deck-generation workflow and real PPT production.
- `powerpoint` handles compatibility / mechanical `.pptx` operations when needed.
- `ppt-visual-system` decides which additional design or image skills should be brought in so PPT work does not become a plain text-and-bullets task.

## When to Use

Use this skill when any of the following are true:

- The user wants to make a PPT look better, more polished, more premium, or more professional.
- The task involves cover slides, section openers, visual assets, illustrations, or diagrams.
- The task involves generating or improving images before placing them into slides.
- The user is combining PPT production with ComfyUI, prompt engineering, design, or visual QA.
- The user asks for "高级感", "审美", "封面", "主视觉", "版面优化", or style consistency.

Do **not** use this skill when:

- The task is only to read a `.pptx`, extract text, or make a tiny text fix.
- The user only needs mechanical PPT editing with no visual/design component.
- The task is purely about one standalone image and does not involve presentation usage.

## Skill Coupling Rules

This skill exists to prevent `powerpoint` from working in isolation.

### Base skill

Always treat `ppt-master` as the base execution workflow when the deliverable is a real `.pptx` deck. Use `powerpoint` only as a secondary compatibility/mechanical skill when small `.pptx` inspection or edits are needed outside the main PPT Master flow.

### Bring in additional skills based on task shape

#### 1. Visual or cover-heavy PPT
Load or consult:
- `design-image-prompt-engineer`
- `comfyui`
- `design-ui-designer`

Use this path when the user wants:
- a cover image
- a hero visual
- section header images
- stronger aesthetics
- image-led slides

#### 2. Narrative / communication-heavy PPT
Load or consult:
- `presentation-script-writing`
- `design-visual-storyteller`
- `powerpoint`

Use this path when the user wants:
- better story flow
- clearer message hierarchy
- more persuasive presentation structure
- stronger opening / closing slides

#### 3. Mixed visual + content PPT
Use both branches:
- `powerpoint`
- `design-image-prompt-engineer`
- `comfyui`
- `presentation-script-writing`

This is the default for high-stakes decks where both content and aesthetics matter.

## Operating Workflow

### Step 1: Classify the PPT task

Before making slides, classify the request into one of four modes:

1. **Structure-first** — mostly text/content editing
2. **Visual-first** — cover images, hero slides, style quality
3. **Mixed deck** — both content and visual polish matter
4. **Asset-first** — generate visuals first, then place into PPT

Completion criterion:
- You can state which mode the task belongs to and why.

### Step 2: Decide whether images are required

Do not assume every PPT needs generated images. Decide intentionally.

Use generated images when they improve:
- cover slide impact
- section transitions
- concept explanation
- style consistency
- visual hierarchy

Do not force generated images when:
- charts/tables are the main content
- the deck is internal and speed matters more than visual polish
- a clean text-led layout is more appropriate

Completion criterion:
- You have explicitly decided whether the deck needs generated visuals, diagrams, or neither.

### Step 3: Classify the visual asset type before prompting

If visuals are needed, do **not** jump straight to one generic prompt style. First classify the asset into one of these four types:

1. **Cover hero visual**
   - strongest atmosphere and opening impact
   - supports title overlay
   - allowed to be the most stylistically expressive

2. **Section opener visual**
   - transitional visual between sections
   - should feel branded and consistent, but lighter than a cover
   - should not look like a standalone poster

3. **Content-slide illustration**
   - supports a specific concept or message on a content page
   - should have one clear focal idea
   - must coexist well with headings, bullets, charts, or paragraphs

4. **Background / atmosphere asset**
   - primarily supports layout and tone
   - should stay quiet, crop-tolerant, and text-friendly
   - should not dominate the slide

Important nuance:
- A PPT visual asset may still use **poster-like composition rhythm** or **cinematic atmosphere**.
- What must be avoided is not all poster influence, but **baked-in text content**: titles, subtitles, credits, slogans, or promotional typography.
- In other words: poster-grade mood is allowed; poster-grade lettering is not.

Asset-specific guidance:

- **Cover hero visual** → prioritize mood, title-safe space, bold material quality, strong composition.
- **Section opener visual** → prioritize transition, consistency, moderate emphasis, clean rhythm.
- **Content-slide illustration** → prioritize concept clarity, single focal subject, lower noise, less poster feel.
- **Background / atmosphere asset** → prioritize simplicity, soft texture, crop tolerance, low distraction.

Completion criterion:
- You can name the exact visual asset type and explain why it fits the slide's role.

### Step 4: If visuals are needed, enhance prompts before generation

Never jump straight from "make PPT" to image generation.

If a slide needs a visual asset:
1. Consult `design-image-prompt-engineer` for prompt quality.
2. Define visual purpose: cover, section divider, concept image, diagram, icon set, etc.
3. Define slide constraints: title overlay area, negative space, 16:9 usage, style consistency.
4. Only then use `comfyui` or another image workflow.

Completion criterion:
- The image prompt includes slide-specific constraints, not just subject matter.

### Step 5: Keep PPT placement logic separate from image generation logic

Generated images should be treated as **presentation assets**, not final slides.

`powerpoint` should handle:
- slide composition
- spacing
- typography
- placement
- final visual QA

`comfyui` should handle:
- image asset generation
- refinement / upscale
- style-controlled visual production

Completion criterion:
- The workflow clearly separates asset creation from slide assembly.

### Step 6: Run visual QA from a presentation perspective

A beautiful image can still be bad for slides.

Check:
- Is there space for titles?
- Is the image too busy for PPT usage?
- Is the contrast good enough for overlay text?
- Does the image style match the rest of the deck?
- Does the deck feel coherent rather than randomly decorated?

Completion criterion:
- You have judged the image as a slide asset, not just as a standalone picture.

## Design Heuristics

### What to optimize for

When doing visual PPT work, prioritize:

1. **Readability over decoration**
2. **Consistency over novelty**
3. **Slide purpose over raw image beauty**
4. **Negative space over clutter**
5. **System-level polish over one "hero" slide**

### Common failure modes

- Calling only `powerpoint` and forgetting prompt/image/design support skills
- Using one generic 'cover-style' prompt for all asset types
- Making visually impressive images that leave no room for titles
- Letting every slide use a different visual language
- Treating ComfyUI output as final without slide-specific QA
- Over-focusing on images while neglecting message hierarchy
- Generating poster-like art when the slide actually needs a quiet content illustration or background asset

## Recommended Combinations

### Combination A — Cover upgrade
Use:
- `ppt-master`
- `design-image-prompt-engineer`
- `comfyui`

For:
- title slide
- keynote opener
- chapter/section cover

### Combination B — Premium full-deck polish
Use:
- `ppt-master`
- `design-ui-designer`
- `design-visual-storyteller`
- `design-image-prompt-engineer`
- `comfyui`

For:
- important client decks
- external presentations
- product/strategy decks

### Combination C — Content-first but not ugly
Use:
- `presentation-script-writing`
- `ppt-master`
- optionally `design-ui-designer`

For:
- decks where structure and explanation matter more than image generation

## Common Pitfalls

1. **Treating `.pptx` handling as the entire task**
   A PPT deliverable often includes visual reasoning beyond file editing.

2. **Generating images too early**
   If the slide role is unclear, image quality will not save the deck.

3. **Ignoring coupling opportunities**
   When a user asks for a better-looking PPT, defaulting to `powerpoint` alone is usually too weak.

4. **Using image skills without PPT constraints**
   Presentation visuals need negative space, composition discipline, and text-overlay awareness.

5. **Optimizing single slides instead of deck coherence**
   The deck must feel like one system.

## Verification Checklist

- [ ] I identified whether the task is structure-first, visual-first, mixed, or asset-first.
- [ ] I used `ppt-master` as the base workflow for real deck execution.
- [ ] I used `powerpoint` only when compatibility or small mechanical `.pptx` work was actually needed.
- [ ] If visuals mattered, I considered `design-image-prompt-engineer` before image generation.
- [ ] If visuals were generated, I treated them as slide assets rather than final slides.
- [ ] I checked title space, contrast, clutter, and style consistency.
- [ ] I did not let `powerpoint` work in isolation on a visual-heavy task.
