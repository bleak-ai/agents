# Layout

## Canvas

- Default viewBox `0 0 1520 880` for landscape multi-panel diagrams.
  Adjust height to content; keep width 1520 unless the archetype says
  otherwise.
- First element is always the background rect filling the viewBox.
- Root `<svg>` carries `role="img"` and an `aria-label` that states the
  claim in one sentence.
- Outer margin 70px. Nothing but the background touches the edge.

## Header

- Title at y=72, subtitle at y=106, both starting at x=70.
- The subtitle states the claim in plain words. If the subtitle cannot
  state the claim, the scoping step failed; go back.

## Panels (cards)

- White rect, radius 18, drop shadow via `filter="url(#soft)"` on a
  wrapping `<g>`.
- No decorative bars: never mark a zone with a colored top border or edge
  strip on a card. The zone accent lives in the content instead: the header
  icon stroke, chip fills and borders, the zone's arrows, and its story
  strip dot.
- Panel header 30px in from the panel's left edge; header baseline about
  52px below the panel top. Pair the header with an icon from
  `design/icons.md`, stroked in the zone accent; the icon is the zone's
  primary color marker.
- The claim carrier may use a tinted card body (its accent's chip fill)
  instead of white; nothing else on a card gets a colored surface.
- Inner blocks (chips): tinted rect, radius 12, 1px border in the border
  tint, 20-30px inset from the panel edges, 16px vertical gap.

## Arrows

- Solid, stroke-width 2.5, accent colored, with a matching triangular
  marker, for primary flows (part of the claim).
- Dashed (`stroke-dasharray="6 4"`), stroke-width 2, for responses and
  secondary flows.
- Dashed faint gray (`stroke-dasharray="4 4"`, width 1.8) for background
  relationships.
- Use gentle cubic curves (`C`) between panels, never elbow connectors.
- Every arrow gets a short label above its midpoint in the arrow's color;
  an optional sublabel below in faint gray.
- Marker template (one per accent, id `arrow-<name>`):

```xml
<marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5"
        markerWidth="8" markerHeight="8" orient="auto-start-reverse">
  <path d="M0 0 L10 5 L0 10 z" fill="#4A6FF3"/>
</marker>
```

## Story strip

- Optional bottom strip of numbered takeaways: filled accent circle
  (r=14) with a white bold number, then one sentence in ink at 14px.
- One entry per zone, in the zone's accent, aligned under its zone.
- Below it, one optional footnote line in faint gray.

## Density

- 3 zones is the sweet spot; 4 is the maximum.
- 3-4 inner blocks per panel maximum.
- If content does not fit, cut content (back to the wireframe), never
  shrink the type scale.

Changed 2026-08-16: removed the accent top bar rule (read as generic AI
output); zone accent moved into content per the Panels section.
