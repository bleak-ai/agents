# Step 1: Explore with the browser

## Purpose

Reach the goal in the browser, record every step, and grow the site knowledge.

## Input

The analysis from step 0; the browser connection; `sites/<domain>/` if present.

## Output

- `runs/{date}-{slug}/1-exploration/results.md`: numbered action sequence with, per action: what was done, the selector or anchor used, what the page showed after, and any branching ("if a cookie banner appears, dismiss it first").
- Updated `sites/<domain>/`: this is mandatory, on success AND failure. Create the folder with the fixed `index.md` sections (Access, Navigation, Selectors, Gotchas) on first contact.

## How to execute

1. Read the site notes first. Reuse known navigation and selectors instead of rediscovering them. Script deterministic stretches through `lib.py` helpers when they exist.
2. Drive the browser with short ad-hoc Python snippets (Playwright attached over CDP; the attach snippet is in the browser connection's index.md). Observe after every action. Record each successful step in the exploration log immediately, not from memory at the end. If the debug port stops answering, restart that Chrome instance yourself with its recorded flags (the procedure is in `commands/setup.md`, section 2) and continue; say one line about it, do not ask. Attach to the default instance from the connection's roster unless the user named another for this run.
3. Pace like a human: brief pauses between actions, no rapid-fire loops against one page.
4. On a blocker, follow the Blockers rule in `style.md`.
5. When the goal is reached, verify it against the success definition.

## Done when

The goal is verified and both the exploration log and the site notes are written.
