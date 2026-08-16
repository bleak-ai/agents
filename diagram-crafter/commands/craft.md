---
description: Create an explanatory SVG diagram from a text.
parameters:
  - name: task
    description: The initial text (or a path to it) and who the diagram is for
    required: true
---

# Craft

Create a diagram for `$task`. Follow `style.md` for every message.

1. Run the full flow in `steps/`: 0 intake, 1 wireframe, 2 draft,
   3 review, 4 save.
2. Step 1 (wireframe) always runs, even when the task names an
   archetype. Composition is decided there and only there.
3. Style comes from `design/` and is never negotiated per run. The user
   decides composition and label wording; the design system decides
   everything else.
4. On success the diagram exists in `diagrams/` with a metadata header
   and the run has a `done/` marker.
