---

description: "Task list for Sticky Section Navigation"
---

# Tasks: Sticky Section Navigation

**Input**: Design documents from `/specs/001-sticky-section-nav/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested (spec Assumptions: manual browser validation only). No automated TDD tasks.

**Organization**: Tasks grouped by user story. Product changes are in `index.html` only (single-file); `[P]` used only where work does not touch the same incomplete file dependency.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single document**: `index.html` at repository root
- Spec Kit docs: `specs/001-sticky-section-nav/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm Spec Kit context and open the only product file for edit

- [x] T001 Confirm active feature path in `.specify/feature.json` points to `specs/001-sticky-section-nav` and open `index.html` for implementation
- [x] T002 [P] Skim `specs/001-sticky-section-nav/plan.md`, `specs/001-sticky-section-nav/contracts/ui-contents.md`, and `specs/001-sticky-section-nav/quickstart.md` so layout/breakpoint (`1024px`) and “Contents” copy are clear before coding

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Unique section targets and a contents region that can replace the pill row — required before any user story UI works

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 In `index.html`, assign a unique non-empty `id` to every primary `<section>` that has an `h2` (fix duplicates such as repeated `b1` / `b4` / `b8` / `b11`); keep `id` stable and hash-safe per `specs/001-sticky-section-nav/data-model.md` (`LessonSection.id` required and unique)
- [x] T004 In `index.html`, restructure markup so the contents landmark (`#nav` or equivalent) sits in a dedicated contents region beside/above the reading column (lead + sections), ready for sticky desktop layout — without yet requiring scroll-spy or mobile disclosure behavior
- [x] T005 In `index.html` `<style>`, add layout/CSS using existing tokens (`--bg`, `--tx`, `--mut`, `--card`, `--bd`, `--ac`, `--say`, etc.) for the contents region and reading column; remove or neutralize the old top pill-row styling as the primary section navigator (FR-009 / contract C3)
- [x] T006 In `index.html` bottom `<script>`, update TOC generation so each contents link `href` is `#` + the section’s unique `id`, `label` derives from `h2` text (may shorten via existing `split(".")[0]`), and `fullTitle` / `title` attribute carries the full heading when shortened (`ContentsItem` rules in `data-model.md`)

**Checkpoint**: Foundation ready — every listed section has a unique id; contents links jump by hash; old pill row is not a competing primary nav

---

## Phase 3: User Story 1 - Jump to a lesson section (Priority: P1) 🎯 MVP

**Goal**: Reader can open contents and jump to any primary lesson section by title

**Independent Test**: At ≥1024px, choose a mid-list section from contents; heading appears near top of reading area; hash matches section id (quickstart Q1)

### Implementation for User Story 1

- [x] T007 [US1] In `index.html`, ensure the wide-layout contents list is a navigation/complementary landmark listing all primary sections in document order with clickable links (contract C1 / FR-001–002)
- [x] T008 [US1] In `index.html` CSS, make the wide (≥1024px) contents region `position: sticky` (or equivalent) so it remains available while scrolling without covering narration or code blocks (FR-004)
- [x] T009 [US1] In `index.html`, verify hash navigation from contents items scrolls the target section heading into view (account for any sticky offset / `scroll-padding-top` already on `html`)
- [x] T010 [US1] Manually validate User Story 1 via `specs/001-sticky-section-nav/quickstart.md` scenario Q1 and mark gaps if jump fails

**Checkpoint**: User Story 1 fully functional and testable independently (MVP)

---

## Phase 4: User Story 2 - Know where I am while reading (Priority: P2)

**Goal**: Contents marks the section currently in primary view while scrolling

**Independent Test**: Scroll across ≥3 consecutive sections; current mark tracks the dominant section (~9/10 informal checks); mark does not cover content (quickstart Q2)

### Implementation for User Story 2

- [x] T011 [US2] In `index.html` `<script>`, add `IntersectionObserver` on primary `section` elements with a root margin biased to the upper reading area; keep at most one contents item current (data-model current-section transitions)
- [x] T012 [US2] In `index.html`, set `aria-current="location"` on the current contents link and clear it from others; style current state with existing tokens (e.g. `--ac` / `--say`) without overlaying narration/code (FR-003, FR-006, contract C1)
- [x] T013 [US2] In `index.html` script, handle edge cases: near top → first section current; past last body → last section current (spec Edge Cases)
- [x] T014 [US2] Manually validate User Story 2 via `specs/001-sticky-section-nav/quickstart.md` scenario Q2

