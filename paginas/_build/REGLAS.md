# REGLAS — Generación de páginas HTML autocontenidas

Convertís **un solo** archivo `.md` (la spec de una página) en **un solo** HTML autocontenido.

## 0. Tu tarea exacta

1. Leé `paginas/_build/plantilla.html` (es la plantilla compartida: `<head>`, sprite SVG, header, drawer móvil, carrusel de redes, footer, JS compartido). No la modificás: la copiás y reemplazás marcadores.
2. Leé **tu** spec en `paginas/<archivo>.md`:
   - **§1 "page.tsx"** y **§2 "Componentes"** = tu contenido. Es lo que tenés que convertir.
   - **§3 "Layout compartido / globals.css / pricing / promises"** = ya está aplicado en la plantilla. **Ignoralo** (salvo para copiar valores de `pricing.ts`/`promises.ts` si §1 los referencia, o tokens de `globals.css` si necesitás un color/sombra puntual).
3. Escribís el resultado en `paginas/paginas_html/<TU_ARCHIVO>.html` (completo, desde `<!doctype html>` hasta `</html>`).

**No** uses el subdirectorio `_build`, **no** edites la plantilla, **no** toques otras páginas.

## 1. Marcadores a reemplazar (todos, en TODAS sus ocurrencias)

| Marcador | Ocurrencias | Qué poner |
|---|---|---|
| `@@TITLE@@` | 3 (`<title>`, og, twitter) | Título SEO de §1 (sin el sufijo `\| Envíos DosRuedas` si ya lo trae el `title` de §1; la plantilla no lo agrega, usá el title completo del md) |
| `@@DESC@@` | 3 (description, og, twitter) | Meta description de §1, plano, sin comillas dobles ni HTML |
| `@@RUTA@@` | 2 (canonical, og:url) | Ruta SIN `/` inicial y SIN `.html`: `servicios/envios-express`, `nosotros/sobre-nosotros`. En home: vacío (queda `https://www.enviosdosruedas.com/`) |
| `@@HEAD_EXTRA@@` | 1 | JSON-LD de la página (BreadcrumbList / Service / FAQPage / ContactPage…), meta extra, `<style>` con CSS propio de la página |
| `@@MAIN@@` | 1 | El contenido `<main>` de la página (§1 renderizada) |
| `@@PAGE_JS@@` | 1 | El JS de interacciones de la página (tabs, accordion, cotizador, etc.) |

Usá `edit` con `replaceAll: true` para `@@TITLE@@` / `@@DESC@@` / `@@RUTA@@`.
Al terminar **no puede quedar ningún `@@`**, con **una única excepción**: el par de marcadores `/*CSS-START*/` … `/*CSS-END*/` dentro del `<style>` del head — esos **quedan intactos y vacíos** (es el hueco donde el build inyecta el CSS compilado al final).

## 1.1 Encoding (IMPORTANTE)

- Escribí los archivos **sólo** con las herramientas `write`/`edit` (producen UTF-8 correcto).
- **No** uses `Get-Content`/`Set-Content` de PowerShell sobre estos HTML: destruye los acentos (mojibake). Si necesitás manipular texto por script, usá Python con `open(..., encoding='utf-8')`.


## 2. Convenciones TSX → HTML

- `className="..."` → `class="..."`. Nada de `{ }`, `=>`, `useState`, `motion.`, `<Image`, `next/image`, `lucide-react`, `react-icons` en el HTML final.
- Componentes funcionales de §2 (p. ej. `<HeroSeccion/>`, `<SeccionTarifas/>`): **inliná su JSX ya resuelto**, sustituyendo sus props por los valores literales que §1 les pasa.
- Expresiones JSX `{cond ? 'a' : 'b'}` → resolvé y dejá el resultado final.
- `{t('clave')}` / objetos de traducción → texto literal en español (el sitio es monolingüe es-AR).
- `<Image src="/heroes/x.webp" …>` o `src="_next/image?url=%2Fheroes%2Fx.webp"` → `<img src="../../public/heroes/x.webp" alt="…" width="…" height="…" loading="lazy" decoding="async">`.
  - Verificá que el archivo exista en `paginas/_build/assets_manifest.txt`. Si **no existe**, usá la URL absoluta `https://www.enviosdosruedas.com/<ruta>`.
  - Decodificá `%2F` → `/`, `%20` → espacio.
