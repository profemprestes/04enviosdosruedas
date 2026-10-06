# -*- coding: utf-8 -*-
"""Ensambla paginas/paginas_html/<slug>.html a partir de la plantilla compartida
y fragmentos por pagina guardados en paginas/_build/pages/:

    <slug>.json       -> { "title": ..., "desc": ..., "ruta": ... }
    <slug>.main.html  -> contenido principal (lo que va dentro de <main>)
    <slug>.head.html  -> (opcional) JSON-LD, metas extra y <style> propio
    <slug>.js.html    -> (opcional) JS propio de la pagina

El CSS compilado se inyecta despues con build.py (marcadores CSS-START/CSS-END
quedan intactos).

Uso:  python assemble.py <slug> [<slug> ...]
      python assemble.py --all
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(BASE, "plantilla.html")
PAGES_DIR = os.path.join(BASE, "pages")
OUT_DIR = os.path.abspath(os.path.join(BASE, "..", "paginas_html"))
MARKERS = ("@@TITLE@@", "@@DESC@@", "@@RUTA@@", "@@HEAD_EXTRA@@", "@@MAIN@@", "@@PAGE_JS@@")


def _read(path, default=""):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return f.read()


def assemble(slug):
    cfg_path = os.path.join(PAGES_DIR, slug + ".json")
    main_path = os.path.join(PAGES_DIR, slug + ".main.html")
    if not os.path.exists(cfg_path):
        print("  [%s] FALTA %s" % (slug, cfg_path))
        return None
    if not os.path.exists(main_path):
        print("  [%s] FALTA %s" % (slug, main_path))
        return None

    cfg = json.loads(_read(cfg_path))
    head = _read(os.path.join(PAGES_DIR, slug + ".head.html"))
    main = _read(main_path)
    js = _read(os.path.join(PAGES_DIR, slug + ".js.html"))

    with open(TPL, encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("@@TITLE@@", cfg["title"])
    tpl = tpl.replace("@@DESC@@", cfg["desc"])
    tpl = tpl.replace("@@RUTA@@", cfg.get("ruta", ""))
    tpl = tpl.replace("@@HEAD_EXTRA@@", head)
    tpl = tpl.replace("@@MAIN@@", main)
    tpl = tpl.replace("@@PAGE_JS@@", js)

    leftover = sorted(set(re.findall(r"@@[A-Z_]+@@", tpl)))
    if leftover:
        print("  [%s] AVISO marcadores sin reemplazar: %s" % (slug, leftover))

    problems = []
    if len(main.strip()) < 400:
        problems.append("main muy corto (%d bytes)" % len(main))
    if main.count("<div") != main.count("</div>"):
        problems.append("divs desbalanceados en main (%d/%d)" % (main.count("<div"), main.count("</div>")))
    if main.count("<section") != main.count("</section>"):
        problems.append("sections desbalanceadas (%d/%d)" % (main.count("<section"), main.count("</section>")))
    if "<h1" not in head and "<h1" not in main:
        problems.append("sin <h1>")

    os.makedirs(OUT_DIR, exist_ok=True)
    dst = os.path.join(OUT_DIR, slug + ".html")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(tpl)
    flag = ("  (%s)" % "; ".join(problems)) if problems else ""
    print("  [%s] -> %s  %d bytes%s" % (slug, dst, len(tpl), flag))
    return dst


if __name__ == "__main__":
    args = sys.argv[1:]
    slugs = []
    if not args or "--all" in args:
        slugs = sorted(
            f[:-5] for f in os.listdir(PAGES_DIR) if f.endswith(".json")
        ) if os.path.isdir(PAGES_DIR) else []
    else:
        slugs = args
    print("ensamblando %d paginas" % len(slugs))
    for s in slugs:
        assemble(s)