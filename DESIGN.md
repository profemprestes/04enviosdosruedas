# Design System: Envíos DosRuedas

Static HTML website for **Envíos DosRuedas** — motorcycle courier & last-mile logistics in Mar del Plata, Argentina. No build step, no package manager, no CI/CD. Deployed as static files.

## 1. Visual Theme & Atmosphere

High-trust, locally-grounded logistics brand for Mar del Plata. Clean blue surfaces convey professionalism and reliability; yellow accents signal urgency, action, and the "express" promise. Hero sections are always bold (blue or yellow), never white — the next section drops to white to breathe. Glassmorphic cards on blue backgrounds (`white/8`–`white/12` with top highlight) create elevation without shadows. Procedural grid patterns and radar/route tracer SVGs reinforce the "movement across the city" metaphor. Zero decorative motion — every animation serves navigation, feedback, or progress. Voseo rioplatense copy throughout ("Cotizá", "Enviá") anchors the voice in local culture.

## 2. Color Palette & Roles

### Primary Foundation (Blue Scale)
- **Abyssal Blue (`#041f63` / `--color-brand-blue-900`)**: Darkest brand blue, used for text on yellow surfaces (knockout text, badge text)
- **Deep Harbor (`#062d85` / `--color-brand-blue-800`)**: Near-black blue, rare — only for highest-contrast text on yellow
- **Navy Anchor (`#083aa3` / `--color-brand-blue-700`)**: Dark blue for secondary text on light, hover states on blue buttons
- **Brand Blue (`#0950f6` / `--color-brand-blue-500`)**: **Primary brand color** — hero surfaces, primary buttons, header bar, footer, CTA outlines, focus rings
- **Brand Blue 600 (`#0a4fc0` / `--color-brand-blue-600`)**: Pressed/active state for primary buttons
- **Skyward (`#1d5ef7` / `--color-brand-blue-450` / `--color-brand-blue-400` equivalent)**: Secondary text on light backgrounds, hover on blue buttons, input focus
- **Azure Line (`#628ff9` / `--color-brand-blue-300` / `--color-brand-blue-300`)**: Input borders, decorative strong lines
- **Mist Border (`#bacefd` / `--color-brand-blue-100` / `--color-border-line`)**: Card borders, decorative hairlines, subtle dividers
- **Mist Surface (`#e6eefe` / `--color-brand-blue-50` / `--color-bg-mist`)**: Card surfaces on white, secondary text on blue, form backgrounds
- **Ice Surface (`#f3f7ff` / `--color-brand-blue-25` / `--color-bg-ice`)**: Section background "ice", alternate to white

### Accent & Interactive (Yellow)
- **Volt Yellow (`#ffec01` / `--color-brand-yellow-500` / `--color-bg-accent`)**: **Primary accent** — CTA backgrounds (nested pills), knockout capsules on blue, hero accents, badge pills, WhatsApp icons, focus highlights
- **Volt Yellow 400 (`#fff12e` / `--color-brand-yellow-400`)**: Hover state for yellow CTAs, secondary yellow accents
- **Volt Yellow 300 (`#fff45c` / `--color-brand-yellow-300`)**: Subtle yellow backgrounds, hover glows

### Typography & Text Hierarchy
- **Abyssal Ink (`#041f63` / `--color-brand-blue-900`)**: Primary text on light surfaces (headings, body)
- **Harbor Ink (`#062d85` / `--color-brand-blue-800`)**: High-emphasis text on light (rare)
- **Navy Ink (`#083aa3` / `--color-brand-blue-700`)**: Secondary text on light, labels
- **Skyward Ink (`#1d5ef7` / `--color-brand-blue-450`)**: Muted text on light, placeholders, helper text
- **White (`#ffffff` / `--color-white`)**: Text on blue/yellow surfaces
- **White 80% (`rgba(255,255,255,0.8)`)**: Secondary text on blue surfaces
- **White 50% (`rgba(255,255,255,0.5)`)**: Muted text on blue surfaces

### Functional States
- **Danger Red (`#dc2626` / `--color-red-600` / `--color-text-danger`)**: Error text only (form validation, destructive actions)
- **Success Green**: WhatsApp icon only (`#25d366` via SVG) — never used elsewhere
- **Focus Ring**: `--color-brand-blue-500` at 20% opacity (`focus:ring-brand-blue-500/20`)