- `href="/ruta"` → ver **§3 Mapa de links** (relativo, con `.html`).
- `target="_blank"` → siempre `rel="noopener noreferrer"`.
- Inputs: agregá `name` e `id`; los `<label>` con `htmlFor` → `for`.

## 3. Mapa de links (obligatorio)

| En el md | En tu HTML |
|---|---|
| `/` | `index.html` |
| `/contacto` | `contacto.html` |
| `/cotizar` | `cotizar.html` |
| `/nosotros` | `nosotros.html` |
| `/nosotros/sobre-nosotros` | `nosotros-sobre-nosotros.html` |
| `/nosotros/preguntas-frecuentes` | `nosotros-preguntas-frecuentes.html` |
| `/nosotros/nuestras-redes` | `nosotros-nuestras-redes.html` |
| `/terminos-y-condiciones` | `terminos-y-condiciones.html` |
| `/politica-de-privacidad` | `politica-de-privacidad.html` |
| `/servicios/envios-express` | `servicios-envios-express.html` |
| `/servicios/envios-lowcost` | `servicios-envios-lowcost.html` |
| `/servicios/enviosflex` | `servicios-enviosflex.html` |
| `/servicios/empresas-cuenta-corriente` | `servicios-empresas-cuenta-corriente.html` |
| `/servicios/deposito-fulfillment` | `servicios-deposito-fulfillment.html` |
| `/servicios/envios-contrareembolso` | `servicios-envios-contrareembolso.html` |
| `/servicios/plan-emprendedores` | `servicios-plan-emprendedores.html` |
| `/servicios` (índice, no existe spec) | `https://www.enviosdosruedas.com/servicios` (absoluto) |
| `/cobertura`, `/guias/...` | URL absoluta `https://www.enviosdosruedas.com/...` |
| `#ancla` interna | `archivo.html#ancla` o `#ancla` si es de tu propia página |

Rutas relativas a la raíz de la carpeta: los HTML viven en `paginas/paginas_html/` y **todos están en el mismo nivel**, por eso los links son planos (`contacto.html`), nunca `/contacto` ni `../`.

## 4. Iconos

Ya hay un sprite SVG inline al principio del `<body>` con 126 símbolos. Lista exacta de ids: `paginas/_build/iconos.txt`.

- Lucide `<Zap className="h-4 w-4 text-brand-yellow-500"/>` →
  `<svg class="h-4 w-4 text-brand-yellow-500" aria-hidden="true"><use href="#i-zap"></use></svg>`
- Marcas: `#i-facebook`, `#i-instagram`, `#i-whatsapp` (relleno, para logo/branding).
- Si el id **no existe**, inlineá el SVG completo:
  `<svg xmlns="http://www.w3.org/2000/svg" class="…" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">…paths…</svg>`
- Los `className` de los iconos (tamaño/color) van tal cual en el `<svg>` contenedor.

## 5. Animaciones / motion (framer-motion → CSS/JS)

- **Nunca** dejes contenido con `opacity: 0` inicial o `hidden` que dependa de JS: todo tiene que verse si el JS falla.
- Entradas on-scroll: `data-reveal` en el elemento (la plantilla ya tiene IntersectionObserver + CSS) y, si querés escalonar, `style="transition-delay:.15s"`.
- Staggers / whileInView de framer → `data-reveal` + `style="transition-delay:…"` en cada hijo.
- `whileHover={{ y: -5, scale: 1.03 }}` → `transition-all hover:-translate-y-1 hover:scale-[1.03]` (o las clases hover que ya traiga el md).
- Bucles (`animate={{ y: [0, -10, 0] }}`, ping, pulse, marquee) → usá clases ya disponibles en globals:
  `animate-floaty`, `animate-ping`, `animate-pulse`, `animate-bounce`, `animate-pulse-ring`,
  `animate-radar`, `animate-draw`, `animate-marquee-left`, `animate-marquee-right`, `animate-grow-x`,
  `animate-road`, `animate-roundtrip`, `animate-shuttle`.
  Si necesitás otra, defilá `@keyframes` + clase en `@@HEAD_EXTRA@@`.
- Transiciones cortas: `duration-200`/`duration-300`; springs de motion (`stiffness 100-300, damping 20-30`) ≈ `cubic-bezier(.25,.8,.25,1)`.
- Respetá `prefers-reduced-motion` si agregás animación propia (medio query con `animation: none`).

