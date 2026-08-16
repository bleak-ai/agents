# pipeline-flow

Actors and hops, left to right. The reference diagram
(`diagrams/gcontext-architecture.svg`) is this archetype.

## When to use

- The claim names 2-4 actors and what moves between them.
- The reader must follow a flow: who initiates, what crosses each hop,
  what comes back.
- Roles differ (one side thinks, the other stores; one requests, the
  other serves).

## Scoping questions

1. Who are the actors, left to right? (2-4; more means the claim is not
   yet a pipeline)
2. What crosses each hop, in one short phrase per direction?
3. Which single hop or actor carries the claim? (it gets the reserved
   accent)
4. What inner detail per actor is worth a chip, and what stays out?

## Wireframe template

```
TITLE: <claim as one sentence>

+-- <Actor A> ----+       +-- <Actor B> ----+       +-- <Actor C> ----+
| <one-liner>     | ----> | <one-liner>     | <---> | <one-liner>     |
|                 | label |                 | label |                 |
|  [chip]         |       |  [chip] [chip]  |       |  [chip]         |
|  [chip]         | <---- |  [chip]         |       |  [chip]         |
|  [chip]         | label |                 |       |  [chip]         |
+-----------------+       +-----------------+       +-----------------+

(1) <takeaway A>          (2) <takeaway B>          (3) <takeaway C>
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1520 880" role="img"
     aria-label="CLAIM SENTENCE"
     font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif">
  <defs>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#4A6FF3"/>
    </marker>
    <marker id="arrow-orange" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#E8963C"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#2FA45C"/>
    </marker>
    <!-- paste the icon defs used below (i-bot, i-server, i-folder) from design/icons.md -->
  </defs>
  <rect width="1520" height="880" fill="#FAF8F3"/>
  <text x="70" y="72" font-size="36" font-weight="700" fill="#1F2A44">Title</text>
  <text x="70" y="106" font-size="18" fill="#6B7385">Subtitle stating the claim.</text>

  <!-- Zone A (blue) -->
  <g filter="url(#soft)"><rect x="70" y="170" width="330" height="470" rx="18" fill="#FFFFFF"/></g>
  <!-- zone accent: header icon, chips, arrows, strip dot; never a bar -->
  <use href="#i-bot" transform="translate(100,198) scale(1.6)" stroke="#4A6FF3"/>
  <text x="150" y="222" font-size="21" font-weight="700" fill="#1F2A44">Actor A</text>
  <text x="100" y="248" font-size="14" fill="#6B7385">one-liner</text>
  <rect x="100" y="280" width="270" height="84" rx="12" fill="#EEF3FE" stroke="#D4DFFB"/>
  <text x="122" y="316" font-size="16" font-weight="600" fill="#1F2A44">chip title</text>
  <text x="122" y="340" font-size="13" fill="#6B7385">chip subtext</text>

  <!-- Zone B (orange) -->
  <g filter="url(#soft)"><rect x="560" y="170" width="380" height="470" rx="18" fill="#FFFFFF"/></g>
  <use href="#i-server" transform="translate(590,198) scale(1.6)" stroke="#E8963C"/>
  <text x="640" y="222" font-size="21" font-weight="700" fill="#1F2A44">Actor B</text>
  <text x="590" y="248" font-size="14" fill="#6B7385">one-liner</text>

  <!-- Zone C (green) -->
  <g filter="url(#soft)"><rect x="1086" y="170" width="364" height="470" rx="18" fill="#FFFFFF"/></g>
  <use href="#i-folder" transform="translate(1116,198) scale(1.6)" stroke="#2FA45C"/>
  <text x="1166" y="222" font-size="21" font-weight="700" fill="#1F2A44">Actor C</text>
  <text x="1116" y="248" font-size="14" fill="#6B7385">one-liner</text>

  <!-- hops -->
  <path d="M400 330 C 470 330, 490 330, 552 330" fill="none" stroke="#4A6FF3" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <text x="476" y="316" font-size="13" fill="#4A6FF3" text-anchor="middle">hop label</text>
  <path d="M940 360 C 1010 360, 1020 360, 1078 360" fill="none" stroke="#2FA45C" stroke-width="2.5" marker-end="url(#arrow-green)" marker-start="url(#arrow-green)"/>
  <text x="1010" y="346" font-size="13" fill="#2FA45C" text-anchor="middle">hop label</text>

  <!-- story strip -->
  <circle cx="90" cy="720" r="14" fill="#4A6FF3"/>
  <text x="90" y="725" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="116" y="725" font-size="14" fill="#1F2A44">takeaway for zone A</text>
</svg>
```

## Composition rules

- One panel per actor; the middle actor may be wider when it holds the
  mechanism.
- Chips stack vertically inside a panel, 100px pitch (84 high, 16 gap).
- Return flows run dashed, lower than the forward flow, in the responding
  zone's accent.
- The story strip repeats the claim as numbered takeaways, one per zone.

## Pitfalls

- More than 4 actors: merge or cut; this is not an org chart.
- Arrow labels that describe the arrow ("sends to") instead of what
  crosses it ("read, write, run").
- Chips used as a feature list instead of the 2-3 details the claim needs.
