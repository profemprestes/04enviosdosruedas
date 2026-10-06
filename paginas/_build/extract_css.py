"""Extrae todos los bloques <style> de scrapeado/*.html y arma el CSS compartido unico."""
import re, glob, os, hashlib

OUT = os.path.join(os.path.dirname(__file__), "shared_compiled.css")
chunks = {}
for f in glob.glob(os.path.join(os.path.dirname(__file__), "..", "..", "scrapeado", "*.html")):
    html = open(f, encoding="utf-8").read()
    for m in re.finditer(r"<style[^>]*>(.*?)</style>", html, re.DOTALL):
        css = m.group(1)
        if len(css) < 200:
            continue
        # trocea por reglas top-level para dedup fina
        for rule in re.findall(r"(@(?:keyframes|font-face|property|layer|media|supports|utility|theme|custom-variant)[^{]*\{(?:[^{}]|\{[^{}]*\})*\}|[^{}@]+\{(?:[^{}]|\{[^{}]*\})*\})", css):
            h = hashlib.md5(rule.strip().encode()).hexdigest()
            if h not in chunks:
                chunks[h] = rule.strip()

order = list(chunks.values())
merged = "\n".join(order)
open(OUT, "w", encoding="utf-8").write(merged)
print(f"reglas unicas: {len(order)}  bytes: {len(merged)}")

# Chequeo de cobertura: clases usadas en los .md vs CSS compilado
used = set()
for f in glob.glob(os.path.join(os.path.dirname(__file__), "..", "*.md")):
    txt = open(f, encoding="utf-8").read()
    for m in re.finditer(r'className="([^"]+)"', txt):
        for c in m.group(1).split():
            if re.match(r"^[a-z0-9:\[\]/_.%#()!,-]+$", c) and not c.startswith("http"):
                used.add(c)
print(f"clases distintas en md: {len(used)}")

def has(cls):
    esc = re.escape(cls).replace(r"\:", r"\\?:").replace(r"\[", r"\\?\[").replace(r"\]", r"\\?\]")
    esc = esc.replace(r"\/", r"\\?/").replace(r"\.", r"\\?\.%\)?".replace("%)", "")) if False else esc
    return re.search(r"\." + re.escape(cls).replace(":", r"\\:") + r"[\s,{:.]", merged) is not None

missing = sorted(c for c in used if not has(c))
print(f"sin cubrir: {len(missing)}")
open(os.path.join(os.path.dirname(__file__), "missing_classes.txt"), "w", encoding="utf-8").write("\n".join(missing))
print("\n".join(missing[:80]))
