# -*- coding: utf-8 -*-
"""
Tento soubor obsahuje jednotkové testy, které testují
jednotlivé metody používané programem.

Created on Tue Dec  1 17:33:30 2020

@author: jakub
"""
import classes

pravouhly_trojuhelnik = classes.trojuhelnik(0, 0, 0, 15, 20, 0)
nepravouhly_trojuhelnik = classes.trojuhelnik(1, 1, 17, 18, 30, 15)
nesetrojitelny_trojuhelnik = classes.trojuhelnik(0, 5, 0, 10, 0, 35)


def test_pravouhlytrojuhelnik_sestrojitelny():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje, zda je trojúhelník sestavitelný či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.jeSestrojitelny()
    assert total == "ANO"


def test_pravouhlytrojuhelnik_pravouhly():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje, zda je trojúhelník pravoúhlý či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.jePravouhly()
    assert total == "ANO"


def test_pravouhlytrojuhelnik_delkaA():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje délku strany.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("a")
    assert total == 25


def test_pravouhlytrojuhelnik_delkaB():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje délku strany.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("b")
    assert total == 20


def test_pravouhlytrojuhelnik_delkaC():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje délku strany.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.delkaStrany("c")
    assert total == 15


def test_pravouhlytrojuhelnik_obvod():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje obvod trojúhelníku.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.obvod()
    assert total == 60


def test_pravouhlytrojuhelnik_obsah():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje obsah trojúhelníku.

    Args:
        Žádné argumenty.
    """
    total = pravouhly_trojuhelnik.obsah()
    assert total == 150


def test_nepravouhlytrojuhelnik_sestrojitelny():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje, zda je trojúhelník sestavitelný či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nepravouhly_trojuhelnik.jeSestrojitelny()
    assert total == "ANO"


def test_nepravouhlytrojuhelnik_pravouhly():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje, zda je trojúhelník pravoúhlý či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nepravouhly_trojuhelnik.jePravouhly()
    assert total == "NE"


def test_nesestrojitelnytrojuhelnik_sestrojitelny():
    """
    Metoda, která je jednotkovým testem k
    funkci, která určuje, zda je trojúhelník sestavitelný či
    nikoliv.

    Args:
        Žádné argumenty.
    """
    total = nesetrojitelny_trojuhelnik.jeSestrojitelny()
    assert total == "NE"
