---
id: browser-recipes
name: Browser Recipes
description: >
  Explore browser actions with AI, then crystallize them into reusable Python
  scripts. Recipes self-heal: when a script fails, the agent falls back to
  live exploration and updates the recipe.
parameters:
  - name: action
    description: What to do, in plain words (e.g. "export the monthly report from the admin dashboard")
    required: true
flow:
  - Describe a browser action in plain words
  - The agent reuses a saved recipe when one matches
  - Otherwise it explores the site live and records every step
  - A tested script is saved for next time
  - Broken recipes are re-explored and replaced
connections:
  - kind: browser
    description: A browser automation interface (Chrome CDP, Playwright, or similar)
    examples: [Chrome CDP, Playwright, Selenium]
tags: [automation, browser]
learns: >
  This agent saves every browser action as a reusable Python script. When a
  site changes and a script breaks, it re-explores and replaces the recipe.
---

Turn a plain-language browser action into a reusable Python script. The agent explores the target site with AI-driven browser control, records every step, and produces a parameterized recipe. On future runs, the recipe executes directly (fast, no AI needed). If a recipe fails, the agent re-explores and updates it automatically.

The `action` parameter is a plain-language description of what to do. Examples: "export the monthly report from the admin dashboard", "change the team name in the settings page", "download all invoices for Q2".

## Run naming

Each run folder is named with a kebab-case slug derived from the action description. For example, "export the monthly sales report" becomes `export-monthly-sales-report`. The slug is decided during step 0 (analyze).

## How it learns

The agent accumulates knowledge in one place:

1. **Recipes** (`recipes/`): parameterized Python scripts for browser actions the agent has performed before. Step 0 (analyze) checks this library first. If a recipe matches, the agent runs it directly via the `run-recipe` command. Step 3 (test) saves new recipes here after a successful test. Each recipe has a `.py` file (the script) and a `.md` file (metadata, parameters, origin).

2. **Run history** (`runs/`): every completed action is a structured folder with analysis, exploration log, recipe proposal, and outcome. The agent can search past runs to find how a similar action was handled before.

When a saved recipe fails, the agent falls back to the full four-step process. The re-exploration produces an updated recipe that replaces the broken one. Recipes improve over time as sites change.
