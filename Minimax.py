""".
Created on Sun Dec 13 13:31:54 2020

@author: Martin Danielčík
"""

# importuji funkci randint z modulu random a funkci sys
from random import randint
import sys

# deklaruji si pole a proměnou Boolean test pro další postup
pole = []
test = True
"""
Ověřím zda nebyl zadán nějaký argument,
pokud ne vygeneruji pole, pokud ano jdu dál
"""
if len(sys.argv) < 2:
    # 20x vygeneruji číslo mezi 1 až 30 na koenc pole
    for i in range(0, 20):
        pole.append(randint(1, 30))
    print("Pole s 20 pseudonáhodně vygenerovanými prvky mezi čísly 1 a 30:")
    """
    Ověřím zda je první argument název textového souboru,
    pokud ano výtahnu z něj data do pole, pokud ne jdu dál
    """
elif sys.argv[1].endswith(".txt") is True:
    file = open(sys.argv[1], "r")
    # začnu tahat data ze souboru, řádek po řádku
    for i in file.readlines():
        """
        nejdřív vždy vyzkouším zda je řádek možné převést na celé číslo,
        kdyby ne nastavím test na False a vyhnu se Erroru
        """
        try:
            int(i)
        except ValueError:
            test = False
        if test is True:
            tmp = int(i)
            pole.append(tmp)
    # pokud byly všechny řádky v pořádku vypíšu tuto větu
    if test is True:
        print("Pole s hodnotami obsažené ve vašem souboru", sys.argv[1], ":")
    file.close()
    """
    Pokud zde byly argumenty a první nebyl název textového souboru,
    tak museli být zadané čísla
    """
else:
    for i in range(1, len(sys.argv)):
        """
        Nejdříve ověřím zda je argument možné převést na celé číslo, pokud ne,
        nastavím test na False a vyhnu se erroru
        """
        try:
            int(sys.argv[i])
        except ValueError:
            test = False
        if test is True:
            pole.append(int(sys.argv[i]))
    # pokud byly všechny argumenty v pořádku vypíšu tuto větu
    if test is True:
        print("Pole s vámi zadanými hodnotami:")
"""
pokud byly všechny požadavky splněny vypíšu pole a pokračuju dál,
pokud ne napíšu chybovou hlášku
"""
if test is True:
    print(pole)
    # najdu minimální a maximální prvek
    mini = min(pole)
    maxi = max(pole)
    """
    vypíšu hodnotu minimálního prvku a projdu celé pole vždy,
    když se číslo v poli shoduje vypíšu jeho pozici
    """
    print("Nejmenší hodnota v poli", mini, "se nachází na pozici/pozicích:")
    for i in range(0, len(pole)):
        if pole[i] == mini:
            print(i)
    """
    vypíšu hodnotu největšího prvku a projdu celé pole vždy,
    když se číslo v poli shoduje vypíšu jeho pozici
    """
    print("Nevětší hodnota v poli", maxi, "se nachází na pozici/pozicích:")
    for i in range(0, len(pole)):
        if pole[i] == maxi:
            print(i)
    """
    budu se ptát na to, jaký třídící algoritmus chce uživatel použít,
    dokud nezadá celé číslo mezi 1 a 3
    """
    al = 24
    while al > 3 or al < 1:
        al = input("1)Bubble Sort 2) Insertion Sort 3)Selection Sort(1-3)):")
        test = True
        try:
            int(al)
        except ValueError:
            al = 24
            test = False
        if test is True:
            al = int(al)
    # podle inputu do uživatele provedu třídící algoritmus
    # Bubble sort
    if al == 1:
        for i in range(len(pole)):
            for j in range(len(pole) - 1):
                if pole[j] > pole[j+1]:
                    pole[j], pole[j+1] = pole[j+1], pole[j]
    # Insertion sort
    elif al == 2:
        for i in range(1, len(pole)):
            hodnota = pole[i]
            pozice = i
            while pozice > 0 and pole[pozice - 1] > hodnota:
                pole[pozice] = pole[pozice - 1]
                pozice = pozice - 1
            pole[pozice] = hodnota
    # Seletion sort
    else:
        for i in range(len(pole)):
            min_i = i
            for j in range(i + 1, len(pole)):
                if pole[min_i] > pole[j]:
                    min_i = j
            pole[i], pole[min_i] = pole[min_i], pole[i]
    print("Seřazené pole:", pole)
else:
    print("parametry nebo soubor neodpovídají požadavku")
input("Zmáčkni Enter pro ukončení...")
