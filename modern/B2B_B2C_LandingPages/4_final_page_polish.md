Your job is to act as the final visual polish on our landing page, which is meant to avoid common “ai design” faux-pas, and make it feel more professional and finalized. Take the following as guidance:
### 1) Color System & Contrast
AI trap: Random brand colors + trendy gradients; insufficient contrast.


Polish: Define a 8–12 token palette: primary/brand, accent, success, warning, danger, neutral-0…900. Keep gradients for one hero moment max.


Quick test: WCAG AA contrast ≥ 4.5:1 for body, ≥ 3:1 for large text; no more than 2 brand hues on any single view.


### 2) Typographic Rhythm & Scale
AI trap: Overlarge headlines, inconsistent weights, default line-heights.


Polish: One font for UI, optional display for hero. Use a modular scale (e.g., 1.2): 12/14/16/19/23/28/34/41. Line-height: 1.4–1.6 for body, 1.15–1.3 for headings.


Quick test: Scan the page at 50% zoom—can you identify a clean H1→H2→H3 ladder instantly?


### 3) Spacing System & Grid
AI trap: “Auto” padding everywhere; irregular gaps.


Polish: 4/8 spacing scale (e.g., 4,8,12,16,24,32,48,64). Establish a content max-width (e.g., 72ch for articles, 1200px for marketing) and a 12-col grid with consistent gutters.


Quick test: Draw horizontal rules across sections—do baselines align? No “1-off” paddings like 22px.


### 4) Hierarchy & Information Scent
AI trap: Too many equally loud elements; hero competes with secondary CTAs.


Polish: One primary CTA, one secondary. Apply “90/9/1” emphasis: ~10% of pixels carry 90% of attention (headline + CTA).


Quick test: Squint test: can you state the page promise and next action in 3 seconds?


### 5) CTA Craft & States
AI trap: Generic “Learn more”, identical primary/secondary styles, missing states.


Polish: Action + outcome (“Get your audit →”). Size: 44px min height. States: default/hover/active/focus/disabled + loading spinner label.


Quick test: Keyboard through CTAs—does focus ring meet 3:1 contrast and remain visible on gradients?


### 6) Forms That Don’t Fight
AI trap: Placeholder-as-label, no error copy, inconsistent inputs.


Polish: Always-visible labels, helpful microcopy (“We’ll never spam”), inline validation, specific errors, wide tap targets, autofill enabled.


Quick test: Attempt submission with all fields blank—do you know exactly how to fix each error in ≤2 seconds?


### 7) Motion & Micro-interactions
AI trap: Overused parallax/blur, chaotic durations, easing defaults.


Polish: Subtle only; 150–250ms UI motions, 300–450ms hero entrances; use standard easing (e.g., cubic-bezier(0.2, 0.8, 0.2, 1)). Animate opacity/transform, not layout.


Quick test: Turn on “Reduce Motion” in OS. Does the site gracefully cut motion without breaking context?


### 8) Visual Cohesion: Icons, Imagery, Shadows
AI trap: Mixed icon sets, stocky images, harsh drop shadows.


Polish: Single icon family; image treatment consistent (same color grade or subtle duotone). Use elevation tokens: shadow-1: y=2 blur=6 opacity 12%, shadow-2: y=8 blur=24 opacity 14%.


Quick test: Place three random icons next to each other—do stroke widths and corner radii match?


### 9) Content Density & Scannability
AI trap: Wall-of-text sections or over-fragmented bullet spam.


Polish: Follow the “Promise → Proof → Path” block: headline (promise), 1–2 lines of benefit (proof), CTA (path). Use 5–7 word subheads, 40–80 char lines for body.


Quick test: Remove all images—does the copy alone sell the click?


### 10) Responsiveness, Performance & Loading
AI trap: Desktop-first, layout collapses at 1024/768, heavy assets.


Polish: Design for 360, 768, 1280, 1440 breakpoints. Ship responsive images (srcset, sizes), preconnect critical domains, lazy-load below-the-fold, <100KB CSS, <150ms TTFB if possible.


Quick test: Lighthouse + throttled 3G: is LCP under 2.5s and CLS < 0.1? Does the hero message appear within 1s on mid-tier hardware?



AI-Specific Smell Tests & Fixes
Gradient discipline: If the hero uses a gradient, keep buttons solid. If buttons have gradient, hero stays flat. Never both.


Tokenization over ad-hoc styles: Centralize colors, spacing, radii, shadows, z-index; ban inline hex codes in components.


Semantic HTML first: <h1> only once; logical heading order; proper <label for>; landmarks (<header> <main> <nav> <footer>).


Consistent radii: Pick one base (e.g., 8px). Only upscale by 2× for “cards” and 4× for “dialogs”—no random 6/10/14px corners.


Copy + design lock: Every section must answer: “**Why should I care?**” and “**What should I do now?**” If not, re-write or remove.

