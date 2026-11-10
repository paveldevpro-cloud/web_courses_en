# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary users are junior-to-mid Python learners following a spoken video lesson. They keep this page open beside the video, jump between sections, and copy code blocks into their editor.

## Product Purpose

`index.html` is a self-contained English course script for building a local RAG system with LangChain, LangGraph, Chroma, and Ollama. Success means a reader can follow narration, jump sections, and copy working code without leaving the page.

## Positioning

A tabbed, copy-first teaching script for a full RAG path (basics → agent → streaming → FastAPI → advanced), not a marketing site and not a runnable app shell.

## Operating Context

Opened locally in a browser while watching a course video. Typical scene: laptop screen, lesson audio, terminal/editor nearby. Chrome includes a top Advanced-course promo, course topic tabs, sticky section contents on longer lessons, narration blocks, and copyable code.

## Capabilities and Constraints

- Single static HTML deliverable (`index.html`); no build pipeline required for the page itself.
- Learner-facing UI chrome is English.
- Promo code string must stay aligned with the end-of-lesson offer (`PROMO_CODE_HERE`).
- Sticky TOC remains the primary section navigator on Agent / Streaming / Advanced lesson layouts.
- **Redesign freeze (user-confirmed):** do not change lesson text, code samples, tab labels/order, text order, or informational content. Allowed changes are fonts, visual layout styling, and animation styling only.

## Brand Commitments

- Visual redesign direction pinned by the user: **Apple-inspired** (system-like clarity, restraint, and polish).
- Content and information architecture stay as shipped; the redesign replaces look-and-feel, not curriculum.

## Evidence on Hand

- Shipping page: `index.html` (tabs: Home, Basics, LLM Agent, LangGraph streams, CLI streaming, FastAPI, Advanced · SSE; promo; sticky TOC; narration + code).
- Source lesson material also present as `deepseek_html_final.html` (reference only; not the shipping shell).
- No fabricated testimonials, pricing, or enrollment metrics. Do not invent commercial claims.

## Product Principles

1. Reading and copying code beat decorative chrome.
2. Visual change must never reorder or rewrite curriculum.
3. Navigation stays obvious: tabs for topics, TOC for sections.
4. Motion supports attention; it never hides content.
5. Progressive enhancement: content remains readable if script or motion fails.

## Accessibility & Inclusion

Keyboard-focusable tabs and Copy controls; visible focus; respect `prefers-reduced-motion` and `prefers-color-scheme`. No product-specific WCAG target beyond those basics was set.
