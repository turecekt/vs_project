"""Projekt AK1VS - Trojúhelník."""
from math import sqrt


def kontrola_vstupu(vstup):
    """Kontroluje, jestli je vstup int. Pokud ne, vyzve k novému zadání."""
    try:
        return int(vstup)
    except ValueError:
        while True:
            try:
               vstup = input("Zadej celé číslo: ")
               return int(vstup)
            except ValueError:
                continue
            else:
                break


def delka_strany(a1, a2, b1, b2):
    """Vypočítá délku strany, vrací jeho přesnou hodnotu.

    Argumenty:
        a1 - souřadnice x 1. bodu
        a2 - souřadnice y 1. bodu
        b1 - souřadnice x 2. bodu
        b2 - souřadnice y 2. bodu
    """
    return sqrt(((b1 - a1) ** 2) + ((b2 - a2) ** 2))


def sestrojitelnost(a1, b1, c1):
    """Určí, jestli lze trojúhelník sestrojit. Pokud ano, vrací 1, jinak 0."""
    if a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1:
        return 1
    else:
        return 0


def obvod(a1, b1, c1):
    """Spočítá obvod, vrátí jeho přesnou hodnotu."""
    return a1 + b1 + c1


def obsah(a1, b1, c1):
    """Pomocí Heronova vzorce spočítá obsah a vrátí jeho hodnotu."""
    s = (a1 + b1 + c1) / 2
    return sqrt(s * (s - a1) * (s - b1) * (s - c1))


def pravouhlost(a1, b1, c1):
    """Pythagorovou větou určí pravoúhlost, pokud je pravoúhlý, vrací 1."""
    if c1 ** 2 == (a1 ** 2 + b1 ** 2) and (a1 != 0 and b1 != 0 and c1 != 0):
        return 1
    else:
        return 0


if __name__ == '__main__':
    ax = kontrola_vstupu(input("Zadej souřadnici x bodu A: "))
    ay = kontrola_vstupu(input("Zadej souřadnici y bodu A: "))
    bx = kontrola_vstupu(input("Zadej souřadnici x bodu B: "))
    by = kontrola_vstupu(input("Zadej souřadnici y bodu B: "))
    cx = kontrola_vstupu(input("Zadej souřadnici x bodu C: "))
    cy = kontrola_vstupu(input("Zadej souřadnici y bodu C: "))
    a = delka_strany(bx, by, cx, cy)
    b = delka_strany(ax, ay, cx, cy)
    c = delka_strany(ax, ay, bx, by)
    print("Délka strany a je ", "{:.2f}".format(a))
    print("Délka strany b je ", "{:.2f}".format(b))
    print("Délka strany c je ", "{:.2f}".format(c))
    if sestrojitelnost(a, b, c):
        print("Trojúhelník lze setrojit.")
        print("Obvod trojúhelníku je ", "{:.2f}".format(obvod(a, b, c)))
        print("Obsah trojúhelníku je ", "{:.2f}".format(obsah(a, b, c)))
        if pravouhlost(a, b, c):
            print("Trojúhelník je pravoúhlý.")
    else:
        print("Zadaný trojúhelník neexistuje.")
    


def test_obvod():
    """Testuje funkci pro výpočet obvodu."""
    assert obvod(1, 2, 3) == 6


def test_obsah():
    """Testuje funkci pro výpočet obsahu."""
    assert obsah(5, 4, sqrt(41)) == 10


def test_pravouhlost():
    """Testuje funkci pro určení pravoúhlosti."""
    assert pravouhlost(3, 4, 5) == 1


def test_delka_strany():
    """Testuje funkci pro výpočet délek stran."""
    assert delka_strany(0, 0, 0, 5) == 5


def test_sestrojitelnost():
    """Testuje funkci pro určení sestrojitelnosti."""
    assert sestrojitelnost(3, 4, 5) == 1


def test_kontrola_vstupu():
    """Testuje funkci pro kontrolu vstupu od uživatele."""
    assert kontrola_vstupu("1") == 1
