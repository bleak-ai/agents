# Recipes

One folder per task the agent has crystallized. Each `recipes/<name>/` has an `index.md` (YAML frontmatter with description and parameters, then goal, success definition, script verdict with reason, read-only or mutating flag, source site, blocks used) and, when the verdict allows, a `script.py`.

Each recipe is also its own slash command: `commands/recipe.md` is a template (`each: recipes/*/`) that registers one prompt per folder here, named `recipe_<name>` (hyphens become underscores), with the frontmatter description shown in the client's picker. A new recipe's command appears after the client reconnects.

Consulted during step 0 (analyze). Step 3 (test) adds entries. `run_recipe` heals broken entries autonomously (3 attempts, then report).

## Contents

_(no recipes yet; they are created by run_create_cookbook)_
