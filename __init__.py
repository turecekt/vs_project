"""Program určí, zda je vstupní číslo prvočíslo či nikoliv.

Pro vyšší čísla program použije některou z heuristických či statistických
metod, o použití alternativní metody program bude informovat uživatele.

VSTUP
    - Libovolné celé číslo zadané uživatelem
    - Program neakceptuje jiný/neplatný vstup
VÝSTUP
    - Informace o tom zda je číslo prvočíslo či nikoliv
    - Informace jakým způsobem byl výsledek zjištěn
        (deterministickou/heuristickou metodou)


"""

import math
from os import path


def Vstup(NapsanaRadka):
    """Funkce ověří vstup od uživatele a ošetří jej proti chybám.

    Returns:
        - output - Vrátí číslo uživatele nebo 0 jako chybu

    #UNIT TESTY:
    >>> Vstup("A")
    0

    >>> Vstup("12")
    12

    >>> Vstup("3")
    3
    """
    for znak in NapsanaRadka:
        if not(znak in "0123456789"):
            return 0

    vstupniCislo = int(NapsanaRadka)

    return vstupniCislo


def Vystup(pouzitaMetoda=0):
    """Funkce vypíše výstup programu (chybu, je či není prvočíslo; použitá metoda).

    Args:
        - pouzitaMetoda - Metoda, kterou program použil pro zjištění výsledku

    #UNIT TESTY
    >>> Vystup()
    ------------------------------------------------------------
    Nastala CHYBA způsobená uživatelem.
    ------------------------------------------------------------
    Zadaná hodnota neopodívá formátu, který se dá přečíst pro
    rozpoznání prvočísla. Zkuste program restartovat a zadat
    přirozené číslo. (1 až nekonečno)

    >>> Vystup(-1)
    Zadané číslo NEPATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita HEURISTICKÁ metoda - 1
    ------------------------------------------------------------
    Metoda rozpozná číslici 1 a vyřadí ji z pátrání, protože
    toto číslo nesplňuje definici prvočísel. (číslo musí být
    dělitelné DVĚMA čísly, samosebou a jedničkou)

    >>> Vystup(-2)
    Zadané číslo NEPATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita HEURISTICKÁ metoda - pravidla dělitelnosti
    ------------------------------------------------------------
    Metoda určí některá neprvočísla, pomocí toho, že je číslo
    končí určitým číslem, které podle pravidel dělitelnosti,
    lze vydělit již prvočíslem. (např. čísla končící na číslo
    5 a 0 jdou vždy vydělit 5)

    >>> Vystup(-3)
    Zadané číslo NEPATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita HEURISTICKÁ metoda - Wilsonova věta
    ------------------------------------------------------------
    Metoda používá matematický vztah '((n - 1)! + 1) % n' pro
    zjištění některých prvočísel.

    >>> Vystup(3)
    Zadané číslo PATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita HEURISTICKÁ metoda - Wilsonova věta
    ------------------------------------------------------------
    Metoda používá matematický vztah '((n - 1)! + 1) % n' pro
    zjištění některých prvočísel.

    >>> Vystup(-4)
    Zadané číslo NEPATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita DETERMINISTICKÁ metoda
    ------------------------------------------------------------
    Metoda zkouší pokud je číslo dělitelné některým z již
    předtím nalezených prvočísel do maximální hodnoty odmocniny
    ze zadaného čísla. Pokud číslo není dělitelné, je to další
    prvočíslo.
    Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4,
    tudíž číslem 2 a 3, nevznikne zbytek 0 a tak je číslo 7
    prvočíslo. (metoda používá paměť s vypočítanými prvočísly
    k zrychlení procesu)

    >>> Vystup(4)
    Zadané číslo PATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Byla použita DETERMINISTICKÁ metoda
    ------------------------------------------------------------
    Metoda zkouší pokud je číslo dělitelné některým z již
    předtím nalezených prvočísel do maximální hodnoty odmocniny
    ze zadaného čísla. Pokud číslo není dělitelné, je to další
    prvočíslo.
    Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4,
    tudíž číslem 2 a 3, nevznikne zbytek 0 a tak je číslo 7
    prvočíslo. (metoda používá paměť s vypočítanými prvočísly
    k zrychlení procesu)

    >>> Vystup(5)
    Zadané číslo PATŘÍ mezi prvočísla.
    ------------------------------------------------------------
    Pravděpodobně jde o nějakou metodu, kterou si vymyslela
    umělá inteligence vašeho počítače. Tuhle zprávu byste
    totiž neměli nikdy vidět.
    """
    if(pouzitaMetoda == 0):
        print("------------------------------------------------------------")
        print("Nastala CHYBA způsobená uživatelem.")
        print("------------------------------------------------------------")
        print("Zadaná hodnota neopodívá formátu, který se dá přečíst pro\n" +
              "rozpoznání prvočísla. Zkuste program restartovat a zadat\n" +
              "přirozené číslo. (1 až nekonečno)")
        return
    elif(pouzitaMetoda > 0):
        print("Zadané číslo PATŘÍ mezi prvočísla.")
    else:
        print("Zadané číslo NEPATŘÍ mezi prvočísla.")
        pouzitaMetoda *= (-1)

    print("------------------------------------------------------------")

    # Popis postupů
    if(pouzitaMetoda == 1):
        print("Byla použita HEURISTICKÁ metoda - 1")
        print("------------------------------------------------------------")
        print("Metoda rozpozná číslici 1 a vyřadí ji z pátrání, protože\n" +
              "toto číslo nesplňuje definici prvočísel. (číslo musí být\n" +
              "dělitelné DVĚMA čísly, samosebou a jedničkou)")
    elif(pouzitaMetoda == 2):
        print("Byla použita HEURISTICKÁ metoda - pravidla dělitelnosti")
        print("------------------------------------------------------------")
        print("Metoda určí některá neprvočísla, pomocí toho, že je číslo\n" +
              "končí určitým číslem, které podle pravidel dělitelnosti,\n" +
              "lze vydělit již prvočíslem. (např. čísla končící na číslo\n" +
              "5 a 0 jdou vždy vydělit 5)")
    elif(pouzitaMetoda == 3):
        print("Byla použita HEURISTICKÁ metoda - Wilsonova věta")
        print("------------------------------------------------------------")
        print("Metoda používá matematický vztah '((n - 1)! + 1) % n' pro\n" +
              "zjištění některých prvočísel.")
    elif(pouzitaMetoda == 4):
        print("Byla použita DETERMINISTICKÁ metoda")
        print("------------------------------------------------------------")
        print("Metoda zkouší pokud je číslo dělitelné některým z již\n" +
              "předtím nalezených prvočísel do maximální hodnoty odmocniny\n" +
              "ze zadaného čísla. Pokud číslo není dělitelné, je to další\n" +
              "prvočíslo.\n" +
              "Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4,\n" +
              "tudíž číslem 2 a 3, nevznikne zbytek 0 a tak je číslo 7\n" +
              "prvočíslo. (metoda používá paměť s vypočítanými prvočísly\n" +
              "k zrychlení procesu)")
    else:
        print("Pravděpodobně jde o nějakou metodu, kterou si vymyslela\n" +
              "umělá inteligence vašeho počítače. Tuhle zprávu byste\n" +
              "totiž neměli nikdy vidět.")


