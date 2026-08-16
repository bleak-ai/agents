# Step 3: Review

## Purpose

Catch geometry mistakes before the user sees the draft, then run the
feedback loop. Rendering is an aid, never a required step.

## Input

`2-draft/draft.svg`; `scripts/render.py`.

## Output

- `runs/{date}-{slug}/3-review/` with `draft.png` (when rendering
  worked) and `notes.md` (self-review findings and user feedback).

## How to execute

1. RENDERING status line. Run `scripts/render.py` with `run_script`,
   arguments: the draft path and the output path
   `runs/{date}-{slug}/3-review/draft.png`.
2. If the script reports NO_BROWSER or fails, note `render skipped` in
   `notes.md` and continue; per `style.md` this is never a blocker.
3. If a PNG was produced, look at it and self-check:
   - No overlapping text or elements; nothing clipped by the viewBox.
   - Labels fit their containers; nothing wraps or truncates.
   - The claim carrier is the most prominent colored element.
   - Zone accents follow the palette assignment rules.
   Fix findings in the SVG and re-render once. Record findings in
   `notes.md`.
4. Present the result to the user: the SVG path (and PNG path when it
   exists), with the claim sentence. This is the proposal prose allowed
   by `style.md`.
5. Feedback loop:
   - Style remarks: apply the fix directly to the SVG. If the same
     style correction happens a second time (this run or recorded in
     `design/` history), propose the design-system edit per `style.md`.
   - Composition changes (add, remove, reorder, reconnect): redraw the
     one-line wireframe delta and confirm through the question tool
     before editing the SVG.
   - After each edit, re-render best effort and show the updated path.
6. Loop until the user approves the diagram through the question tool
   (approve / more changes).

## Done when

The user has approved the diagram.
