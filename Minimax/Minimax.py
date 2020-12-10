import sys, getopt
import random
from Quicksort import quick_sort
from Heapsort import heap_sort
from array import array

def min(nums):
    min_value = None
    for value in nums:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

def max(nums):
    max_value = nums[0]
    for value in nums:
        if value > max_value:
            max_value = value
    return max_value

def min_max(mylist):
    print("Nejmenší prvek v seznamu má hodnotu: " + str(min(mylist)) + " a nachazi se na indexu: " + str(mylist.index(min(mylist))))
    print("Největší prvek v seznamu má hodnotu: " + str(max(mylist)) + " a nachazi se na indexu: " + str(mylist.index(max(mylist))))

def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], end = " ")
    print()

def sort(mylist):
    print("Jaký řadící algortimus chcete použít?") 
    print("Quick sort[1], Heap sort[2], Python Builtin[3]")
    x = input()
    if x == '1':
        for i in range(0, len(mylist)):
            mylist[i] = int(mylist[i])
        arr = array("i", mylist)
        quick_sort(arr, 0, len(arr)-1)
        print_array(arr)
    elif x == '2':
        for i in range(0, len(mylist)):
            mylist[i] = int(mylist[i])
        arr = array("i", mylist)
        heap_sort(arr)
        print_array(arr)
    elif x == '3':
        mylist.sort()
        print(mylist)

def generate_array():
    mylist = []
    while len(mylist) < 20:
        r = random.randint(1, 100)
        if r not in mylist:
            mylist.append(r)
    print("Sorted list: ", mylist)
    min_max(mylist)

def read_input(argument=None):
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

read_input()
