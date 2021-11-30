import sys
import random


def minimax(cislo):
    """
    Funkcia pre najdenie maxima a minima zadanej sekvencie cisiel.

    Funkcia vracia 4 hodnoty: minimum, index minium, maximum, index maximum (v poradi)
    >>> minimax([1, 2, 3, -1])
    (-1, 3, 3, 2)

    Implementacia hladania minima a maxima nevyuziva built-in funkcie
    min(x)/max(x), pretoze to pravdepodobne nebolo cielom tohoto zadania.
    Bezne by sme ale chceli vyuzit tieto funkcie, namiesto implementovania
    niecoho co jazyk samotny uz podporuje.
    """
    minimum = cislo[0]
    maximum = cislo[0]
    i_min = 0
    i_max = 0

    for i, cislo in enumerate(cislo):
        if cislo < minimum:
            minimum = cislo
            i_min = i
        if cislo > maximum:
            maximum = cislo
            i_max = i

    return minimum, i_min, maximum, i_max


def bubble_sort(cisla):
    """
    Tato funkcia vyuziva bubble sort algoritmus na zoradenie daneho listu cisel.

    Vstup pre funkciu je list cisel, a vystupom je novy, zoradeny list cisel.
    Bubble Sort ma komplexitu O(N^2).
    """
    cisla = cisla.copy()
    for _ in range(1, len(cisla)):
        for j in range(len(cisla) -1):
            if cisla[j] > cisla[j+1]:
                cisla[j], cisla[j+1] = cisla [j+1], cisla[j]
    return cisla


def _partition(arr, start, end):
    """
    Podporna funkcia pre quick_sort.

    V tejto funkcii zoradujeme dany list na 2 skupiny:
    1. Cisla vatsie ako pivot
    2. Cisla mensie ako pivot
    - Pivot je cislo vybrane zo sekvencie, v tomto pripade
    vyberame posledny prvok.

    Funkcia prejde cez elementy listu v danom intervale a
    presunie ich pred alebo za pivot index.

    Vraciame index tohoto pivotu, a list zoradujeme na mieste (in-place).
    """
    # Nastavenie pivotu na posledny element
    # Pivot je hodnota na zaklade ktorej budeme porovnavat
    # ostatne elementy
    pivot_hodnota = arr[end]
    pivot_index = start

    # Prejdeme cez start-end elementy a vymenime dany element
    # s elementom na pivot_indexe vzdy ked je hodnota mensia
    # ako hodnota pivotu po vymene zvysime pivot_index o 1
    for i in range(start, end):
        if arr[i] < pivot_hodnota:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    # Posledna vymena aby sme dostali pivot do stredu
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return pivot_index


def quick_sort(arr, start=None, end=None):
    """
    Tato funkcia vyuziva quick sort algoritmus na zoradenie daneho listu cisiel.

    Na vstupe je zadany list ktory chceme zoradit. Radenie sa deje in-place (
    nevytvarame kopiu!). Quick sort ma komplexitu O(n*log n).

    Funkcia berie 3 hodnoty: list, start, end.
    - list: list cisiel na zoradenie (in-place)
    - start: zaciatocny index pre zoradovanie (default: `0` - nutny pre rekurzivne volania)
    - end: koncovy index pre zoradovanie (default: `len(list) - 1` - nutny pre rekurzivne volania)
    >>> lst = [1, 8, 0, -5, 2, 9, 100, 6]
    >>> quick_sort(lst, 0, len(lst) - 1)
    None  # quick_sort nevracia ziadny vystup, zoraduje na mieste
    """
    # Vychodzie hodnoty pre start a end:
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1

    # Ak sa dostaneme na koniec, sekcia je zoradena
    if start >= end:
        return

    # Zoradenie prvkov k pivotu (strednej hodnote), index je
    # pozicia tohoto pivotu
    index = _partition(arr, start, end)

    # Zoradenie hodnot v 2 zostavajucich sekciach (pred a za
    # strednym indexom pivotu)
    quick_sort(arr, start, index - 1)
    quick_sort(arr, index + 1, end)

def insertion_sort(cisla):
    for index in range(1, len(cisla)):
        current_value = cisla[index]
        current_position = index
        while current_position > 0 and cisla[current_position - 1] > current_value:
            cisla[current_position] = cisla[current_position -1]
            current_position = current_position - 1
        cisla[current_position] = current_value

def main():
    """Hlavna funkcia programu."""
    argumenty = sys.argv[1:]
    if len(argumenty) == 1:
        with open(argumenty[0], "r") as f:
            cisla = [int(x) for x in f.read().split()]
    elif len(argumenty) > 1:
        cisla = [int(x) for x in argumenty]
    else:
        cisla = [random.randint(-100, 100) for _ in range(20)]

    # bubble sort vyrvara novy zoradeny list
    bubble_sort_zoradene = bubble_sort(cisla)
    # quick sort funguje in-place.
    quick_sort_zoradenie = cisla.copy()
    quick_sort(quick_sort_zoradenie)

    insertion_sort_zoradene = cisla.copy()
    insertion_sort(insertion_sort_zoradene)

    print(minimax(cisla))
    print(bubble_sort_zoradene)
    print(quick_sort_zoradenie)
    print(insertion_sort_zoradene)


if __name__ == "__main__":
    main()