### Shadows & Elevation (Blue-tinted only)
- **Float Shadow (`--shadow-float`)**: `0 25px 50px -12px #0950f626` — cards on light, hero elements
- **Antigravity Deep (`--shadow-antigravity-deep`)**: `0 24px 64px #0950f638` — featured cards, modals
- **CTA Glow Yellow**: `0 0 0 3px #ffec0140` — yellow nested pills hover
- **Elevated Header**: `shadow-elevated` — scrolled header state
- **On Blue**: No black shadows. Elevation via `white/8`–`white/12` translucent layers + 1px top highlight (`border-white/10`)

### Gradients & Patterns
- **Procedural Grid (Hero)**: 48×48 SVG pattern — white dashed lines + yellow dots at intersections (`hero-procedural-grid-blue`)
- **Radar/Route Tracer**: Yellow pulsing rings + dotted routes from real pins (Friuli 1972, zones) — animated via `motion-safe:animate-pulse`
- **Ghost Wordmark**: "Envíos Dos Ruedas" at 4–6% opacity behind hero (SVG `text-brand-blue-500/5`)
- **Mesh Gradients**: Radial glows on social cards (`rgba(255,236,1,0.08)` at 50%), footer (`rgba(9,80,246,0.5)` at 40%)

## 3. Typography Rules

| Role | Font | Size / Weight / Leading / Tracking | Treatment |
|------|------|-------------------------------------|-----------|
| **Display / H1 / H2 / Impact Numbers** | Anton (`--font-display`) | `text-4xl`–`text-6xl` / `extrabold` / `leading-[0.95]` / `tracking-tight` / `uppercase` | `text-wrap: balance`, `text-brand-blue-500` on light, `text-white` on blue, `text-brand-yellow-500` for highlight spans |
| **H3 / Subheadings / Buttons / Labels / Nav** | Bebas Neue (`--font-subheading`) | `text-base`–`text-xl` / `bold` / `leading-none` / `tracking-wider` / `uppercase` | Min 13px (`text-sm`), `text-brand-blue-500` or `text-white` |
| **Body / UI / Paragraphs** | Outfit (`--font-sans`) | `text-sm`–`text-lg` / `400`–`600` / `leading-relaxed` (1.6) / `normal` | Sentence case, `text-brand-blue-700`/`900` on light, `text-brand-blue-50` on blue |
| **Prices / Distances / Times / Phones** | Geist Mono (`--font-mono`) | `text-sm`–`text-xl` / `500`–`700` / `leading-none` / `tabular-nums` **always** | `font-mono tabular-nums`, `text-brand-blue-500` or `text-brand-yellow-500` |
| **Captions / Meta / Timestamps** | Outfit / Geist Mono | `text-2xs` (`.625rem` / 10px min) / `400`–`600` / `leading-none` / `tracking-widest` | Uppercase for labels, `text-brand-blue-500/60` on light |

**Minimum text size**: 11px (`text-2xs` = `.625rem`). No 9/10px. No Inter, system fonts, Title Case, English copy.

**Font Stack**:
- `--font-display`: `"Anton SC", "Anton", sans-serif`
- `--font-subheading`: `"Bebas Neue", sans-serif`
- `--font-sans`: `"Outfit", "IBM Plex Sans", sans-serif`
- `--font-mono`: `"Geist Mono", monospace`

## 4. Component Stylings

### Buttons

| Variant | Surface | Fill | Text | Border | Radius | Height | Hover | Focus | Icon Shift |
|---------|---------|------|------|--------|--------|--------|-------|-------|------------|
| **CTA Nested Pill (Primary)** | Any | `--color-brand-yellow-500` | `--color-brand-blue-900` | none | `rounded-full` | `min-h-[48px]` (default), `sm:44px`, `lg:56px` | `bg-brand-yellow-400`, `shadow-glow-yellow` | `ring-2 ring-brand-blue-500/20` | 4px right (`.cta-nested-icon translate-x-1`) |
| **CTA Nested Pill (Outline)** | Light | `transparent` | `--color-brand-blue-500` | `2px solid --color-brand-blue-100` | `rounded-full` | `min-h-[48px]` | `bg-brand-blue-50`, `border-brand-blue-300` | `ring-2 ring-brand-blue-500/20` | 4px right |
| **CTA Nested Pill (Ghost on Blue)** | Blue | `transparent` | `white` | `1px solid white/15` | `rounded-full` | `min-h-[48px]` | `bg-white/10` | `ring-2 ring-white/30` | 4px right |
| **CTA Nested Pill (Blue on Yellow)** | Yellow | `--color-brand-blue-500` | `white` | none | `rounded-full` | `min-h-[48px]` | `bg-brand-blue-600` | `ring-2 ring-white/30` | 4px right |
| **Secondary Link** | Any | `transparent` | `--color-brand-blue-500` / `white` | none | none | auto | `text-brand-yellow-500`, `translate-x-1` | `outline-none focus-visible:ring-2` | none |

