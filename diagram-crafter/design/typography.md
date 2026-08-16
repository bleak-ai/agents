# Typography

## Family

Set once on the root `<svg>` element:

```
font-family="-apple-system, 'SF Pro Text', 'Segoe UI', Helvetica, Arial, sans-serif"
```

## Scale

| Role | Size | Weight | Fill |
|------|------|--------|------|
| diagram title | 36 | 700 | ink |
| diagram subtitle | 18 | 400 | muted |
| panel header | 21 | 700 | ink |
| panel subheader | 14 | 400 | muted |
| item title (chip, block) | 15-16 | 600 | ink |
| item subtext | 13 | 400 | muted |
| arrow label | 13 | 400 | the arrow's accent |
| arrow sublabel | 12 | 400 | faint |
| chip / pill text | 12.5 | 400 | accent dark text |
| story strip text | 14 | 400 | ink |
| footnote | 13 | 400 (italic allowed) | faint |

## Rules

- Never more than two weights in one diagram (400 and 600/700).
- Sentence case everywhere. No all-caps labels.
- Every text element gets an explicit `font-size`; never rely on
  inheritance except for the family.
- Keep label lines short enough to fit their container at the given size;
  wrapping in SVG is manual, so prefer rewording over wrapping.
