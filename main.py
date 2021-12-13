import sys
from random import randint


def min_max(numbers):
    """Funkce na zjisteni nejmensiho a nejvetsiho cisla a jeho indexu."""
    min_n = f"Min number:{min(numbers)}, Index:{numbers.index(min(numbers))}"
    max_n = f"Max number:{max(numbers)}, Index:{numbers.index(max(numbers))}"

    return f"{min_n}\n{max_n}"


def bubblesort(list):
    """Funkce na serazeni listu pomoci bubblesortu."""
    for i in range(len(list)):
        for n in range(len(list) - 1):
            if list[n] > list[n + 1]:
                list[n], list[n + 1] = list[n + 1], list[n]
    return list


def selectionsort(list):
    """Funkce na serazeni listu pomoci selectionsortu."""
    for i in range(len(list) - 1):
        minimum = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[minimum]):
                minimum = j
        if(minimum != i):
            list[i], list[minimum] = list[minimum], list[i]
    return list


def shellsort(list):
    """Funkce na serazeni listu pomoci shellsortu."""
    n = len(list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j-gap] > temp:
                list[j] = list[j-gap]
                j = j - gap
            list[j] = temp
        gap = gap // 2
    return list
