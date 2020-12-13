"""
Program pro zjištění minima, maxima prvku v poli.

A jeho setřídění 3 různými třídícími algoritmy.
"""


import sys
import random
from Quicksort import quick_sort
from Heapsort import heap_sort


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
    (print("Nejmenší prvek v seznamu má hodnotu: "
     + str(min(mylist)) + " a nachazi se na indexu: "
     + str(mylist.index(min(mylist)))))
    (print("Největší prvek v seznamu má hodnotu: "
     + str(max(mylist)) + " a nachazi se na indexu: "
     + str(mylist.index(max(mylist)))))


# Switch na zvolení typu řadícího algortimu
def sort(mylist):
    """
    Return min, max value and sorted array.

    Using specific sort chosen by a user.
    """
    print("Jaký řadící algortimus chcete použít?")
    print("Quick sort[1], Heap sort[2], Python Builtin[3]")
    x = input()
    if x == '1':
        quick_sort(mylist, 0, len(mylist)-1)
        print(mylist)
    elif x == '2':
        heap_sort(mylist)
        print(mylist)
    elif x == '3':
        mylist.sort()
        print(mylist)


# Generovaní pole při zavolání funkce uživatele bez argumentů
def generate_array():
    """Return generated array if program is called without argumets."""
    mylist = []
    while len(mylist) < 20:
        r = random.randint(1, 100)
        if r not in mylist:
            mylist.append(r)
    print("Generated list: ", mylist)
    sort(mylist)
    min_max(mylist)

# Vstup:
inputTestFails = False
mylist = []
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if argument[-3:] == 'txt':
        row_data = []
        file = open(sys.argv[1], "r")
        lines = file.read().splitlines()
        file.close()
        for line in lines:
            row_data = line.split()
            for num in row_data:
                try:
                    mylist.append(int(num))
                except ValueError:
                    inputTestFails = True
        print(mylist)
        min_max(mylist)
        sort(mylist)
    else:
        mylist = []
        for i in sys.argv[1:]:
            try:
                mylist.append(i)
            except ValueError:
                inputTestFails = True
        min_max(mylist)
        sort(mylist)
else:
    generate_array()


# Unittesty
def test_min():
    """Min test."""
    test_list = [1, 2, 3]
    assert(min(test_list)) == 1


def test_max():
    """Max test."""
    test_list = [1, 2, 3]
    assert(max(test_list)) == 3
