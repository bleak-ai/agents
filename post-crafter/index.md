---
id: post-crafter
name: Post Crafter
description: >
  A marketing post agent that puts the headline first. Each post starts from
  a chosen angle, then a headline workshop generates candidates from proven
  persuasion formulas (Cialdini, Kahneman, Caples), scores them, red-teams
  the best, and lets the user pick or rewrite. The body follows in two
  layers: a System 1 hook to stop the scroll, then System 2 proof to close
  the deal. The user controls every content decision. Product knowledge
  accumulates in a shared products/ folder so repeat runs stop re-asking.
flow:
  - Describe the product and what the post should achieve
  - The agent loads products/<slug>/info.md (or creates it on first run) and the user picks the audience segment
  - Angle step proposes 3-5 distinct claims for this post; the user picks one
  - Headline workshop generates 15-25 scored candidates, red-teams the top 5, and presents the survivors
  - The user picks a headline (or writes their own), then refines from variations
  - Body draft follows System 1 hook then System 2 proof, each block approved separately, close checked for click path
  - Final post assembled and saved
connections: []
tags: [marketing, content, copywriting]
learns: >
  Two layers. products/<slug>/info.md at the state root holds everything
  known about a product: positioning, audience segments with awareness
  stages, numbers, and post defaults, so repeat runs only ask what is new.
  posts/ holds every completed post with its angle, headline formula, and
  persuasion levers, so the angle step can avoid repeating what has been
  said. voice.md accumulates lines the user approved.
---

All paths in commands and steps are relative to this module folder, except
paths starting with `products/`, which are relative to the state root (see
`style.md`). After `gcontext add`, prefix module paths with
`modules/post-crafter/`.

Create marketing posts with the headline as the center of gravity. The agent
reads persuasion formulas from `formulas/`, loads product knowledge from
`products/` at the state root, and walks the user through an angle-first,
headline-centered writing flow. Every content decision belongs to the user.
The agent proposes, scores, and drafts. The user picks, rewrites, and
approves.

Note on portability: this module depends on the shared `products/` folder at
the state root, so copying the module folder alone does not carry the
product knowledge. The setup command scaffolds `products/` on a fresh
install.

## Entry points

- `craft`: the primary action. Create a post for a product.
- `setup`: configure the agent, seed formulas, scaffold `products/`.

## Contents

- `commands/`: user-invokable entry points, exposed as slash commands.
- `steps/`: the ordered five-step flow the craft command follows.
- `formulas/`: persuasion and headline formulas as editable markdown files.
- `voice.md`: voice rules, banned words, and approved lines.
- `posts/`: completed posts, one file per post.
- `runs/`: one folder per execution, named by date and task slug.
- `style.md`: the message regime every command follows.

Shared state outside the module (state root):

- `products/`: one folder per product with its `info.md`.
