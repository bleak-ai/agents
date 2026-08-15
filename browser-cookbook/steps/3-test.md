# Step 3: Test and save

## Purpose

Prove the recipe works, then save it.

## Input

The approved recipe proposal from step 2; the browser connection.

## Output

- On success: `recipes/{name}/index.md`, `recipes/{name}/script.py` when the verdict is yes, updated `recipes/index.md`, and `runs/{date}-{slug}/done/info.md`.
- On failure: the diagnosis recorded in the run folder.

## How to execute

1. For a script verdict: write `recipes/{name}/script.py` first, then run it via run_script with the test-plan args. The script takes its parameters as positional CLI args, in the order the recipe frontmatter declares them; the generated recipe command relies on this order. If the test finally fails, remove the file with an ad-hoc script so no unproven recipe remains. For a playbook: walk it once.
2. Verify against the success definition.
3. On success, complete the recipe folder (for a script verdict, `script.py` already exists from step 1):
   - `recipes/{name}/index.md`: starts with a `---` YAML frontmatter block holding `description` (one line, shown next to the recipe's slash command in the client), `parameters` (list of `name`, `description`, `required`, and `default` where the proposal gave one; a default makes the argument optional in the picker), and `anchoring` (the anchoring block from step 2: list of anchors with their strategies and the durability line). After the frontmatter, the prose: goal, success definition, script verdict with reason, read-only or mutating flag, source site, blocks used, source run slug, creation date.
   - Update `recipes/index.md` with the recipe's line in the Index format stated there, and, if helpers were added, `sites/<domain>/lib.py` and the site index.
   - Write or update `sites/<domain>/selftest.py`: attach over CDP, load each page the site's scripts depend on, assert every recorded anchor still resolves. Read-only, no mutations. Exit 0 when all anchors pass, exit 1 and print dead anchors. Append the new recipe's anchors without removing existing checks.
   - Write `runs/{date}-{slug}/done/info.md`: what was achieved, what was learned.
   - End the final report with this handoff block, filled in (values are the test-plan args that just proved the recipe; `<alias>` is derived per `style.md`):

     ```
     Recipe saved: {name}
     Next: type /mcp in your client to reconnect. The new command then appears in the picker.
     Run it: /mcp__<alias>__recipe_{name_with_underscores}   {param}: {value used in the test}
     Before you reconnect, use: /mcp__<alias>__run_recipe recipe: {name}
     All recipes: type /recipe in the picker, or read recipes/index.md
     ```
4. On failure: this is the healing path. Diagnose (transient, site changed, blocker), fix the responsible file, re-run. Budget: 3 heal attempts, then stop and report. Blockers escalate immediately.

## Done when

The recipe is saved and listed, or the failure is reported with its diagnosis.
