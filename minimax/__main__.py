import sys
import random

from minimax import utils


def parse_args():
    """
    Tato funkcia analyzuje obdrzane argumenty a vracia sekvenciu cisiel.

    - Pokial sme obdrzali 1 argument, predpokladame ze to bol subor
      a cisla su ulozene v nom na jednom riadku oddelene medzerami
    - Pokial sme obdrzali viac argumentov, predpokladame ze to bola
      nasa sekvencia cisiel
    - Pokial sme neobdrzali argument, vytvorime 20 nahodnych cisel
      ako nasu sekvenciu

    Funkcia vracia list cisiel.
    """
    argumenty = sys.argv[1:]
    if len(argumenty) == 1:
        with open(argumenty[0], "r") as f:
            cisla = [int(x) for x in f.read().split()]
        print(f"Cisla obdrzane zo suboru: {cisla}")
    elif len(argumenty) > 1:
        cisla = [int(x) for x in argumenty]
        print(f"Obdrzane cisla: {cisla}")
    else:
        cisla = [random.randint(-100, 100) for _ in range(20)]
        print(f"Cisla neboli zadane, nahodne vygenerovana sekvencia: {cisla}")
    return cisla


def main():
    """Hlavna funkcia programu."""
    cisla = parse_args()

    # bubble sort a insertion sort vyrvaraju novy zoradeny list
    bubble_sort_zoradene = utils.bubble_sort(cisla)
    insertion_sort_zoradene = utils.insertion_sort(cisla)

    # quick sort funguje in-place.
    quick_sort_zoradenie = cisla.copy()
    utils.quick_sort(quick_sort_zoradenie)

    print(utils.minimax(cisla))
    print(bubble_sort_zoradene)
    print(quick_sort_zoradenie)
    print(insertion_sort_zoradene)


if __name__ == "__main__":
    main()
