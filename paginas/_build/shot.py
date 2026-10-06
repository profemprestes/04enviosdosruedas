"""Screenshot rápido para validar un HTML generado (file://)."""
import sys, os, json
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "shots")
os.makedirs(OUT, exist_ok=True)

targets = sys.argv[1:] or [os.path.join(BASE, "pilot.html")]
full = os.environ.get("FULL", "1") == "1"

with sync_playwright() as p:
    try:
        browser = p.chromium.launch()
    except Exception:
        browser = p.chromium.launch(channel="chrome")
    for t in targets:
        t = os.path.abspath(t)
        name = os.path.splitext(os.path.basename(t))[0]
        errs = []
        for label, vw, vh in (("desktop", 1440, 900), ("mobile", 390, 844)):
            ctx = browser.new_context(viewport={"width": vw, "height": vh},
                                      device_scale_factor=1)
            page = ctx.new_page()
            page.on("console", lambda m: errs.append(m.type + ": " + m.text)
                    if m.type in ("error", "warning") else None)
            page.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
            page.goto("file:///" + t.replace("\\", "/"))
            page.wait_for_timeout(1800)
            path = os.path.join(OUT, f"{name}-{label}.png")
            if full:
                page.screenshot(path=path, full_page=True)
            else:
                page.screenshot(path=path)
            # altura total
            h = page.evaluate("document.body.scrollHeight")
            print(f"{name} [{label}] -> {path} (scrollHeight={h})")
            ctx.close()
        if errs:
            print(f"  CONSOLA {name}:")
            for e in dict.fromkeys(errs):
                print("   -", e[:200])
        else:
            print(f"  consola {name}: sin errores")
    browser.close()
