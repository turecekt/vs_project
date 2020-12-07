"""Skript pro spravnou kontrolu zapsanehorim. c..

Tento skript bude prilozen pozdeji do celeho projektu
"""


def test_checkcorrect1():
    """Funkce pro kontrolu zadaneho cisla.

    Testovaci funkce kontrolu
    >>> checkcorrect("LL")
    False
    >>> checkcorrect("IMI")
    False
    >>> checkcorrect("ILM")
    False
    >>> checkcorrect("CCCCC")
    False
    >>> checkcorrect("LLL")
    False
    >>> checkcorrect("LC")
    False
    >>> checkcorrect("AA")
    False
    """


def test_suma2():
    """Testy pro prevod.

    Otestuje převod
    >>> suma("IM")
    999
    >>> suma("I")
    1
    >>> encodetorim("IM")
    999
    >>> encodetorim("I")
    1
    >>> encodetorim("III")
    3
    """


def checkcorrect(numb):
    """Funkce pro zjištění jestli je  ř. č. v dobrem tvaru).

    Vystup bool
    """
    cisla = ["I", "V", "X", "L", "C", "D", "M"]
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


def suma(value):
    """Funkce pro prepocet.

    Vstup sting vystup int
    """
    cisla = ["I", "V", "X", "L", "C", "D", "M"]
    cislaar = [1, 5, 10, 50, 100, 500, 1000]
    x = 0
    if len(value) > 1:
        x = x-cislaar[cisla.index(value[0])]
        x = x+cislaar[cisla.index(value[1])]
    else:
        x = x+cislaar[cisla.index(value[0])]
    return x


def encodetorim(cislo):
    """Funkce pro prepocet.

    Vstup sting vystup int
    """
    pokracuj = checkcorrect(cislo)
    hodnota = 0
    if (pokracuj):
        number = cislo
        cisl = ["I", "V", "X", "L", "C", "D", "M"]
        position = 0
        while position < len(number):
            if position+1 < len(number):
                d = cisl.index(number[position])
                if d < cisl.index(number[position+1]):
                    hodnota = hodnota+suma(number[position]+number[position+1])
                    position = 1+position
                else:
                    hodnota = hodnota+suma(number[position])
            else:
                hodnota = hodnota+suma(number[position])
            position = 1+position
    return hodnota


# ukazka zavolani
s = encodetorim("VI")
print(s)
