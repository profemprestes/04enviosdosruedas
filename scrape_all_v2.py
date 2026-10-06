import asyncio
import os
import re
from playwright.async_api import async_playwright

URLS = [
    ("https://www.enviosdosruedas.com/", "scrapeado/index.html"),
    ("https://www.enviosdosruedas.com/contacto", "scrapeado/contacto.html"),
    ("https://www.enviosdosruedas.com/cotizar", "scrapeado/cotizar.html"),
    ("https://www.enviosdosruedas.com/servicios/enviosflex", "scrapeado/servicios-enviosflex.html"),
    ("https://www.enviosdosruedas.com/servicios/deposito-fulfillment", "scrapeado/servicios-fulfillment.html"),
    ("https://www.enviosdosruedas.com/servicios/envios-lowcost", "scrapeado/servicios-lowcost.html"),
    ("https://www.enviosdosruedas.com/servicios/envios-express", "scrapeado/servicios-express.html"),
    ("https://www.enviosdosruedas.com/servicios/envios-contrareembolso", "scrapeado/servicios-contrareembolso.html"),
    ("https://www.enviosdosruedas.com/servicios/plan-emprendedores", "scrapeado/servicios-plan-emprendedores.html"),
    ("https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata", "scrapeado/guias-envios-flex.html"),
    ("https://www.enviosdosruedas.com/nosotros/sobre-nosotros", "scrapeado/nosotros.html"),
    ("https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes", "scrapeado/preguntas-frecuentes.html"),
    ("https://www.enviosdosruedas.com/nosotros/nuestras-redes", "scrapeado/redes.html"),
    ("https://www.enviosdosruedas.com/terminos-y-condiciones", "scrapeado/terminos-y-condiciones.html"),
    ("https://www.enviosdosruedas.com/politica-de-privacidad", "scrapeado/politica-de-privacidad.html"),
]

local_map = {
    "/": "index.html",
    "/contacto": "contacto.html",
    "/cotizar": "cotizar.html",
    "/servicios/enviosflex": "servicios-enviosflex.html",
    "/servicios/deposito-fulfillment": "servicios-fulfillment.html",
    "/servicios/envios-lowcost": "servicios-lowcost.html",
    "/servicios/envios-express": "servicios-express.html",
    "/servicios/envios-contrareembolso": "servicios-contrareembolso.html",
    "/servicios/plan-emprendedores": "servicios-plan-emprendedores.html",
    "/guias/envios-flex-mar-del-plata": "guias-envios-flex.html",
    "/nosotros/sobre-nosotros": "nosotros.html",
    "/nosotros/preguntas-frecuentes": "preguntas-frecuentes.html",
    "/nosotros/nuestras-redes": "redes.html",
    "/terminos-y-condiciones": "terminos-y-condiciones.html",
    "/politica-de-privacidad": "politica-de-privacidad.html",
    # Also handle trailing slash variants
    "/servicios/": "servicios-enviosflex.html",
    "/nosotros/": "nosotros.html",
    "/guias/": "guias-envios-flex.html",
}

# Additional internal links that might appear
extra_paths = [
    "/servicios/empresas-cuenta-corriente",
    "/servicios#ecommerce-24hs",
    "/cobertura",
]

async def rewrite_links(html):
    """Rewrite internal links to point to local files."""
    for old_path, new_file in local_map.items():
        # Handle both single and double quotes
        html = html.replace(f'href="{old_path}"', f'href="{new_file}"')
        html = html.replace(f"href='{old_path}'", f"href='{new_file}'")
        html = html.replace(f'href="{old_path}/"', f'href="{new_file}"')
        html = html.replace(f"href='{old_path}/'", f"href='{new_file}'")
    # For extra paths that don't have a direct local file, point to closest
    for path in extra_paths:
        html = html.replace(f'href="{path}"', 'href="servicios-enviosflex.html"')
        html = html.replace(f"href='{path}'", "href='servicios-enviosflex.html'")
    return html