**Checkpoint**: User Stories 1 and 2 both work independently

---

## Phase 5: User Story 3 - Use contents on a phone-sized screen (Priority: P2)

**Goal**: On narrow viewports, same section list behind a compact “Contents” control; panel does not stick open after jump

**Independent Test**: ~390px width — no permanent wide sidebar; open Contents, jump mid-page, reading unobstructed within ~10s (quickstart Q3); keyboard Tab/Enter/Escape (Q4)

### Implementation for User Story 3

- [x] T015 [US3] In `index.html` CSS, below `1024px` hide the persistent sticky sidebar list and show a compact control whose accessible name includes “Contents” (English) (FR-005, contract C2)
- [x] T016 [US3] In `index.html` markup/script, implement open/close for the contents panel; default closed on load so the full list does not permanently consume most reading width
- [x] T017 [US3] In `index.html` script, close the panel on contents item activation, on Escape, and via an explicit dismiss control; restore focus to the Contents button on close (FR-008, research R5)
- [x] T018 [US3] Manually validate User Story 3 via `specs/001-sticky-section-nav/quickstart.md` scenarios Q3 and Q4

**Checkpoint**: All three user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Progressive enhancement, no duplicate nav, full quickstart pass

- [x] T019 In `index.html`, confirm primary lesson content (headings, narration, code) remains in HTML and readable with scripting disabled; unique section `id`s still support in-page `#` targets (FR-007, SC-004, quickstart Q6)
- [x] T020 In `index.html`, confirm no duplicate primary section navigator (old pills + new contents) in the default JS-on experience (FR-009, quickstart Q5)
- [x] T021 Run full `specs/001-sticky-section-nav/quickstart.md` scenarios Q1–Q6 and fix any remaining gaps in `index.html`
- [x] T022 [P] Update `specs/001-sticky-section-nav/tasks.md` checkboxes to reflect completed work after validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational — MVP
- **User Story 2 (Phase 4)**: Depends on Foundational; builds on US1 contents links in the same `index.html` (sequential on one file)
- **User Story 3 (Phase 5)**: Depends on Foundational; reuses same contents list as US1 (sequential on one file)
- **Polish (Phase 6)**: After desired stories complete

### User Story Dependencies

- **US1 (P1)**: After Phase 2 — no dependency on US2/US3
- **US2 (P2)**: After Phase 2 — needs US1 contents links present to mark current
- **US3 (P2)**: After Phase 2 — needs US1 contents list; ideally after US1 layout exists

### Within Each User Story

- No automated tests in this feature
- Markup/CSS before behavior where listed
- Manual quickstart check at end of each story phase

### Parallel Opportunities

- T002 can run in parallel with T001 (docs vs confirm path)
- T022 can run after implementation while browsing quickstart notes
- **Limited parallelism**: almost all product tasks edit `index.html` — execute **sequentially** T003→T021 for a single implementer
- Do not split US2/US3 across agents on the same file without coordination

---

## Parallel Example: User Story 1

```bash
# Single-file feature: run US1 tasks in order, not parallel agents:
Task: "T007 [US1] landmark contents list in index.html"
Task: "T008 [US1] sticky wide contents CSS in index.html"
Task: "T009 [US1] hash scroll / scroll-padding in index.html"
Task: "T010 [US1] quickstart Q1 validation"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (unique ids + contents shell)
3. Complete Phase 3: User Story 1 (jump + sticky list)
4. **STOP and VALIDATE**: quickstart Q1
5. Demo locally via `open index.html`

### Incremental Delivery

1. Setup + Foundational → hash-safe sections + contents shell
2. US1 → jump works (MVP)
3. US2 → scroll-spy current mark
4. US3 → mobile Contents disclosure
5. Polish → Q1–Q6 full pass

### Parallel Team Strategy

Not recommended for this feature (single `index.html`). One implementer sequential through phases.

---

## Notes

- Quote from data-model enforced in tasks: `LessonSection.id` required + unique; `ContentsItem` label may shorten with full title retained for accessibility
- Breakpoint locked at **1024px** per plan/research
- Learner-facing control copy: **Contents** (English)
- Commit after each phase checkpoint if desired (user must request commits explicitly in this repo’s agent rules)
