# -*- coding: utf-8 -*-
"""Build de paginas/paginas_html:
   1) (--pilot) genera _pilot.html de prueba desde la plantilla
   2) compila Tailwind por pagina (v4 CLI) y le inyecta el CSS entre /*CSS-START*//*CSS-END*/
   3) verifica marcadores y residuos de JSX
"""
import os, re, subprocess, sys, glob

BASE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(BASE, "..", "paginas_html")
OUT = os.path.join(BASE, "out")
CSS_RE = re.compile(r"/\*CSS-START\*/.*?/\*CSS-END\*/", re.S)


def build_page_input(html_path):
    rel = os.path.relpath(html_path, BASE).replace("\\", "/")
    p = os.path.join(BASE, ".page_input.css")
    with open(p, "w", encoding="utf-8") as f:
        f.write('@import "tailwindcss";\n@import "./globals.css";\n@source "%s";\n' % rel)
    return p


def compile_css(html_path):
    os.makedirs(OUT, exist_ok=True)
    inp = build_page_input(html_path)
    outp = os.path.join(OUT, os.path.splitext(os.path.basename(html_path))[0] + ".css")
    r = subprocess.run(["npx", "tailwindcss", "-i", inp, "-o", outp, "--minify"],
                       cwd=BASE, capture_output=True, text=True, shell=True)
    if not os.path.exists(outp):
        print("  FALLO tailwind:", (r.stdout + r.stderr)[:400])
        return None
    with open(outp, encoding="utf-8") as f:
        return f.read()


def inject(html_path, css):
    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    if not CSS_RE.search(html):
        return False, "sin marcadores CSS"
    block = "/*CSS-START*/\n" + css + "\n/*CSS-END*/"
    html = CSS_RE.sub(lambda m: block, html, count=1)
    with open(html_path, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    return True, len(css)


def gen_pilot():
    with open(os.path.join(BASE, "plantilla.html"), encoding="utf-8") as f:
        tpl = f.read()
    with open(os.path.join(BASE, "pilot_main.html"), encoding="utf-8") as f:
        main = f.read()
    html = (tpl.replace("@@TITLE@@", "Piloto de validacion")
                .replace("@@DESC@@", "Pagina piloto para validar el pipeline de build.")
                .replace("@@RUTA@@", "")
                .replace("@@HEAD_EXTRA@@", "")
                .replace("@@PAGE_JS@@", ""))
    html = html.replace("@@MAIN@@", main)
    leftover = re.findall(r"@@\w+@@", html)
    if leftover:
        print("  piloto con marcadores sobrantes:", set(leftover))
    os.makedirs(PAGES, exist_ok=True)
    dst = os.path.join(PAGES, "_pilot.html")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    print("  piloto ->", dst, len(html), "bytes")
    return dst


def verify():
    files = sorted(glob.glob(os.path.join(PAGES, "*.html")))
    print("paginas:", len(files))
    bad_tokens = ["className", "lucide-react", "react-icons", "next/image", "motion.",
                  "useState", "=> {", "<Image", "@@MAIN@@", "@@TITLE@@"]
    for p in files:
        with open(p, encoding="utf-8") as f:
            h = f.read()
        name = os.path.basename(p)
        marks = set(re.findall(r"@@\w+@@", h))
        resid = [t for t in bad_tokens if t in h]
        has_css = bool(CSS_RE.search(h)) and "/*CSS-START*/" in h
        css_len = 0
        m = CSS_RE.search(h)
        if m:
            css_len = len(m.group(0))
        print(f"  {name:45s} {len(h):>9d}b css={css_len:>7d} doctype={'<!doctype' in h.lower()} "
              f"script={'</script>' in h} marks={sorted(marks) or '-'} resid={resid or '-'}")
    return files


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--pilot" in args:
        print("[1] generando piloto")
        gen_pilot()
    if "--no-css" not in args:
        print("[2] compilando + inyectando CSS por pagina")
        for p in sorted(glob.glob(os.path.join(PAGES, "*.html"))):
            css = compile_css(p)
            if css is None:
                continue
            ok, info = inject(p, css)
            print(f"  {os.path.basename(p):45s} {'OK' if ok else 'SIN-MARCADORES'} {info}")
    print("[3] verificacion")
    verify()
