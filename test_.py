# -*- coding: utf-8 -*-

"""
Tento soubor obsahuje jednotkové testy.

Testovány jsou jednotlivé metody ve třídě
trojuhelník používané programem.

Created on Tue Dec  1 17:33:30 2020

@author: jakub
"""
import classes

pravouhly_trojuhelnik = classes.trojuhelnik(0, 0, 0, 15, 20, 0)
nepravouhly_trojuhelnik = classes.trojuhelnik(1, 1, 17, 18, 30, 15)
nesetrojitelny_trojuhelnik = classes.trojuhelnik(0, 5, 0, 10, 0, 35)


def test_pravouhlytrojuhelnik_sestrojitelny():
    """
    Jednotkový test k metodě určující sestrojitelnost.

    Funkci, která určuje, zda je trojúhelník sestavitelný či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.jeSestrojitelny()
    assert total == "ANO"


def test_pravouhlytrojuhelnik_pravouhly():
    """
    Jednotkový test k metodě jePravouhly().

    Test testuje metodu určující, zda se se jedná o pravoúhlý
    trojuhelník či nikoliv.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.jePravouhly()
    assert total == "ANO"


def test_pravouhlytrojuhelnik_delkaA():
    """
    Jednotkový test k metodě určující délku strany.

    V tomto případě je testována délka strany "a".

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("a")
    assert total == 25


def test_pravouhlytrojuhelnik_delkaB():
    """
    Jednotkový test k metodě určující délku strany.

    V tomto případě je testována délka strany "b".

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("b")
    assert total == 20


def test_pravouhlytrojuhelnik_delkaC():
    """
    Jednotkový test k metodě určující délku strany.

    V tomto případě je testována délka strany "c".

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("c")
    assert total == 15


def test_pravouhlytrojuhelnik_obvod():
    """
    Jednotkový test k metodě určující obvod.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.obvod()
    assert total == 60


def test_pravouhlytrojuhelnik_obsah():
    """
    Jednotkový test k metodě určující obsah.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.obsah()
    assert total == 150


def test_nepravouhlytrojuhelnik_sestrojitelny():
    """
    Jednotkový test k metodě jeSestrojitelny().

    Test testuje metodu určující, zda se dá daný trojuhelník
    sestrojit či nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nepravouhly_trojuhelnik.jeSestrojitelny()
    assert total == "ANO"


def test_nepravouhlytrojuhelnik_pravouhly():
    """
    Jednotkový test k metodě jePravouhly().

    Test testuje metodu určující, zda se se jedná o pravoúhlý
    trojuhelník či nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nepravouhly_trojuhelnik.jePravouhly()
    assert total == "NE"


def test_nesestrojitelnytrojuhelnik_sestrojitelny():
    """
    Jednotkový test k metodě jeSestrojitelny().

    Test testuje metodu určující, zda se dá daný trojuhelník
    sestrojit či nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nesetrojitelny_trojuhelnik.jeSestrojitelny()
    assert total == "NE"


def test_vstup():
    """
    Jednotkový test k vstup().

    Args:
        Žádné argumenty.
    """
    trojuhelnik = classes.vstup("3 4", "5 6", "7 8")
    total1 = trojuhelnik.Ax
    total2 = trojuhelnik.Ay
    total3 = trojuhelnik.Bx
    total4 = trojuhelnik.By
    total5 = trojuhelnik.Cx
    total6 = trojuhelnik.Cy
    assert total1 == 3
    assert total2 == 4
    assert total3 == 5
    assert total4 == 6
    assert total5 == 7
    assert total6 == 8
