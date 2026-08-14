---
description: Promote the last browse run into a saved recipe, without re-exploring.
parameters:
  - name: run
    description: Run folder name to promote, format <YYYY-MM-DD>-<slug> (default is the most recent unfinished run)
---

# Save recipe

Crystallize an already-explored run into a recipe. The exploration is done; do not redo it. Follow `style.md` for every message (SAVING lines).

1. Find the run to promote. When `$run` is given, use `runs/$run/`. Otherwise take the most recent `runs/<date>-<slug>/` that has `1-exploration/results.md` and no `done/` folder. When several candidates are equally plausible, present them through the question tool with their task lines.
2. Check freshness. If the run failed, or the site notes changed after the run, say so. Re-explore only the broken part (follow `steps/1-explore.md` for that part alone), not the whole task.
3. Execute step 2 (`steps/2-propose.md`): script verdict, parameters (with defaults where a sensible value exists), test plan. The user approves the proposal.
4. Execute step 3 (`steps/3-test.md`): run the test, save the recipe folder, update `recipes/index.md`, and end with the handoff block from that step.