## 6. Componentes compartidos (definidos por globals.css — sólo clases, ya compiladas)

- **CTA pill**: `class="cta-nested-pill group inline-flex items-center justify-between gap-3 rounded-full font-subheading uppercase tracking-wider font-bold transition-all duration-200 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-500 focus-visible:ring-offset-2 select-none border"` + variante:
  - primaria: `px-8 py-3 text-base min-h-13 bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-500 shadow-accent-sm hover:shadow-cta-glow hover:bg-brand-yellow-400 active:scale-98 active:translate-y-px`
  - chip final: `<span class="cta-nested-icon w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-all duration-200 bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-brand-yellow-500 group-hover:translate-x-1"><svg class="w-4 h-4" aria-hidden="true"><use href="#i-arrow-right"></use></svg></span>`
  (Ver ejemplos exactos dentro de la plantilla: pill del drawer y del banner del footer.)
- **Double bezel card**: `<div class="double-bezel-outer"><div class="double-bezel-inner p-6">…</div></div>` (los tokens `--color-*` ya están en globals).
- **Eyebrow**: `px-3 py-1 rounded-full text-xs font-subheading font-bold uppercase tracking-widest` (copiá las variantes tal cual del md).
- **Tipografía**: `font-display` (Anton, headings), `font-subheading` (Bebas, labels/botones), `font-sans` (Outfit, cuerpo), `font-mono` (Geist Mono, números). Números/tabular: `tabular-nums`.
- Los `@utility` disponibles (copialos tal cual del md si los ves): `text-display`, `text-h1`, `text-h2`, `double-bezel-outer`, `double-bezel-inner`, `cta-nested-pill`, `cta-nested-icon`, `kinetic-font-stretch`, `no-scrollbar`, `is-paused`.

## 7. Layout de tu contenido

- La plantilla ya abre `<main id="main-content" class="grow pt-18">` y cierra `</main>`: **tu `@@MAIN@@` va adentro**, sin re-declarar `<main>`, header, footer, nav ni carrusel.
- Arrancá directo con tu hero/sección. El hero del sitio va con clase `bg-brand-blue-700`/`bg-brand-blue-600`… (copiá las del md).
- Máximos de contenido: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8` (patrón del sitio).
- Secciones alternan `bg-white` / `bg-brand-blue-50` / `bg-brand-blue-700`… — **respetá el orden del md**, no lo reordenes.

## 8. Accesibilidad / calidad mínima

- Un solo `<h1>` por página; jerarquía sin saltos.
- `alt` en toda imagen decorativa puede ser `""` + `aria-hidden="true"`.
- Botones accionables → `<button type="button">`; sólo enlaces reales → `<a>`.
- Acordeones/tabs: `aria-expanded`, `aria-controls`, `role="tablist"` cuando aplique.
- El JS de tu página va dentro de `@@PAGE_JS@@` en un IIFE `('use strict')`, con `document.addEventListener('DOMContentLoaded', …)` si querés (el script corre al final del body igual).
- Para acordeones existen las clases genéricas: item `[data-acc]` con botón `[data-acc-btn]` y panel `.acc-panel` (contenedor con `data-acc-single` para abrir uno a la vez). Mirá su CSS en la plantilla.

## 9. Verificación final antes de responder

Checklist (hacelo con grep sobre tu archivo):
- [ ] No quedó ningún `@@`.
- [ ] No quedó `className`, `=> `, `<Image`, `motion.`, `useState`, `lucide-react`, `react-icons`, `next/`.
- [ ] Ningún href con `/ruta` de Next (todo resuelto con el §3).
- [ ] Ninguna imagen `/heroes/...` o `_next/image` sin resolver.
- [ ] Los `src` de imagen apuntan a `../../public/…` y existen en `assets_manifest.txt` (o URL absoluta del sitio).
- [ ] Tiene `<style>` del CSS propio y `<script>` de JS propios **dentro** de los marcadores correspondientes (si los hay).
- [ ] HTML bien cerrado (balanceá `<div>`/`</div>` de las secciones que escribiste).

Reportá al final: archivo generado, nº de secciones, dudas/decisiones tomadas (p. ej. "el md no traía X, usé Y"), y cualquier cosa que haya quedado pendiente.