### Cards

| Variant | Shell | Core | Border | Radius | Padding | Shadow | Featured |
|---------|-------|------|--------|--------|---------|--------|----------|
| **Double Bezel (Light)** | `#bacefd` (`border-line`) 1px | `white` | `--color-brand-blue-100` | `rounded-2xl` (24px) | `p-6`–`p-8` | `--shadow-float` | `.is-featured` = yellow core (`bg-brand-yellow-500`) |
| **Double Bezel (On Blue)** | `white/8`–`white/12` backdrop-blur | `white/10`–`white/15` | `white/15` | `rounded-2xl` | `p-6`–`p-8` | none (top highlight only) | `.is-featured` = `bg-brand-yellow-500/20` |
| **Social Block** | Platform tint (`#1877F2`/30, `#E1306C`/30, yellow/30) | Gradient platform bg | Platform border/30 | `rounded-2xl` shell + `rounded-xl` core | `p-6`–`p-7` | `shadow-xl` | Platform glow on hover |
| **Testimonial Card** | `white/10` on blue | `white/10` core | `white/10` top border | `rounded-2xl` | `p-6` | none | Rotated ±6° (`style="rotate:2px"`) |

### Navigation

- **Header**: Fixed, `bg-brand-blue-500 py-4` → scrolled: `bg-brand-blue-500/95 backdrop-blur-md shadow-elevated border-b border-white/10 py-2.5`
- **Logo**: `font-display text-2xl–3xl uppercase` + `font-mono text-xs tracking-widest` tagline
- **Desktop Nav**: `font-subheading text-base uppercase tracking-wider`, dropdown `w-64 bg-brand-blue-500 rounded-2xl shadow-2xl border-white/15`
- **Mobile Menu**: Slide-down panel, same styling as desktop dropdown
- **Active/Selected**: `text-brand-yellow-500`, `bg-white/10` on hover

### Inputs & Forms

- **Base**: `h-11 w-full border-2 border-brand-blue-100/20 rounded-xl pl-11 pr-4 bg-white text-brand-blue-500 placeholder:text-brand-blue-500/40`
- **Icon Prefix**: `absolute left-3.5 top-1/2 -translate-y-1/2 h-5 w-5 text-brand-blue-500/60`
- **Focus**: `focus:border-brand-blue-500 focus:ring-2 focus:ring-brand-blue-500/20`
- **Label**: `text-xs font-subheading tracking-wider text-brand-blue-500 uppercase font-bold`
- **Select**: Same as input + `appearance-none cursor-pointer`
- **Error**: `border-red-600 focus:border-red-600`, helper text `text-red-600 text-xs font-mono`

### Badges / Pills / Knockouts

- **Knockout (−1°)**: Rotated capsule (`style="rotate:-1deg"`) with keyword. `tone="yellow"` on blue: `bg-brand-yellow-500 text-brand-blue-900`. `tone="blue"` on yellow: `bg-brand-blue-500 text-white`.
- **Eyebrow (Yellow)**: `.eyebrow` — `px-4 py-1.5 bg-brand-yellow-500 text-brand-blue-900 rounded-full text-xs font-bold tracking-widest inline-block font-subheading uppercase`
- **Eyebrow Soft**: `.eyebrow-soft` — Same but `bg-brand-yellow-500/20` or `bg-brand-blue-50`
- **Status Chip**: Pill (`rounded-full`), icon + explicit label. Colors: yellow (primary), blue (secondary), platform colors (social)

### Hero Sections

- **Surface**: Always `.surface-blue` (`bg-brand-blue-500`) or `.surface-accent` (`bg-brand-yellow-500`) — **never white/ice/mist**
- **Pattern**: Procedural grid SVG (`hero-procedural-grid-blue`) or radial mesh gradient
- **Ghost Wordmark**: "Envíos Dos Ruedas" at 4–6% opacity (`text-brand-blue-500/5` or `text-brand-yellow-500/5`)
- **Radar/Route Tracer**: Animated SVG from real pins (Friuli 1972) — `motion-safe:animate-pulse`
- **Content**: H1 (Anton, uppercase), subheadline (Outfit, sentence case), CTA nested pill, trust signals (stats in Geist Mono tabular-nums)

