# Quickstart Validation: Sticky Section Navigation

## Prerequisites

- Repo checkout with updated `index.html` after implementation
- Desktop browser (Chrome, Safari, or Firefox)
- Ability to resize the window / use responsive mode (~390px width)
- Optional: disable JavaScript once for SC-004 check

## Setup

```bash
cd /Users/pavel/work/COURSE/html_web_courses_en
open index.html
# or: python3 -m http.server 8080  →  http://localhost:8080/index.html
```

## Scenarios

### Q1. Jump to a section (SC-001 / FR-001–002)

1. Open the page at width ≥1024px.
2. From the sticky contents, choose a mid-list section (e.g. a “Block N” title).
3. **Expect**: that section’s heading is visible near the top of the reading
   column within a few seconds; URL hash matches the section id.

### Q2. Current section while scrolling (SC-002 / FR-003)

1. At ≥1024px, slowly scroll through at least three consecutive sections.
2. **Expect**: the contents “current” mark tracks the section that dominates
   the reading viewport (spot-check ~10 transitions; ≥9 should feel correct).
3. **Expect**: the mark does not cover narration or code.

### Q3. Narrow Contents panel (SC-003 / FR-005)

1. Set viewport width ≈390px.
2. **Expect**: no permanent wide sidebar eating most of the width.
3. Open “Contents”, pick a mid-page section.
4. **Expect**: jump succeeds; panel closes (or reading is unobstructed);
   finish within ~10 seconds.

### Q4. Keyboard (FR-008)

1. Tab to Contents control (narrow) or into contents links (wide).
2. Activate with Enter/Space as appropriate; Escape closes the narrow panel.
3. **Expect**: focus moves predictably; control has a clear accessible name.

### Q5. No duplicate primary nav (SC-005 / FR-009)

1. Default reading view (JS on).
2. **Expect**: only the new contents pattern — no parallel pill row of the
   same section links.

### Q6. JS disabled (SC-004 / FR-007)

1. Disable JavaScript and reload.
2. **Expect**: narration and code still readable.
3. If any in-page `#section-id` links exist in markup, following them still
   lands on the matching unique section id.

## Related artifacts

- Requirements: [spec.md](./spec.md)
- Model: [data-model.md](./data-model.md)
- UI contract: [contracts/ui-contents.md](./contracts/ui-contents.md)
