"""
Created on Sun Dec 13 13:31:54 2020

@author: Martin Danielčík
"""

# importuji funkci randint z modulu random a funkci sys
from random import randint
import sys

# deklaruji si pole a proměnou Boolean test pro další postup
pole = []
test = True 
# ověřím zda nebyl zadán nějaký argument, pokud ne vygeneruji pole, pokud ano jdu dál
if len(sys.argv) < 2:
    for i in range(0, 20): 
        pole.append(randint(1, 30))
    print ("Pole s 20 pseudonáhodně vygenerovanými prvky mezi čísly 1 a 30:")
# ověřím zda je první argument název textového souboru, pokud ano výtahnu z něj data do pole, pokud ne jdu dál
elif sys.argv[1].endswith(".txt") == True:
    file = open(sys.argv[1], "r")
    # začnu tahat data ze souboru, řádek po řádku
    for i in file.readlines():
        # nejdřív vždy vyzkouším zda je řádek možné převést na celé číslo, kdyby ne nastavím test na False a vyhnu se Erroru
        try:
            int(i)
        except ValueError:
            test = False
        if test == True:
            tmp = int(i)
            pole.append(tmp)
    # pokud byly všechny řádky v pořádku vypíšu tuto větu
    if test == True:
        print ("Pole s hodnotami obsažené ve vašem soubotu", sys.argv[1],":")
    file.close()
# Pokud zde byly argumenty a první nebyl název textového souboru tak museli být zadané čísla
else:
    for i in range(1, len(sys.argv)):
        # Nejdříve ověřím zda je argument možné převést na celé číslo, pokud ne, nastavím test na False a vyhnu se erroru
        try:
            int(sys.argv[i])
        except ValueError:
            test = False
        if test == True:
            pole.append(int(sys.argv[i]))
    # pokud byly všechny argumenty v pořádku vypíšu tuto větu
    if test == True:
        print ("Pole s vámi zadanými hodnotami:")
# pokud byly všechny požadavky splněny vypíšu pole, pokud ne napíšu chybovou hlášku
if test == True:
    print(pole)
else:
    print("parametry nebo soubor neodpovídají požadavku")
input("Zmáčkni Enter pro ukončení...")