### Footer

- **Surface**: `bg-brand-blue-500` + top accent bar `h-1.5 bg-brand-yellow-500 shadow-md shadow-brand-yellow-500/30`
- **Pattern**: Radial mesh (`rgba(255,236,1,0.08)`), grid lines (`linear-gradient` 32px), grid dots
- **Links**: `text-brand-blue-50 hover:text-brand-yellow-500`, `font-subheading uppercase tracking-wider`
- **Contact Cards**: `bg-brand-blue-500/80 p-3 rounded-xl border-white/15`, icon `p-2 bg-white/10 rounded-lg text-brand-yellow-500`
- **Back to Top**: `bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 rounded-full shadow-accent-md`

## 5. Layout Principles

- **Container Max Width**: `max-w-7xl` (1280px / 80rem) for main content, `max-w-6xl` for CTA sections
- **Base Spacing Unit**: 4px (`--spacing: .25rem`) → Tailwind scale (1 = 4px, 2 = 8px, 4 = 16px, 6 = 24px, 8 = 32px, 10 = 40px, 12 = 48px, 16 = 64px, 20 = 80px, 24 = 96px, 28 = 112px, 32 = 128px)
- **Section Padding**: `py-20` (mobile) → `py-28`/`py-32` (desktop), `px-4` → `px-6` → `px-8`
- **Card Padding**: `p-6` (mobile) → `p-8` (desktop)
- **Vertical Rhythm**: Sections separated by alternating surfaces — **Hero (blue/yellow) → White → Blue/Ice → Mist → Accent Band (yellow) → Footer (blue)**
- **Never Two Blue Sections Consecutively**: Strict alternation enforced
- **Grid System**: CSS Grid / Flexbox, `gap-6` (mobile) → `gap-8`/`gap-10` (desktop), `grid-cols-1` → `sm:grid-cols-2` → `lg:grid-cols-3`/`lg:grid-cols-4`
- **Responsive Breakpoints**: `sm: 640px`, `md: 768px`, `lg: 1024px`, `xl: 1280px`, `2xl: 1536px`
- **Touch Targets**: Minimum 44×44px (nested pills `min-h-[48px]`, social icons `h-10 w-10`, nav items `py-2.5`)
- **Border Radius Scale**: `rounded-xl` (16px) inputs/buttons, `rounded-2xl` (24px) cards, `rounded-full` (9999px) pills/badges, `rounded-[20px]`/`rounded-[30px]` feature containers

## 6. Design System Notes for Stitch Generation

### Atmosphere Keywords
`high-trust local logistics`, `Mar del Plata motorcycle courier`, `blue professionalism + yellow urgency`, `glassmorphic cards on blue`, `procedural grid hero patterns`, `radar route tracer from real pins`, `voseo rioplatense voice`, `zero decorative motion`, `spring physics (100/20)`, `WCAG contrasts verified`

### Canonical Color Names with Hex
| Token | Hex | Role |
|-------|-----|------|
| `--color-brand-blue-500` | `#0950f6` | Primary brand, hero surfaces, header, footer, primary CTAs |
| `--color-brand-yellow-500` | `#ffec01` | Accent CTAs, knockouts, badges, WhatsApp, focus highlights |
| `--color-brand-blue-900` | `#041f63` | Text on yellow, knockout text |
| `--color-brand-blue-50` | `#e6eefe` | Card surfaces on white, form backgrounds |
| `--color-brand-blue-100` | `#bacefd` | Card borders, decorative lines |
| `--color-brand-blue-300` | `#628ff9` | Input borders |
| `--color-brand-blue-450` | `#1d5ef7` | Secondary text, hover on blue |
| `--color-white` | `#ffffff` | Text on blue/yellow, card cores |
| `--color-red-600` | `#dc2626` | Error text only |

### Component Prompts for Future Screen Generation

1. **Hero Section (Blue Surface)**: "Full-bleed hero on `#0950f6` surface with procedural grid SVG pattern, ghost wordmark at 5% opacity, radar tracer from Friuli 1972 pulsing via `motion-safe:animate-pulse`. H1 in Anton uppercase `text-5xl–6xl tracking-tight`, subheadline Outfit sentence case `text-lg`, CTA nested pill yellow `min-h-[48px]` with WhatsApp icon shifting 4px on hover. Trust stats in Geist Mono `tabular-nums` below."

