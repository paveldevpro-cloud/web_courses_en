---

description: "Task list for Top Promo Block"
---

# Tasks: Top Promo Block

**Input**: Design documents from `/specs/002-top-promo-block/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested (manual browser validation only). No automated TDD tasks.

**Organization**: Tasks grouped by user story. Product changes are in `index.html` only; `[P]` only where work does not conflict on the same incomplete edit.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single document**: `index.html` at repository root
- Spec Kit docs: `specs/002-top-promo-block/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm feature context before editing product HTML

- [x] T001 Confirm `.specify/feature.json` points to `specs/002-top-promo-block` and open `index.html` for implementation
- [x] T002 [P] Skim `specs/002-top-promo-block/plan.md`, `specs/002-top-promo-block/contracts/ui-top-promo.md`, and `specs/002-top-promo-block/quickstart.md` (placement above `.page`, code `PROMO_CODE_HERE`, reduced-motion rules)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Markup shell and shared offer fields required before polish/animation stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 In `index.html`, insert a top promo region as the first major chrome above `.page` (placement `page-top` per `data-model.md`; above lesson `<h1>`; NOT inside sticky TOC)
- [x] T004 In `index.html`, fill the promo with English `headline`, `body`, visible `code` that MUST equal the Block 15 string `PROMO_CODE_HERE`, and an English Copy `actionLabel` control (`PromoOffer` / `TopPromoBlock` required fields)
- [x] T005 In `index.html`, ensure the promo is not sticky (`sticky` MUST be `false`) and is not marked as a competing lesson-section navigator alongside `#nav`

**Checkpoint**: Foundation ready — promo markup present above title with matching code

---

## Phase 3: User Story 1 - Notice the promo at page open (Priority: P1) 🎯 MVP

**Goal**: Reader immediately sees a clear Advanced-course promo with actionable code at the top

**Independent Test**: Load page without deep scroll; promo above title shows offer + code; Copy works (quickstart Q1)

### Implementation for User Story 1

- [x] T006 [US1] In `index.html` `<style>`, style `.promo-top` (or chosen class) brighter than `.say` cards using existing tokens (`--ac`, `--say`, `--card`, `--bd`, `--tx`) per FR-003 / contract P1
- [x] T007 [US1] In `index.html` CSS, make the promo wrap cleanly at ~390px without page-wide horizontal scroll
- [x] T008 [US1] In `index.html` `<script>`, wire the promo Copy button to copy `PROMO_CODE_HERE` using the same clipboard pattern as `.cb` Copy buttons
- [x] T009 [US1] Manually validate User Story 1 via `specs/002-top-promo-block/quickstart.md` scenario Q1 (and brightness spot-check Q2)

**Checkpoint**: User Story 1 fully functional (MVP)

---

## Phase 4: User Story 2 - Feel a bright animated emphasis (Priority: P2)

**Goal**: Noticeable CSS animation when motion is allowed; static bright when reduced motion is preferred

**Independent Test**: Motion on → perceptible animation within ~3s; reduced-motion → no continuous distraction (quickstart Q3–Q4)

### Implementation for User Story 2

- [x] T010 [US2] In `index.html` CSS, add entrance `@keyframes` and a subtle looping emphasis for the promo under `@media (prefers-reduced-motion: no-preference)` so `motionMode` is `animated`
- [x] T011 [US2] In `index.html` CSS, under `@media (prefers-reduced-motion: reduce)`, disable entrance/loop motion and keep static bright styles (`motionMode` `static-bright`)
- [x] T012 [US2] Manually validate User Story 2 via `specs/002-top-promo-block/quickstart.md` scenarios Q3 and Q4

**Checkpoint**: US1 + US2 both work

---

## Phase 5: User Story 3 - Keep reading and navigating the lesson (Priority: P2)

**Goal**: Promo does not break sticky TOC or cover lesson content while scrolling

**Independent Test**: Jump via contents to mid-page; scroll narration/code; promo not sticky overlay (quickstart Q5)

### Implementation for User Story 3

- [x] T013 [US3] In `index.html`, verify TOC markup/script (`#nav` / Contents) remains the sole primary section navigator and promo has no competing section-nav role (FR-006)
- [x] T014 [US3] In `index.html` CSS, confirm promo uses normal document flow (no `position: sticky`/`fixed` that covers `.say` or code while scrolling the lesson body)
- [x] T015 [US3] Manually validate User Story 3 via `specs/002-top-promo-block/quickstart.md` scenario Q5

**Checkpoint**: All three user stories independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Progressive enhancement and full quickstart pass

- [x] T016 In `index.html`, confirm promo message and code remain in HTML if animation/JS fail; lesson content still readable (FR-008, quickstart Q6)
- [x] T017 Run full `specs/002-top-promo-block/quickstart.md` scenarios Q1–Q6 and fix remaining gaps in `index.html`
- [x] T018 [P] Update `specs/002-top-promo-block/tasks.md` checkboxes after validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Start immediately
- **Foundational (Phase 2)**: Depends on Setup — **BLOCKS** all user stories
- **US1 (Phase 3)**: Depends on Foundational — MVP
- **US2 (Phase 4)**: Depends on Foundational; needs US1 bright base styles
- **US3 (Phase 5)**: Depends on Foundational; regression after US1 placement
- **Polish (Phase 6)**: After desired stories

### User Story Dependencies

- **US1 (P1)**: After Phase 2
- **US2 (P2)**: After US1 styling exists (same `index.html`, sequential)
- **US3 (P2)**: After promo is in the shell (can follow US1; sequential on one file)

### Parallel Opportunities

- T002 parallel with T001
- T018 after implementation
- All other product tasks sequential on `index.html`

---

## Parallel Example: User Story 1

```bash
# Single-file: run in order
Task: "T006 [US1] bright promo CSS in index.html"
Task: "T007 [US1] narrow wrap CSS in index.html"
Task: "T008 [US1] Copy wiring in index.html"
Task: "T009 [US1] quickstart Q1/Q2"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Setup + Foundational (markup + shared code)
2. US1 bright styles + Copy
3. **STOP** — validate Q1/Q2

### Incremental Delivery

1. Foundation → visible top promo
2. US1 → bright + actionable
3. US2 → animation + reduced-motion
4. US3 → TOC/scroll regression
5. Polish → Q1–Q6

### Parallel Team Strategy

Not recommended (single `index.html`).

---

## Notes

- Quote constraints: `code` MUST equal Block 15 `PROMO_CODE_HERE`; `sticky` MUST be `false`; English copy required
- No dismiss/persistence in v1
