# Step 2: Draft

## Purpose

Expand the approved wireframe into a complete SVG.

## Input

`1-wireframe/results.md`; the chosen archetype file; all of `design/`.

## Output

- `runs/{date}-{slug}/2-draft/draft.svg`

## How to execute

1. Read the chosen archetype's Skeleton and Composition rules, and all
   four design files (`palette`, `typography`, `layout`, `icons`).
2. Start from the skeleton. Map every wireframe element to skeleton
   geometry: panels, chips, arrows, strip entries. Apply the composition
   rules for pitch and sizing.
3. Apply the design system without deviation: palette assignment rules
   (one accent per zone, reserved hue on the claim carrier), the type
   scale, arrow conventions, and only the icon defs actually used.
4. Write the `aria-label` and the subtitle as the claim sentence from
   intake.
5. Self-check against the source text: every label in the SVG must be
   true to the text; no invented numbers or names.
6. Save to `runs/{date}-{slug}/2-draft/draft.svg`. DRAFTING status line;
   do not present the draft yet, review comes first.
7. Set the run index status line to `draft written`.

## Done when

`draft.svg` exists and applies the wireframe and the design system.
