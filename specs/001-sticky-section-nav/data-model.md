# Data Model: Sticky Section Navigation

In-page conceptual model only (no persistence).

## Entities

### LessonSection

| Field | Type | Rules |
|-------|------|--------|
| `id` | string | Required; unique among all primary sections on the page; used as hash target |
| `title` | string | Required; taken from the section’s primary heading (`h2`), or a stable fallback if a section has no `h2` (such sections are omitted from contents, matching current behavior) |
| `element` | DOM section | The `<section>` node in document order |

**Validation**:
- Every contents-listed section MUST have a unique non-empty `id`.
- Sections without `h2` are not contents entities (skipped).

**Identity**: Document order among `section` elements that have an `h2`.

### ContentsItem

| Field | Type | Rules |
|-------|------|--------|
| `label` | string | Display label derived from `title` (may be shortened for chrome) |
| `fullTitle` | string | Full section title for tooltip / accessibility when shortened |
| `targetId` | string | Equals related `LessonSection.id` |
| `href` | string | `#` + `targetId` |
| `isCurrent` | boolean | At most one item `true` at a time while scroll-spy runs |

**Relationships**:
- Each `ContentsItem` points to exactly one `LessonSection`.
- The contents list is an ordered collection mirroring section document order.

## State Transitions

### Current section (`isCurrent`)

```text
[none / first] --observer sees section A primary--> A current
A current --observer sees section B primary--> B current (A cleared)
(near top) --> first section current
(past last body) --> last section current
```

### Mobile contents panel

```text
closed --activate Contents--> open
open --choose item | Escape | close control--> closed
```

No server-side state; reload resets panel to closed and recomputes current
section from scroll position after script runs.
