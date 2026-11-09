# Data Model: Top Promo Block

In-page conceptual model only (no persistence).

## Entities

### TopPromoBlock

| Field | Type | Rules |
|-------|------|--------|
| `placement` | enum | Always `page-top` — above `.page` / lesson title |
| `headline` | string | Required; English; short Advanced-course pitch |
| `body` | string | Required; English; one short supporting sentence |
| `code` | string | Required; MUST equal the bottom Block 15 promo code string (`PROMO_CODE_HERE` today) |
| `actionLabel` | string | Required; English control label for copying the code (e.g. Copy) |
| `sticky` | boolean | MUST be `false` (scrolls away; does not cover lesson body) |
| `motionMode` | enum | `animated` when reduced-motion is off; `static-bright` when reduced-motion is on |

**Validation**:
- Must not introduce a second section-navigation landmark competing with `#nav`.
- Must remain in document content (not injected-only ephemeral UI) so message
  survives without animation.

### PromoOffer

| Field | Type | Rules |
|-------|------|--------|
| `product` | string | Advanced course |
| `code` | string | Shared with bottom promo; single source of truth in markup or one shared literal |
| `channel` | string | Udemy checkout (stated in copy, consistent with Block 15) |

**Relationships**:
- `TopPromoBlock` presents exactly one `PromoOffer`.
- Bottom Block 15 promo presents the same `PromoOffer.code`.

## State Transitions

### Motion

```text
[load] --prefers-reduced-motion: no-preference--> animated
[load] --prefers-reduced-motion: reduce--> static-bright
```

No dismiss / closed state in v1.
