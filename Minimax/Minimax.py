"""
Program pro zjištění minima, maxima prvku v poli.

A jeho setřídění 3 různými třídícími algoritmy.
"""


import sys
import random


# Funkce pro zjištění nejmenšího prvku v poli
def min(nums):
    """Return minimum value in given array."""
    min_value = None
    for value in nums:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


# Funkce pro zjištění největšího prvku v poli
def max(nums):
    """Return maximum value in given array."""
    max_value = nums[0]
    for value in nums:
        if value > max_value:
            max_value = value
    return max_value


# Výpis nejmenšího a největšího prvku v poli s jeho indexem
def min_max(mylist):
    """Print outputs."""
    minVal = min(mylist)
    maxVal = max(mylist)
    minIdx = mylist.index(minVal)
    maxIdx = mylist.index(maxVal)
    (print("Nejmenší prvek v seznamu má hodnotu: "
     + str(minVal) + " a nachazi se na indexu: "
     + str(minIdx)))
    (print("Největší prvek v seznamu má hodnotu: "
     + str(maxVal) + " a nachazi se na indexu: "
     + str(maxIdx)))
    return str(minVal), str(maxVal), str(minIdx), str(maxIdx)


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
    return arr


# Konstrukce haldy, použití tzv. maximové haldy (bubble up - bublání nahoru)
def heapify(arr, n, i):
    """Return BubbleUp (heap collection) from given array."""
    # inicializace bublání, n - velikost velikost haldy, kořen na indexu i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Porovnání levých synů stromu, jestli jsou větší než kořen tak prohodíme
    if left < n and arr[i] < arr[left]:
        largest = left
    # Porovnání pravých synů stromu, jestli jsou větší než kořen tak prohodíme
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Výměna kořene (opakované mazání maxima)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Main funkce heap (halda) sortu
def heap_sort(arr):
    """Return sorted array."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Switch na zvolení typu řadícího algortimu
def sort_choice(mylist, x):
    """
    Return min, max value and sorted array.

    Using specific sort chosen by a user.
    """
    if x == '1':
        quick_sort(mylist, 0, len(mylist)-1)
    elif x == '2':
        heap_sort(mylist)
    elif x == '3':
        mylist.sort()
    else:
        print("Nevalidní hodnota")
        return


# Generovaní pole při zavolání funkce uživatele bez argumentů
def generate_array():
    """Return generated array if program is called without argumets."""
    mylist = []
    while len(mylist) < 20:
        r = random.randint(1, 100)
        if r not in mylist:
            mylist.append(r)
    return mylist


def read_file():
    """Read text file line by line and return array."""
    output = []
    row_data = []
    # file = open(sys.argv[1], "r")
    file = open("soubor-s-cisly.txt", "r")
    lines = file.read().splitlines()
    file.close()
    for line in lines:
        row_data = line.split()
        for num in row_data:
            output.append(int(num))
    return output


# Vstup:
mylist = []
print("Jaký řadící algortimus chcete použít?")
x = input("Quick sort[1], Heap sort[2], Python Builtin[3]")
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if argument[-3:] == 'txt':
        mylist = read_file()
        print("Input Array: ", mylist)
        min_max(mylist)
        sort_choice(mylist, x)
        print("Sorted Array: ", mylist)
    else:
        for i in sys.argv[1:]:
            mylist.append(i)
        print("Input Array: ", mylist)
        min_max(mylist)
        sort_choice(mylist, x)
        print("Sorted Array: ", mylist)
else:
    mylist = generate_array()
    print("Input Array: ", mylist)
    min_max(mylist)
    sort_choice(mylist, x)
    print("Sorted Array: ", mylist)


# Unittesty
def test_min():
    """Min test."""
    test_list = [1, 2, 3]
    assert(min(test_list)) == 1


def test_max():
    """Max test."""
    test_list = [1, 2, 3]
    assert(max(test_list)) == 3


# Unittest Quicksortu
def test_quicksort():
    """Quicksort Unittest."""
    test_arr = [7, 13, 5]
    assert quick_sort(test_arr, 0, len(test_arr)-1) == [5, 7, 13]
    # test nahodných vstupů
    # test_rArr = [random.sample(range(100), 10)]
    # test_rArrCopy = test_rArr.copy()
    # quick_sort(test_rArr, 0, len(test_rArr)-1)
    # test_rArrCopy.sort()
    # assert (test_rArr) == test_rArrCopy


# Unittest heapsortu
def test_heapsort():
    """Heapsort Unittest."""
    test_arr = [37, 41, 73, 13, 7, 101]
    assert(heap_sort(test_arr)) == [7, 13, 37, 41, 73, 101]
    # test nahodných vstupů
    # test_rArr = [random.sample(range(100), 10)]
    # test_rArrCopy = test_rArr.copy()
    # heap_sort(test_rArr)
    # test_rArrCopy.sort()
    # assert (test_rArr) == test_rArrCopy


def test_readfile():
    """Test reading values in a text file."""
    test_arr = read_file()
    assert test_arr == [57, 21, 63, 3, 15, 7, 68, 46, 20, 58, 48, 41]


def test_generateRandom():
    """
    Test array generate_array function.

    By checking their resulting lengths.
    """
    test_arr = generate_array()
    test_arr2 = generate_array()
    assert len(test_arr) == len(test_arr2)


def test_sort_choice1():
    """Test switch."""
    test_arr = [57, 21, 63, 15]
    sort_choice(test_arr, '1')
    assert test_arr == [15, 21, 57, 63]


def test_sort_choice2():
    """Test switch."""
    test_arr = [57, 21, 63, 15]
    sort_choice(test_arr, '2')
    assert test_arr == [15, 21, 57, 63]


def test_sort_choice3():
    """Test switch."""
    test_arr = [57, 21, 63, 15]
    sort_choice(test_arr, '3')
    assert test_arr == [15, 21, 57, 63]


def test_min_max():
    """Test min_max function."""
    res = min_max([57, 21, 63, 15])
    assert res[0] == '15'
    assert res[1] == '63'
    assert res[2] == '3'
    assert res[3] == '2'
    # test_minmax = min_max([57, 21, 63, 15])
    # assert test_minmax == ['15', '63', '3', '2']
