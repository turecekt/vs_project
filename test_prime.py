"""Funkce test_Metody zjistuje co je použito za metody u kterých čísel."""


def test_Metody():
    """Test metod"""
    assert Metody(1) == -1
    assert Metody(36) == -2
    assert Metody(3) == 3
    assert Metody(8) == -3
    assert Metody(50013) == -4
    assert Metody(50011) == -4
    print ('done')


def test_MetodaPravidelDelitelnosti(MetodaPravidelnosti):
    """Funkce určí některá neprvočísla,pomocí toho, že je číslo končí"""
    """určitým číslem,které podle pravidel,lze vydělit již prvočíslem."""
    assert MetodaPravidelDelitelnosti(88) is True
    assert MetodaPravidelDelitelnosti(87) is False
    return MetodaPravidelnosti

try:
    test_MetodaPravidelDelitelnosti(87)
except AssertionError as msg:
    print(msg)


def test_DeterministickaMetoda(50013, 50011):
    """Funkce zjistuje u téhle metody,jestli je číslo prvočíslo"""
    assert DeterministickaMetoda(50013) is False
    assert DeterministickaMetoda(50011) is False
    return test_DeterministickaMetoda

    test_DeterministickaMetoda(50013, 50011)


def test_HeurestickaMetoda(17, 12, 6):
    """Funkce zjistuje u téhle metody,jestli je číslo prvočíslo"""
    assert HeurestickaMetoda(17) is True
    assert HeurestickaMetoda(12) is False
    assert HeurestickaMetoda(6) is False
    return test_HeurestickaMetoda

    test_HeurestickaMetoda(True, False, False)


def test_Vstup():
    """Správně pouze celá čísla 0-9 ne znaky a písmena)"""
    assert Vstup("1") == 1
    assert Vstup("k") == 0
    return None


def Vstup(Napsanecislo):
    """Funkce získá vstup od uživatele proti chybám."""
    for znak in Napsanecislo:
        if not (znak in "0123456789"):
            return 0

    vstupniCislo = int(Napsanecislo)

    return vstupniCislo


def Vystup(pouzitaMetoda=0):
    """Funkce vypíše výstup(chybu,je či není prvočíslo;použitá metoda)."""
    if (pouzitaMetoda == 0):
        print('CHYBA zadávání. Zadaná hodnota neopodívá formátu,který' +
              'se dá přečíst.Restartuj a zadej přirozené číslo.')

        return
    elif (pouzitaMetoda > 0):
        print("Zadané číslo", moznePrvocislo, "PATŘÍ mezi prvočísla.")
    else:
        print("Zadané číslo", moznePrvocislo, "NEPATŘÍ mezi prvočísla.")
        pouzitaMetoda *= (-1)

    print()

# Popis postupů

    if (pouzitaMetoda == 1):
        print('HEURISTICKÁ metoda-Rozpozná číslo 1 a vyřadí ho, číslo není' +
              'prvočíslo.Číslo musí být dělitelné 2 čísly, sebou a jedničkou')
    elif (pouzitaMetoda == 2):
        print('HEURISTICKÁ metoda-pravidla dělitelnosti.Určí neprvočísla,' +
              'pomocí toho, že číslo končí určitým číslem podle,pravidel' +
              'dělitelnosti, lze vydělit prvočíslem.')
    elif (pouzitaMetoda == 3):
        print('HEURISTICKÁ metoda-Wilsonova věta.Používá vztah n-1!+1%n')
    elif (pouzitaMetoda == 4):
        print('DETERMINISTICKÁ m.-Zkouší pokud je číslo dělitelné některým' +
              'z nalezených prvočísel do maximální hodnoty odmocniny' +
              'ze zadaného čísla.Pokud není dělitelné,je to prvočíslo.')


def Metody(cislo):
    """použita metoda"""
    pouzitaMetoda = 1
    if (cislo <= 1):
        return -pouzitaMetoda

    pouzitaMetoda = 2
    if (MetodaPravidelDelitelnosti(cislo)):
        return -pouzitaMetoda

    pouzitaMetoda = 3
    if (cislo < 40000):
        if (HeurestickaMetoda(cislo)):
            return pouzitaMetoda
        else:
            return -pouzitaMetoda

    pouzitaMetoda = 4
    if (DeterministickaMetoda(cislo)):
        return pouzitaMetoda
    else:
        return -pouzitaMetoda


def MetodaPravidelDelitelnosti(cislo):
    """Je číslo větší jak 9 a zároveň končí čílicí 0-9 není prvočíslo."""
    return (cislo > 9 and str(cislo)[-1] in "024568")


def DeterministickaMetoda(cislo):
    """Pokud číslo není dělitelné prvočísly odmocnina z čísla,je prvočíslo."""
    """number=int(input("Zadej celé číslo: "))prvočísla jsou větší než 1"""
    if cislo > 1:
        for i in range(2, cislo):
            if (cislo % i) == 0:
                return False
        else:
            print("Zadané číslo", cislo, "PATŘÍ mezi prvočísla.")
            return True


def HeurestickaMetoda(o):
    """Funkce zkouší zjistit prvočíslo Heurestickou metodou ((n-1)!+1)%n."""
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
    moznePrvocislo = Vstup(input("Zadej číslo:"))  # Získá vstup od uživatele

    if (moznePrvocislo > 0):             # Otestuje chybový vstup
        Vystup(Metody(moznePrvocislo))  # Vystup s řešením
    else:
        Vystup()                        # Vystup s chybovou hláškou
