from math import sqrt
"""
Projekt AK1VS - Trojúhelník
"""
"""
Fuknce pro výpočet délky stran.
Délka je počítána přesně, nicméně se v programu zobrazují pouze dvě desetinná místa.
a1, a2 jsou souřadnice bodu A; b1, b2 souřadnice bodu B
"""


def delka_strany(a1, a2, b1, b2):
    return sqrt(((b1-a1)**2)+((b2-a2)**2))


"""
Funkce určuje, jestli lze daný trojúhelník sestrojit.
Pokud ano, vrací 1, jinak 0. 
"""


def setrojitelnost(a1, b1, c1):
    if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
        return 1
    else:
        return 0


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
print()
if setrojitelnost(a, b, c) == 1:
    print("Zadaný trojúhelník lze setrojit.")
else:
    print("Zadaný trojúhelník neexistuje.")

