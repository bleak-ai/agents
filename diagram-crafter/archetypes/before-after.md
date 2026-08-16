# before-after

Two states side by side, the difference highlighted. The claim lives in
the delta.

## When to use

- The claim is a change: what it was, what it is now, what improved.
- The reader must compare the same elements in both states.
- There are at most 3-4 comparable elements (more wants a table, not a
  diagram).

## Scoping questions

1. What are the two states called? (real names: "before gcontext",
   "with gcontext"; never just "before" and "after")
2. Which elements appear in both states, in the same order?
3. What is the single difference that carries the claim?
4. What quantity, if any, sums up the delta? (a number makes the strip)

## Wireframe template

```
TITLE: <claim as one sentence>

+-- <State 1> --------+          +-- <State 2> --------+
|  [element 1: bad]   |          |  [element 1: good]  |
|  [element 2: bad]   |  =====>  |  [element 2: good]  |
|  [element 3: bad]   |  <verb>  |  [element 3: good]  |  <- delta chip highlighted
+---------------------+          +---------------------+

(number or one-line delta summary)
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 760" role="img"
     aria-label="CLAIM SENTENCE"
     font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif">
  <defs>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#2FA45C"/>
    </marker>
  </defs>
  <rect width="1400" height="760" fill="#FAF8F3"/>
  <text x="70" y="72" font-size="36" font-weight="700" fill="#1F2A44">Title</text>
  <text x="70" y="106" font-size="18" fill="#6B7385">Subtitle stating the claim.</text>

  <!-- before: faint gray accent, muted chips; no bars anywhere -->
  <g filter="url(#soft)"><rect x="70" y="170" width="540" height="440" rx="18" fill="#FFFFFF"/></g>
  <text x="100" y="222" font-size="21" font-weight="700" fill="#6B7385">State 1</text>
  <rect x="100" y="260" width="480" height="80" rx="12" fill="#F1F1F3" stroke="#DDDEE3"/>
  <text x="122" y="294" font-size="16" font-weight="600" fill="#1F2A44">element</text>
  <text x="122" y="318" font-size="13" fill="#6B7385">its cost in this state</text>

  <!-- transition -->
  <path d="M610 390 C 660 390, 680 390, 782 390" fill="none" stroke="#2FA45C" stroke-width="2.5" marker-end="url(#arrow-green)"/>
  <text x="700" y="376" font-size="13" fill="#2FA45C" text-anchor="middle">what changed</text>

  <!-- after: green accent carried by chips and the transition arrow -->
  <g filter="url(#soft)"><rect x="790" y="170" width="540" height="440" rx="18" fill="#FFFFFF"/></g>
  <text x="820" y="222" font-size="21" font-weight="700" fill="#1F2A44">State 2</text>
  <rect x="820" y="260" width="480" height="80" rx="12" fill="#EFF9F2" stroke="#CFEBD9"/>
  <text x="842" y="294" font-size="16" font-weight="600" fill="#1F2A44">element</text>
  <text x="842" y="318" font-size="13" fill="#6B7385">its state now</text>

  <text x="700" y="690" font-size="14" fill="#1F2A44" text-anchor="middle">one-line delta summary or number</text>
</svg>
```

## Composition rules

- The before panel is visually quieter: muted header, gray chip tints.
  The after panel's accent lives in its chips and the transition arrow;
  no colored bars on either panel.
- Elements appear in the same order in both panels so the eye can pair
  them. Same chip heights, same y positions.
- Exactly one chip in the after panel is the delta carrier; it may use a
  stronger tint or a small badge, nothing else may.
- The center transition arrow gets a verb, not a label like "after".

## Pitfalls

- Symmetric styling that makes both states equally attractive.
- Elements in different order left vs right (breaks comparison).
- Before-state exaggeration; the diagram loses trust if the before is a
  strawman.
