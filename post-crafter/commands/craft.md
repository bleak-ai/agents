---
description: Create a marketing post for a product.
parameters:
  - name: task
    description: What product to write about and what the post should achieve
    required: true
---

# Craft

Create a marketing post for `$task`. Follow `style.md` for every message and
`voice.md` for every piece of copy.

1. Run the full flow in `steps/`: 0 intake, 1 angle, 2 headline, 3 body,
   4 assemble.
2. Step 2 (headline) is the core. Spend the most resources there: generate
   wide, score, red-team, then present the top 5.
3. Every piece of user-facing copy must go through the user for approval
   before the agent continues.
4. On success the post exists in `posts/` and the run has a `done/` marker.
5. Product knowledge in `products/<product-slug>/info.md` (state root) is
   created or updated regardless of outcome.
