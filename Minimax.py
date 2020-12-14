"""
Program pro zjištění minima, maxima prvku v poli.

A jeho setřídění 3 různými třídícími algoritmy.
"""


import sys
import random


# Funkce pro zjištění nejmenšího prvku v poli
def min(nums):
    """Return minimum value in given array.

    Args:
        - nums - Input array of numbers
    Returns:
        - min_value - Minimum value in the array
    """
    min_value = None
    for value in nums:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


# Funkce pro zjištění největšího prvku v poli
def max(nums):
    """Return maximum value in given array.

    Args:
        - nums - Input array of numbers
    Returns:
        - max_value - Maximum value in the array
    """
    max_value = nums[0]
    for value in nums:
        if value > max_value:
            max_value = value
    return max_value


# Funkce pro zjištění indexu nejmenšího prvku v poli
def findMinIdx(nums, minVal):
    """Find index of min value in the array."""
    minIdx = nums.index(minVal)
    return minIdx


# Funkce pro zjištění indexu největšího prvku v poli
def findMaxIdx(nums, maxVal):
    """Find index of min value in the array."""
    maxIdx = nums.index(maxVal)
    return maxIdx


# Výpis nejmenšího a největšího prvku v poli s jeho indexem
def min_max(nums):
    """Print function for min and max values in array."""
    (print("Nejmenší prvek v seznamu má hodnotu: "
     + str(min(nums)) + " a nachazi se na indexu: "
     + str(findMinIdx(nums, min(nums)))))
    (print("Největší prvek v seznamu má hodnotu: "
     + str(max(nums)) + " a nachazi se na indexu: "
     + str(findMaxIdx(nums, max(nums)))))


# Quicksort třídící algoritmu
def quick_sort(arr):
    """Sort the array by using quicksort."""
    left = []
    middle = []
    right = []
    if len(arr) > 1:
        # Rozdělení vstupu podle pivota na levou, pravou a střední část
        pivot = arr[0]
        for x in arr:
            # Umístění všech prvků menších než je pivot nalevo od něj
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            elif x > pivot:
                right.append(x)
        return quick_sort(left)+middle+quick_sort(right)
        # Spojení částí pole
    else:
        return arr


# Insertionsort třídící algoritmus
def insertion_sort(arr):
    """Sorting the array using insertionsort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Mergesort třídící algoritmus
def merge_sort(arr):
    """Sort the array using mergesort."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Rekurzivní volání druhé poloviny
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        # Iterátor kořenového listu
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Zbývající hodnoty
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# Switch na zvolení typu řadícího algortimu
def sort_choice(mylist, x):
    """
    Return min, max value and sorted array.

    Using specific sort chosen by a user.
    """
    if x == '1':
        sorted_array = quick_sort(mylist)
    elif x == '2':
        sorted_array = insertion_sort(mylist)
    elif x == '3':
        sorted_array = merge_sort(mylist)
    else:
        raise Exception("Nevalidní hodnota.")
    return sorted_array


# Generovaní pole při zavolání funkce uživatele bez argumentů
def generate_array():
    """Return generated array if program is called without argumets."""
    mylist = []
    while len(mylist) < 20:
        r = random.randint(-100, 100)
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


# Hlavní funkce:
def main():
    """Run main driver function of the program."""
    print("Jaký řadící algortimus chcete použít?")
    x = str(input("Quicksort[1], Insertionsort[2], Mergesort[3]"))
    mylist = []
    if len(sys.argv) > 1:
        # Txt file passed as args -> read txt file
        argument = sys.argv[1]
        if argument[-3:] == 'txt':
            mylist = read_file()
        else:
            # Integers passed as args -> read integers
            for i in sys.argv[1:]:
                mylist.append(int(i))
    # No args passed -> generate array of integers
    else:
        mylist = generate_array()
    # Výpis:
    print("Input: ", end='')
    for i in mylist:
        print(i, " ", end='')
    print()
    min_max(mylist)
    sorted = sort_choice(mylist, x)
    if len(sorted) > 0:
        print("Sorted: ", end='')
        for x in sorted:
            print(x, " ", end='')
        print()
    return sorted


# Unittesty
def test_min():
    """Min test."""
    assert(min([1, 2, 3, -4, -2])) == -4


def test_max():
    """Max test."""
    assert(max([1, 2, 3, -4, -2])) == 3


# Unittest Quicksortu
def test_quicksort():
    """Quicksort Unittest."""
    assert(quick_sort([7, 13, 5])) == [5, 7, 13]
    # test nahodných vstupů
    # test_rArr = [random.sample(range(100), 10)]
    # test_rArrCopy = test_rArr.copy()
    # quick_sort(test_rArr, 0, len(test_rArr)-1)
    # test_rArrCopy.sort()
    # assert (test_rArr) == test_rArrCopy


# Unittest Mergesortu
def test_mergesort():
    """Mergesort Unittest."""
    assert(merge_sort([37, 41, 73, 13, 7, 101])) == [7, 13, 37, 41, 73, 101]


# Unittest Insertionsortu
def test_insertionsort():
    """Insertionsort Unittest."""
    assert(insertion_sort([37, 41, 73, 13, 7, 101])) ==\
        [7, 13, 37, 41, 73, 101]


def test_readfile():
    """Test reading values in a text file."""
    # test_arr = read_file()
    assert read_file() == [57, 21, 63, 3, 15, 7, 68, 46, 20, 58, 48, 41]


def test_generateRandom():
    """
    Test array generate_array function.

    By checking their resulting lengths.
    """
    assert len(generate_array()) == len(generate_array())
    # test_arr = generate_array()
    # test_arr2 = generate_array()
    # assert len(test_arr) == len(test_arr2)


def test_sort_choice1():
    """Test switch if user inserts choice no. 1."""
    assert sort_choice([57, 21, 63, 15], '1') == [15, 21, 57, 63]


def test_sort_choice2():
    """Test switch if user inserts choice no. 2."""
    assert sort_choice([57, 21, 63, 15], '2') == [15, 21, 57, 63]


def test_sort_choice3():
    """Test switch if user inserts choice no. 3."""
    assert sort_choice([57, 21, 63, 15], '3') == [15, 21, 57, 63]


def test_findMinIdx():
    """Test findMinIndex."""
    assert findMinIdx([57, 21, 63, 15], min([57, 21, 63, 15])) == 3


def test_findMaxIdx():
    """Test findMaxIndex."""
    assert findMaxIdx([57, 21, 63, 15], max([57, 21, 63, 15])) == 2


def test_minmax_Print():
    """Print test."""
    assert(min_max([57, 21, 63, 15])) == (print(
     "Nejmenší prvek v seznamu má hodnotu: "
     + str(15) + " a nachazi se na indexu: "
     + str(3)))
    (print("Největší prvek v seznamu má hodnotu: "
     + str(63) + " a nachazi se na indexu: "
     + str(2)))


if __name__ == "__main__":
    main()
