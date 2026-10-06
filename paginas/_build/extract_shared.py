"""Extrae globals.css (bloque de estilos globales) y componentes UI compartidos desde home.md."""
import re, os, io

BASE = os.path.dirname(os.path.abspath(__file__))
home = io.open(os.path.join(BASE, "..", "home.md"), encoding="utf-8").read()

# 1) globals.css
m = re.search(r"### Global CSS Styles & Design Tokens.*?```css\n(.*?)```", home, re.DOTALL)
css = m.group(1)
# quita @import tailwindcss (lo provee el CLI) — se deja igual, el CLI lo resuelve
open(os.path.join(BASE, "globals.css"), "w", encoding="utf-8").write(css)
print("globals.css:", len(css), "bytes")

# 2) componentes UI compartidos que usan varias paginas
comps = ["CTANestedPill", "Knockout", "Badge", "DoubleBezelCard", "HeroProceduralBackground", "index.ts"]
for c in comps:
    mm = re.search(r"### Componente: `src/components/ui/" + re.escape(c) + r"`\n\n```tsx\n(.*?)```", home, re.DOTALL)
    if mm:
        open(os.path.join(BASE, f"ui_{c.replace('.', '_')}.tsx"), "w", encoding="utf-8").write(mm.group(1))
        print(f"ui_{c}:", len(mm.group(1)), "bytes")
    else:
        print("NO ENCONTRADO:", c)
