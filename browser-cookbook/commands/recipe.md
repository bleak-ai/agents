---
description: Run a saved recipe
each: recipes/*/
---

Run the saved recipe `$each` now. Call run_script with path `recipes/$each/script.py`, passing the argument values below as positional CLI args in the order listed; a value left empty takes its stated default. Do not read any recipe or site files first. Print the script output as the result, then DONE (`style.md` applies).

Only when that call fails (script missing or nonzero status): read `recipes/$each/index.md` and follow `commands/run_recipe.md` from its step 4, including the heal budget. A recipe without `script.py` is a playbook; this failure path covers it.
