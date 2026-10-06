import re
with open('scrapeado/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Check a few specific links
for path in ['href="/"', 'href="/contacto"', 'href="/cotizar"', 'href="/servicios/enviosflex"']:
    if path in content:
        print(f"FOUND (NOT REPLACED): {path}")
    else:
        print(f"NOT FOUND (replaced?): {path}")
# Check for local file links
for path in ['href="index.html"', 'href="contacto.html"', 'href="cotizar.html"', 'href="servicios-enviosflex.html"']:
    if path in content:
        print(f"LOCAL LINK FOUND: {path}")