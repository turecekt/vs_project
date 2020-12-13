"""Minimax.py program pro serazeni cisel a vypisu informaci o prvcich."""
import sys
import random
import pytest

def main():
    """Hlavni funkce."""
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
                numbers.append(int(vstup[x]))
                # preda polozku jako cislo do promenne

    roztrizene = moznostizoradenia(numbers)  # vyber tridiciho algoritmu
    if len(roztrizene) > 0:  # provede jestli existuje vystup
        print("Vstup: ", end='')
        for x in numbers:  # napise vstupni cisla
            print(x, " ", end='')
        print()
        print("Nejmensi prvek: ", roztrizene[0])  # napise prvni cislo
        print("Nejvetsi prvek: ", roztrizene[len(roztrizene)-1])
        # napise posledni cislo
        print("Roztrizene cisla: ", end='')
        for x in roztrizene:  # napise roztrizena cisla
            print(x, " ", end='')


def readfile():  # funkce precte soubor a rozdeli skupiny znaku do listu
    """Cteni souboru."""
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
    """Generace cisel."""
    array = []  # vytvori pole
    for x in range(20):  # Cyklus ktorý sa bude opakovať 20 krát
        array.append(random.randint(0, 200))  # Pridanie cisla do pola
    return array


def bubble_sort(pomocna):  # funkce bubble sort
    """Bubble_sort."""
    for i in range(0, len(pomocna)-1):  # Cyklus pre každý prvek
        for j in range(0, len(pomocna)-1):  # Cyklus pre každý prvek
            if pomocna[j] > pomocna[j+1]:  # Porovnani čisel
                a = pomocna[j]  # Priradenie sučasneho čisla do pomocnej
                pomocna[j] = pomocna[j+1]  # Vymena čisel
                pomocna[j+1] = a  # Priradenie nasledujúceho čisla na promenu

    return pomocna


def selection_sort(pole):  # funkce selection sort
    """Selection_sort."""
    for i in range(0, len(pole)):  # Cyklus pro každý prvek.
        mezivypocet = i  # Uložení prvního prvku do proměnné
        for j in range(i, len(pole)):  # Cyklus pro každý nezařazený prvek.
            if pole[mezivypocet] > pole[j]:
                mezivypocet = j
                # Pokud je současný prvek vyšší než mezivýpočet,
                # tak se prvek stává mezivýpočtem
        mezivypocet2 = pole[i]
        pole[i] = pole[mezivypocet]
        pole[mezivypocet] = mezivypocet2  # Zařazení prvku

    return pole


def quick_sort(pole):
    """Quick_sort."""
    for i in range(1, len(pole)):  # Cyklus pro každý prvek
        val = pole[i]  # Vložení soucasneho prvku do proměnné
        j = i - 1  # Uložení indexu o jeden méňe než současný index
        while j >= 0 and val < pole[j]:  # Prochazi prvky od j po 0/val
            pole[j+1] = pole[j]  # Vymeni polozku
            j = j - 1  # Zmensi j
        pole[j+1] = val  # Zapise val na misto j+1

    return pole


def moznostizoradenia(cislo):  # funkce moznosti zoradenia
    """Vyber sortu."""
    pole = cislo.copy()
    print('Moznosti zoradenia:\n '
          '1 - Zoradenie pomocou bubble sort\n '
          '2 - Zoradenie pomocou selection sort\n '
          '3 - Zoradenie pomocou quick sort ')  # Vypis moznosti zoradenia
    klavesa = input('Prosim zadaj moznost zoradenia :\n ')
    # Žadosť o zadanie možnosti zoradenia
    if klavesa == '1':  # Načitanie čisla
        serazeno = bubble_sort(pole)  # Odkaz na funkciu bubble sort
    elif klavesa == '2':  # Načitanie čisla
        serazeno = selection_sort(pole)  # Odkazo na funkciu selection sort
    elif klavesa == '3':  # Načitanie čisla
        serazeno = quick_sort(pole)  # Odkaz na funkci quick sort
    else:  # Ak zadané čislo sa nenachádza v možnostiach
        print('Zadali ste spatnu hodnotu')  # Vypis chybného hlášenia
        return
    return serazeno

def test_bubble_sort():
    assert bubble_sort([45, 2077, 69, 420, 3, 666, 2020, 56, 28, 99, 4, 68])==[3, 4, 28,45, 56, 68, 69, 99, 420, 666, 2020, 2077]

def test_selection_sort():
    assert selection_sort([45, 2077, 69, 420, 3, 666, 2020, 56, 28, 99, 4, 68])==[3, 4, 28,45, 56, 68, 69, 99, 420, 666, 2020, 2077]

def test_quick_sort():
    assert quick_sort([45, 2077, 69, 420, 3, 666, 2020, 56, 28, 99, 4, 68])==[3, 4, 28,45, 56, 68, 69, 99, 420, 666, 2020, 2077]

if __name__ == '__main__':  # umoznuje psani funkci pod main
    main()  # zavola main funkci
