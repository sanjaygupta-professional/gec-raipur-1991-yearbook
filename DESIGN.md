# Design System: GEC Raipur 1991 Living Yearbook

## 1. Visual Theme & Atmosphere
An Apple-caliber digital archive and museum-grade collegiate memorial. 
The atmosphere is restrained, gallery-airy, and tactile: a calibrated darkroom studio combining Swiss typographic precision with engineering drafting heritage.
- **Density:** 4 (Gallery Airy — generous breathing room, intentional spatial rhythm)
- **Variance:** 6 (Offset Asymmetric — Apple bento architecture, weighted editorial visual anchors)
- **Motion:** 6 (Fluid Spring — Apple keynote physics, weighted dampening, tactile feedback)

---

## 2. Color Palette & Roles
Strictly neutral charcoal/titanium base with a single restrained champagne gold accent. Zero purple gradients, zero neon glows, zero pure black.

### Three Selectable Appearance Modes (Persistent across pages)
1. **Dark (Darkroom Obsidian)**:
   - Root Canvas: `#0b0c0e` | Containers: `#131518` | Controls: `#1a1d22`
   - Primary Text: `#f4f5f7` | Secondary: `#8e939e` | Accent: `#d4af37`
   - Purpose: Low-glare darkroom studio; maximum contrast for faded historical photography.
2. **Linen (Archival Cotton Rag / Off-White)**:
   - Root Canvas: `#f5f2eb` | Containers: `#ffffff` | Controls: `#ede7dc`
   - Primary Text: `#1d1914` | Secondary: `#6e675d` | Accent: `#9a7322`
   - Purpose: Warm paper tactile quality; reminiscent of physical 1991 degree thesis paper.
3. **Light (Studio Pure Light)**:
   - Root Canvas: `#f4f5f7` | Containers: `#ffffff` | Controls: `#eaedf1`
   - Primary Text: `#0f141c` | Secondary: `#5e6878` | Accent: `#a17822`
   - Purpose: Apple gallery daylight aesthetic; high legibility in bright rooms.

- **Obsidian Darkroom** (`#0b0c0e`) — Root background canvas; deep, non-glare photographic ground
- **Titanium Surface** (`#131518`) — Primary container, card, and navigation bar background
- **Elevated Slate** (`#1a1d22`) — Active segmented controls, hovering states, input focus fill
- **Hairline Border** (`rgba(255, 255, 255, 0.08)`) — 1px crisp structural division lines
- **Hairline Border Hover** (`rgba(255, 255, 255, 0.16)`) — Tactile hover border enhancement
- **Primary Text** (`#f4f5f7`) — Headlines, primary names, high-contrast labels (95% contrast)
- **Secondary Steel** (`#8e939e`) — Descriptions, roles, metadata, and timestamps
- **Muted Carbon** (`#555a64`) — Placeholders, inactive telemetry, micro-labels
- **Champagne Gold** (`#d4af37`) — Singular accent for active spotlights, verification badges, and focal rings
- **Emerald Verification** (`#10b981`) — Verified pixel authenticity badge and save confirmation
- **Banned:** Pure black (`#000000`), neon purple, cyan glows, multi-color card borders, oversaturated accents (>80% saturation).

---

## 3. Typographic Architecture
Apple Precision font pairing: modern neo-grotesque sans-serif with track-tight headline pacing, paired with an authentic monospace for engineering telemetry.

- **Display & Headings:** `Geist`, `-apple-system`, `BlinkMacSystemFont`, sans-serif.
  - Scale: `clamp(2.5rem, 6vw, 4.25rem)` for hero title; `clamp(1.75rem, 3.5vw, 2.5rem)` for section titles.
  - Tracking: `-0.03em` (track-tight, confident, non-screaming).
  - Line height: `1.08` to `1.15`.
- **Body & Editorial Copy:** `Geist`, `system-ui`, sans-serif.
  - Scale: `1rem` (16px) with relaxed leading `1.6`.
  - Max line length: `64ch` for comfortable reading.
- **Engineering Telemetry & Microdata:** `Geist Mono`, `SF Mono`, `Consolas`, monospace.
  - Used for: coordinates (`X: 1076.00  Y: 545.00`), roll numbers, sheet metadata, timestamps, and row counts.
  - Scale: `0.75rem` to `0.85rem` with `tabular-nums` enabled.
- **Banned:** `Inter` font, generic `Times New Roman`, comic/handwriting fonts, emojis in titles or buttons, italic body text, faux-bold 900 weights.

---

## 4. Hero Section Architecture
- **Asymmetric Balance:** Two-column split on desktop (55% editorial narrative + search, 45% interactive live photograph stage).
- **Inline Typographic Punctuation:** Small authentic circular face crops embedded directly inline alongside batchmate names.
- **No Overlapping:** Clean spatial separation; text never collides with imagery.
- **Search Command Bar:** Apple Spotlight-inspired search bar with tactile keyboard badge (`↵ Return`) and live count indicator.
- **Zero Filler:** No "Scroll down to explore" chevrons, no animated bouncing arrows.

---

## 5. Component Behaviors
- **Segmented Controls (View & Theme Switchers):**
  - Integrated pill track in Titanium Surface (`#131518`) with 4px inner padding.
  - Active pill floats with subtle elevation, crisp hairline border, and bright text.
  - Tactile transition: `transform 0.18s cubic-bezier(0.16, 1, 0.3, 1)`.
- **Buttons:**
  - Solid Champagne Gold or Titanium fill with `-1px` active push feedback.
  - Minimum touch target: 44px × 44px on mobile devices.
  - Clean vector stroke iconography only (Phosphor icons or inline SVGs); zero emojis.
- **Bento Feature Grid:**
  - Asymmetric 2×2 / 3-column bento box with variable cell dimensions (1 large 2-span hero card + 2 stacked cards).
  - Generous 24px internal padding, 16px corner radius, hairline borders with subtle corner highlights.
- **Face Hotspots & Halo:**
  - Discrete hairline rings with subtle champagne pulse (`scale(1.05)` to `scale(1.15)`).
  - Smooth 2.4x camera pan & zoom centered with spring damping on selection.

---

## 6. Anti-Patterns (Strictly Banned)
- ❌ **NO EMOJIS ANYWHERE IN THE UI**: No 🏛️, 📐, 🎞️, 🎬, 💻, 💡, 🔍, 📥, 🖼️, 🌓, 📜, 📲, ⭐ in buttons, headers, or pill tabs. Use minimalist vector icons or plain text labels.
- ❌ **NO PURE BLACK (`#000000`)**: Always use Obsidian Darkroom (`#0b0c0e`).
- ❌ **NO NEON OR PURPLE GLOWS**: No blurred colored drop shadows behind buttons or cards.
- ❌ **NO 3-EQUAL-CARD ROWS**: Replace with Apple bento grid layouts.
- ❌ **NO AI COPYWRITING CLICHÉS**: Banned words: "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionary", "Cutting-edge". Use ASD-STE100 active collegiate facts.
- ❌ **NO FAKE METRICS**: No invented uptime percentages or synthetic statistics. Only real historical data (67 members, 4 rows, 1991).
- ❌ **NO FACIAL DISTORTION**: Original optical grain preserved with zero AI hallucinations.
