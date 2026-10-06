# GUIA — Cómo generar UNA página (flujo por fragmentos)

Convertís **una** spec `.md` de `paginas/` en **fragmentos**; un script los ensambla con la plantilla compartida y produce el HTML final. **No** copies/pegues la plantilla ni el header/footer/sprite.

## Paso 1 — Leer
1. `paginas/_build/REGLAS.md` → convenciones de conversión TSX→HTML, mapa de links, iconos, assets, motion, componentes. **Obligatorio.**
2. Tu spec: `paginas/<archivo>.md`. Usá **§1 (page.tsx)** y **§2 (componentes propios)**. Ignorá **§3 (layout/globals compartidos)** — ya está en la plantilla.
3. Consultas: `paginas/_build/iconos.txt` (ids de sprite), `paginas/_build/assets_manifest.txt` (assets disponibles en `public/`).

## Paso 2 — Escribir tus 3 archivos en `paginas/_build/pages/`

Con las herramientas `write`/`edit` (UTF-8 correcto; **nunca** `Get-Content`/`Set-Content` de PowerShell).

### `<slug>.json`
```json
{
  "title": "<title SEO completo (como en §1, sin repetir si ya trae '| Envíos DosRuedas')>",
  "desc": "<meta description de §1, texto plano>",
  "ruta": "<ruta sin slash inicial ni .html, ej: servicios/envios-express; home = ''>"
}
```

### `<slug>.main.html`
Sólo el contenido interno de `<main>` (una o más `<section>`), sin `<main>`, `<header>`, `<footer>` ni `<html>`.
- El `<h1>` de la página va acá.
- Clases Tailwind tal cual salen del md.

### `<slug>.head.html` (opcional)
JSON-LD de la página, metas extra y `<style>` propio si necesitás CSS a medida.

### `<slug>.js.html` (opcional)
JS de interacciones (tabs, accordion, cotizador) en un IIFE. Nunca dejes contenido invisible si el JS falla.

## Paso 3 — Ensamblar y verificar
```bash
cd paginas/_build
python assemble.py <slug>
```
Esto escribe `paginas/paginas_html/<slug>.html` (con los marcadores `/*CSS-START*/ … /*CSS-END*/` intactos; el CSS se inyecta después con `build.py`).

Si imprime avisos (marcadores sin reemplazar, divs desbalanceados, sin `<h1>`), corregí y volvé a correr.

## Mapa slug ↔ archivo

| spec | slug / salida |
|---|---|
| `home.md` | `index` |
| `contacto.md` | `contacto` |
| `cotizar.md` | `cotizar` |
| `nosotros.md` | `nosotros` |
| `nosotros-sobre-nosotros.md` | `nosotros-sobre-nosotros` |
| `nosotros-preguntas-frecuentes.md` | `nosotros-preguntas-frecuentes` |
| `nosotros-nuestras-redes.md` | `nosotros-nuestras-redes` |
| `terminos-y-condiciones.md` | `terminos-y-condiciones` |
| `politica-de-privacidad.md` | `politica-de-privacidad` |
| `servicios-envios-express.md` | `servicios-envios-express` |
| `servicios-envios-lowcost.md` | `servicios-envios-lowcost` |
| `servicios-enviosflex.md` | `servicios-enviosflex` |
| `servicios-empresas-cuenta-corriente.md` | `servicios-empresas-cuenta-corriente` |
| `servicios-deposito-fulfillment.md` | `servicios-deposito-fulfillment` |
| `servicios-envios-contrareembolso.md` | `servicios-envios-contrareembolso` |
| `servicios-plan-emprendedores.md` | `servicios-plan-emprendedores` |

## Reglas de oro
- **Un solo `<h1>`**; jerarquía de headings sin saltos.
- **Hero** con `data-reveal` opcional; nunca dejar nada en `opacity:0` sin JS.
- Assets: `src="../../public/<ruta>"` (verificar en `assets_manifest.txt`); si no existe, `https://www.enviosdosruedas.com/<ruta>`.
- Links internos según el mapa de REGLAS.md (archivos planos: `contacto.html`, `servicios-envios-express.html`, …). `/servicios` (índice sin spec) → `https://www.enviosdosruedas.com/servicios`.
- Iconos vía sprite: `<svg class="h-4 w-4" aria-hidden="true"><use href="#i-zap"></use></svg>`.
- Voseo rioplatense (viene en el md); no inventar datos ni métricas.
- Al terminar, reportá: slug, secciones, decisiones dudosas y cualquier dato faltante en el md.