def Metody(cislo):
    """Funkce zkouší zjistit výsledek různými metodami podle typu čísla.

    Označení metod:
        1 - Metoda 0 a 1
        2 - MetodaPravidelDelitelnosti
        3 - HeurestickaMetoda
        4 - DeterministickaMetoda

    Args:
        - cislo - Číslo, u kterého se má zjistit, zda-li je prvočíslo

    Returns:
        - output - Číslo použité metody a znaménko určující je/není prvočíslo

    #UNIT TESTY:
    >>> Metody(1)
    -1

    >>> Metody(14)
    -2

    >>> Metody(3)
    3

    >>> Metody(4)
    -3

    >>> Metody(40013)
    4

    >>> Metody(40011)
    -4
    """
    pouzitaMetoda = 1
    if(cislo <= 1):
        return -pouzitaMetoda

    pouzitaMetoda = 2
    if(MetodaPravidelDelitelnosti(cislo)):
        return -pouzitaMetoda

    pouzitaMetoda = 3
    if(cislo < 40000):
        if(HeurestickaMetoda(cislo)):
            return pouzitaMetoda
        else:
            return -pouzitaMetoda

    pouzitaMetoda = 4
    if(DeterministickaMetoda(cislo)):
        return pouzitaMetoda
    else:
        return -pouzitaMetoda


def MetodaPravidelDelitelnosti(cislo):
    """Funkce zkouší, zda číslo není prvočíslo.

    Je-li je číslo větší jak 9 a zároveň končí čílicí 0, 2, 4, 5, 6 či 8,
    tak toto číslo provčíslo není.

    Args:
        - cislo - Číslo, u kterého se má zjistit, zda-li je prvočíslo

    Returns:
        - output - Boolean pokud je/není prvočíslo.

    #UNIT TESTY:
    >>> MetodaPravidelDelitelnosti(40)
    True

    >>> MetodaPravidelDelitelnosti(42)
    True

    >>> MetodaPravidelDelitelnosti(44)
    True

    >>> MetodaPravidelDelitelnosti(45)
    True

    >>> MetodaPravidelDelitelnosti(46)
    True

    >>> MetodaPravidelDelitelnosti(48)
    True

    >>> MetodaPravidelDelitelnosti(51)
    False
    """
    return (cislo > 9 and str(cislo)[-1] in "024568")


