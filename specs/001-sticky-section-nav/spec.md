# Feature Specification: Sticky Section Navigation

**Feature Branch**: `001-sticky-section-nav`

**Created**: 2026-11-05

**Status**: Draft

**Input**: User description: "Change page navigation from the top pill link row to a sticky table of contents that highlights the current lesson section while reading; on narrow screens, expose the same contents behind a compact Contents control. Preserve readable content if enhancement fails. Reuse the page's existing look."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Jump to a lesson section (Priority: P1)

A reader opens the long course script page and wants to jump to a specific
lesson section (by its section title) without scrolling the whole document.

**Why this priority**: Jumping between sections is the core job of navigation;
without it the feature has no value.

**Independent Test**: Open the page, use the contents list, select a known
section title, and confirm the viewport lands on that section's heading.

**Acceptance Scenarios**:

1. **Given** the page lists multiple lesson sections, **When** the reader
   chooses a section title from the contents list, **Then** the page moves to
   that section so its heading is visible near the top of the reading area.
2. **Given** the reader is mid-page, **When** they choose another section from
   the contents list, **Then** they arrive at the newly chosen section without
   leaving the page.

---

### User Story 2 - Know where I am while reading (Priority: P2)

While scrolling through narration and code, the reader wants to see which
section they are currently in so they do not lose place in a long lesson.

**Why this priority**: Orientation while scrolling is the second major pain
after jumping; it completes the “reader-first” goal but is not required for
a minimal jump-only MVP.

**Independent Test**: Scroll so a middle section dominates the viewport and
confirm the contents list marks that section as current; scroll to another
section and confirm the marker moves.

**Acceptance Scenarios**:

1. **Given** the reader is viewing a section, **When** they scroll until the
   next section becomes the primary content in view, **Then** the contents
   list updates so the new section is marked as current and the previous one
   is not.
2. **Given** a section is marked current, **When** the reader looks at the
   contents list without interacting, **Then** the current mark remains
   visible without covering narration or code blocks.

---

### User Story 3 - Use contents on a phone-sized screen (Priority: P2)

On a narrow screen, the reader still needs the same section list, but a
persistent full list must not steal most of the reading width.

**Why this priority**: Many viewers read on phones; desktop-only contents
would fail constitution “mobile usable” rule. Equal priority to P2 orientation
because both complete the agreed UX; P1 jump can still ship if mobile uses a
compact access pattern to the same list.

**Independent Test**: At ~390px width, open Contents, pick a section, confirm
jump works, then dismiss or auto-close so reading space returns.

**Acceptance Scenarios**:

1. **Given** a narrow viewport, **When** the page loads, **Then** the full
   contents list is not permanently occupying most of the reading width.
2. **Given** a narrow viewport, **When** the reader activates the Contents
   control, **Then** they see the same section titles available on wide
   layouts and can jump to a section.
3. **Given** the contents panel is open on a narrow viewport, **When** the
   reader jumps to a section or dismisses the panel, **Then** the reading
   area is usable again without a stuck overlay.

---

### Edge Cases

- What happens when the page has only one section? Contents still lists it;
  jumping is a no-op that keeps that section in view; current mark stays on it.
- What happens when section titles are very long? Labels remain readable
  (wrap or truncate with the full title available to assistive tech / title
  affordance) without breaking the layout of the reading column.
- What happens when JavaScript enhancements fail? Lesson headings, narration,
  and code remain readable; in-page links to sections still work if present
  in the document.
- What happens at the very top or bottom of the page? Current-section marking
  still resolves to a sensible section (first when above all, last when past
  the final section body).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The page MUST present a contents list of all primary lesson
  sections, using each section’s title as the label.
- **FR-002**: Choosing an item in the contents list MUST move the reader to
  the corresponding section on the same page.
- **FR-003**: While the reader scrolls, the contents list MUST indicate which
  section is currently in primary view.
- **FR-004**: On wide layouts, the contents list MUST remain available while
  scrolling (sticky / persistent chrome) without covering narration or code.
- **FR-005**: On narrow layouts, the same contents MUST be reachable through a
  compact Contents control rather than a permanently wide side list.
- **FR-006**: The contents experience MUST visually match the existing page
  theme (including light and dark preference) and MUST NOT introduce a
  separate visual system.
- **FR-007**: Core lesson content MUST remain readable if navigation
  enhancements fail; section targets that exist in the page MUST remain
  reachable via normal in-page links.
- **FR-008**: Interactive contents controls MUST be operable with keyboard
  (focus, activate, and dismiss where a disclosure exists) and MUST have
  clear accessible names.
- **FR-009**: The feature MUST replace the current top-of-page pill link row
  as the primary section navigation; it MUST NOT leave two competing primary
  section navigations visible.

### Key Entities

- **Lesson section**: A primary content block on the course page with a
  distinct title; the unit listed in contents and used for “current” marking.
- **Contents item**: A labeled entry pointing to one lesson section; shown in
  the contents list on both wide and narrow layouts.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A reader can jump from any scroll position to a named section
  in under 5 seconds using only the contents UI (no manual scrolling hunt).
- **SC-002**: After scrolling across at least three consecutive sections, the
  “current” marker matches the section that occupies the majority of the
  reading viewport in at least 9 of 10 informal checks.
- **SC-003**: On a ~390px-wide viewport, a reader can open contents, jump to a
  mid-page section, and return to an unobstructed reading view within
  10 seconds.
- **SC-004**: With navigation scripting disabled, 100% of narration and code
  blocks remain visible and readable; existing in-page section links still
  reach their targets.
- **SC-005**: No primary duplicate section navigation (old pill row plus new
  contents) appears simultaneously for the default reading experience.

## Assumptions

- Primary lesson sections are the existing top-level section blocks already
  present on the course page (each with a clear title); nested step headings
  are out of scope for the contents list unless already treated as primary
  sections today.
- Learner-facing chrome copy stays in English (e.g., “Contents”).
- No search, progress persistence, bookmarks, or account-related navigation
  is in scope.
- Verification is manual in a browser at desktop (≥1024px) and narrow
  (~390px) widths, including a keyboard pass for new controls; automated TDD
  is out of scope for this change.
- The page remains a single static HTML document opened locally or via a
  simple static host.
