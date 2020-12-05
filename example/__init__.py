import os.path
import math
from os import path

"""Ukázka souboru: """
"""This is the "example" module.

The example module supplies one function: compute(). For example,

>>> compute(3)
3
"


def compute(x):
    "Functon compute returns evaluation of expression using argument x.

    Args:
        - x - Input of the function

    Returns:
        - output - Output of the function
    "
    return x * x - 2 * x

"""

"""
Zadání úkolu: Prvočíslo
------------------------------------------------------------------------------

Program určí, zda je vstupní číslo prvočíslo či nikoliv. Pro vyšší čísla program použije
některou z heuristických či statistických metod, o použití alternativní metody program bude
informovat uživatele.
VSTUP
    - Libovolné celé číslo zadané uživatelem
    - Program neakceptuje jiný/neplatný vstup
VÝSTUP
    - Informace o tom zda je číslo prvočíslo či nikoliv
    - Informace jakým způsobem byl výsledek zjištěn (deterministickou/heuristickou metodou)

- Klasický kód -
"""
def Vstup():
    # Funkce na ošetření vstupu, vrátí hodnotu čísla, popřípadě vrátí hodnotu 0 pokud
    # vstup neodpovídá číslu na ověření
    
    #    >> TADY BY MĚL BYT KOD CO UDĚLÁ RADIM II <<
    vstupniCislo = 0

    return vstupniCislo

def Vystup(pouzitaMetoda = 0):
    # Funkce vypíše výstup, 
    # Obsahuje parametr int (pro označení použité metody a zda výsledek vyšel či ne)
    # Zobrazí i informace o použité metodě, ne jen její název

    if(pouzitaMetoda == 0):
        print("-------------------------------------------------------------------------------")
        print("Nastala CHYBA způsobená uživatelem.")
        print("-------------------------------------------------------------------------------")
        print("Zadaná hodnota neopodívá formátu, který se dá přečíst pro rozpoznání prvočísla.")
        print("Zkuste program restartovat a zadat přirozené číslo. (1 až nekonečno)")
        return
    elif(pouzitaMetoda > 0):
        print("Zadané číslo PATŘÍ mezi prvočísla.")
    else:
        print("Zadané číslo NEPATŘÍ mezi prvočísla.")
        pouzitaMetoda *= (-1)

    print("-------------------------------------------------------------------------------")

    #Popis postupů
    if(pouzitaMetoda == 1):
        print("Byla použita HEURISTICKÁ metoda - 1")
        print("-------------------------------------------------------------------------------")
        print("Metoda rozpozná číslici 1 a vyřadí ji z pátrání, protože toto číslo nesplňuje")
        print("definici prvočísel. (číslo musí být dělitelné DVĚMA čísly, samosebou a jedničkou)")
    elif(pouzitaMetoda == 2):
        print("Byla použita HEURISTICKÁ metoda - pravidla dělitelnosti")
        print("-------------------------------------------------------------------------------")
        print("Metoda určí některá neprvočísla, pomocí toho, že je číslo končí určitým číslem, ")
        print("které podle pravidel dělitelnosti, lze vydělit již prvočíslem. (např. čísla končící")
        print("na číslo 5 a 0 jdou vždy vydělit 5)")
    elif(pouzitaMetoda == 3):
        print("Byla použita HEURISTICKÁ metoda - Wilsonova věta")
        print("-------------------------------------------------------------------------------")
        print("Metoda používá matematický vztah '((n - 1)! + 1) % n' pro zjištění některých ")
        print("prvočísel.")
    elif(pouzitaMetoda == 4):
        print("Byla použita DETERMINISTICKÁ metoda")
        print("-------------------------------------------------------------------------------")
        print("Metoda zkouší pokud je číslo dělitelné některým z již předtím nalezených")
        print("prvočísel do maximální hodnoty odmocniny ze zadaného čísla. Pokud číslo není")
        print("dělitelné, je to další prvočíslo.")
        print("Např. u čísla 7 otestuje dělitelnost prvočísly do čísla 4, tudíž číslem 2 a 3,")
        print("nevznikne zbytek 0, tudíž číslo 7 je prvočíslo.")
        print("(metoda používá paměť s vypočítanými prvočísly k zrychlení procesu)")
    else:
        print("Pravděpodobně jde o nějakou metodu, kterou si vymyslela umělá inteligence")
        print("vašeho počítače. Tuhle zprávu byste totiž neměli nikdy vidět.")

def Metody(cislo):
    # Funkce, kde se budou zkoušet jednotlivé metody a podle toho se bude informovat uzivatel
    # Vrátí int, s mínusem pokud číslo není prvočíslo, s plusem pokud je
    # Číslo navíc ozančuje číslo metody, která byla použita k dostání výsledku

    # Označení metod:
    # 1 - Metoda 0 a 1
    # 2 - MetodaPravidelDelitelnosti
    # 3 - HeurestickaMetoda
    # 4 - DeterministickaMetoda

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
    # Funkce zkouší, zda-li je číslo větší jak 9 a zároveň končí čílicí 0, 2, 4, 5, 6 či 8
    # Pokud funkce splňuje podmínky, je jasné, že zadané číslo není prvočíslo
    # Vrací True pokud číslo není prvočíslo
    return (cislo > 9 and str(cislo)[-1] in "024568")

def DeterministickaMetoda(moznePrvocislo):
    #Funkce zkouší zjistit prvočíslo Deterministickou metodou
    
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
        
        if(odmocninaMoznehoPrvocisla > int(driveNalezenaPrvocisla[len(driveNalezenaPrvocisla) - 1])):
            driveNalezenaPrvocisla = ZjistiVicePrvocisel(driveNalezenaPrvocisla, odmocninaMoznehoPrvocisla)

        for prvocislo in driveNalezenaPrvocisla:
            if(int(prvocislo) > odmocninaMoznehoPrvocisla):
                break
            if(moznePrvocislo % int(prvocislo) == 0):
                return False
                
    return True

def ZjistiVicePrvocisel(cachePrvocisel, doCisla):
    if(int(cachePrvocisel[len(cachePrvocisel) - 1]) == 2):
        cislo = 3
    else:
        cislo = int(cachePrvocisel[len(cachePrvocisel) - 1])
    step = 1

    while(cislo < doCisla):
        if(cislo < 13):
            step = 1
        elif(str(cislo)[-1] == '3'):
            step = 4
        else:
            step = 2

        jePrvocislo = True
        for prvocislo in cachePrvocisel[1:]:
            if(cislo % int(prvocislo) == 0):
                jePrvocislo = False
                break
        if(jePrvocislo):
            cachePrvocisel.append(str(cislo))

        cislo += step
    #END WHILE

    cachePrvociselSoubor = open("nalezenaPrvocisla.txt", "w")
    cachePrvociselSoubor.write("\n".join(cachePrvocisel))
    cachePrvociselSoubor.close()

    return cachePrvocisel

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

# FUNKCE MAIN >>
moznePrvocislo = Vstup()            # Získá vstup od uživatele

if(moznePrvocislo > 0):             # Otestuje chybový vstup
    Vystup(Metody(moznePrvocislo))  # Vystup s řešením
else:
    Vystup()                        # Vystup s chybovou hláškou
