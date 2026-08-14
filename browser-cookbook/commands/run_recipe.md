---
description: Run a saved recipe by name. Diagnoses and heals itself on failure (3 heal attempts, then report).
parameters:
  - name: recipe
    description: The recipe name to execute (e.g. "find-posts")
    required: true
---

# Run recipe

Follow `style.md`: RUNNING while executing, HEALING per attempt, BLOCKED on escalation, then the result and DONE.

1. Read `recipes/index.md` to find `$recipe`. If not found: report the error, list available recipes, stop.
2. Read `recipes/$recipe/index.md`: parameters, success definition, read-only or mutating flag.
3. Fill parameter values: use what the user provided, apply the declared default for any empty value that has one, and ask only for required values still missing.
4. If the recipe has `script.py`: run it with run_script, passing the parameters as CLI args. If it is a playbook: read the referenced site notes and blocks, then drive the browser directly, scripting deterministic parts through the site `lib.py`.
5. On success: report the result. Done.
6. On failure, heal autonomously. Budget: 3 heal attempts after the first failure.
   1. Diagnose first: transient, site changed, or blocker. Inspect the open browser to see what state the half-run left. For a mutating recipe this inspection is mandatory before any re-run, so side effects are not duplicated.
   2. A blocker escalates immediately: follow the Blockers rule in `style.md`.
   3. Otherwise fix what is wrong (site notes, blocks, lib.py, or the script), update the files, and re-run. Do not ask permission for these fixes. When the fix needs re-exploration, follow `steps/1-explore.md`, logging to a new run folder `runs/<date>-heal-<recipe>/1-exploration/results.md` created for the healing pass, and update the recipe from what it finds.
   4. After 3 failed attempts: stop. Report the diagnosis, what was tried, and what the user should look at.
7. When healing changed any file, say so in the final report (which files, what changed).
