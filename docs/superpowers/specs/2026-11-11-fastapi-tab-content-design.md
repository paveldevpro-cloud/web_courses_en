# Design: FastAPI tab content in index.html

Date: 2026-11-11  
Source: `fastapi_rag_lesson.html`  
Target: `#panel-fastapi` in `index.html`

## Goal

Adapt the FastAPI RAG lesson into the empty FastAPI course tab, matching the Streams tab markup pattern so the lesson feels like part of the same course site.

## Decisions

- Structure: numbered **Block 0…N** (like Streams), not Video 1–5 headings as the primary nav.
- Depth: step-by-step snippets during the lesson **plus** a complete `main.py` block at the end.
- Include Teaching notes; exclude Student exercise and Suggested next lesson.
- Approach: mirror Streams shell and styles; do not import CSS/JS from `fastapi_rag_lesson.html`.
- Leave `fastapi_rag_lesson.html` unchanged as a source artifact.
- Scope of code change: fill `#panel-fastapi` only. No CSS/tab JS changes (TOC for fastapi is already registered).

## Panel shell

Reuse the Streams layout:

```html
<div class="tab-panel" id="panel-fastapi" ...>
  <div class="page">
    <aside class="toc" id="toc-fastapi">...</aside>
    <main class="content">
      <h1>...</h1>
      <p class="lead">...</p>
      <!-- Block sections -->
    </main>
  </div>
</div>
```

TOC IDs already wired in `initSectionToc`:

- `toc-fastapi`, `nav-fastapi`, `toc-fastapi-toggle`, `toc-fastapi-close`

## Content map

| Block | Section id | Title | Source material |
|-------|------------|-------|-----------------|
| Title | — | Building a RAG API with FastAPI | Hero title + lead |
| 0 | `fastapi-overview` | What we are going to build | Overview + endpoints + video breakdown table |
| 1 | `fastapi-intro` | Introduction to FastAPI | Video 1 narration + before/after |
| 2 | `fastapi-setup` | Setup and Pydantic models | Video 2: install, imports, app, models |
| 3 | `fastapi-index` | Indexing endpoint | Video 3: return value + `POST /index` |
| 4 | `fastapi-ask` | Ask endpoint | Video 4: return dict + `POST /ask` |
| 5 | `fastapi-run` | Run and test | Video 5: `fastapi dev` + Swagger examples |
| 6 | `fastapi-complete` | Complete main.py | Full consolidated file |
| 7 | `fastapi-notes` | Teaching notes | Instructor notes list only |

Out of scope content:

- “What changed in the old code” before/after evolution section
- Student exercise checklist
- Suggested next lesson

## Markup conventions

- Narration → `<div class="say"><b class="t">Narration</b>…</div>`
- Code → `<div class="cb"><span class="lang">python|bash|json</span><pre><code>…</code></pre></div>`
- Copy buttons: existing page script attaches to `.cb`; do not add lesson-local copy JS
- Tables: native `<table>` as used in Streams
- Callouts/warnings from the source lesson: plain paragraphs or short emphasized notes using existing course patterns (no `.callout` / `.warning` classes from the standalone file)
- Language: English (same as the rest of `index.html` course content)

## Non-goals

- Redesigning the course chrome, tabs, or promo blocks
- Changing Agent / Streams / other tab content
- Adding streaming FastAPI endpoints
- Deleting or rewriting `fastapi_rag_lesson.html`

## Acceptance criteria

1. Opening the FastAPI tab shows a full lesson with sticky TOC listing Blocks 0–7.
2. All instructional narration and code needed to build `POST /index` and `POST /ask` are present.
3. Complete `main.py` and Teaching notes appear at the end.
4. Copy buttons work on code blocks via existing `.cb` wiring.
5. No regressions to other tabs or global scripts.
