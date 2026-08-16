# concept-hero

One idea, one big visual metaphor. A single central figure the reader
remembers, with a small number of annotations pointing into it.

## When to use

- The claim is one concept, not a structure: "an agent is a folder",
  "state outlives sessions".
- A structural archetype would dilute it into boxes.
- There is a natural visual metaphor (a container, a bridge, an anchor,
  a layerless object).

## Scoping questions

1. What is the one sentence the reader must remember?
2. What object or metaphor embodies it? (offer 2 in the wireframe step
   if unsure)
3. What 2-4 annotations make the metaphor precise instead of decorative?
4. What must NOT be in the picture? (hero diagrams die of clutter first)

## Wireframe template

```
TITLE: <the one sentence>

                 <annotation 1> --\
                                   v
              +---------------------------+
              |                           |
              |   <THE CENTRAL FIGURE>    |  <-- <annotation 2>
              |   <its label>             |
              |                           |
              +---------------------------+
                                   ^
                 <annotation 3> --/

<one supporting caption line>
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img"
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
  <rect width="1200" height="800" fill="#FAF8F3"/>
  <text x="600" y="90" font-size="36" font-weight="700" fill="#1F2A44" text-anchor="middle">The one sentence</text>

  <!-- central figure: composed shapes, not a stock icon; this rect is a stand-in -->
  <g filter="url(#soft)"><rect x="400" y="220" width="400" height="340" rx="24" fill="#FFFFFF"/></g>
  <text x="600" y="410" font-size="24" font-weight="700" fill="#1F2A44" text-anchor="middle">central figure label</text>

  <!-- annotation: repeat 2-4 times around the figure -->
  <text x="180" y="300" font-size="15" font-weight="600" fill="#1F2A44">annotation title</text>
  <text x="180" y="322" font-size="13" fill="#6B7385">one line of detail</text>
  <path d="M330 306 C 360 306, 370 300, 392 290" fill="none" stroke="#4A6FF3" stroke-width="1.8" marker-end="url(#arrow-blue)"/>

  <text x="600" y="700" font-size="15" fill="#6B7385" text-anchor="middle">supporting caption line</text>
</svg>
```

## Composition rules

- The central figure takes at least a third of the canvas and is built
  from composed shapes (rects, paths, icons from `design/icons.md`
  scaled up), never a single stock icon blown up.
- Title centered above; this archetype may center the header,
  overriding the default left header.
- 2-4 annotations, short leader lines with gentle curves, never
  crossing the figure.
- Generous whitespace is the style; if it looks empty, it is working.

## Pitfalls

- Metaphor drift: decoration that contradicts the claim.
- Turning it into a labeled parts diagram (5+ annotations).
- Tiny hero: if the figure is under a third of the canvas, the layout
  has reverted to a panel diagram.
