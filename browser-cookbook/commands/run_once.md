---
description: Do a browser task without saving a recipe. Site knowledge still updates.
parameters:
  - name: task
    description: What to do, in plain words
    required: true
---

# Run once

Perform `$task` in the browser. Do not create a recipe.

1. Follow steps 0 (analyze) and 1 (explore) from `steps/`. If a matching recipe already exists, say so and suggest `run_recipe` instead; continue only if the user declines.
2. Before touching the browser, read `sites/<domain>/index.md` and any relevant `blocks/*.md` for the target site. Use `lib.py` helpers through ad-hoc scripts for the deterministic parts (login, navigation, extraction).
3. Perform the task. On a blocker, follow the blocker rule in `steps/1-explore.md`.
4. Report the result against the success definition from step 0.
5. Update `sites/<domain>/` with anything learned (new selectors, changed navigation, new gotchas). This step is not optional; a failed run also updates the notes with what failed.
6. Do NOT write a recipe folder and do NOT write a script verdict.