def DeterministickaMetoda(moznePrvocislo):
    """Funkce zkouší zjistit prvočíslo deterministickou metodou.

    Pokud číslo není dělitelné prvočísly do odmocnina z čísla,
    pak je prvočíslo. Funkce vytváří cache soubor.

    Args:
        - moznePrvocislo - Číslo, u kterého se má zjistit, zda-li je prvočíslo

    Returns:
        - output - Boolean pokud je/není prvočíslo.

    #UNIT TESTY:
    >>> DeterministickaMetoda(3)
    True

    >>> DeterministickaMetoda(7)
    True

    >>> DeterministickaMetoda(40013)
    True

    >>> DeterministickaMetoda(40011)
    False
    """
    if(not path.exists("nalezenaPrvocisla.txt")):
        cachePrvociselSoubor = open("nalezenaPrvocisla.txt", "w")
        cachePrvociselSoubor.write("2\n")
        cachePrvociselSoubor.close()

    cachePrvociselSoubor = open("nalezenaPrvocisla.txt", "r")
    driveNalezenaPrvocisla = cachePrvociselSoubor.read().strip().split("\n")

    cachePrvociselSoubor.close()

    if(str(moznePrvocislo) in driveNalezenaPrvocisla):
        return True
    else:
        odmocninaMoznehoPrvocisla = int(math.ceil(math.sqrt(moznePrvocislo)))

        if(odmocninaMoznehoPrvocisla >
                int(driveNalezenaPrvocisla[len(driveNalezenaPrvocisla)-1])):
            driveNalezenaPrvocisla = ZjistiVicePrvocisel(
                driveNalezenaPrvocisla, odmocninaMoznehoPrvocisla)

        for prvocislo in driveNalezenaPrvocisla:
            if(int(prvocislo) > odmocninaMoznehoPrvocisla):
                break
            if(moznePrvocislo % int(prvocislo) == 0):
                return False

    return True


def ZjistiVicePrvocisel(cachePrvocisel, doCisla):
    """Funkce zjišťuje a vytváří nová prvočísla. Vytváří cache soubor.

    Args:
        - cachePrvocisel - Pole dříve nalezených prvočísel
        - doCisla - Do jakého čísla hledat prvočísla

    Returns:
        - output - Pole všech dosud nalezených prvočísel

    #UNIT TESTY:
    >>> ZjistiVicePrvocisel(["2", "3", "5", "7", "11", "13"], 25)
    ['2', '3', '5', '7', '11', '13', '17', '19', '23']

    >>> ZjistiVicePrvocisel(["2", "3", "5", "7"], 15)
    ['2', '3', '5', '7', '11', '13']

    >>> ZjistiVicePrvocisel(["2"], 10)
    ['2', '3', '5', '7']
    """
    if(int(cachePrvocisel[len(cachePrvocisel) - 1]) == 2):
        cislo = 3
    else:
        cislo = int(cachePrvocisel[len(cachePrvocisel) - 1])
    step = 1

    while(cislo < doCisla):
        startIndex = 1

        if(cislo < 13):
            step = 1
            startIndex = 0
        elif(str(cislo)[-1] == '3'):
            step = 4
        else:
            step = 2

        jePrvocislo = True
        for prvocislo in cachePrvocisel[startIndex:]:
            if(cislo % int(prvocislo) == 0):
                jePrvocislo = False
                break
        if(jePrvocislo):
            cachePrvocisel.append(str(cislo))

        cislo += step
    # END OF WHILE

    cachePrvociselSoubor = open("nalezenaPrvocisla.txt", "w")
    cachePrvociselSoubor.write("\n".join(cachePrvocisel))
    cachePrvociselSoubor.close()

    return cachePrvocisel


def HeurestickaMetoda(o):
    """Funkce zkouší zjistit prvočíslo Heurestickou metodou ((n-1)!+1)%n.

    Args:
        - o - Číslo, u kterého se má zjistit, zda-li je prvočíslo

    Returns:
        - output - Boolean pokud je/není prvočíslo.

    #UNIT TESTY:
    >>> HeurestickaMetoda(7)
    True

    >>> HeurestickaMetoda(6)
    False
    """
    k = 1
    factorial = 1
    for k in range(1, int(o)):
        factorial = factorial * k
    number = factorial + 1
    if int(number) % int(o) == 0:
        return True
    else:
        return False
    pass


# FUNKCE MAIN >>
if __name__ == "__main__":
    moznePrvocislo = Vstup(input())            # Získá vstup od uživatele

    if(moznePrvocislo > 0):             # Otestuje chybový vstup
        Vystup(Metody(moznePrvocislo))  # Vystup s řešením
    else:
        Vystup()                        # Vystup s chybovou hláškou
