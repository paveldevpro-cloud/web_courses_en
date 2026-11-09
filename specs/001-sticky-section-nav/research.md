# Research: Sticky Section Navigation

## R1. Layout pattern (desktop sticky TOC + mobile disclosure)

**Decision**: Use a page shell with a reading column and a contents region.
At `min-width: 1024px`, the contents region is a left sticky sidebar.
Below that breakpoint, hide the persistent sidebar and expose the same
list via a “Contents” disclosure control (button + panel, or native
`<details>` styled to match tokens).

**Rationale**: Matches FR-004/FR-005 and constitution II without a second
nav system. Sticky `position: sticky` on the sidebar keeps chrome in view
while scrolling `main` content. Narrow layouts reclaim width for narration.

**Alternatives considered**:
- Top horizontal scroll chips — keeps current density problems; fails
  “where am I” orientation.
- Right-side TOC — common for docs, but left matches reading start and
  avoids colliding with code “Copy” controls on the right.
- Always-visible compact select (`<select>`) — weaker scanning of many
  section titles; worse for SC-002 current marking.

## R2. Building the contents list

**Decision**: Keep generating contents items from `document.querySelectorAll("section")`
+ first `h2` text (same data source as today), but fix section `id`s so each
target is unique before wiring `href="#id"`. Truncate visible labels as today
(`textContent.split(".")[0]`) while keeping the full title on `title` /
accessible name where truncated.

**Rationale**: Constitution V prefers editing existing nav generation.
Duplicate ids already exist in `index.html` (several `b1`, `b4`, …); hash
navigation and FR-002 cannot work reliably until ids are unique.

**Alternatives considered**:
- Hand-maintained TOC in HTML — drifts from sections; higher maintenance.
- Include `h3.step` headings — out of scope per spec assumptions (primary
  sections only).

## R3. Current-section highlighting

**Decision**: Use `IntersectionObserver` on each primary `section`, with a
root margin biased toward the upper reading area, and mark the matching
contents link with an `aria-current="location"` (and a CSS class using
existing `--ac` / `--say` tokens).

**Rationale**: Efficient, standard for TOC spy behavior; meets FR-003 /
SC-002 without scroll-event thrashing. `aria-current` supports FR-008.

**Alternatives considered**:
- Scroll position math on `scroll` — more code, harder to get right.
- `:target` only — updates on click, not while scrolling.

## R4. Progressive enhancement

**Decision**: Keep TOC population and scroll-spy in the existing bottom
`<script>`. Ensure every primary section has a unique `id` in markup so
any in-page `#` links work with JS disabled. Content (h1, narration, code)
stays in HTML and remains readable if the script fails. Do not gate
content rendering on JS.

**Rationale**: Satisfies constitution III and SC-004 without a build step
or second file. Empty TOC when JS fails is acceptable; blank page is not.

**Alternatives considered**:
- Fully static TOC in HTML — better PE, but duplicates titles and fights
  “smallest change”; deferred unless converge demands it.
- Separate `nav.js` — violates single-file preference (constitution I).

## R5. Mobile panel behavior

**Decision**: “Contents” control toggles a panel over/near the top of the
reading area; choosing a link closes the panel; Escape and a visible close
control also dismiss; restore focus to the Contents button on close.

**Rationale**: FR-005, FR-008, SC-003. Prevents stuck overlays (edge case).

**Alternatives considered**:
- Bottom sheet only — more motion/CSS; unnecessary for first ship.
- Navigate without auto-close — leaves reading obstructed on phones.

## R6. Testing approach

**Decision**: Manual browser validation per `quickstart.md` (desktop ≥1024px,
~390px, keyboard, JS-disabled spot check). No automated TDD harness.

**Rationale**: Spec assumptions and constitution workflow; HTML-only repo
has no test runner.

**Alternatives considered**:
- Playwright — useful later, out of scope for this change.
