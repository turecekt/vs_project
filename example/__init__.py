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
    Bubble Sort ma komplexitu O(N).
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


def quick_sort(arr, start, end):
    """
    Tato funkcia vyuziva quick sort algoritmus na zoradenie daneho listu cisiel.

    Na vstupe je zadany list ktory chceme zoradit. Radenie sa deje in-place (
    nevytvarame kopiu!). Quick sort ma komplexitu O(n*log n).
    """
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


def main():
    """Hlavna funkcia programu."""
    cisla = [2, 7, 1, 23, 6]

    # bubble sort vyrvara novy zoradeny list
    bubble_sort_zoradene = bubble_sort(cisla)
    # quick sort funguje in-place.
    quick_sort_zoradenie = cisla.copy()
    quick_sort(quick_sort_zoradenie, 0, len(quick_sort_zoradenie) - 1)

    print(minimax(cisla))
    print(bubble_sort_zoradene)
    print(quick_sort_zoradenie)


if __name__ == "__main__":
    main()
