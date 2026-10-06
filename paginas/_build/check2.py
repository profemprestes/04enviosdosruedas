import os, sys, json
from playwright.sync_api import sync_playwright

target = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "../paginas_html/_pilot.html")
with sync_playwright() as p:
    try:
        b = p.chromium.launch()
    except Exception:
        b = p.chromium.launch(channel="chrome")
    pg = b.new_context(viewport={"width": 1440, "height": 900}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.type + ": " + m.text) if m.type == "error" else None)
    pg.goto("file:///" + target.replace("\\", "/"))
    pg.wait_for_timeout(1200)
    # scroll lento hasta abajo
    h = pg.evaluate("document.body.scrollHeight")
    y = 0
    while y < h:
        y += 700
        pg.evaluate(f"window.scrollTo(0,{y})")
        pg.wait_for_timeout(160)
    pg.wait_for_timeout(1000)
    hidden = pg.evaluate("[...document.querySelectorAll('[data-reveal]')].filter(e=>getComputedStyle(e).opacity!=='1').length")
    total = pg.evaluate("document.querySelectorAll('[data-reveal]').length")
    print(f"reveals: {total-hidden}/{total} visibles tras scroll")
    # header scrolleado
    print("header scrolleado bg:", pg.evaluate("getComputedStyle(document.getElementById('optimized-header')).backgroundColor"))
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(500)
    print("header top bg:", pg.evaluate("getComputedStyle(document.getElementById('optimized-header')).backgroundColor"))
    # accordion
    pg.click("[data-acc-btn]")
    pg.wait_for_timeout(500)
    print("acc panel h:", pg.evaluate("document.querySelector('.acc-panel').getBoundingClientRect().height"))
    # fuentes
    print("font subheading:", pg.evaluate("(e=>e&&getComputedStyle(e).fontFamily)(document.querySelector('.font-subheading'))"))
    print("font mono:", pg.evaluate("(e=>e&&getComputedStyle(e).fontFamily)(document.querySelector('.font-mono'))"))
    # acentos en texto renderizado
    txt = pg.inner_text("body")
    lines = [repr(l) for l in txt.splitlines() if any(ord(c) > 127 for c in l)]
    probe = "\n".join(lines)[:600]
    print("acentos:", probe[:600])
    print("errores:", errs[:5])
    pg.screenshot(path=os.path.join(os.path.dirname(target), "..", "_build", "shots", "_pilot-full.png"), full_page=True)
    b.close()
