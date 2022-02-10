"""
Program určí, zda je vstupní číslo prvočíslo či nikoliv.
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


def test_Metody():
    assert Metody(1) == -1
    assert Metody(36) == -2
    assert Metody(3) == 3
    assert Metody(7) == -3
    assert Metody(50013) == 4
    assert Metody(50011) == -4


def test_MetodaPravidelDelitelnosti():
    assert MetodaPravidelDelitelnosti(88) == True
    assert MetodaPravidelDelitelnosti(61) == False


def test_DeterministickaMetoda():
    assert DeterministickaMetoda(90901) == True
    assert DeterministickaMetoda(50011) == False


def test_HeurestickaMetoda():
    assert HeurestickaMetoda(17) == True
    assert HeurestickaMetoda(12) == False


def Vstup(Napsanecislo):
    """
    Funkce získá vstup od uživatele proti chybám.
    """

    for znak in Napsanecislo:
        if not(znak in "0123456789"):
            return 0

    vstupniCislo = int(Napsanecislo)

    return vstupniCislo


def Vystup(pouzitaMetoda=0):
    """
    Funkce vypíše výstup programu (chybu, je či není prvočíslo; použitá metoda).
    """
    if(pouzitaMetoda == 0):
        print()
        print("Nastala CHYBA způsobená uživatelem při zadávání.")
        print()
        print("Zadaná hodnota neopodívá formátu, který se dá přečíst pro " +
              "rozpoznání prvočísla.")
        print("Zkuste program restartovat a zadat přirozené číslo od 1 až do nekonečna. ")

        return
    elif(pouzitaMetoda > 0):
        print("Zadané číslo" , moznePrvocislo , "PATŘÍ mezi prvočísla.")
    else:
        print("Zadané číslo" , moznePrvocislo , "NEPATŘÍ mezi prvočísla.")
        pouzitaMetoda *= (-1)

    print()

# Popis postupů
    if(pouzitaMetoda == 1):
        print("Byla použita HEURISTICKÁ metoda - 1")
        print()
        print("Metoda rozpozná číslici 1 a vyřadí ji z pátrání, protože " +
              "toto číslo nesplňuje definici prvočísel. (číslo musí být ")
        print("dělitelné DVĚMA čísly, samosebou a jedničkou)")
    elif(pouzitaMetoda == 2):
        print("Byla použita HEURISTICKÁ metoda - pravidla dělitelnosti")
        print()
        print("Metoda určí některá neprvočísla, pomocí toho, že je číslo "
              "končí určitým číslem, které podle pravidel dělitelnosti, lze ")
        print("vydělit již prvočíslem. (např. čísla končící na číslo 5 a 0 ")
        print("jdou vždy vydělit 5)")
    elif(pouzitaMetoda == 3):
        print("Byla použita HEURISTICKÁ metoda - Wilsonova věta")
        print()
        print("Metoda používá matematický vztah '((n - 1)! + 1) % n' pro " +
              "zjištění některých prvočísel.")
    elif(pouzitaMetoda == 4):
        print("Byla použita DETERMINISTICKÁ metoda")
        print()
        print("Metoda zkouší pokud je číslo dělitelné některým z již " +
              "předtím nalezených prvočísel do maximální hodnoty odmocniny ")
        print("ze zadaného čísla. Pokud číslo není dělitelné, je to ")
        print("další prvočíslo.")
        print("Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4, " +
              "tudíž číslem 2 a 3, nevznikne zbytek 0 a tak je číslo 7 ")
        print("prvočíslo. (metoda používá paměť s vypočítanými prvočísly " +
              "k zrychlení procesu)")


def Metody(cislo):
    """
    Funkce zkouší zjistit výsledek různými metodami podle typu čísla.
    Označení metod:
        1 - Metoda 0 a 1
        2 - MetodaPravidelDelitelnosti
        3 - HeurestickaMetoda
        4 - DeterministickaMetoda
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
    """
    Funkce zkouší, zda číslo není prvočíslo.
    Je-li je číslo větší jak 9 a zároveň končí čílicí 0, 2, 4, 5, 6 či 8,
    tak toto číslo provčíslo není.
    """
    return (cislo > 9 and str(cislo)[-1] in "024568")


def DeterministickaMetoda(moznePrvocislo):
    """
    Funkce zkouší zjistit prvočíslo deterministickou metodou.
    Pokud číslo není dělitelné prvočísly do odmocnina z čísla,
    pak je prvočíslo. Funkce vytváří cache soubor.
    """

# number=int(input("Zadej celé číslo: "))
# prvočísla jsou větší než 1
    if moznePrvocislo > 1:
# omezující podmínky
        for i in range(2, moznePrvocislo):
            if (moznePrvocislo % i) == 0:
                break
        else:
            print("Zadané číslo" , moznePrvocislo , "PATŘÍ mezi prvočísla.")


def HeurestickaMetoda(o):
    """
    Funkce zkouší zjistit prvočíslo Heurestickou metodou ((n-1)!+1)%n.
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

if __name__ == "__main__":
    # MAIN
    moznePrvocislo = Vstup(input("Zadej číslo:")) # Získá vstup od uživatele
    
    if(moznePrvocislo > 0):             # Otestuje chybový vstup
        Vystup(Metody(moznePrvocislo))  # Vystup s řešením
    else:
        Vystup()                        # Vystup s chybovou hláškou
