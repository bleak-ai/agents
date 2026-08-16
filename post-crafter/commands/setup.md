---
description: Configure the agent, seed formulas, scaffold the products folder.
---

# Setup

Initialize the post-crafter agent. Follow `style.md` for every message.

1. Check that `formulas/` contains at least the seed formula files. If any
   are missing, report which ones.
2. Check that `voice.md` exists. If missing, report it.
3. Check that `products/index.md` exists at the state root. If not, create
   it:

```markdown
# Products

One folder per product. Each folder has an `info.md` with everything the
post workflow knows about the product.

(no products yet)
```

4. List the current formula files and their descriptions.
5. Ask the user if they want to register a product now through the question
   tool (add / skip). If adding, create `products/<slug>/info.md` from the
   template below, asking for each section, and add a line to
   `products/index.md`.
6. Ask the user if they want to add a custom formula through the question
   tool (add / skip). If adding: ask for the formula name, mechanism, and
   example pattern. Save to `formulas/<name>.md`.
7. Print DONE with the count of available formulas and products.

## info.md template

```markdown
# <Product name>

## What it does
<one short paragraph>

## Who it is for
<one line per segment. Format: "- <segment>: <one line>. Awareness stage: <unaware|problem aware|solution aware|product aware|unknown>">

## Problem it solves
<one sentence>

## Differentiators
1. <...>

## Positioning vs alternatives
<one line per alternative: what it does well, where it falls short>

## Numbers and proof
<real metrics only; "none yet" is valid>

## Post defaults
<answers that repeat across runs: default goal, primary link, install command, preferred levers, claims to avoid>

## Voice notes
<optional product-specific overrides of voice.md>
```
