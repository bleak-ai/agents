# Icons

Inline Lucide icons (ISC license, lucide.dev). Copy the needed defs into
the `<defs>` of the SVG. All are 24x24 stroke-based; color comes from the
`stroke` attribute at the `<use>` site, so one def serves every zone.

## Usage

```xml
<use href="#i-bot" transform="translate(122,300) scale(1.85)" stroke="#4A6FF3"/>
```

- Scale 1.6-1.9 for panel headers and chips.
- Stroke color is always the zone accent.
- Only include the defs the diagram actually uses.

## Library

```xml
<g id="i-bot" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/>
  <path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>
</g>
<g id="i-sparkles" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/>
  <path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/>
</g>
<g id="i-terminal" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>
</g>
<g id="i-server" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect width="20" height="8" x="2" y="2" rx="2" ry="2"/><rect width="20" height="8" x="2" y="14" rx="2" ry="2"/>
  <line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>
</g>
<g id="i-file" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"/>
  <path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>
</g>
<g id="i-plug" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 22v-5"/><path d="M15 8V2"/><path d="M9 8V2"/>
  <path d="M17 8a1 1 0 0 1 1 1v4a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1z"/>
</g>
<g id="i-folder" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>
</g>
<g id="i-lock" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
</g>
```

## Adding icons

Take the path data from lucide.dev, wrap it in
`<g id="i-<name>" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">`,
and append it to the library above with a one-line note of when to use it.
