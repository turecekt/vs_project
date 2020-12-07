"""Program pro převod čísla z desítkové soustavy.

Program obsahuje 1 funkci: prevod()
"""
# -*- coding: utf-8 -*-
import math as m


def prevod(c, s):
    """Funkce prevod převádí zadané číslo z 10-ové soustavy na zvolenou soustavu.

    Args:
        - c - kladné celé číslo v desítkové soustavě
        - s - 2, 8, 12 nebo 16 - cílová soustava, do které chceme převést
        číslo c

    Returns:
        - output - řetězec vracející číslo v cílové číselné soustavě
    """
    # vytvoření prázdného řetězce "vysledek" pro uložení výsledné hodnoty
    vysledek = ""
    # cyklus, ve kterém číslo dělíme soustavou, dokud se nerovná 0
    while(c/s != 0):
        # ukládání zbytku po dělení do proměnné "zbytek"
        zbytek = c % s
        vysledek = vysledek + str(zbytek)
        # přepsání hodnoty do proměnné "c" po vydělení a zaokrouhlení
        c = m.floor(c/s)

    # Výsledek otočen a vypsán
    return vysledek[::-1]


def test_soustava():
    """Funkce pro otestování programu."""
    assert prevod(405, 8) == '625'
