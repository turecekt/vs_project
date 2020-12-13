import sys
import random
from Quicksort import quick_sort
from Heapsort import heap_sort
from array import array
import pytest

#Funkce pro zjištění nejmenšího prvku v poli
def min(nums):
    min_value = None
    for value in nums:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

#Funkce pro zjištění největšího prvku v poli
def max(nums):
    max_value = nums[0]
    for value in nums:
        if value > max_value:
            max_value = value
    return max_value

#Výpis nejmenšího a největšího prvku v poli s jeho indexem
def min_max(mylist):
    print("Nejmenší prvek v seznamu má hodnotu: " + str(min(mylist)) + " a nachazi se na indexu: " + str(mylist.index(min(mylist))))
    print("Největší prvek v seznamu má hodnotu: " + str(max(mylist)) + " a nachazi se na indexu: " + str(mylist.index(max(mylist))))

#Switch na zvolení typu řadícího algortimu
def sort(mylist):
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

#Generovaní pole při zavolání funkce uživatele bez argumentů
def generate_array():
    mylist = []
    while len(mylist) < 20:
        r = random.randint(1, 100)
        if r not in mylist:
            mylist.append(r)
    print("Generated list: ", mylist)
    list2 = [rand = random.randint() if rand not in for _ in range(10)]
    print("list comp rand:", list2)
    sort(mylist)
    min_max(mylist)

#Vstup:
mylist = []
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if argument[-3:]=='txt':
        row_data = []
        file = open(sys.argv[1], "r")
        lines = file.read().splitlines()
        file.close()
        for line in lines:
            row_data = line.split()
            for num in row_data:
                mylist.append(int(num))
        print(mylist)
        min_max(mylist)
        sort(mylist)
    else:
        mylist = []
        for i in sys.argv[1:]:
            mylist.append(i)
        min_max(mylist)
        sort(mylist)
else:
        generate_array()

#Unittesty
def test_min():
    """Min test."""
    test_list = [1, 2, 3]
    assert(min(test_list)) == 1

def test_max():
    """Max test."""
    test_list = [1, 2, 3]
    assert(max(test_list)) == 3 

def testQuicksort():
    """Quicksort test."""
    test_arr = [7, 13, 5]
    quick_sort(test_arr, 0, len(test_arr)-1)
    assert test_arr == [5, 7, 13]


