# Palette

Warm paper background, dark blue ink, three accents. Neutral and general
purpose; no product branding.

## Base

| Role | Value | Use |
|------|-------|-----|
| background | `#FAF8F3` | full-canvas rect, always first element |
| card | `#FFFFFF` | panel bodies |
| ink | `#1F2A44` | titles, labels, primary text |
| muted | `#6B7385` | subtitles, secondary text |
| faint | `#8A90A0` | footnotes, de-emphasized arrows and captions |

## Accents

| Role | Blue | Orange | Green |
|------|------|--------|-------|
| accent (arrows, arrow labels, icon strokes, strip dots) | `#4A6FF3` | `#E8963C` | `#2FA45C` |
| dark text (labels needing more contrast, on white or tint) | `#3A55BE` | `#C77E28` | `#20794A` |
| pill text (only inside pill fills) | use dark text | `#7A4A12` | use dark text |
| chip fill (inner blocks, 60px+ tall) | `#EEF3FE` | `#FDF6EC` | `#EFF9F2` |
| pill fill (small tags and pills, under 40px tall) | use chip fill | `#FDF1E1` | use chip fill |
| special-shape tint (cut shapes like a folder tab) | use chip fill | use chip fill | `#DFF3E6` |
| chip border | `#D4DFFB` | `#F3E0C4` | `#CFEBD9` |

One value per role. When a role says "use chip fill" or "use dark text", that accent has no separate value for the role; reuse the named one.

## Assignment rules

1. One accent per zone. A zone is a panel or a group of related elements.
   Everything inside a zone (header icon stroke, chips, its outgoing
   arrows and arrow labels, its story strip dot) uses that zone's accent.
   Never as a colored top border or edge strip on a card; see layout.md.
2. One hue is reserved for the element that carries the claim. Pick it at
   draft time and do not use it for anything decorative.
3. Order of assignment when reading left to right or top to bottom:
   blue, orange, green. Do not shuffle without a reason.
4. `faint` gray is for relationships that are secondary to the claim
   (dashed, thinner stroke).
5. Never introduce a fourth accent. If the composition seems to need one,
   the composition has too many zones; go back to the wireframe.

## Shadow

One reusable filter, applied to panel rects only, never to text or chips:

```xml
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#1F2A44" flood-opacity="0.10"/>
</filter>
```

Changed 2026-08-16: accent role no longer includes bars; colored top or
edge bars on cards are banned.
