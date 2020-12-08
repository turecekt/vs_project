"""MinMax projekt."""
import sys
import random


def GetMinMax(pole):
    """Funkce pro minimum a maximum v poli."""
    min = pole[0]
    minIndex = 0
    max = pole[0]
    maxIndex = 0

    for i in range(1, len(pole)):

        if pole[i] < min:
            min = pole[i]
            minIndex = i

        if pole[i] > max:
            max = pole[i]
            maxIndex = i

    print("Minimum je cislo", min, "na indexu", minIndex)
    print("Maximum je cislo", max, "na indexu", maxIndex)


def bubblesort(pole):
    """Tridici algoritmus bubblesort."""
    for _ in pole:
        for j in range(len(pole) - 1):
            if pole[j] > pole[j + 1]:
                temp = pole[j]
                pole[j] = pole[j + 1]
                pole[j + 1] = temp

    print("Serazene pole:", pole)


def insertionsort(pole):
    """Tridici algoritmus insertionsort."""
    for i in range(1, len(pole)):
        prvek = pole[i]
        j = i - 1

        while j >= 0 and pole[j] > prvek:
            pole[j + 1] = pole[j]
            j -= 1

        pole[j + 1] = prvek

    print("Serazene pole:", pole)


def selectionsort(pole):
    """Tridici algoritmus selectionsort."""
    for i in range(len(pole)):
        minIndex = i
        for j in range(i + 1, len(pole)):
            if pole[j] < pole[minIndex]:
                minIndex = j
        pole[i], pole[minIndex] = pole[minIndex], pole[i]

    print("Serazene pole:", pole)


def vstup():
    """Funkce se vyreseni vstupu."""
    cisla = []
    platnyVStup = True
    # zadny vstupni argument - nahodna cisla
    if len(sys.argv) == 1:
        cisla = [random.randint(0, 1000) for i in range(20)]

    # vstupni argument nazev souboru
    elif len(sys.argv) == 2:
        nazevSouboru = sys.argv[1]
        soubor = open(nazevSouboru, "r")
        obsah = soubor.read()
        cislaString = obsah.split(" ")

        try:
            cisla = list(map(int, cislaString))
        except ValueError:
            platnyVStup = False
            print("Soubor musi obsahovat pouze cela cisla oddelena mezerou.")
        soubor.close()

    # vstupni argumenty cisla
    else:
        for i in range(1, len(sys.argv)):
            try:
                cisla.append(int(sys.argv[i]))
            except ValueError:
                platnyVStup = False
                print("Vstupni argumenty musi byt cela cisla!")
                break

    return (platnyVStup, cisla)


# vstup je platny, mame pole cisel
if vstup()[0]:
    print("Vstup:", vstup()[1])
    print()
    GetMinMax(vstup()[1])
    print()
    print("Ktery tridici algoritmus chcete pouzit?")
    sortingAlgo = input(
        "Bubblesort(b) / InsertionSort(i) / SelectionSort(s) ").lower()
    print()

    # bubblesort
    if sortingAlgo == "b":
        bubblesort(vstup()[1])

    # insertion sort
    elif sortingAlgo == "i":
        insertionsort(vstup()[1])

    # selection sort
    elif sortingAlgo == "s":
        selectionsort(vstup()[1])

    # neplatny algoritmus
    else:
        print("Vybrani algoritmu selhalo!")
