import sys
import random


def main():
    vstup = []  # vytvori list vstup
    numbers = []  # vytvori list filtrovany vstup

    for x in sys.argv:  # nacte vsechny arumenty do listu vstup
        vstup.append(x)
    vstup.pop(0)  # ondstrani prvni argument (cestu k souboru)

    if len(vstup) == 0:  # nahodne generovani cisel
        numbers = randomnumbers()
    elif vstup[0] == "soubor-s-cisly.txt":  # funkce pro cteni ze souboru
        vstup = readfile()

    if len(vstup) > 0:
        for x in range(0, len(vstup)):
            if vstup[x].isnumeric():  # zjisti jestli je polozka cislo
                numbers.append(int(vstup[x]))  # preda polozku jako cislo do promenne

    moznostizoradenia(numbers)
    # for y in vstup:  # docasne, vypise cisla
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
            if pomocna[j] > pomocna[j+1]:  # Porovnani sučasného čisla s nasledujúcim čislem
                a = pomocna[j]  # Priradenie sučasneho čisla do pomocnej
                pomocna[j] = pomocna[j+1]  # Priradenie sučasneho čísla na nasledujúce čislo
                pomocna[j+1] = a  # Priradenie nasledujúceho čisla na promenu

    return pomocna


def selection_sort(pole):  # funkce selection sort
    for i in range(0, len(pole)):  # Cyklus, který se bude opakovat pro každý prvek.
        mezivypocet = i  # Přiřazení prvního nezařazeného prvku jako mezivýpočet
        for j in range(i, len(pole)):  # Cyklus, který se bude opakovat pro každý nezařazený prvek.
            if pole[mezivypocet] > pole[j]:
                mezivypocet = j  # Pokud je současný prvek vyšší než mezivýpočet, tak se prvek stává mezivýpočtem
        mezivypocet2 = pole[i]
        pole[i] = pole[mezivypocet]
        pole[mezivypocet] = mezivypocet2  # Zařazení prvku

    return pole


def quick_sort(pole):
    for i in range(1, len(pole)):
        val = pole[i]
        j = i - 1
        while j >= 0 and val < pole[j]:
            pole[j+1] = pole[j]
            j = j - 1
        pole[j+1] = val
    return pole


def moznostizoradenia(cislo):  # funkce moznosti zoradenia
    print('Moznosti zoradenia:\n '
          '1 - Zoradenie pomocou bubble sort\n '
          '2 - Zoradenie pomocou selection sort\n '
          '3 - Zoradenie pomocou ')  # Vypis moznosti zoradenia
    klavesa = input('Prosim zadaj moznost zoradenia :\n ')  # Žadosť o zadanie možnosti zoradenia
    if klavesa == '1':  # Načitanie čisla
        serazeno = bubble_sort(cislo)  # Odkazovanie na funkciu bubble sort
    elif klavesa == '2':  # Načitanie čisla
        serazeno = selection_sort(cislo)  # Odkazovanie na funkciu selection sort
    elif klavesa == '3':  # Načitanie čisla
        serazeno = quick_sort(cislo)  # Odkaz na funkci quick sort
    else:  # Ak zadané čislo sa nenachádza v možnostiach
        print('Zadali ste spatnu hodnotu')  # Vypis chybného hlášenia
        return
    for i in serazeno:
        print(i)


if __name__ == '__main__':  # umoznuje psani funkci pod main
    main()  # zavola main funkci
