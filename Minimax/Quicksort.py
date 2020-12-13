"""Quicksort rekurzivní třídící funkce."""


import random


# Rozdělení vstupu podle pivota na levou, pravou a střední část
def partition(arr, low, high):
    """Return partitioned array into three sections left, right and middle."""
    i = (low-1)  # Index menšího prvku
    pivot = arr[high]
    for j in range(low, high):
        # Umístění všech prvků menších než je pivot nalevo od něj
        if arr[j] <= pivot:
            # Inkrementovaní indexu menšího prvku
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


# Main funkce Quicksortu
def quick_sort(arr, low, high):
    """Return sorted array."""
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        # Rekurzivní setřídění levé a pravé části,
        # prostřední je sama od sebe setříděná
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# Unittest Quicksortu
def test_Quicksort():
    """Quicksort Unittest."""
    test_arr = [7, 13, 5]
    quick_sort(test_arr, 0, len(test_arr)-1)
    assert test_arr == [5, 7, 13]
    # test nahodných vstupů
    test_rArr = [random.sample(range(100), 10)]
    test_rArrCopy = test_rArr.copy()
    quick_sort(test_rArr, 0, len(test_rArr)-1)
    test_rArrCopy.sort()
    assert (test_rArr) == test_rArrCopy
