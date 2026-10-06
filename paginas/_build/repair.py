# -*- coding: utf-8 -*-
"""Repara mojibake UTF-8<->cp1252/ANSI iterativamente y valida con cadenas clave."""
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "plantilla.html"
APPLY = "--apply" in sys.argv

# cp1252: chars con byte especial (0x80-0x9F)
CP = {
    "\u20ac": 0x80, "\u201a": 0x82, "\u0192": 0x83, "\u201e": 0x84,
    "\u2026": 0x85, "\u2020": 0x86, "\u2021": 0x87, "\u02c6": 0x88,
    "\u2030": 0x89, "\u0160": 0x8A, "\u2039": 0x8B, "\u0152": 0x8C,
    "\u017D": 0x8E, "\u2018": 0x91, "\u2019": 0x92, "\u201C": 0x93,
    "\u201D": 0x94, "\u2022": 0x95, "\u2013": 0x96, "\u2014": 0x97,
    "\u02DC": 0x98, "\u2122": 0x99, "\u0161": 0x9A, "\u203A": 0x9B,
    "\u0153": 0x9C, "\u017E": 0x9E, "\u0178": 0x9F,
}
GOOD = set("áéíóúñÁÉÍÓÚÑ¿¡üÜç°‘’“”…—×·€")


def to_bytes(t):
    out = bytearray()
    for ch in t:
        o = ord(ch)
        if o < 0x100:
            out.append(o)            # latin-1 directo (incluye slots indefinidos)
        elif ch in CP:
            out.append(CP[ch])
        else:
            try:
                out += ch.encode("cp1252")
            except Exception:
                out += b"?"
    return bytes(out)


def goodness(t):
    good = sum(1 for c in t if c in GOOD)
    bad = sum(t.count(x) for x in ("\u00c3", "\u00c2", "\u00ff", "\ufffd"))
    return good, bad


PROBES = [
    "Men\u00fa principal",
    "Cerrar men\u00fa",
    "Cotiz\u00e1 tu env\u00edo",
    "\u00bfTen\u00e9s env\u00edos para hoy?",
    "Canales Oficiales",
    "Nuestra Comunidad Digital",
    "Volver al inicio",
    "Horarios de Despacho",
    "Chate\u00e1 con Nosotros",
    "SEGU\u00cd NUESTRO",
]

raw = open(PATH, "rb").read()
s = raw.decode("utf-8", errors="replace")
print("start:", goodness(s))

cur = s
for i in range(6):
    try:
        nxt = to_bytes(cur).decode("utf-8")
    except UnicodeDecodeError as e:
        print("iter", i, "utf8 fail:", e)
        break
    if nxt == cur:
        print("iter", i, "estable")
        break
    cur = nxt
    print("iter", i + 1, goodness(cur))

print("final:", goodness(cur))
ok = True
for p in PROBES:
    found = p in cur
    if not found:
        ok = False
    print(("  OK  " if found else "  FALTA ") + p.encode("unicode_escape").decode())

# residuos
for tok in ("\u00c3", "\ufffd", "\ufeff"):
    if tok in cur:
        print("residuo", tok.encode("unicode_escape").decode(), cur.count(tok))

if APPLY and ok:
    open(PATH, "w", encoding="utf-8", newline="").write(cur)
    print("APLICADO ->", PATH)
else:
    print("no aplicado (ok=%s, apply=%s)" % (ok, APPLY))
