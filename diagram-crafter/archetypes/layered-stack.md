# layered-stack

What sits on what. Vertical bands; higher means closer to the user, lower
means closer to the foundation.

## When to use

- The claim is about dependency or abstraction: X builds on Y, Y hides Z.
- The reader must see which layer they touch and which layers exist below.
- Order matters, movement between layers does not (movement wants
  pipeline-flow or cycle-loop).

## Scoping questions

1. What are the layers, top to bottom? (3-5)
2. Which layer carries the claim? (it gets the reserved accent; the rest
   stay neutral tints)
3. What one phrase describes each layer's job?
4. Are there side notes (a caller, a constraint) worth a margin
   annotation, or do they stay out?

## Wireframe template

```
TITLE: <claim as one sentence>

+---------------------------------------------------+
|  <Layer 1: what the reader touches>   <one-liner> |
+---------------------------------------------------+
|  <Layer 2>                            <one-liner> |   <- claim layer
+---------------------------------------------------+
|  <Layer 3: the foundation>            <one-liner> |
+---------------------------------------------------+

note: <optional margin annotation>
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" role="img"
     aria-label="CLAIM SENTENCE"
     font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif">
  <defs>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
    </filter>
  </defs>
  <rect width="1200" height="760" fill="#FAF8F3"/>
  <text x="70" y="72" font-size="36" font-weight="700" fill="#1F2A44">Title</text>
  <text x="70" y="106" font-size="18" fill="#6B7385">Subtitle stating the claim.</text>

  <!-- layer band: repeat with y += 140 -->
  <g filter="url(#soft)"><rect x="70" y="170" width="900" height="110" rx="14" fill="#FFFFFF"/></g>
  <text x="106" y="218" font-size="21" font-weight="700" fill="#1F2A44">Layer name</text>
  <text x="106" y="246" font-size="14" fill="#6B7385">what this layer does</text>
  <text x="940" y="230" font-size="13" fill="#8A90A0" text-anchor="end">margin note</text>

  <!-- claim layer variant: tinted body instead of white -->
  <g filter="url(#soft)"><rect x="70" y="310" width="900" height="110" rx="14" fill="#FDF6EC"/></g>
  <text x="106" y="358" font-size="21" font-weight="700" fill="#1F2A44">Claim layer</text>
  <text x="106" y="386" font-size="14" fill="#6B7385">why it matters</text>

  <text x="70" y="700" font-size="13" fill="#8A90A0">footnote</text>
</svg>
```

## Composition rules

- Bands are full content width, 110px high, 30px vertical gap. No edge or
  top bars; a band's accent shows only in an optional header icon stroke
  and in its margin note.
- Exactly one band is tinted: the claim layer. All others stay white.
- Margin annotations right-aligned inside the band, faint gray.
- Optional narrow side rail (arrow spanning all bands) only when the
  claim includes direction ("requests flow down").

## Pitfalls

- Equal visual weight on all layers when one carries the claim.
- Using a stack for things that are peers, not layers (peers want panels
  side by side).
- More than 5 bands; merge the foundation layers.
