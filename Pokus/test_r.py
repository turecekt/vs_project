"""Finalni uprava na num. c.

Tento skript bude dan pozdeji do celeho projektu
"""


def test_decode2_doctest():
    """Funkce pro kontrolu decode finální úprava cast pomocí doctestu.

    Testovaci funkce na finalni upravu pomoci doctestu
    >>> finalupdate(0,1,['IV', 'X', ''])
    ('IV', 'X')
    >>> finalupdate(0,1,['I', 'X', ''])
    ('I', 'X')
    >>> finalupdate(0,1,['VII', 'XC', ''])
    ('II', 'VC')
    >>> finalupdate(0,1,['IX', 'XC', ''])
    ('', 'IC')
    """


def finalupdate(firstint, secondint, listofrome):
    """Funkce pro minimalizaci rimska cisla z 1. cast.

    Vstup 2x číslo které je z předchozí funkce, výstup je co zbylo
    """
    cisla = ["I", "V", "X", "L", "C", "D", "M"]
    x = ""
    y = ""
    pok1 = False
    pok2 = len(listofrome[secondint]) == 2
    if pok2:
        pok1 = listofrome[secondint][0] != listofrome[secondint][1]
    q = cisla.index(listofrome[firstint][0])
    pok3 = q - cisla.index(listofrome[secondint][0]) == -1
    pok4 = listofrome[firstint][-1] == listofrome[secondint][0]
    if pok4 and len(listofrome[firstint]) == 2 and pok2 and pok1:
        y += listofrome[firstint][0] + listofrome[secondint][1:]
    elif pok3 and pok2 and pok1:
        y += listofrome[firstint][0] + listofrome[secondint][1:]
        x += listofrome[firstint][1:]
    else:
        x += listofrome[firstint]
        y += listofrome[secondint]
    return x, y
