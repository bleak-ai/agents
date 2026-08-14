---
description: Do a browser task AND crystallize it into a recipe (script by default).
parameters:
  - name: task
    description: What to do, in plain words
    required: true
---

# New recipe

Perform `$task` and turn it into a recipe. Follow `style.md` for every message.

1. Run the full flow in `steps/`: 0 analyze, 1 explore, 2 propose, 3 test.
2. Step 2 MUST produce the script verdict: script candidate or not, with the reason. The default answer is yes; justify a no.
3. On success the recipe exists in `recipes/<name>/` and `recipes/index.md` lists it. Step 3 ends with the handoff block that tells the user exactly how to run the recipe again.
4. Site knowledge in `sites/<domain>/` is updated regardless of outcome.
