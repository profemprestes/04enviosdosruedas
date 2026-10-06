import os

files = [
    "scrapeado/index.html",
    "scrapeado/contacto.html",
    "scrapeado/cotizar.html",
    "scrapeado/servicios-enviosflex.html",
    "scrapeado/servicios-fulfillment.html",
    "scrapeado/servicios-lowcost.html",
    "scrapeado/servicios-express.html",
    "scrapeado/servicios-contrareembolso.html",
    "scrapeado/servicios-plan-emprendedores.html",
    "scrapeado/guias-envios-flex.html",
    "scrapeado/nosotros.html",
    "scrapeado/preguntas-frecuentes.html",
    "scrapeado/redes.html",
    "scrapeado/terminos-y-condiciones.html",
    "scrapeado/politica-de-privacidad.html",
]

for f in files:
    if os.path.exists(f):
        size = os.path.getsize(f)
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read(500)
        has_style = '<style>' in content
        has_script = '<script>' in content
        has_doctype = content.strip().startswith('<!DOCTYPE html>')
        print(f"{f}: {size/1024:.1f}KB | DOCTYPE: {has_doctype} | <style>: {has_style} | <script>: {has_script}")
    else:
        print(f"{f}: MISSING")