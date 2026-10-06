import os
import re

files = [
    "scrapeado/index.html",
    "scrapeado/contacto.html",
    "scrapeado/cotizar.html",
    "scrapeado/servicios-enviosflex.html",
    "scrapeado/nosotros.html",
    "scrapeado/preguntas-frecuentes.html",
    "scrapeado/terminos-y-condiciones.html",
]

# Check that no absolute internal URLs remain
internal_paths = [
    '/contacto', '/cotizar', '/servicios/enviosflex', '/servicios/deposito-fulfillment',
    '/servicios/envios-lowcost', '/servicios/envios-express', '/servicios/envios-contrareembolso',
    '/servicios/plan-emprendedores', '/guias/envios-flex-mar-del-plata', '/nosotros/sobre-nosotros',
    '/nosotros/preguntas-frecuentes', '/nosotros/nuestras-redes', '/terminos-y-condiciones',
    '/politica-de-privacidad', '/servicios/empresas-cuenta-corriente', '/cobertura', '/guias/',
    '/nosotros/', '/servicios/'
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Check for unreplaced internal links
        found = []
        for path in internal_paths:
            for quote in ['"', "'"]:
                if f'href={quote}{path}{quote}' in content or f'href={quote}{path}/{quote}' in content:
                    found.append(f'href={quote}{path}{quote}')
        if found:
            print(f"{f}: STILL HAS internal links: {found[:3]}")
        else:
            print(f"{f}: OK - all internal links rewritten")
        # Check for local file links
        local_found = []
        for path in ['index.html', 'contacto.html', 'cotizar.html', 'servicios-enviosflex.html', 
                      'servicios-fulfillment.html', 'servicios-lowcost.html', 'servicios-express.html',
                      'servicios-contrareembolso.html', 'servicios-plan-emprendedores.html',
                      'guias-envios-flex.html', 'nosotros.html', 'preguntas-frecuentes.html',
                      'redes.html', 'terminos-y-condiciones.html', 'politica-de-privacidad.html']:
            if f'href="{path}"' in content or f"href='{path}'" in content:
                local_found.append(path)
        if local_found:
            print(f"  -> Local links found: {local_found[:5]}")