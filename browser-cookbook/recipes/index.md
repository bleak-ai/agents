# Recipes

One folder per task the agent has crystallized. Each `recipes/<name>/` has an `index.md` (YAML frontmatter with description and parameters, then goal, success definition, script verdict with reason, read-only or mutating flag, source site, blocks used) and, when the verdict allows, a `script.py`.

Each recipe is also its own slash command: `commands/recipe.md` is a template (`each: recipes/*/`) that registers one prompt per folder here. The registered name is `recipe_<name>` (hyphens become underscores), invoked as `/mcp__<alias>__recipe_<name>` (alias from the client config), with the frontmatter description shown in the client's picker. A parameter with a `default:` in the frontmatter is optional in the picker. A new recipe's command appears after the client reconnects; until then `run_recipe` works.

Consulted during step 0 (analyze). Step 3 (test) adds entries. `run_recipe` heals broken entries autonomously (3 heal attempts, then report).

## Index

One line per recipe: `- <name>: <description> (command recipe_<x>; params: <name per param, "=default" where one exists>)`.

_(no recipes yet; they are created by new_recipe or save_recipe)_
