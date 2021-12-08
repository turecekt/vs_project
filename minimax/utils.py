"""
Tento subor obsahuje potrebne utility funkcie vyuzivane v
hlavnom skripte.
"""
from typing import List, Tuple, Sequence, MutableSequence, Optional


def minimax(cisla: Sequence[int]) -> Tuple[int, int, int, int]:
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
    minimum = cisla[0]
    maximum = cisla[0]
    i_min = 0
    i_max = 0

    for i, cislo in enumerate(cisla):
        if cislo < minimum:
            minimum = cislo
            i_min = i
        if cislo > maximum:
            maximum = cislo
            i_max = i

    return minimum, i_min, maximum, i_max


def bubble_sort(cisla: Sequence[int]) -> List[int]:
    """
    Tato funkcia vyuziva bubble sort algoritmus na zoradenie daneho listu cisel.

    Vstup pre funkciu je list cisel, a vystupom je novy, zoradeny list cisel.
    >>> cisla = [2, -5, 1, 26, 8]
    >>> bubble_sort(cisla)
    [-5, 1, 2, 8, 26]

    Bubble Sort ma komplexitu O(N^2).
    """
    cisla = list(cisla)  # Vytvorenie kopie sekvencie ako list
    for _ in range(1, len(cisla)):
        for j in range(len(cisla) - 1):
            if cisla[j] > cisla[j + 1]:
                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
    return cisla


def _partition(arr: MutableSequence[int], start: int, end: int) -> int:
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


def _quick_sort(
        arr: MutableSequence[int],
        start: Optional[int] = None,
        end: Optional[int] = None
) -> None:
    """
    Tato funkcia vyuziva quick sort algoritmus na zoradenie daneho listu cisiel.

    Na vstupe je zadany list ktory chceme zoradit. Radenie sa deje in-place (
    nevytvarame kopiu!).

    Funkcia berie 3 hodnoty: list, start, end.
    - list: list cisiel na zoradenie (in-place)
    - start: zaciatocny index pre zoradovanie (default: `0` - nutny pre rekurzivne volania)
    - end: koncovy index pre zoradovanie (default: `len(list) - 1` - nutny pre rekurzivne volania)
    >>> lst = [1, 8, 0, -5, 2, 9, 100, 6]
    >>> _quick_sort(lst, 0, len(lst) - 1)

    - quick_sort nevracia ziadny vystup, zoraduje na mieste

    Quick sort ma komplexitu O(n*log n).
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
    _quick_sort(arr, start, index - 1)
    _quick_sort(arr, index + 1, end)


def quick_sort(arr: Sequence[int]) -> List[int]:
    """
    Wrapper pre _quick_sort ktory funguje na principe kopii namiesto in-place upravy listu.
    >>> lst = [1, 8, 0, -5, 2, 9, 100, 6]
    >>> quick_sort(lst)
    [-5, 0, 1, 2, 6, 8, 9, 100]

    Pre detaily o quick_sort algoritme vid docstring pre _quick_sort funkciu.
    """
    arr = list(arr)  # Vytvorenie kopie sekvencie ako list
    _quick_sort(arr)
    return arr


def insertion_sort(cisla: Sequence[int]) -> List[int]:
    """
    Tato funkcia vyuziva insertion sort algoritmus na zoradenie daneho listu cisel.

    Vstup pre funkciu je list cisel, a vystupom je novy, zoradeny list cisel.

    >>> cisla = [2, -5, 1, 26, 8]
    >>> insertion_sort(cisla)
    [-5, 1, 2, 8, 26]

    Insertion Sort ma komplexitu O(N^2)
    """
    cisla = list(cisla)  # Vytvorenie kopie sekvencie ako list
    for index in range(1, len(cisla)):
        current_value = cisla[index]
        current_position = index
        while current_position > 0 and cisla[current_position - 1] > current_value:
            cisla[current_position] = cisla[current_position - 1]
            current_position = current_position - 1
        cisla[current_position] = current_value
    return cisla
