"""MinMax, najde minimum a maximum."""

import sys
import os
import random


def get_input():
    """
    Input.

    Získává data z příkazové řádky nebo ze soubouru nebo obojí.
    """
    ret_val = []
    # Pro každý řetěžec ve stupních argumentech
    # v poli stupních argumentů od indexu 1
    # protože 0 index obsahuje řetězec
    # se jménem programu
    for string in sys.argv[1:]:
        # Jestli je argument název souboru, tak zpracuj soubor
        # jinak zpracuj argument jako řetězec
        if os.path.isfile(string):
            # Otevři soubor pro čtení v bloku
            with open(string, 'r') as file:
                # Rozsekej soubor na rádky a ty na slova
                # každé slovo zpracuj jako číslo
                for line in file:
                    for word in line.split():
                        ret_val.append(int(word))
        else:
            ret_val.append(int(string))
    return ret_val


def get_random_input():
    """
    Random Imput.

    Vytvoří list 20 náhodných čísel v rozsahu (-9000,9000).
    """
    return [random.randint(-9000, 9000) for x in range(0, 20)]


def bubbleSort(arr):
    """
    Bubble Sort.

    Bublinkové řazení jednoduchý řadící algoritmus.
    """
    n = len(arr)

    # Projde přes všechny prvky v poli
    for i in range(n):

        # Poslední i se setřizuje
        for j in range(0, n - i - 1):

            # Projde přes prvky od 0 do n-i-1
            # Vymění to když je element nalazen a je větší
            # Než je další element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def cocktailSort(a):
    """
    Cocktail Sort.

    Koktejlové řazení funguje podopně jako bubblesort,
    akorát mění strany (Jde zleva do prava a zprava do leva).
    """
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped):

        # Restartuje vyměněné hodnoty na celé smyčce,
        # protože to může být zminulého běhu pravdivé
        # iterace.
        swapped = False

        # Smyčkuje to zleva do prava stejně jako v bubble
        # sortu
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # Pokud se nic nepohne, tak jsou prvky vyřešeny.
        if (not swapped):
            break

        # Jinak se restartuje vyměněné hodnoty tak, že
        # Můžou být použity v dalším krokucan be used in the next stage
        swapped = False

        # Posune se na konec o jedno zpátky, protoze
        # Položka na konci je na správném místě
        end = end - 1

        # Z prava do leva, delá to samé
        # Stejně jako v minulé fazi
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # Zvětší se začínající hodnota, protože
        # poslední fáze se pohnula dál
        # Nejmenší číslo se posune na nejlepší místo
        start = start + 1


def insertionSort(arr):
    """
    InsertionSort.

    Najde nejvyšśí prvke, a za něj zařadí druhý největší a posune se doleva
    """
    # Projde přes 1 do len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Posune elementy z arr[0..i-1], jsou
        # Větší než klíč k další pozici
        # Z jejich nové pozice
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    # Pokud je počet argumentů větší jak
    # 1(uživatel zadal argument zpracuj argumenty
    # jinak získej náhodná čísla
    if len(sys.argv) > 1:
        y = get_input()
    else:
        y = get_random_input()

    print("minimum: {}".format(min(y)))
    print("maximum: {}".format(max(y)))

    # Vytvoř slovník s řaďícími funkcemi
    sort_dict = {"bubble": bubbleSort,
                 "cocktail": cocktailSort,
                 "insertion": insertionSort}

    msg = "{}\nzvolte jeden radici algoritmus:". format([x for x in sort_dict])
    sort_str = input(msg)
    # Zavolej správnou funkci podle vstupu uživatele
    sort_dict[sort_str](y)
    print(y)
