import sys
import random

def main():
    input = []  # vytvori list input

    for x in sys.argv:  # nacte vsechny arumenty do listu input
        input.append(x)
    input.pop(0)
    if len(input) == 0:  # tady se prida funkce na nahodne generovain cisel
        input = randomnumbers()
    elif input[0] == "soubor-s-cisly.txt":  # funkce pro cteni ze souboru
        input = readfile()

    bubble_sort(input)
    selection_sort(input)


    # for y in input:  # docasne, vypise cisla
    #    print(y)


def readfile():  # funkce precte soubor a rozdeli skupiny znaku do listu
    file = open("soubor-s-cisly.txt", "r")  # otevre textovy soubor pro cteni
    text = file.read()  # ulozi obsah textoveho souboru do promenne
    output = []  # vytvoří list
    i = ''  # vytvoří promennou
    for j in text:  # projde kazdy znak ze souboru
        if j == ' ':
            output.append(i)  # prida vse z i do listu
            i = ''  # "vynuluje" i
        else:
            i = i + j  # prida aktualni znak k i
    if len(text) != 0:  # prida posledni cislo do listu
        output.append(i)

    return output


def randomnumbers():  # funkce vygenereuje 20 nahodnich cisel
    array = []  # vytvori pole
    for x in range(20):  # Cyklus ktorý sa bude opakovať 20 krát
        array.append(random.randint(0, 200))  # Pridanie cisla do pola
    return array


def bubble_sort(pomocna):  # funkce bubble sort
    for i in range(0, len(pomocna)-1):  # Cyklus ktorý sa bude opakovat pre každý prvek
        for j in range(0, len(pomocna)-1):  # Cyklus ktorý sa bude opakovat pre každý prvek
            if int(pomocna[j]) > int(pomocna[j+1]):  # Porovnani sučasného čisla s nasledujúcim čislem
                a = pomocna[j]  # Priradenie sučasneho čisla do pomocnej
                pomocna[j] = pomocna[j+1]  # Priradenie sučasneho čísla na nasledujúce čislo
                pomocna[j+1] = a  # Priradenie nasledujúceho čisla na promenu
    for y in pomocna:  # docasne, vypise cisla
        print(y)

def selection_sort(pole): # funkce selection sort
    for i in range (0, len(pole)-1): # Cyklus, který se bude opakovat pro každý prvek.
        mezivypocet = i # Přiřazení prvního nezařazeného prvku jako mezivýpočet
        for j in range (i, len(pole)): # Cyklus, který se bude opakovat pro každý nezařazený prvek.
            if pole[mezivypocet] > pole[j]:
                mezivypocet = j # Pokud je současný prvek vyšší než mezivýpočet, tak se prvek stává mezivýpočtem
        mezivypocet2 = pole[i]
        pole[i] = pole[mezivypocet]
        pole[mezivypocet] = mezivypocet2 # Zařazení prvku

    for y in pole:  # Dočasně vypíše čísla
        print(y)
    return pole













if __name__ == '__main__':  # umoznuje psani funkci pod main
    main()  # zavola main funkci
