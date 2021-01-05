#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 6 16:44:53 2020.

@author: ondrej
"""
import math


def sestrojitelnost(a, b, c):
    """Zjistí zda jde tento trojúhelník sestrojit."""
    if (a + b) > c and (b + c) > a and (c + a) > b:
        return True
    else:
        return False


# obvod obsah
def obvod(a, b, c):
    """Vypocita obvod trojuhelniku."""
    return a + b + c


def obsah(a, b, c):
    """Vypočítá obsah trojúhelníku."""
    s = (a + b + c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def pveta(c, b, a):
    """Vypočítá pythagorovu větu a ověří její pravdivost."""
    cd = c*c
    ab2 = (a * a) + (b * b)

    if (cd == ab2):
        return True
    else:
        return False


def prepona(a, b, c):
    """Určení nejdelší strany trojúhelníku, část I."""
    if (a > b):
        if (a > c):
            if (pveta(a, b, c)):
                return True
            else:
                return False
        else:
            if (pveta(c, a, b)):
                return True
            else:
                return False
    else:
        if (b > c):
            if (pveta(b, a, c)):
                return True
            else:
                return False
        else:
            if (pveta(c, a, b)):
                return True
            else:
                return False


def prepona_info(test):
    """Určení nejdelší strany trojúhelníku, část II."""
    prav = "Trojuhelnik je pravouhly"
    neprav = "Trojuhelnik neni pravouhly"
    if test:
        return prav
    else:
        return neprav


def delkastrany(x1, y1, x2, y2):
    """Metoda na výpočet délky strany trojúhelníku."""
    return math.sqrt(((y2-y1)**2) + ((x2-x1)**2))


def trojuhelnik(ax, ay, bx, by, cx, cy):
    """Postupně provede všechny potřebné kroky k vypočítání trojúhelníku."""
    c = delkastrany(ax, ay, bx, by)  # délka strany c
    b = delkastrany(ax, ay, cx, cy)  # délka strany b
    a = delkastrany(bx, by, cx, cy)  # délka strany a
    # výpíše délky stran
    print("Delka strany a: ", a, "Delka strany b: ", b, "Delka strany c: ", c)
    if sestrojitelnost(a, b, c):    # overeni sestrojitelnosti trouhelniku
        print("Lze setrojit", "Obvod trojuhelniku je: ", obvod(a, b, c),
              "Obsah trojuhelniku je: ", obsah(a, b, c),
              prepona_info(prepona(a, b, c)))
    else:
        print("Trojuhelnik nelze sestrojit")


if __name__ == '__main__':
    """Vstup dat od uzivatele."""
    try:
        trojuhelnik(
                # x souřadnice bodu A
                int(input("Zadejte x souřadnici bodu A: ")),
                # y souřadnice bodu A
                int(input("Zadejte y souřadnici bodu A: ")),
                # x souřadnice bodu B
                int(input("Zadejte x souřadnici bodu B: ")),
                # y souřadnice bodu B
                int(input("Zadejte y souřadnici bodu B: ")),
                # x souřadnice bodu C
                int(input("Zadejte x souřadnici bodu C: ")),
                # y souřadnice bodu C
                int(input("Zadejte y souřadnici bodu C: ")))
    except ValueError:  # ošetření zadání nečíselné hodnoty
        print("Zadali jste špatnou hodnotu!")


def test_sestrojitelnost():
    """Ověří funčnost metody sestrojitelnost."""
    assert sestrojitelnost(5, 7, 8.60) is True


def test_obvod():
    """Ověří funčnost metody obvod."""
    assert obvod(5, 7, 8.60) == 20.60


def test_obsah():
    """Ověří funčnost metody obsah."""
    assert obsah(5, 7, 8.60) == 17.49999714285692


def test_pveta():
    """Ověří funčnost metody pveta."""
    assert pveta(17.12, 3.61, 15.03) is False


def test_prepona():
    """Ověří funčnost metody prepona."""
    assert prepona(2.24, 1.0, 1.41) is False


def test_delkastrany():
    """Ověří funčnost metody delkastrany."""
    assert delkastrany(1, 2, 1, 6) == 4


def test_prepona_info():
    """Ověří funkčnost metody prepona_info."""
    assert prepona_info(True) == "Trojuhelnik je pravouhly"
