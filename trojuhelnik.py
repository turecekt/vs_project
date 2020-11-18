# --coding: utf-8 --


from math import sqrt


"""
Projekt AK1VS - Trojuhelnik
"""


# Fuknce pro vypocet delky stran.
# Delka je pocitana presne, nicmene se v programu zobrazuji pouze dve desetinna mista.
# a1, a2 jsou souradnice bodu A; b1, b2 souradnice bodu B
def delka_strany(a1, a2, b1, b2):
    return sqrt(((b1 - a1) ** 2) + ((b2 - a2) ** 2))


# Funkce urcuje, jestli lze dany trojuhelnik sestrojit.
# Pokud ano, vraci 1, jinak 0.
def setrojitelnost(a1, b1, c1):
    if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
        return 1
    else:
        return 0


# Funkce pocita obvod trojuhelniku.
# Pocita presne, zobrazeny budou ale jen dve desetinna cisla.
def obvod(a1, b1, c1):
    return a1 + b1 + c1


# Funkce pocita obsah pomoci Heronova vzorce, tudiz neni potreba znat vysku v trojuhelniku.
def obsah(a1, b1, c1):
    s = (a1 + b1 + c1) / 2
    return sqrt(s * (s - a1) * (s - b1) * (s - c1))


# Funkce pomoci Pythagorovy vety zjisti pravouhlost trojuhelniku.
def pravouhlost(a1, b1, c1):
    if c1 ** 2 == (a1 ** 2 + b1 ** 2) and (a != 0 and b != 0 and c != 0):
        return 1
    else:
        return 0


# Program zacina v tomto miste.
# Uzivatel je vyzvan, aby zadal souradnice bodu.


# Hodonoty bodů jsou zadány kvůli testování. 

"""
ax = int(input("Zadej souřadnici x bodu A: "))
ay = int(input("Zadej souřadnici y bodu A: "))
bx = int(input("Zadej souřadnici x bodu B: "))
by = int(input("Zadej souřadnici y bodu B: "))
cx = int(input("Zadej souřadnici x bodu C: "))
cy = int(input("Zadej souřadnici y bodu C: "))
""" 

ax = 1
ay = 1
bx = 2
by = 5
cx = 7
cy = 3

# Vypocet delek stran. Promenne budou pouzity pro dalsi vypocty.
a = delka_strany(bx, by, cx, cy)
b = delka_strany(ax, ay, cx, cy)
c = delka_strany(ax, ay, bx, by)

print()
print("Délky stran:")
print("Délka strany a je ", "{:.2f}".format(a))
print("Délka strany b je ", "{:.2f}".format(b))
print("Délka strany c je ", "{:.2f}".format(c))
print()

if setrojitelnost(a, b, c):
    print("Zadaný trojúhelník lze setrojit.")
    print("Obvod trojúhelníku je ", "{:.2f}".format(obvod(a, b, c)))
    print("Obsah trojúhelníku je ", "{:.2f}".format(obsah(a, b, c)))
else:
    print("Zadaný trojúhelník neexistuje - nelze spočítat obvod a obsah ani určit pravoúhlost.")
if pravouhlost(a, b, c):
    print("Trojúhelník je pravoúhlý.")


def test_obvod():
    assert obvod(1, 2, 3) == 6
    
