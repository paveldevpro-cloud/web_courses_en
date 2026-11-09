# Feature Specification: Top Promo Block

**Feature Branch**: `002-top-promo-block`

**Created**: 2026-11-06

**Status**: Draft

**Input**: User description: "Добавить promoblock в верху страницы, яркий с анимацией" — Add a bright, animated promo block at the top of the page.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Notice the promo at page open (Priority: P1)

A reader opens the course script page and immediately sees a bright promo
block at the top that draws attention to the Advanced course offer without
hiding the lesson title or the section contents navigation.

**Why this priority**: Without a visible top promo, the feature has no value;
placement at the top is the requested outcome.

**Independent Test**: Open the page at a typical reading width and confirm a
distinct promo region appears above the main lesson title area, with readable
offer text and a clear call to action.

**Acceptance Scenarios**:

1. **Given** the reader loads the page, **When** the first viewport settles,
   **Then** a promo block is visible at the top of the page before they scroll
   deep into the lesson.
2. **Given** the promo is visible, **When** the reader looks at it, **Then**
   they can understand what is offered and what action to take (for example,
   copy a promo code or follow the stated next step) without opening another
   document first.

---

### User Story 2 - Feel a bright animated emphasis (Priority: P2)

The promo should feel vivid and animated so it stands out from ordinary
narration cards, while remaining readable and not causing motion sickness for
readers who prefer reduced motion.

**Why this priority**: “Bright with animation” is an explicit request, but a
static bright block would still deliver P1 value; motion is the enhancement.

**Independent Test**: With motion allowed, observe a clear animated emphasis
on load or while the block is in view; with reduced-motion preference on,
confirm the promo remains bright and usable without distracting continuous
motion.

**Acceptance Scenarios**:

1. **Given** the reader has no reduced-motion preference, **When** they view
   the top promo, **Then** they perceive a noticeable animation (entrance
   and/or subtle ongoing emphasis) that makes the block feel more vivid than
   a static narration card.
2. **Given** the reader prefers reduced motion, **When** they view the top
   promo, **Then** the block remains clearly visible and usable, and motion
   is minimized or replaced with a non-animated emphasis.

---

### User Story 3 - Keep reading and navigating the lesson (Priority: P2)

After noticing the promo, the reader can still use the sticky section
contents and read narration/code without the promo permanently covering the
lesson or replacing primary section navigation.

**Why this priority**: Constitution requires reader-first navigation and no
competing primary section navigators; the promo must not break that.

**Independent Test**: Confirm contents navigation still works; promo does not
obscure code Copy controls or the sticky contents while scrolling the lesson.

**Acceptance Scenarios**:

1. **Given** the page includes the top promo, **When** the reader uses the
   section contents control/list, **Then** they can still jump between lesson
   sections as before.
2. **Given** the reader scrolls through the lesson, **When** they read
   narration and code, **Then** the promo does not sit as a second sticky
   layer that covers those blocks.

---

### Edge Cases

- What if the viewport is very narrow (~390px)? The promo remains readable,
  wraps cleanly, and does not force horizontal scrolling of the whole page.
- What if animation scripting or CSS motion fails? The promo content (message
  and action) remains visible in a bright static form.
- What if the same Advanced-course offer already appears at the bottom of the
  page? The top promo may repeat that offer; it MUST NOT invent a conflicting
  promo code or contradictory claim.
- What if the reader has already scrolled past the top? Returning to the top
  (browser top / hash to page start) shows the promo again; no account-based
  “seen” state is required for v1.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The page MUST show a dedicated promo block at the top of the
  page (above the main lesson title).
- **FR-002**: The promo block MUST present a clear Advanced-course promotional
  message and a concrete learner action consistent with the existing end-of-
  page promo offer (same offer family; no conflicting code or claim).
- **FR-003**: The promo block MUST appear visually brighter / higher emphasis
  than ordinary narration cards so it reads as promotional chrome.
- **FR-004**: The promo block MUST include animation when the reader has not
  requested reduced motion.
- **FR-005**: When the reader prefers reduced motion, the promo MUST remain
  usable and bright with motion minimized or disabled.
- **FR-006**: The promo MUST NOT replace or duplicate the primary sticky
  section contents navigation, and MUST NOT cover narration or code while the
  reader scrolls the lesson body.
- **FR-007**: Promo learner-facing copy MUST be in English.
- **FR-008**: Core lesson content MUST remain readable if promo animation
  fails; the promo message itself MUST still be present in the page content.

### Key Entities

- **Top promo block**: The top-of-page promotional region with message, visual
  emphasis, optional motion, and a learner action.
- **Promo offer**: The Advanced-course offer (message + action) aligned with
  the existing bottom promo on the same page.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On first load at desktop and ~390px widths, a new reader can
  locate the top promo and state the offer within 5 seconds without scrolling
  past the first screen of content.
- **SC-002**: At least 9 of 10 informal observers describe the top promo as
  “brighter” or “more attention-grabbing” than a standard narration card on
  the same page.
- **SC-003**: With motion allowed, 100% of quick checks show a perceptible
  animated emphasis on the promo within the first 3 seconds of viewing it.
- **SC-004**: With reduced-motion preference enabled, the promo remains fully
  readable and actionable with no continuous distracting motion.
- **SC-005**: After adding the promo, section jump via contents still succeeds
  for a mid-page section in under 5 seconds (same as prior navigation success).

## Assumptions

- The promo promotes the same Advanced course / coupon family already shown in
  the final lesson promo section; exact wording may be shortened for a banner.
- v1 is not dismissible and does not persist “closed” state across visits.
- Animation may be CSS-driven; no new build tooling or external animation
  libraries.
- Visual design reuses the page’s existing color tokens, with stronger use of
  the accent for “bright,” rather than introducing a separate brand palette.
- Verification is manual in a browser (desktop ≥1024px and ~390px), including a
  reduced-motion check; automated TDD is out of scope.
- The page remains a single static HTML document.
