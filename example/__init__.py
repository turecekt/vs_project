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
    # Funkce na ošetření vstupu, vrátí hodnotu čísla, popřípadě vrátí hodnotu -1 pokud
    # vstup neodpovídá číslu na ověření
    vstupniCislo = 0

    return vstupniCislo

def Vystup(pouzitaMetoda = 0):
    # Funkce vypíše výstup, 
    # Obsahuje parametr int (pro označení použité metody a zda výsledek vyšel či ne)
    # Zobrazí i informace o použité metodě, ne jen její název

    pass

def Metody(prvocislo):
    # Funkce, kde se budou zkoušet jednotlivé metody a podle toho se bude informovat uzivatel
    # Vrátí int, s mínusem pokud číslo není prvočíslo, s plusem pokud je
    # Číslo navíc ozančuje číslo metody, která byla použita k dostání výsledku
    # V metodě lze použít multitasking
    pouzitaMetoda = 0


    return pouzitaMetoda

def KlasickaMetoda():
    # Funkce zkouší všechny dělitele a podle toho zjišťuje, zda-li je číslo prvočíslo
    # Velmi pomalá (musí být omezena do 700000 max)
    pass

def MetodaPravidelDelitelnosti():
    # Funkce zkouší, zda-li je číslo větší jak 9 a zároveň končí čílicí 0, 2, 4, 5, 6 či 8
    # Pokud funkce splňuje podmínky, je jasné, že zadané číslo není prvočíslo

    pass

def DeterministickaMetoda():
    #Funkce zkouší zjistit prvočíslo Deterministickou metodou

    pass

def HeurestickaMetoda():
    #Funkce zkouší zjistit prvočíslo Heurestickou metodou

    pass

#FUNKCE MAIN >>
moznePrvocislo = Vstup()            # Získá vstup od uživatele

if(moznePrvocislo > 0):             # Otestuje chybový vstup
    Vystup(Metody(moznePrvocislo))  # Vystup s řešením
else:
    Vystup()                        # Vystup s chybovou hláškou