async def scrape_page(page, url, output_path):
    try:
        print(f"Scraping: {url}")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await page.wait_for_load_state("networkidle")
        
        # Get the full HTML content
        html = await page.content()
        
        # Get all stylesheets content
        styles = await page.evaluate("""
            () => {
                const sheets = Array.from(document.styleSheets);
                let css = '';
                for (const sheet of sheets) {
                    try {
                        const rules = Array.from(sheet.cssRules || sheet.rules || []);
                        for (const rule of rules) {
                            css += rule.cssText + '\\n';
                        }
                    } catch (e) {
                        console.log('Could not read stylesheet:', sheet.href, e);
                    }
                }
                return css;
            }
        """)
        
        # Get all inline styles
        inline_styles = await page.evaluate("""
            () => {
                const styleElements = Array.from(document.querySelectorAll('style'));
                return styleElements.map(el => el.textContent).join('\\n');
            }
        """)
        
        # Get all scripts (inline only)
        scripts = await page.evaluate("""
            () => {
                const scriptElements = Array.from(document.querySelectorAll('script:not([src])'));
                return scriptElements.map(el => el.textContent).join('\\n');
            }
        """)
        
        # Rewrite internal links in the full HTML
        html = await rewrite_links(html)
        
        # Remove external stylesheet links (we'll inline the CSS)
        html = re.sub(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', '', html)
        html = re.sub(r'<link[^>]*rel=["\']preload["\'][^>]*as=["\']style["\'][^>]*>', '', html)
        
        # Remove external script tags (keep inline scripts)
        html = re.sub(r'<script[^>]*src=["\'][^"\']+["\'][^>]*></script>', '', html)
        html = re.sub(r'<script[^>]*src=["\'][^"\']+["\'][^>]*/>', '', html)
        
        # Remove Next.js specific scripts and data
        html = re.sub(r'<script[^>]*id=["\']__NEXT_DATA__["\'][^>]*>.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'<script[^>]*id=["\']__NEXT_LOADED_PAGES__["\'][^>]*>.*?</script>', '', html, flags=re.DOTALL)
        
        # Create combined CSS
        combined_css = styles + "\n" + inline_styles
        
        # Create combined JS
        combined_js = scripts
        
        # Inject combined CSS into head (replace or add style tag)
        style_tag = f'<style>\n{combined_css}\n</style>'
        # Try to replace existing style tags or add to head
        if '<style>' in html:
            # Replace first style tag with our combined one, remove others
            html = re.sub(r'<style>.*?</style>', style_tag, html, count=1, flags=re.DOTALL)
            html = re.sub(r'<style>.*?</style>', '', html, flags=re.DOTALL)
        else:
            # Add to head
            html = html.replace('</head>', f'{style_tag}\n</head>')
        
        # Inject combined JS before closing body
        script_tag = f'<script>\n{combined_js}\n</script>'
        html = html.replace('</body>', f'{script_tag}\n</body>')
        
        # Ensure proper DOCTYPE and html tag
        if not html.startswith('<!DOCTYPE html>'):
            html = '<!DOCTYPE html>\n' + html
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"  [OK] Saved to {output_path}")
        return True
    except Exception as e:
        print(f"  [ERROR] Error scraping {url}: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    os.makedirs("scrapeado", exist_ok=True)
    
    async with async_playwright() as p:
        # Connect to existing Chrome on port 9222
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = context.pages[0] if context.pages else await context.new_page()
        
        results = []
        for url, output_path in URLS:
            success = await scrape_page(page, url, output_path)
            results.append((url, output_path, success))
        
        await browser.close()
        
        print("\n=== RESUMEN ===")
        for url, path, success in results:
            status = "[OK]" if success else "[FAIL]"
            print(f"  {status} {url} -> {path}")

if __name__ == "__main__":
    asyncio.run(main())