from math import sqrt
"""
Projekt AK1VS - Trojúhelník
"""
"""
Fuknce pro výpočet délky stran.
Délka je počítána přesně, nicméně se v programu zobrazují pouze dvě desetinná místa.
"""


def delka_strany(a1, a2, b1, b2):
    return sqrt(((b1-a1)**2)+((b2-a2)**2))


"""
Program začíná v tomto místě.
Uživatel je vyzván, aby zadal souřadnice bodů.
"""
ax = int(input("Zadej souřadnici x bodu A: "))
ay = int(input("Zadej souřadnici y bodu A: "))
bx = int(input("Zadej souřadnici x bodu B: "))
by = int(input("Zadej souřadnici y bodu B: "))
cx = int(input("Zadej souřadnici x bodu C: "))
cy = int(input("Zadej souřadnici y bodu C: "))

""""
Výpočet délek stran
"""
a = delka_strany(bx, by, cx, cy)
b = delka_strany(ax, ay, cx, cy)
c = delka_strany(ax, ay, bx, by)
print()
print("Délky stran:")
print("Délka strany a je ", "{:.2f}".format(a))
print("Délka strany b je ", "{:.2f}".format(b))
print("Délka strany c je ", "{:.2f}".format(c))
