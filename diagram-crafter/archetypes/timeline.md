# timeline

Stages over time, left to right along an axis. Time or sequence is the
message; the stages do not loop.

## When to use

- The claim is progression: phases, versions, a rollout, a history.
- The reader must see order and relative position, not interaction.
- 3-6 stages; each has a name and one outcome.

## Scoping questions

1. What are the stages, in order, with real names or dates?
2. What one outcome defines each stage?
3. Which stage carries the claim (usually "now" or the turning point)?
4. Does the reader need a "you are here" marker?

## Wireframe template

```
TITLE: <claim as one sentence>

  [<stage 1>]      [<stage 2>]      [<stage 3>]      [<stage 4>]
   <outcome>        <outcome>        <outcome>        <outcome>
 ----o----------------o----------------o----------------O--------->
   <date>           <date>           <date>          <date, claim stage>
```

## Skeleton

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1520 620" role="img"
     aria-label="CLAIM SENTENCE"
     font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif">
  <defs>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
    </filter>
    <marker id="arrow-gray" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 z" fill="#8A90A0"/>
    </marker>
  </defs>
  <rect width="1520" height="620" fill="#FAF8F3"/>
  <text x="70" y="72" font-size="36" font-weight="700" fill="#1F2A44">Title</text>
  <text x="70" y="106" font-size="18" fill="#6B7385">Subtitle stating the claim.</text>

  <!-- axis -->
  <path d="M100 430 L1440 430" stroke="#8A90A0" stroke-width="2" marker-end="url(#arrow-gray)"/>

  <!-- stage: repeat with x pitch = usable width / (stages - 1) -->
  <circle cx="180" cy="430" r="9" fill="#4A6FF3"/>
  <text x="180" y="466" font-size="13" fill="#8A90A0" text-anchor="middle">date</text>
  <g filter="url(#soft)"><rect x="80" y="220" width="200" height="150" rx="14" fill="#FFFFFF"/></g>
  <text x="100" y="262" font-size="16" font-weight="600" fill="#1F2A44">stage name</text>
  <text x="100" y="288" font-size="13" fill="#6B7385">outcome line</text>
  <path d="M180 370 L180 418" stroke="#4A6FF3" stroke-width="1.8" stroke-dasharray="4 4"/>

  <!-- claim stage: larger dot, tinted card, reserved accent -->
  <circle cx="1260" cy="430" r="12" fill="#E8963C"/>
</svg>
```

## Composition rules

- One accent for the ordinary stages, the reserved accent for the claim
  stage only (its dot larger, its card tinted).
- Cards above the axis, dates below. If cards collide, alternate above
  and below rather than shrinking.
- Even x pitch between stage dots; time distortion needs a footnote.

## Pitfalls

- Stages that interact (arrows between cards): that is a pipeline.
- Wall-of-text cards; one outcome line per stage.
- Uneven pitch used to encode duration without saying so.
