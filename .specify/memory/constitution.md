<!--
Sync Impact Report
- Version change: 1.0.0 → 1.1.0
- Modified principles:
  - II. Reader-First Navigation → same title; now requires sticky TOC as the
    primary section navigator (desktop sticky / narrow Contents disclosure)
  - V. Smallest Useful Change → same title; forbids a second competing primary
    section navigation alongside the TOC
- Added sections: none (Delivery Constraints + Development Workflow expanded)
- Removed sections: none
- Deferred TODOs: none
-->
# HTML Web Courses Constitution

## Core Principles

### I. Single-File Clarity
The course page ships as a self-contained HTML document readers can open
locally. Features MUST prefer in-file HTML/CSS/JS over new build steps,
frameworks, or package managers unless the change cannot be done otherwise.
Rationale: the artifact is a teaching script, not an app shell.

### II. Reader-First Navigation
Primary section navigation MUST be the sticky table of contents: on wide
layouts (≥1024px) a persistent sticky contents list; on narrow layouts a
compact Contents control that reveals the same list. Navigation MUST help
readers jump between lesson sections quickly without covering narration or
code. Active section state MUST stay visible while scrolling (when scripted
enhancement runs). Mobile and desktop layouts MUST both remain usable with
one hand / one pointer.
Rationale: the page is long; lost context is the main friction. The sticky
TOC pattern is now the established primary navigator.

### III. Progressive Enhancement
Core content (headings, narration, code) MUST remain readable if JavaScript
fails. Script MAY enhance navigation (highlighting, sticky chrome, mobile
toggle) but MUST NOT be required to access section content via in-page
anchors when JS is available; if anchors exist in markup, they MUST work
without JS. New behavior MUST degrade without blanking the page.
Rationale: offline / print / reduced environments are normal for course
materials.

### IV. Visual Continuity
UI changes MUST reuse existing CSS variables and typography from
`index.html` (`--bg`, `--tx`, `--mut`, `--card`, `--bd`, `--ac`, etc.) and
MUST respect light/dark via `prefers-color-scheme`. Do not introduce a
second design system.
Rationale: the script already has a settled look; navigation should feel
native to it.

### V. Smallest Useful Change
Ship the smallest change that solves the stated reader problem. Prefer
editing the existing contents/`#nav` generation over parallel navigation
systems. The page MUST NOT present two competing primary section
navigators (for example, a legacy pill row plus the TOC). No speculative
features (search, bookmarks, progress sync) unless the active spec requires
them.
Rationale: Spec Kit practice stays focused; the page stays teachable.

## Delivery Constraints

- Primary deliverable: `index.html` (and only files a static browser needs).
- No Node/npm build pipeline for this project unless a future constitution
  amendment explicitly allows it.
- English UI copy for learner-facing chrome unless a feature spec says
  otherwise.
- Keep accessibility basics: focusable controls, visible focus, sufficient
  contrast against theme tokens, meaningful link/button labels.
- Primary lesson sections that appear in contents MUST keep unique, stable
  `id` values suitable as in-page hash targets.

## Development Workflow

1. Agree the change in Spec Kit artifacts (`spec` → `plan` → `tasks`) before
   editing product HTML for multi-step work.
2. Implement from `tasks.md`, then run `/speckit-converge` before claiming
   the feature done; resolve any appended convergence tasks via
   `/speckit-implement`.
3. Verify in a browser at desktop width (≥1024px) and a narrow width
   (~390px).
4. Confirm keyboard access for new interactive controls (Tab / Enter /
   Escape where a disclosure exists).
5. Do not expand scope mid-implement; amend the spec first.

## Governance

This constitution supersedes ad-hoc chat instructions when they conflict.
Amendments require an updated `constitution.md`, a bumped version
(MAJOR/MINOR/PATCH as defined by Spec Kit practice), and a short note in
the Sync Impact Report comment before commit. Reviews of feature work
MUST check principles I–V against the diff. Complexity beyond the active
spec MUST be rejected or deferred to a new change.

**Version**: 1.1.0 | **Ratified**: 2026-11-05 | **Last Amended**: 2026-11-06
