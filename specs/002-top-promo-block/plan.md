# Implementation Plan: Top Promo Block

**Branch**: `002-top-promo-block` | **Date**: 2026-11-06 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-top-promo-block/spec.md`

## Summary

Add a full-width, non-sticky, accent-bright Advanced-course promo banner at
the top of `index.html` (above `.page` / lesson title), with CSS entrance +
subtle loop animation gated by `prefers-reduced-motion`, English copy, and
promo code `PROMO_CODE_HERE` matching Block 15 plus a Copy control. Preserve
sticky TOC and lesson readability.

## Technical Context

**Language/Version**: HTML5 + CSS3 (+ existing vanilla JS copy pattern)

**Primary Dependencies**: None (no npm/build; CSS `@keyframes` only)

**Storage**: N/A

**Testing**: Manual browser validation (`quickstart.md`)

**Target Platform**: Modern browsers; static `index.html`

**Project Type**: Single-page static teaching document

**Performance Goals**: Lightweight CSS animation; no layout thrash on scroll

**Constraints**: Single file; existing CSS tokens; English chrome; non-sticky
promo; same promo code as Block 15; must not replace TOC; reduced-motion safe

**Scale/Scope**: One banner region in `index.html`; ~10–20 lines markup + CSS

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Single-File Clarity | PASS | Changes only in `index.html` |
| II. Reader-First Navigation | PASS | TOC untouched as primary nav; promo not a section nav |
| III. Progressive Enhancement | PASS | Markup present; motion is CSS enhancement |
| IV. Visual Continuity | PASS | Stronger `--ac` / `--say` usage, no new palette |
| V. Smallest Useful Change | PASS | One banner; shared code string; no dismiss/state |
| Delivery: unique section ids | PASS | Promo is not a lesson section; ids unchanged |
| Workflow: desktop + narrow + keyboard | PASS | In quickstart; Copy control focusable |

**Gate result**: PASS

### Post–Phase 1 re-check

Design keeps promo outside sticky TOC and non-sticky. PASS unchanged.

## Project Structure

### Documentation (this feature)

```text
specs/002-top-promo-block/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── ui-top-promo.md
└── tasks.md             # /speckit-tasks (later)
```

### Source Code (repository root)

```text
index.html               # Sole product file
```

**Structure Decision**: Extend existing single-document page; insert promo
above `.page`; add CSS (+ wire Copy like existing `.cb` buttons).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| — | — | — |

## Phase 0 & 1 Outputs

| Artifact | Path |
|----------|------|
| Research | [research.md](./research.md) |
| Data model | [data-model.md](./data-model.md) |
| UI contract | [contracts/ui-top-promo.md](./contracts/ui-top-promo.md) |
| Quickstart | [quickstart.md](./quickstart.md) |

## Implementation Approach (for `/speckit-tasks`)

1. Markup: top promo region above `.page` with headline, body, code, Copy
   button (English; code = Block 15).
2. CSS: bright accent styling; `@keyframes` entrance + subtle pulse; disable
   under `prefers-reduced-motion: reduce`; responsive wrapping.
3. JS: attach Copy behavior for the promo code control (reuse pattern).
4. Validate: `quickstart.md` Q1–Q6 including TOC regression.
