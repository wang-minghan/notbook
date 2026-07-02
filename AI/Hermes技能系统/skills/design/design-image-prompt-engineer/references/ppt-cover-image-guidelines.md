# PPT Cover Image Guidelines

Use this reference when generating images meant to sit behind PowerPoint title text.

## Goal

A PPT cover image is not a generic "pretty image" and not a poster. It must support typography and message hierarchy.

## Priority criteria

1. **Title-safe negative space**
   - Reserve a large clean area for title + subtitle.
   - Prefer one side (often left) to stay visually quieter.
2. **Single dominant focal region**
   - Put visual energy on the opposite side from the text block.
   - Avoid multiple competing focal points.
3. **Low clutter in text area**
   - Avoid dense particles, objects, faces, or bright highlights where text will sit.
4. **Business / deck appropriateness**
   - Should feel like a premium presentation background, not a random wallpaper, movie poster, or flashy concept art.
5. **No text artifacts**
   - Explicitly suppress letters, pseudo-text, logos, watermarks, UI fragments, and signage unless the slide truly needs them.

## Prompt pattern

Structure prompts around:
- subject/theme
- composition
- text-safe region
- visual weight placement
- tone/style
- artifact suppression

Example pattern:

`professional presentation cover background, [theme], clean negative space on the left for title and subtitle, visual focus on the right, premium corporate aesthetic, layered depth, elegant lighting, minimal clutter in title area, no text, no letters, no watermark, no logo`

## Negative prompt ideas

Use when supported:
- `text, letters, words, watermark, logo`
- `busy composition, cluttered center, multiple focal points`
- `poster layout, crowded foreground`
- `anime, cartoon` (when business/corporate style is desired)

## Workflow guidance

- Generate several candidates first; do not trust a single sample.
- Judge images by **cover usability**, not just beauty.
- If the image looks like a wallpaper but not a slide cover, reject it.
- If the model keeps producing pseudo-text, strengthen the no-text instructions and reduce scene complexity.

## Review rubric

When reviewing candidates, rank them by:
1. text placement safety
2. business/premium feel
3. message clarity
4. absence of pseudo-text and visual noise
