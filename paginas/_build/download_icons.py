"""Descarga iconos (Lucide + marcas FA) y arma el sprite SVG compartido."""
import urllib.request, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_SVG = os.path.join(BASE, "sprite.svg")
OUT_IDS = os.path.join(BASE, "iconos.txt")

LUCIDE = [
    "arrow-right", "arrow-left", "arrow-up", "arrow-up-right", "arrow-down",
    "chevron-down", "chevron-right", "chevron-left", "chevron-up",
    "menu", "x", "plus", "minus", "check", "external-link", "link",
    "phone", "mail", "map-pin", "clock", "calendar", "message-circle", "message-square",
    "zap", "trending-down", "trending-up", "shopping-bag", "package", "package-check",
    "store", "building-2", "warehouse", "truck", "bike", "motorcycle",
    "layers", "boxes", "route", "navigation", "map", "globe",
    "timer", "hourglass", "gauge", "scale", "weight", "ruler", "target",
    "circle-check", "circle-alert", "triangle-alert", "shield-check", "badge-check",
    "lock", "refresh-cw", "repeat", "shuffle",
    "wallet", "credit-card", "landmark", "receipt", "hand-coins", "coins", "banknote",
    "percent", "tag", "users", "user", "briefcase", "rocket", "handshake", "megaphone",
    "sparkles", "star", "thumbs-up", "eye", "lightbulb", "qr-code", "smartphone",
    "printer", "clipboard-list", "list-checks", "file-text", "book-open",
    "help-circle", "circle-help", "info", "share-2", "home", "layout-grid",
    "calculator", "crosshair", "sliders-horizontal", "search", "send", "download", "upload",
    "cloud-rain", "chart-column", "chart-line", "key", "circle-dot", "activity",
    "server", "folder", "play", "phone-call", "funnel", "filter",
    "arrow-down-wide-narrow", "circle-dot-dashed", "split", "git-merge",
    "shield", "wrench", "settings", "power", "battery-charging", "flag",
    "clock-3", "map-pinned", "locate-fixed", "move-right", "corner-down-right",
]

FA = ["whatsapp", "facebook", "instagram"]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8")


def inner(svg, brand=False):
    body = re.sub(r"^.*?<svg[^>]*>", "", svg, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body, flags=re.S).strip()
    if brand:
        return '<g fill="currentColor" stroke="none">%s</g>' % body
    body = re.sub(r'\s(class|stroke-width|stroke-linecap|stroke-linejoin)="[^"]*"', "", body)
    return '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</g>' % body


symbols, missing = [], []
for name in LUCIDE:
    url = f"https://unpkg.com/lucide-static@latest/icons/{name}.svg"
    try:
        svg = get(url)
    except Exception as e:
        missing.append(f"{name} ({type(e).__name__})")
        continue
    vb = re.search(r'viewBox="([^"]+)"', svg)
    vb = vb.group(1) if vb else "0 0 24 24"
    symbols.append(f'<symbol id="i-{name}" viewBox="{vb}">{inner(svg)}</symbol>')

for name in FA:
    url = f"https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6/svgs/brands/{name}.svg"
    try:
        svg = get(url)
    except Exception as e:
        missing.append(f"fa-{name} ({type(e).__name__})")
        continue
    vb = re.search(r'viewBox="([^"]+)"', svg)
    vb = vb.group(1) if vb else "0 0 24 24"
    symbols.append(f'<symbol id="i-{name}" viewBox="{vb}">{inner(svg, brand=True)}</symbol>')

sprite = "<!-- SPRITE DE ICONOS (autocontenido) -->\n<svg xmlns=\"http://www.w3.org/2000/svg\" style=\"position:absolute;width:0;height:0;overflow:hidden\" aria-hidden=\"true\" focusable=\"false\">\n" + "\n".join(symbols) + "\n</svg>\n"
open(OUT_SVG, "w", encoding="utf-8").write(sprite)
ids = [re.search(r'id="([^"]+)"', s).group(1) for s in symbols]
open(OUT_IDS, "w", encoding="utf-8").write("\n".join(ids))
print(f"simbolos: {len(symbols)}  bytes: {len(sprite)}")
if missing:
    print("FALTAN:")
    for m in missing:
        print("  -", m)
