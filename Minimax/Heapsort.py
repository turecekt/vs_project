import random

#Konstrukce haldy, použití tzv. maximové haldy (bubble up - bublání nahoru) 
def heapify(arr, n, i):
    #inicializace bublání, n - velikost velikost haldy, kořen na indexu i
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    #Porovnání levých synů stromu, jestli jsou větší než kořen tak prohodíme
    if l < n and arr[i] < arr[l]:
        largest = l
    #Porovnání pravých synů stromu, jestli jsou větší než kořen tak prohodíme
    if r < n and arr[largest] < arr[r]:
        largest = r
    #Výměna kořene (opakované mazání maxima)
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

#Main funkce heap (halda) sortu
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#Unittest heapsortu
def test_heapsort():
    """Heapsort Unittest."""
    test_arr = [37, 41, 73, 13, 7, 101]
    heap_sort(test_arr)
    assert(test_arr) == [7, 13, 37, 41, 73, 101]
    #test nahodných vstupů
    test_rArr = [random.sample(range(100), 10)]
    test_rArrCopy = test_rArr.copy()
    heap_sort(test_rArr)
    test_rArrCopy.sort()
    assert (test_rArr) == test_rArrCopy

