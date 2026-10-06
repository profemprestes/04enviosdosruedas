# -*- coding: utf-8 -*-
"""Detecta y repara mojibake (UTF-8 leido como cp1252 y reescrito) en un archivo."""
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "plantilla.html"
APPLY = "--apply" in sys.argv

GOOD = set("áéíóúñÁÉÍÓÚÑ¿¡üÜçÇ°—‘’“”…")
BAD_TOKENS = ("Ã¡", "Ã©", "Ã­", "Ã³", "Ãº", "Ã±", "Ã‘", "Ã“", "Ã“", "Â", "Ã©", "â€™", "â€œ")


def stats(t):
    good = sum(1 for c in t if c in GOOD)
    bad = sum(t.count(tok) for tok in BAD_TOKENS)
    repl = t.count("�")
    q = t.count("?")
    return dict(good=good, bad=bad, repl=repl, q=q)


def attempt(t, times=3):
    cur = t
    for _ in range(times):
        try:
            nxt = cur.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if nxt == cur:
            break
        cur = nxt
    return cur


raw = open(PATH, "rb").read()
t = raw.decode("utf-8", errors="replace")
print("original:", stats(t))

fixed = attempt(t)
print("reparado:", stats(fixed))

# ¿quedan secuencias raras de doble mojibake?
for tok in ("Ãƒ", "Ã‚", "Ã¢", "Ã¼Ã"):
    if tok in fixed:
        print("doble mojibake?", tok, fixed.count(tok))

if APPLY and stats(fixed)["bad"] < stats(t)["bad"]:
    open(PATH, "w", encoding="utf-8", newline="").write(fixed)
    print("APLICADO ->", PATH)
else:
    print("(dry-run, sin escribir)")

# contextos de ? sueltos
import re
n = 0
for m in re.finditer(r".{20}\?.{20}", fixed):
    if n < 8:
        print("  ? ctx:", repr(m.group(0)))
    n += 1
print("total ? :", n)
