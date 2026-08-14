---
description: Do a browser task without saving a recipe. Site knowledge still updates.
parameters:
  - name: task
    description: What to do, in plain words
    required: true
---

# Browse

Perform `$task` in the browser. Do not create a recipe. Follow `style.md` for every message.

1. Follow steps 0 (analyze) and 1 (explore) from `steps/`.
2. Before touching the browser, read `sites/<domain>/index.md` and any relevant `blocks/*.md` for the target site. Use `lib.py` helpers through ad-hoc scripts for the deterministic parts (login, navigation, extraction).
3. Perform the task. One BROWSING line per action group. On a blocker, follow the Blockers rule in `style.md`.
4. Report the result against the success definition from step 0: the data, then DONE.
5. Update `sites/<domain>/` with anything learned (new selectors, changed navigation, new gotchas). Not optional; a failed run also updates the notes with what failed.
6. Do NOT write a recipe folder and do NOT write a script verdict.
7. End with one line, invocation built per `style.md`: `To save as recipe: /mcp__<alias>__save_recipe`
