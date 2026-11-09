# Research: Top Promo Block

## R1. Placement in the page shell

**Decision**: Insert a full-width promo region as the first visible chrome
above the existing `.page` grid (TOC + main), still inside `body`, so it sits
above the lesson `<h1>` and does not live inside the sticky TOC column.

**Rationale**: FR-001 requires top-of-page above the main title; FR-006 forbids
covering lesson content or replacing TOC. A non-sticky banner above `.page`
scrolls away with the document.

**Alternatives considered**:
- Inside `main.content` above `<h1>` — works on mobile, but on desktop leaves
  empty space beside TOC above the title only; full-width above `.page` is
  more “banner-like.”
- `position: sticky` top bar — rejects FR-006 (would cover content while
  scrolling).

## R2. Offer content and CTA

**Decision**: Reuse the Advanced-course offer family from Block 15: short
English headline + one-line supporting text + visible promo code
`PROMO_CODE_HERE` with a Copy control (same code string as the bottom block).

**Rationale**: FR-002 / edge case forbid conflicting codes; constitution
English copy; smallest change vs inventing new marketing copy.

**Alternatives considered**:
- Link-only CTA without code — weaker match to bottom promo action.
- Different code in the top banner — violates spec consistency rule.

## R3. “Bright” visual emphasis

**Decision**: Style with stronger accent usage (`--ac`, `--say`), higher
contrast border/background than `.say` cards, slightly larger type for the
headline; stay on existing CSS variables (constitution IV).

**Rationale**: Spec assumes token reuse with stronger accent; no second
palette.

**Alternatives considered**:
- Neon gradients outside tokens — fights Visual Continuity.
- Identical `.say` styling — fails SC-002 brightness bar.

## R4. Animation approach

**Decision**: Pure CSS: short entrance (`@keyframes` opacity/transform) plus a
subtle looping emphasis (e.g. soft border/glow pulse) under
`@media (prefers-reduced-motion: no-preference)`. Under
`prefers-reduced-motion: reduce`, disable loops and entrance motion; keep
static bright styles.

**Rationale**: FR-004/005, single-file, no animation libraries (assumptions).

**Alternatives considered**:
- JS-driven animation — unnecessary for this effect.
- Infinite high-amplitude bounce — poor a11y / distracting.

## R5. Progressive enhancement

**Decision**: Promo markup (message, code, button shell) is in HTML/CSS.
Animation is CSS-only enhancement. Copy button may reuse the existing
script pattern; without JS, code text remains selectable/visible.

**Rationale**: FR-008 and constitution III.

## R6. Testing

**Decision**: Manual quickstart checks at ≥1024px and ~390px, plus DevTools
emulation of `prefers-reduced-motion: reduce`, plus one contents jump
regression check.

**Rationale**: Spec assumptions; no TDD harness.
