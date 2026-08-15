---
description: Do a browser task without saving a recipe. Site knowledge still updates.
parameters:
  - name: task
    description: What to do, in plain words
    required: true
---

# Browse

Perform `$task` in the browser. Do not create a recipe. Follow `style.md` for every message.

1. **Fast-path analysis** (inline, no step files):
   - Parse the task. Identify the target URL or app and the goal.
   - Ask through the question tool ONLY when genuinely ambiguous (two plausible targets or two plausible goals). Do not ask to confirm an analysis you are sure of.
   - Derive a kebab-case slug (two or three short words).
   - Check `recipes/index.md` for a matching recipe. If one matches, offer it through the question tool (run the recipe / continue browsing). Running it means: read `commands/run_recipe.md` and follow it, skipping its lookup step. Stop here if they agree.
   - Create `runs/<YYYY-MM-DD>-<slug>/index.md` with target, goal, success definition, and a status line. This happens only when no matching recipe was accepted.
2. Before touching the browser, read `sites/<domain>/index.md` and any relevant `blocks/*.md` for the target site. Use `lib.py` helpers through ad-hoc scripts for the deterministic parts (login, navigation, extraction).
3. Perform the task. One BROWSING line per action group. On a blocker, follow the Blockers rule in `style.md`. Record each action in `runs/<date>-<slug>/1-exploration/results.md` as it goes: numbered action sequence with, per action, what was done, the selector or anchor used, what the page showed after, and any branching. This log is what `save_recipe` promotes later.
4. Report the result against the success definition: the data, then DONE.
5. Update `sites/<domain>/` with anything learned (new selectors, changed navigation, new gotchas). Not optional; a failed run also updates the notes with what failed.
6. Do NOT write a recipe folder and do NOT write a script verdict.
7. End with one line, invocation built per `style.md`: `To save as recipe: /mcp__<alias>__save_recipe`
