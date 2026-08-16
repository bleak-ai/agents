# Step 3: Body draft

## Purpose

Draft the post body in two layers. System 1 (emotional hook) first, System 2
(rational proof) second. Close with a checked call to action.

## Input

- `runs/{date}-{slug}/2-headline/results.md` (final headline, formula used).
- `runs/{date}-{slug}/1-angle/results.md` (chosen angle).
- `runs/{date}-{slug}/0-intake/results.md` (product, goal, segment).
- `products/<product-slug>/info.md`.
- `voice.md`.

## Output

- `runs/{date}-{slug}/3-body/results.md` with:
  - **Hook** (System 1): the opening 2-3 sentences.
  - **Proof** (System 2): the body with features, numbers, or specifics.
  - **Close**: the call to action with its click-path checklist.

## How to execute

### Layer 1: System 1 hook (stop the scroll)

1. Draft 2-3 opening sentences. These must continue the headline and serve
   the chosen angle. Techniques:
   - **Personal frustration**: "I spent X doing Y before I found Z."
   - **Surprising fact**: a number or claim that makes the reader pause.
   - **Relatable scenario**: the reader's problem in their own words.
   - **Continuation of the headline**: expand its promise with a detail.
2. Present the hook draft through the question tool (approve / adjust /
   rewrite). The user must approve this block before the agent continues.

### Layer 2: System 2 proof (close the deal)

3. Draft the body. Structure depends on the post goal:
   - **Awareness**: what the product does, one concrete example, one
     differentiator.
   - **Launch**: what is new, why it matters, one early result or metric.
   - **Feature highlight**: the feature, the problem, before/after.
   - **Social proof**: numbers, one quote or data point.
   Everything in the body must serve the chosen angle. Cut anything that
   belongs to a different angle, even if it is true and impressive.
4. Keep it short. Each block is 2-4 sentences maximum. If it needs more,
   split into bullet points.
5. Present the body draft through the question tool (approve / adjust /
   rewrite).

### Close: call to action with click-path check

6. Draft the call to action. One sentence. Then fill the click-path
   checklist and present both together:
   - **Action**: the one thing the reader does next, named exactly
     (install, star, subscribe, reply).
   - **Target**: the exact link or command, from the "Post defaults"
     section of `info.md` when recorded.
   - **Assumptions**: what the reader must already have for the action to
     work (a terminal, uv installed, an account). If the assumption is
     heavy, propose a lighter first step.
   - **Landing match**: does the target page's own headline match this
     post's promise. If the agent cannot check, flag it as unverified
     instead of guessing.
7. Present close plus checklist through the question tool (approve /
   adjust / rewrite).

## Body quality rules

- The hook and the headline must feel like one thought.
- Use the same persuasion lever from the headline in the hook.
- Do not list more than 3 features. Pick for the chosen segment.
- Everything passes `voice.md`. When the user rewrites a block in their own
  words, append the user's version to the "Lines that sound right" section
  of `voice.md`.

## Done when

The user has approved the hook, body, and close. The results file is
written. Set the run index status line to `body approved`.
