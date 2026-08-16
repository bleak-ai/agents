# Step 4: Assemble

## Purpose

Combine the headline and body into the final base post. Save it. Channel
adaptation happens later in a separate workflow; this step produces the one
base post.

## Input

- `runs/{date}-{slug}/2-headline/results.md` (final headline).
- `runs/{date}-{slug}/3-body/results.md` (hook, body, close).
- `runs/{date}-{slug}/1-angle/results.md` (chosen angle).
- `runs/{date}-{slug}/0-intake/results.md` (product slug, goal).
- `voice.md`.

## Output

- `runs/{date}-{slug}/4-assemble/results.md`: the complete post, ready to
  copy.
- `posts/<YYYY-MM-DD>-<slug>.md`: the post saved to the library.
- `runs/{date}-{slug}/done/info.md`: marks the run as complete.

## How to execute

1. Ask the user about the post format through the question tool:
   - **Text only**: headline + body, ready to paste.
   - **Image + caption**: headline as the image text, body as the caption.
     Note what the image should show.
   - **Video hook**: headline as the first 3 seconds, body as description.
2. Assemble the final post according to the chosen format. The assembled
   text must pass `voice.md` and the product voice notes.
3. Present the full post to the user for final approval (approve / adjust).
4. Save to `posts/<YYYY-MM-DD>-<slug>.md` with frontmatter:

```yaml
---
product: <product-slug>
goal: <post-goal>
angle: <the chosen angle, one sentence>
headline_formula: <formula-name>
persuasion_levers: [<lever-1>, <lever-2>]
format: <text|image-caption|video-hook>
date: <YYYY-MM-DD>
---
```

5. Update the "Post defaults" section of `products/<product-slug>/info.md`
   with anything this run settled (goal default, link, install command).
6. Write the `done/` marker. Set the run index status line to `done`.

## Done when

The post is saved to `posts/` and the run is marked done. Print DONE with
the path to the saved post.
