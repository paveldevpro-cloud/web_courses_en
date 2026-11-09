# UI Contract: Course Page Contents

Audience: implementers of `index.html` navigation chrome.

## Surfaces

### C1. Contents list (wide ≥1024px)

- **Role**: complementary / navigation landmark for primary lesson sections.
- **Items**: one link per `LessonSection` (see `data-model.md`), document order.
- **Behavior**: activating a link moves focus of reading to that section
  (hash navigation); does not open a new document.
- **Persistence**: remains visible while the reader scrolls the lesson
  (sticky region); must not overlay narration or code blocks in the reading
  column.
- **Current item**: exactly one item may be marked current while scroll-spy
  is active; expose via `aria-current="location"` on the current link.

### C2. Contents disclosure (narrow <1024px)

- **Control name**: accessible name MUST include “Contents” (English).
- **Closed default**: full list MUST NOT permanently consume most of the
  reading width.
- **Open**: reveals the same items/labels/targets as C1.
- **Close**: on item activation, Escape, and an explicit dismiss affordance;
  focus returns to the Contents control.

### C3. Replacement of legacy chrome

- The previous top-of-page pill row MUST NOT appear as a second primary
  section navigator alongside C1/C2.

## Tokens / theming

- Use existing page CSS variables (`--bg`, `--tx`, `--mut`, `--card`, `--bd`,
  `--ac`, `--say`, etc.).
- Honor `prefers-color-scheme` the same way as the rest of the page.

## Non-goals (contract exclusions)

- Search, filter, progress %, remote sync.
- Nested step (`h3.step`) entries in the contents list.