2. **Double Bezel Card Grid (Light Surface)**: "Three-column card grid on white (`bg-white`) with `gap-8`. Each card: double bezel — shell `border-brand-blue-100` 1px, core `bg-white`, `rounded-2xl p-6–8`, `--shadow-float`. Featured card gets `bg-brand-yellow-500` core. Content: eyebrow yellow pill, H3 Bebas Neue uppercase, body Outfit, price Geist Mono tabular-nums, CTA nested pill outline."

3. **CTA Band Before Footer (Blue Surface with Glass Form)**: "Section on `bg-brand-blue-500` with radial mesh glow. Container: `rounded-[30px] bg-white/10 backdrop-blur-md border-white/25 shadow-2xl` → inner `bg-white rounded-[20px] p-8–14`. Left: eyebrow, H2 Anton, body Outfit, mono `text-xs tracking-widest` SLA badge. Right: Form in `bg-brand-blue-50 p-8 rounded-[20px] border-2 border-brand-blue-100/20` — inputs with icon prefix, focus `border-brand-blue-500 ring-brand-blue-500/20`, submit yellow nested pill full-width `min-h-13`."

4. **Social Proof Carousel (Blue Surface)**: "Marquee carousel on `bg-brand-blue-500` with `animate-marquee-left 30s linear infinite`. Cards rotated ±6° (`style="rotate:-2px"`), `bg-white/10 backdrop-blur-md border-white/10 p-6 rounded-2xl`. Content: quote icon, 5 yellow stars, eyebrow tag (Bebas Neue), testimonial text Outfit, author avatar + name + meta. Respects `prefers-reduced-motion` (pauses animation)."

5. **Footer (Blue Surface with Yellow Accent Bar)**: "`bg-brand-blue-500` with top `h-1.5 bg-brand-yellow-500 shadow-brand-yellow-500/30`. Mesh gradients + grid pattern. Four-column grid: Brand (logo + tagline + social icons), Services (nested links with yellow zap icons), Contact (info cards `bg-brand-blue-500/80 border-white/15` with mono phone/email), Legal links. Back-to-top yellow pill fixed bottom-right."

### Motion & Interaction Specs
- **Spring Physics**: `stiffness: 100, damping: 20` (cubic-bezier(0, 0, .2, 1)) — no bounce/elastic
- **Transitions**: `--default-transition-duration: .15s`, `--default-transition-timing-function: cubic-bezier(.4, 0, .2, 1)`
- **Hover Lift**: `hover:-translate-y-1.5` (cards), `hover:translate-x-1` (links), icon shift 4px (nested pills)
- **Focus Visible**: `focus-visible:ring-2 focus-visible:ring-brand-yellow-500` (on blue), `focus-visible:ring-brand-blue-500` (on light)
- **Reduced Motion**: All `animate-*` wrapped in `motion-safe:`, `motion-reduce:animate-none` for ping/pulse. Checked via `window.matchMedia('(prefers-reduced-motion: reduce)').matches` in inline JS.
- **Scroll Header**: Passive listener, toggles `bg-brand-blue-500/95 backdrop-blur-md shadow-elevated border-b border-white/10 py-2.5` at `scrollY > 20px`

### Anti-Patterns (Never Do)
- ❌ Raw hex in markup — always semantic tokens
- ❌ Black, Tailwind grays, green (except WhatsApp SVG), purple/cyan gradients
- ❌ Two blue sections consecutively
- ❌ Hero on white/ice/mist
- ❌ Shadows on blue — use translucent white layers + top highlight
- ❌ Title Case, English copy, "usted" — voseo rioplatense mandatory
- ❌ Hardcoded prices — source from `llms.txt`
- ❌ Missing `tabular-nums` on prices/distances/phones
- ❌ Text below 11px
- ❌ Emojis in UI — Lucide icons only
- ❌ Clichés: "Elevá tu logística", "Seamless", "Next-Gen", generic names
- ❌ Metrics/testimonials without source — use `[métrica]` or "A VERIFICAR"
- ❌ Content stuck at `opacity: 0`

### Verification Checklist
- [ ] Hero is blue or yellow; next section is white
- [ ] No two blue sections in a row
- [ ] All colors use semantic tokens (no raw hex)
- [ ] Text contrasts pass (check `white/80`, `brand-blue-100`, `brand-blue-400` on blue — they fail)
- [ ] Voseo rioplatense throughout
- [ ] Prices match `llms.txt`
- [ ] `tabular-nums` on all prices/distances/phones
- [ ] `prefers-reduced-motion` respected
- [ ] Tested at 390px and 1280px