# AGENTS.md — Envíos DosRuedas Static Site

## Project Overview
Static HTML website for **Envíos DosRuedas** — motorcycle courier & last-mile logistics in Mar del Plata, Argentina. No build step, no package manager, no CI/CD. Deployed as static files.

## Structure
```
html/           # All HTML pages (13 pages: home, servicios/*, nosotros/*, contacto)
public/         # Assets: images, logos, manifest.json, llms.txt, llms-full.txt
```

## Key Conventions (from dosruedas-brand-system)

### Brand Palette (3 colors only)
- **Blue**: `#0950F6` — darkest allowed blue. No navy, no `#0636A5`, no darker shades.
- **Yellow**: `#FFEC01` — accent only (CTAs, badges, hero backgrounds)
- **White**: `#FFFFFF`

**Tokens** (Tailwind v4 `@theme` in each HTML's `<style>` block):
- `brand-blue-25` (`bg-ice`) `#F3F7FF` — section background "ice"
- `brand-blue-50` (`bg-mist`) `#E6EEFE` — card surfaces, secondary text on blue
- `brand-blue-100` (`border-line`) `#BACEFD` — decorative borders only
- `brand-blue-300` (`border-line-strong`) `#628FF9` — input borders
- `brand-blue-450` (`text-ink-muted`) `#1D5EF7` — secondary text on light, hover on blue buttons
- `brand-blue-500` (`text-ink`, `bg-brand-blue-500`) `#0950F6` — primary blue
- `brand-yellow-500` (`bg-accent`) `#FFEC01` — CTA background, knockout, hero accent
- `text-danger` `#DC2626` — error text only

**Never use**: raw hex in markup, black, Tailwind grays, green (except WhatsApp icon), purple/cyan gradients.

### Typography
| Role | Font | Treatment |
|------|------|-----------|
| H1/H2, impact numbers | Anton | Uppercase, tracking-negative, `text-wrap: balance` |
| H3, buttons, labels, nav | Bebas Neue | Uppercase, tracking-wide, min 13px |
| Body & UI | Outfit | Sentence case, 16–20px, leading 1.6 |
| Prices, distances, times, phones | Geist Mono | `tabular-nums` always |

Minimum text size: 11px (`text-2xs`). No 9/10px. No Inter, system fonts, Title Case, English copy.

### Component Primitives (reuse, don't reinvent)
- **Knockout (−1°)**: rotated capsule with keyword — `tone="yellow"` on blue, `tone="blue"` on yellow
- **CTA Nested Pill** (`.cta-nested-pill`): round, icon shifts 4px on hover. Sizes: `sm` 44px, default 48px, `lg` 56px. Variants: `outline` (light), `ghost` (on blue), `blue` (on yellow)
- **Double Bezel Card**: mist shell (`#BACEFD` border) + white core. On blue: glass white shell + translucent white core. `.is-featured` = yellow core
- **Eyebrow** (`.eyebrow` yellow) / **Eyebrow soft** (`.eyebrow-soft`) before H2s
- **Radar/route tracer**: yellow pulsing rings & dotted routes from real pins (Friuli 1972, zones). Never decorative.
- **Ghost wordmark**: "Envíos Dos Ruedas" at 4–6% opacity behind hero

### Layout Rules
- Hero **always** blue or yellow surface (`.surface-blue` or `.surface-accent`), never white/ice/mist
- Next section after hero is always white (`.surface-page`)
- Never two blue sections consecutively — alternate: blue → white/ice → blue → mist → accent band before footer
- Shadows on light: blue-tinted `rgba(9,80,246,α)` or yellow `rgba(255,236,1,α)` — never black
- On blue: elevation via white translucent layers (`white/8`–`white/12`) + top highlight, not shadows

### Copy Rules
- **Voseo rioplatense mandatory**: "Cotizá", "Enviá" — never "usted"
- Real Mar del Plata anchors: Friuli 1972, General Pueyrredón, Batán, Zona Güemes, Playa Grande
- Prices/hours/weights from `llms.txt` — never hardcode
- No metrics/testimonials/names without source. Use `[métrica]` or "A VERIFICAR" if missing
- No emojis in UI/copy (Lucide icons only)
- No clichés: "Elevá tu logística", "Seamless", "Next-Gen", generic names

### Motion & Accessibility
- Springs: `stiffness: 100, damping: 20` — no bounce/elastic
- Respect `prefers-reduced-motion` (checked in inline JS)
- No content stuck at `opacity: 0`
- WCAG contrasts verified in brand system

## Development Workflow

### Editing Pages
Each HTML file is **self-contained** with:
- Inlined Tailwind v4 CSS (entire framework in `<style>`)
- Inlined navigation data (`window.__NAV`) + header/nav JS
- SVG sprite for icons
- Schema.org JSON-LD

**To change shared UI (header, nav, footer, tokens)**: edit every HTML file. There is no templating or include system.

### Common Tasks
| Task | How |
|------|-----|
| Update brand token | Edit `@layer theme` in `<style>` of **every** HTML file |
| Add navigation item | Update `window.__NAV` array in **every** HTML file |
| Change hero image | Replace file in `public/heroes/` or `public/elementos/`, update `<img src>` |
| Add new page | Copy existing HTML, update title/meta/content, add to `window.__NAV` in all files |
| Update prices/hours | Edit `public/llms.txt` + `public/llms-full.txt` + every HTML with hardcoded prices |

### Verification Checklist (before considering done)
- [ ] Hero is blue or yellow; next section is white
- [ ] No two blue sections in a row
- [ ] All colors use semantic tokens (no raw hex)
- [ ] Text contrasts pass (check `white/80`, `brand-blue-100`, `brand-blue-400` on blue — they fail)
- [ ] Voseo rioplatense throughout
- [ ] Prices match `llms.txt`
- [ ] `tabular-nums` on all prices/distances/phones
- [ ] `prefers-reduced-motion` respected
- [ ] Tested at 390px and 1280px

## Assets
- `public/manifest.json` — PWA manifest (update shortcuts if adding pages)
- `public/llms.txt` / `llms-full.txt` — LLM knowledge base (prices, services, policies) — **source of truth for copy**
- `public/elementos/` — UI illustrations (knockout pieces, icons, hero elements)
- `public/heroes/` — Hero background images per service
- `public/cards/` — Service card backgrounds
- `public/redes/`, `public/assets/` — Social media assets

## Deployment
Static hosting (Netlify, Vercel, Cloudflare Pages, GitHub Pages, or any static host). No build command. Publish `html/` as root or configure rewrites for `.html` extension.

## Related Instruction Files
- `public/llms.txt` — Authoritative service data, prices, policies, red lines
- `dosruedas-brand-system` skill — Full design system (colors, components, anti-patterns, 3D kit)
- `rebrand-envios` skill — Generates prompts to adapt HTML to brand colors