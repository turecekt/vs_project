"""Skript pro provod rim. c. na num.

Tento skript bude prilozen pozdeji do celeho projektu
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
    number = cislo
    cisl = ["I", "V", "X", "L", "C", "D", "M"]
    position = 0
    hodnota = 0
    while position < len(number):
        if position+1 < len(number):
            if cisl.index(number[position]) < cisl.index(number[position+1]):
                hodnota = hodnota+suma(number[position]+number[position+1])
                position = 1+position
            else:
                hodnota = hodnota+suma(number[position])
        else:
            hodnota = hodnota+suma(number[position])
        position = 1+position
    return hodnota
