---
id: browser-cookbook
name: Browser Cookbook
description: >
  A browser agent that learns your sites. It performs browser tasks through
  your real Chrome, accumulates per-site knowledge, and crystallizes
  repetitive tasks into plain Python scripts that run without AI. Broken
  knowledge heals itself; blockers like captchas escalate to you.
parameters:
  - name: task
    description: What to do, in plain words (e.g. "export this month's invoices from the billing dashboard")
    required: true
flow:
  - Describe a browser task in plain words
  - The agent reuses a saved recipe when one matches
  - Known sites run warm from accumulated site notes
  - run_once performs without saving a recipe; run_create_cookbook crystallizes one
  - Broken recipes diagnose and heal themselves (3 attempts, then report)
connections:
  - kind: browser
    description: Playwright attached over CDP to a Chrome instance the user chooses (daily profile or a dedicated one; roster with a default recorded in the connection)
    examples: [Chrome CDP via Playwright]
tags: [automation, browser]
learns: >
  Two layers. sites/<domain>/ holds how each site works (map, reusable
  blocks, a Python helper lib) and grows on every browser contact, even
  failed ones. recipes/<name>/ holds per-task recipes; a script is the
  default outcome and skipping it needs a written justification.
---

Turn browser work into accumulated knowledge. The agent drives your real Chrome (your logins persist), records what it learns about each site, and turns repetitive tasks into parameterized Python scripts that replay in seconds without AI.

Token economy is a design goal: AI time is spent only where judgment is needed. Deterministic parts (login, navigation, extraction) live in per-site Python helpers even when the task itself stays AI-driven.

## Entry points

- `run_once`: do the task, no recipe. Site knowledge still updates.
- `run_create_cookbook`: do the task and crystallize a recipe (full explore, verdict, save flow).
- `run_recipe`: execute a saved recipe by name; heals itself on failure.

## The script verdict

After every `run_create_cookbook` exploration the agent writes a verdict into the recipe: script candidate or not, with the reason. The default is yes; NOT scripting must be justified (content-dependent branching, layout instability, anti-bot pressure).

## Blockers

Captcha, unexpected 2FA, strange modal: the agent pauses and asks in the session. If a notification connection exists (e.g. Telegram), it also sends a message there. You fix it in the visible Chrome window; the run continues from the same page.

## Run naming

Each run folder is named with a kebab-case slug derived from the task description, decided during step 0 (analyze).
