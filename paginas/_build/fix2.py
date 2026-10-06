# -*- coding: utf-8 -*-
"""Diagnostica por que falla la inversion de mojibake."""
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "plantilla.html"
t = open(PATH, encoding="utf-8").read()

# 1) que caracteres NO se pueden encodear a cp1252?
fallan = sorted({c for c in t if ord(c) > 127 and not _try(c)}) if False else []
for c in sorted(set(t)):
    if ord(c) > 127:
        try:
            c.encode("cp1252")
        except Exception:
            fallan.append(c)
print("no cp1252:", [(hex(ord(c)), c.encode("unicode_escape").decode()) for c in fallan])

# 2) muestra de no-ascii
noascii = sorted({c for c in t if ord(c) > 127})
print("no-ascii:", [(hex(ord(c)), c.encode("unicode_escape").decode()) for c in noascii])

# 3) intento char por char a bytes, dejando intactos los que fallan
buf = bytearray()
malos = []
for c in t:
    try:
        buf += c.encode("cp1252")
    except Exception:
        malos.append(c)
        buf += b"?"
try:
    txt = bytes(buf).decode("utf-8")
    print("iter1 ok, len", len(txt))
except Exception as e:
    print("iter1 utf8 fail:", e)
    txt = bytes(buf).decode("utf-8", errors="replace")

buf2 = bytearray()
malos2 = []
for c in txt:
    try:
        buf2 += c.encode("cp1252")
    except Exception:
        malos2.append(c)
        buf2 += b"?"
try:
    txt2 = bytes(buf2).decode("utf-8")
    print("iter2 ok, len", len(txt2))
except Exception as e:
    print("iter2 utf8 fail:", e)
    txt2 = bytes(buf2).decode("utf-8", errors="replace")

print("malos1:", [c.encode("unicode_escape").decode() for c in sorted(set(malos))])
print("malos2:", [c.encode("unicode_escape").decode() for c in sorted(set(malos2))])
for probe in ("Men", "Cotiz", "env", "j"):
    i = txt2.find(probe)
    print(probe, "->", repr(txt2[i:i + 40]) if i >= 0 else "no")
