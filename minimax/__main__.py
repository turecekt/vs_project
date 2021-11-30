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


def vyber_algoritmus():
    """
    Tato funkcia sa spyta na algoritmus ktory ma byt pouziti a vrati jeho funkciu.

    Podporovane algoritmy:
    - quick sort
    - bubble sort
    - insertion sort
    - Python sort
    """
    algos = {
        "1": ("Quick sort", utils.quick_sort),
        "2": ("Bubble sort", utils.bubble_sort),
        "3": ("Insertion sort", utils.insertion_sort),
        "4": ("Python sort", sorted)
    }
    print("Vyber algoritmus pre zoradenie sekvencie: ")
    for k, (v, _) in algos.items():
        print(f"{k}. {v}")

    while True:
        try:
            moznost = input("> ")
        except KeyboardInterrupt:
            print("\nUkoncene pouzivatelom.")
            exit()

        if not moznost.lower() in algos.keys():
            moznosti = ", ".join(algos.keys())
            print(f"Nespravna moznost! Dostupne moznosti: {moznosti}")
            continue
        return algos[moznost][1]

def main():
    """Hlavna funkcia programu."""
    cisla = parse_args()
    algo = vyber_algoritmus()

    _min, i_min, _max, i_max = utils.minimax(cisla)
    zoradeny_list = algo(cisla)

    print(f"Minimalne cislo v sekvencii: {_min}, na indexe #{i_min}")
    print(f"Maximalne cislo v sekvencii: {_max}, na indexe #{i_max}")
    print(f"Zoradene cisla: {zoradeny_list}")


if __name__ == "__main__":
    main()
