# Quickstart Validation: Top Promo Block

## Prerequisites

- Updated `index.html` after implementation
- Desktop browser; ability to set width ~390px
- DevTools: emulate `prefers-reduced-motion: reduce`

## Setup

```bash
cd /Users/pavel/work/COURSE/html_web_courses_en
open index.html
# or: python3 -m http.server 8080
```

## Scenarios

### Q1. Visible top promo (SC-001 / FR-001–002)

1. Load the page at ≥1024px without scrolling.
2. **Expect**: bright promo above the lesson title with Advanced-course message
   and code `PROMO_CODE_HERE` (same as Block 15).
3. Repeat at ~390px — still readable, no page-wide horizontal scroll.

### Q2. Brightness (SC-002 / FR-003)

1. Compare top promo to a nearby `.say` narration card.
2. **Expect**: promo reads clearly more emphatic / promotional.

### Q3. Animation on (SC-003 / FR-004)

1. Ensure reduced motion is off; reload.
2. **Expect**: perceptible animation within ~3 seconds of viewing the promo.

### Q4. Reduced motion (SC-004 / FR-005)

1. Enable `prefers-reduced-motion: reduce`; reload.
2. **Expect**: promo still bright and actionable; no continuous distracting
   motion.

### Q5. Navigation intact (SC-005 / FR-006)

1. Use sticky/Contents navigation to jump to a mid-page section.
2. Scroll through narration/code.
3. **Expect**: jump works; promo is not a sticky overlay covering content;
   TOC remains the primary section navigator.

### Q6. No-JS / static content (FR-008)

1. Disable JavaScript; reload.
2. **Expect**: promo message and code text still visible; lesson content
   readable.

## Related artifacts

- [spec.md](./spec.md)
- [data-model.md](./data-model.md)
- [contracts/ui-top-promo.md](./contracts/ui-top-promo.md)
