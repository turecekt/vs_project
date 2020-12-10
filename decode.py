"""Skript pro prevod num cisla na rim.

Peterek Novotný
"""


def test_checkcorrect1():
    """Funkce pro kontrolu zadaneho cisla.

    Testovaci funkce kontrolu
    >>> decodetorim("15A")
    ''
    >>> decodetorim("15")
    'XV'
    >>> decodetorim("1589")
    'MDLXXXIX'
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
    pokracuj = False
    textinrome = ""
    try:
        int(cislo)
        pokracuj = True
    except ValueError:
        pokracuj = False
    if(pokracuj):
        number = cislo
        listofrome = []
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
        pocitadlo = 0
        while pocitadlo+1 < size and pocitadlo+1 < 3:
            if listofrome[pocitadlo] != "" and listofrome[pocitadlo+1] != "":
                q, y = finalupdate(pocitadlo, pocitadlo+1, listofrome)
                listofrome[pocitadlo] = q
                listofrome[pocitadlo+1] = y
            pocitadlo = pocitadlo+1
        listofrome.reverse()
        for r in listofrome:
            textinrome += r
    return textinrome


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


# ukazka spusteni
s = decodetorim("15")
print(s)
