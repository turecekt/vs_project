#   Funkce test_Metody zjistuje co je použito za metody u kterých čísel.

def test_Metody():
    assert Metody(1) == -1
    assert Metody(36) == -2
    assert Metody(3) == 3
    assert Metody(8) == -3
    assert Metody(50013) == -4
    assert Metody(50011) == -4

#   Funkce test_MetodaPravidelDelitelnosti určí některá neprvočísla, pomocí toho, že je číslo končí určitým číslem, které podle pravidel dělitelnosti, lze vydělit již prvočíslem. (např. čísla končící na číslo 5 a 0 jdou vždy vydělit 5.
    
def test_MetodaPravidelDelitelnosti():
    assert MetodaPravidelDelitelnosti(88) == True

#   Funkce test_DeterministickaMetoda zjistuje u téhle metody, jestli je číslo prvočíslo = True nebo není = False.
    
def test_DeterministickaMetoda():
    assert DeterministickaMetoda(50013) == False

#   Funkce test_HeurestickaMetoda zjistuje u téhle metody, jestli je číslo prvočíslo = True nebo není = False.
    
def test_HeurestickaMetoda():
    assert HeurestickaMetoda(17) == True
    assert HeurestickaMetoda(12) == False
    
#   Funkce test_vstup zjistuje, jestli byl vstup zadán špatně nebo správně (správně pouze celá čísla a jen čísla 0,1,2,3,4,5,6,7,8,9 ne znaky a písmena to se vyhodnotí chybou)
    
def test_Vstup():
    assert Vstup("k") == False
    assert Vstup("1") == True

def Vstup(Napsanecislo):

#   Funkce získá vstup od uživatele proti chybám.

    for znak in Napsanecislo:
        if not(znak in "0123456789"):
            return 0

    vstupniCislo = int(Napsanecislo)

    return vstupniCislo


def Vystup(pouzitaMetoda=0):
 
#   Funkce vypíše výstup programu (chybu, je či není prvočíslo; použitá metoda).
  
    my_str = 'Nastala CHYBA způsobená uživatelem při zadávání. Zadaná hodnota neopodívá formátu, který se dá přečíst pro rozpoznání prvočísla. Zkuste program restartovat a zadat přirozené číslo od 1 až do nekonečna.'
    
    if(pouzitaMetoda == 0):
        print(my_str)

        return
    elif(pouzitaMetoda > 0):
        print("Zadané číslo" , moznePrvocislo , "PATŘÍ mezi prvočísla.")
    else:
        print("Zadané číslo" , moznePrvocislo , "NEPATŘÍ mezi prvočísla.")
        pouzitaMetoda *= (-1)

    print()

# Popis postupů

    my_str1 = 'Byla použita HEURISTICKÁ metoda - 1 Metoda rozpozná číslici 1 a vyřadí ji z pátrání, protože toto číslo nesplňuje definici prvočísel. (číslo musí být dělitelné DVĚMA čísly, samosebou a jedničkou) '
    my_str2 = 'Byla použita HEURISTICKÁ metoda - pravidla dělitelnosti Metoda určí některá neprvočísla, pomocí toho, že je číslo končí určitým číslem, které podle pravidel dělitelnosti, lze vydělit již prvočíslem. (např. čísla končící na číslo 5 a 0 jdou vždy vydělit 5)'
    my_str3 = 'Byla použita HEURISTICKÁ metoda - Wilsonova věta. Metoda používá matematický vztah ((n - 1)! + 1) % n pro zjištění některých prvočísel.'
    my_str4 = 'Byla použita DETERMINISTICKÁ metoda - Metoda zkouší pokud je číslo dělitelné některým z již předtím nalezených prvočísel do maximální hodnoty odmocniny ze zadaného čísla. Pokud číslo není dělitelné, je to další prvočíslo. Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4, tudíž číslem 2 a 3, nevznikne zbytek 0 a tak je číslo 7 prvočíslo. (metoda používá paměť s vypočítanými prvočísly k zrychlení procesu)'
    
    if(pouzitaMetoda == 1):
        print(my_str1)
    elif(pouzitaMetoda == 2):
        print(my_str2)
    elif(pouzitaMetoda == 3):
        print(my_str3)
    elif(pouzitaMetoda == 4):
        print(my_str4)

def Metody(cislo):

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
   
#  Je-li je číslo větší jak 9 a zároveň končí čílicí 0, 2, 4, 5, 6 či 8, tak toto číslo provčíslo není.
    
    return (cislo > 9 and str(cislo)[-1] in "024568")


def DeterministickaMetoda(cislo):

# Pokud číslo není dělitelné prvočísly do odmocnina z čísla, pak je prvočíslo.

# number=int(input("Zadej celé číslo: "))
# prvočísla jsou větší než 1
    if cislo > 1:
# omezující podmínky
        for i in range(2, cislo):
            if (cislo % i) == 0:
                return False
        else:
            print("Zadané číslo" , cislo , "PATŘÍ mezi prvočísla.")
            return True

def HeurestickaMetoda(o):
    
#   Funkce zkouší zjistit prvočíslo Heurestickou metodou ((n-1)!+1)%n.
    
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
