"""Skript pro spravnou kontrolu zapsanehorim. c..

Tento skript bude prilozen pozdeji do celeho projektu
"""


def test_checkcorrect1():
    """Funkce pro kontrolu zadaneho cisla.

    Testovaci funkce kontrolu
    >>> checkcorrect("LL", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("IMI", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("ILM", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("CCCCC", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("LLL", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("LC", ["I", "V", "X", "L", "C", "D", "M"])
    False
    >>> checkcorrect("AA", ["I", "V", "X", "L", "C", "D", "M"])
    False
    """


def checkcorrect(numb, cisla):
    """Funkce pro zjištění jestli je  ř. č. v dobrem tvaru).

    Vystup bool
    """
    dobre = True
    coun = 0
    numb = numb.upper()
    pocitadlostejnychznaku = 1
    maxy = "M"
    u = 0
    while u < len(numb):
        if numb[u] not in cisla:
            dobre = False
        u = u+1
    if dobre:
        if (len(numb) > 0):
            while coun+1 < len(numb):
                x = cisla.index(numb[coun])
                if (x % 2 == 1 and x + 1 == cisla.index(numb[coun + 1])):
                    dobre = False
                if cisla.index(numb[coun]) < cisla.index(numb[coun+1]):
                    maxy = (numb[coun])
                    if coun+2 < len(numb):
                        q = cisla.index(numb[coun+1])
                        if q <= cisla.index(numb[coun+2]):
                            dobre = False
                elif cisla.index(numb[coun]) > cisla.index(maxy):
                    dobre = False
                else:
                    if numb[coun] != "M" and maxy == numb[coun]:
                        pocitadlostejnychznaku = pocitadlostejnychznaku+1
                        d = (maxy == "L" or maxy == "V" or maxy == "D")
                        if pocitadlostejnychznaku > 3:
                            dobre = False
                        elif pocitadlostejnychznaku > 1 and d:
                            dobre = False
                    else:
                        maxy = numb[coun]
                        pocitadlostejnychznaku = 1
                coun = coun+1
            if numb[len(numb)-1] != "M" and maxy == numb[len(numb)-1]:
                pocitadlostejnychznaku = pocitadlostejnychznaku+1
                d = (maxy == "L" or maxy == "V" or maxy == "D")
                if pocitadlostejnychznaku > 3:
                    dobre = False
                elif pocitadlostejnychznaku > 1 and d:
                    dobre = False
    return dobre
