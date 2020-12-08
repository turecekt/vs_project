"""Skript pro prevod num cisla na rim prvni cast.

Tento skript bude prilozen pozdeji do celeho projektu
"""


def test_checkcorrect1():
    """Funkce pro kontrolu zadaneho cisla.

    Testovaci funkce kontrolu
    >>> decodetorim("15")
    ['V', 'X']
    >>> decodetorim("1589")
    ['IX', 'LXXX', 'D']
    >>> decode(3,1)
    'III'
    >>> decode(4,2)
    'XL'
    >>> decode(7,3)
    'DCC'
    >>> decode(9,1)
    'IX'
    """


def decode(numb, cislo):
    """Funkce pro prevod z numerickeho cisla na rimska cisla 1. cast.

    Vstup číslo plus v jakem řádu, vystup je řetězec decodovaný
    """
    cisla = ["I", "V", "X", "X", "L", "C", "C", "D", "M"]
    p = ""
    if(numb <= 3):
        p += numb*cisla[(cislo*3-3)]
    elif(numb == 4):
        p += cisla[(cislo*3-3)]+cisla[1+(cislo*3-3)]
    elif(numb >= 5 and numb <= 8):
        p += cisla[1+(cislo*3-3)]+numb % 5*cisla[(cislo*3-3)]
    else:
        p += cisla[cislo*3-3]+cisla[2+(cislo*3-3)]
    return p


def decodetorim(cislo):
    """Hlavni funkc.

    Vstup číslo které se bude převádět, vystup ve formátu pole bez tisíců
    """
    number = cislo
    listofrome = []
    textinrome = ""
    num = 0
    size = len(number)
    if(size >= 4):
        textinrome += int((number[0:size-3]))*"M"
        num = number[-3:]
    else:
        num = number
    d = 1
    while d <= 3 and d <= size:
        a = decode(int(num[-d]), d)
        d = d+1
        listofrome.append(a)
    return listofrome
