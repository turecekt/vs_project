"""Funkce které později budou přesunuty do souboru __init__.py."""
import trojuhelnik


def sestrojitelnost(Triangle):
    """Funkce vypíše jeli trojuhelnik sestrojitelný."""
    sides = trojuhelnik.delky_stran(Triangle)
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("Trojuhelnik je sestrojitelny")
    else:
        print("Trojuhelnik neni sestrojitelny")
