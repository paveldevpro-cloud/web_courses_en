---
name: HTML Web Courses EN
description: Apple Support–quiet course script for RAG lessons
colors:
  bg: "#ffffff"
  bg-soft: "#f5f5f7"
  text: "#1d1d1f"
  muted: "#6e6e73"
  border: "#d2d2d7"
  accent: "#0066cc"
  code-bg: "#f5f5f7"
  code-text: "#1d1d1f"
  dark-bg: "#000000"
  dark-bg-soft: "#1c1c1e"
  dark-text: "#f5f5f7"
  dark-muted: "#98989d"
  dark-border: "#38383a"
  dark-accent: "#2997ff"
typography:
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.47
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "2.25rem"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.022em"
  mono:
    fontFamily: "ui-monospace, \"SF Mono\", Menlo, Consolas, monospace"
    fontSize: "0.8125rem"
rounded:
  sm: "6px"
  md: "12px"
  pill: "980px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "28px"
components:
  tab-selected:
    textColor: "{colors.accent}"
    backgroundColor: "transparent"
  button-copy:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    padding: "8px 16px"
  promo-code:
    backgroundColor: "{colors.bg-soft}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "7px 12px"
---

## Overview

Course teaching script restyled as an Apple Support–quiet document: white paper, system SF stack, blue text wayfinding, hairline rules. Content order and curriculum stay fixed; only chrome and type change.

## Colors

Light default: white ground (`#ffffff`), soft gray sheets (`#f5f5f7`), ink (`#1d1d1f`), mute (`#6e6e73`), hairline (`#d2d2d7`), accent link blue (`#0066cc`). Dark follows Apple black (`#000`) with `#2997ff` accent via `prefers-color-scheme`.

## Typography

Body at 17px / 1.47 on the system SF stack. Titles are semibold with negative tracking. Mono (`SF Mono` / ui-monospace) is reserved for code, promo codes, and language labels.

## Layout

Max reading measure ~720–740px; page shell up to ~1120px. Sticky TOC on ≥1024px; Contents disclosure on narrow. Promo → course tabs → lesson column; never reorder curriculum blocks.

## Elevation & Depth

Mostly flat. Soft sheet backgrounds and hairlines carry separation; avoid thick accent side-bars and glow pulses.

## Shapes

12px radius on code wells; pill (`980px`) on Copy / Contents / promo code chips. Tabs are underline indicators, not segmented pills.

## Components

- **Promo strip**: hairline bottom rule; code chip + outline Copy.
- **Course tabs**: text row + bottom rule; selected = accent color + 2px underline. First tab is **Home**.
- **Home (Keynote opener)**: full-width centered hero; display title in ink; rotating stack line in link blue; mute lead; pill CTA in `--link`; secondary text module path. Signature motion: blur-clear rise on enter + stack word crossfade; static stack line under `prefers-reduced-motion`.
- **TOC links**: mute text; current = accent + 2px left rule.
- **Narration (`.say`)**: plain column text; mute label; no left stripe.
- **Code (`.cb`)**: light well, bordered, Copy pill top-right.

## Do's and Don'ts

**Do** keep English chrome, unique section ids, and `PROMO_CODE_HERE` aligned with Block 15.  
**Do** respect `prefers-reduced-motion` (promo entrance only; no pulse).  
**Don't** reintroduce orange promotional AI chrome or thick accent side bars on narration.  
**Don't** change lesson copy, code samples, or tab order when extending the system.
