# Implementation Plan: Sticky Section Navigation

**Branch**: `001-sticky-section-nav` | **Date**: 2026-11-05 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-sticky-section-nav/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command; its definition describes the execution workflow.

## Summary

Replace the top pill-link row with a sticky table of contents that lists
primary lesson sections, highlights the section in view while scrolling, and
on narrow viewports hides behind a “Contents” control. Implement entirely
inside `index.html` (CSS layout + enhance existing nav script): unique
section ids, sticky sidebar ≥1024px, IntersectionObserver scroll-spy,
accessible mobile disclosure. Manual browser checks per `quickstart.md`.

## Technical Context

**Language/Version**: HTML5 + CSS3 + vanilla JavaScript (ES2019+ APIs:
`IntersectionObserver`, `querySelectorAll`) as already used in `index.html`

**Primary Dependencies**: None (no npm/build). Browser built-ins only.

**Storage**: N/A (no persistence)

**Testing**: Manual browser validation (`quickstart.md`); no automated suite

**Target Platform**: Modern desktop and mobile browsers; static file open or
simple static HTTP host

**Project Type**: Single-page static teaching document

**Performance Goals**: Scroll-spy updates without visible jank on a ~15-section
page; TOC build negligible on load

**Constraints**: Single-file deliverable; reuse CSS variables; progressive
enhancement (content readable if script fails); English chrome (“Contents”);
no second design system; no search/bookmarks/progress sync

**Scale/Scope**: One file (`index.html`); ~15 primary sections; one nav
surface (wide + narrow variants)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Single-File Clarity | PASS | All changes in `index.html` only |
| II. Reader-First Navigation | PASS | Sticky TOC + current mark; mobile Contents |
| III. Progressive Enhancement | PASS | Content in HTML; unique ids for hashes; TOC/spy via script |
| IV. Visual Continuity | PASS | Plan reuses `--*` tokens / existing type |
| V. Smallest Useful Change | PASS | Extend existing `#nav` generation; no new systems |
| Delivery: no npm pipeline | PASS | None introduced |
| Workflow: desktop + narrow + keyboard | PASS | Captured in `quickstart.md` |

**Gate result**: PASS (no unjustified violations). Complexity table empty.

### Post–Phase 1 re-check

Design artifacts (`research.md`, `data-model.md`, `contracts/ui-contents.md`,
`quickstart.md`) remain inside Spec Kit docs only; runtime still single-file.
PASS unchanged.

## Project Structure

### Documentation (this feature)

```text
specs/001-sticky-section-nav/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── ui-contents.md   # Phase 1 UI contract
└── tasks.md             # Phase 2 output (/speckit-tasks — not created here)
```

### Source Code (repository root)

```text
index.html               # Sole product file: markup, CSS, nav + copy scripts
```

**Structure Decision**: Keep the existing single-document layout. Do not add
`src/`, packages, or a build. Spec Kit artifacts live under
`specs/001-sticky-section-nav/` only.

## Complexity Tracking

> No constitution violations requiring justification.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| — | — | — |

## Phase 0 & 1 Outputs

| Artifact | Path |
|----------|------|
| Research | [research.md](./research.md) |
| Data model | [data-model.md](./data-model.md) |
| UI contract | [contracts/ui-contents.md](./contracts/ui-contents.md) |
| Quickstart | [quickstart.md](./quickstart.md) |

## Implementation Approach (for `/speckit-tasks`)

1. **Markup/CSS shell**: Restructure so lead + reading column and contents
   region coexist; sticky sidebar ≥1024px; narrow Contents control styles
   using existing tokens; remove visual role of old pill row as primary nav.
2. **Unique section ids**: Assign distinct `id`s to every primary
   `<section>` (fix current duplicates) so `#` targets are unambiguous.
3. **TOC script**: Rebuild `#nav` (or equivalent landmark) from sections +
   `h2`; wire hrefs; set `title`/accessible labels for truncated text.
4. **Scroll-spy**: `IntersectionObserver` + `aria-current="location"`.
5. **Mobile disclosure**: open/close, Escape, close on navigate, focus return.
6. **Validate**: Run `quickstart.md` scenarios Q1–Q6.
