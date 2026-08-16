# cycle-loop

A repeating process. Nodes on a ring, arrows showing the direction, the
compounding effect in the center.

## When to use

- The claim is that the process feeds itself: each pass improves the next.
- There are 3-5 stages and the last leads back to the first.
- If the loop runs once, it is a pipeline or timeline, not a cycle.

## Scoping questions

1. What are the stages, in order? (3-5)
2. What accumulates or improves each pass? (this goes in the center)
3. Which stage carries the claim?
4. Is there an entry point worth marking (where the user starts)?

## Wireframe template

```
TITLE: <claim as one sentence>

            [<stage 1>]
           /           \
          v             \
   [<stage 4>]   ((<what compounds>))   [<stage 2>]
          \             ^
           \           /
            [<stage 3>]

entry: <where the user starts>
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 900" role="img"
     aria-label="CLAIM SENTENCE"
     font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif">
  <defs>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#4A6FF3"/>
    </marker>
  </defs>
  <rect width="1100" height="900" fill="#FAF8F3"/>
  <text x="70" y="72" font-size="36" font-weight="700" fill="#1F2A44">Title</text>
  <text x="70" y="106" font-size="18" fill="#6B7385">Subtitle stating the claim.</text>

  <!-- center: what compounds -->
  <circle cx="550" cy="500" r="110" fill="#EEF3FE" stroke="#D4DFFB"/>
  <text x="550" y="494" font-size="18" font-weight="700" fill="#1F2A44" text-anchor="middle">what compounds</text>
  <text x="550" y="518" font-size="13" fill="#6B7385" text-anchor="middle">grows every pass</text>

  <!-- node card: repeat at 12, 3, 6, 9 o'clock around the center -->
  <g filter="url(#soft)"><rect x="440" y="200" width="220" height="90" rx="14" fill="#FFFFFF"/></g>
  <text x="550" y="242" font-size="16" font-weight="600" fill="#1F2A44" text-anchor="middle">stage name</text>
  <text x="550" y="266" font-size="13" fill="#6B7385" text-anchor="middle">one-liner</text>

  <!-- ring arrow: repeat, rotating around the center -->
  <path d="M680 270 C 800 320, 840 400, 830 470" fill="none" stroke="#4A6FF3" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <text x="810" y="350" font-size="13" fill="#4A6FF3">what passes</text>
</svg>
```

## Composition rules

- Nodes sit at clock positions (12, 3, 6, 9 for four stages), equal size.
- The direction is clockwise unless the domain reads otherwise.
- The center circle holds the compounding thing; it is the claim carrier
  and takes the reserved accent tint.
- Mark the entry stage with a small "start here" caption in faint gray.

## Pitfalls

- A cycle with no center: if nothing compounds, this is not a loop story.
- Uneven node spacing; the ring shape is the message.
- Arrows labeled with stage names instead of what moves between stages.
