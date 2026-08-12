# Step 3: Test and save

## Purpose

Prove the recipe works, then save it.

## Input

The approved recipe proposal from step 2; the browser connection.

## Output

- On success: `recipes/{name}/index.md`, `recipes/{name}/script.py` when the verdict is yes, updated `recipes/index.md`, and `runs/{slug}/done/info.md`.
- On failure: the diagnosis recorded in the run folder.

## How to execute

1. Run the script (via run_script with the test-plan args) or walk the playbook once.
2. Verify against the success definition.
3. On success, write the recipe folder:
   - `recipes/{name}/index.md`: goal, parameters, success definition, script verdict with reason, read-only or mutating flag, source site, blocks used, source run slug, creation date.
   - `recipes/{name}/script.py` when the verdict is yes.
   - Update `recipes/index.md` and, if helpers were added, `sites/<domain>/lib.py` and the site index.
   - Write `runs/{slug}/done/info.md`: what was achieved, what was learned.
4. On failure: this is the healing path. Diagnose (transient, site changed, blocker), fix the responsible file, re-run. Budget: 3 attempts, then stop and report. Blockers escalate immediately.

## Done when

The recipe is saved and listed, or the failure is reported with its diagnosis.
