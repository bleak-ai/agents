# Post Crafter

Create marketing posts with the headline as the center of gravity. The agent generates headline candidates from proven persuasion formulas, shows the reasoning behind each, and lets you pick or rewrite. Then it drafts the body in two layers: a System 1 hook to stop the scroll, followed by System 2 proof to close the deal. You control every content decision.

## Install

```
gcontext add post-crafter
```

Then run setup:

```
/mcp__<instance>__post_crafter__setup
```

## How it works

1. You describe the product and what the post should achieve.
2. The agent loads the product's `info.md` (or creates it on first run) and you pick the audience segment.
3. Angle: the agent proposes 3-5 distinct claims for this post. You pick one.
4. Headline workshop: 15-25 candidates scored on specificity, front-load, provability, angle fit, and voice fit. The top 5 are red-teamed and presented with their strongest objection. You pick one, then refine from variations.
5. Body draft: System 1 hook approved first, then System 2 proof, then a call to action with a click-path check.
6. Final post assembled and saved.

## What it learns

- `products/` (state root): one `info.md` per product with positioning, audience segments and their awareness stages, numbers, and post defaults. Repeat runs only ask what is new.
- `posts/`: every completed post, tagged with the angle, headline formula, and persuasion levers used.
- `voice.md`: voice rules plus lines you approved, growing with every run.

## Formulas

The agent ships with 14 seed formulas from Cialdini, Kahneman, Caples, and positioning practice. Each formula is a markdown file in `formulas/` that you can edit, add to, or remove.

- `loss-aversion` - Frame what the reader loses by not having the product.
- `social-proof` - Show specific numbers and peer adoption.
- `unity-identity` - Signal shared identity with the audience.
- `scarcity` - Real time or quantity constraints.
- `authority` - Credentials and domain experience.
- `curiosity-gap` - Open a gap between what the reader knows and wants to know.
- `reciprocity` - Give something valuable for free first.
- `number-anchor` - Lead with a specific number to anchor expectations.
- `how-to` - Promise practical instruction; the product is the tool inside the method.
- `question` - Make the reader self-diagnose with a pointed question.
- `counterintuitive` - Challenge a belief the audience holds, then defend it.
- `transformation` - Concrete before and after.
- `story` - Personal narrative; the product enters as the resolution.
- `contrast-alternative` - Position against a known alternative, fairly.

## Layout

- `commands/`: user-invokable entry points.
- `steps/`: the five-step flow (intake, angle, headline, body, assemble).
- `formulas/`: persuasion and headline formulas.
- `voice.md`: voice rules and approved lines.
- `posts/`: completed posts.
- `runs/`: one folder per execution.
- `style.md`: the message regime every command follows.
- `products/` (state root, outside the module): one folder per product with its `info.md`.

See `index.md` for the full agent definition.
