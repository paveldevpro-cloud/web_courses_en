# UI Contract: Top Promo Block

Audience: implementers of `index.html` promotional chrome.

## Surface P1. Top promo region

- **Placement**: First major chrome at the top of the document body, above the
  `.page` layout (TOC + lesson main). Appears above the lesson `<h1>`.
- **Role**: complementary promotional banner — NOT a replacement for
  `nav[aria-label="Lesson sections"]`.
- **Content**: English headline, short body, visible promo code matching
  Block 15, and a Copy action for that code.
- **Emphasis**: Visually brighter than `.say` narration cards (accent-forward
  background/border/type).
- **Motion**: Perceptible entrance and/or subtle loop when reduced motion is
  not requested; static bright presentation when reduced motion is requested.
- **Scroll behavior**: Not sticky; must not overlay narration/code while the
  reader scrolls the lesson.
- **Responsive**: Readable at ~390px without forcing page-wide horizontal
  scroll.

## Non-goals

- Dismiss / remember closed.
- Second sticky chrome competing with TOC.
- External animation libraries or build steps.
- Conflicting promo codes.
