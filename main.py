"""Main."""
import sys
import random
from minMax import minMax
from sortingAlgoritms import bubblesort, insertionsort, selectionsort

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

# vstup je platny, mame pole cisel
if platnyVStup:
    print("Vstup:", cisla)
    print()
    minMax(cisla)
    print()
    print("Ktery tridici algoritmus chcete pouzit?")
    sortingAlgo = input(
        "Bubblesort(b) / InsertionSort(i) / SelectionSort(s) ").lower()
    print()

    # bubblesort
    if sortingAlgo == "b":
        bubblesort(cisla)

    # insertion sort
    elif sortingAlgo == "i":
        insertionsort(cisla)

    # selection sort
    elif sortingAlgo == "s":
        selectionsort(cisla)

    # neplatny algoritmus
    else:
        print("Vybrani algoritmu selhalo!")
