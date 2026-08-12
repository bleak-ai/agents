# Recipes

One folder per task the agent has crystallized. Each `recipes/<name>/` has an `index.md` (goal, parameters, success definition, script verdict with reason, read-only or mutating flag, source site, blocks used) and, when the verdict allows, a `script.py`.

Consulted during step 0 (analyze). Step 3 (test) adds entries. `run_recipe` heals broken entries autonomously (3 attempts, then report).

## Index

_(no recipes yet; they are created by run_create_cookbook)_
