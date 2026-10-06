import os, sys
from playwright.sync_api import sync_playwright

target = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "test/pilot.html")
fails = []
with sync_playwright() as p:
    try:
        b = p.chromium.launch()
    except Exception:
        b = p.chromium.launch(channel="chrome")
    pg = b.new_context(viewport={"width": 1440, "height": 900}).new_page()
    pg.on("requestfailed", lambda r: fails.append(r.url + " :: " + str(r.failure)))
    pg.goto("file:///" + target.replace("\\", "/"))
    pg.wait_for_timeout(2500)
    print("FAILS:")
    for f in fails:
        print("  -", f[:220])
    print("FONT h1:", pg.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily"))
    print("FONT body:", pg.evaluate("getComputedStyle(document.body).fontFamily"))
    print("header fixed:", pg.evaluate("getComputedStyle(document.getElementById('optimized-header')).position"))
    print("overflow x:", pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth"))
    print("imgs rotas:", pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.currentSrc||i.src)"))
    pill = pg.evaluate("(e=>e&&getComputedStyle(e).backgroundColor)(document.querySelector('a.cta-nested-pill'))")
    print("cta pill bg:", pill)
    print("reveal ocultos:", pg.evaluate("[...document.querySelectorAll('[data-reveal]')].filter(e=>getComputedStyle(e).opacity!=='1').length"))
    pg.click("[data-dd-toggle]")
    pg.wait_for_timeout(400)
    print("dropdown visibility:", pg.evaluate("getComputedStyle(document.querySelectorAll('.nav-dd')[0]).visibility"))
    pg.set_viewport_size({"width": 390, "height": 844})
    pg.wait_for_timeout(300)
    pg.click("#mobile-menu-toggle-opt")
    pg.wait_for_timeout(700)
    print("drawer transform:", pg.evaluate("getComputedStyle(document.getElementById('mobile-navigation-dialog')).transform"))
    print("drawer link visible:", pg.is_visible("#mobile-navigation-dialog a"))
    b.close()
