"""MinMax Projekt AP1VS.

Závìreènı zápoètovı projekt MinMax v Pythonu Tomáš Uhøík
"""
import random
import sys
import pytest


def program_start(cmd_arg):
    """Function creates an array of integers after starting the script.

    Values of an array are based on paramaters given by user.

    Returns:
        - array - an unsorted array of integers
    """
    array = []
    n = len(cmd_arg)
    if n == 1:
        array = array_insert()
        return array
    elif n == 2:
        try:
            int(cmd_arg[1])
            raise SystemExit('You must enter more than one number')
        except ValueError:
            try:
                with open(cmd_arg[1], "r") as file:
                    for line in file:
                        array = line.split()
                file.close()
                array = convert_to_int(array)
                return array
            except IOError:
                raise SystemExit('Error: File does not appear to exist.')
    elif n > 2:
        del cmd_arg[0]
        for x in range(len(cmd_arg)):
            try:
                array.append(int(cmd_arg[x]))
            except ValueError:
                raise SystemExit('You must enter numbers or name of a file')
        return array


def array_insert():
    """Function returns an array with randomly generated numbers.

    Array has 20 elements with values between -1000 and 1000.
    """
    array = []
    for x in range(20):
        array.append(random.randint(-1000, 1000))
    return array


def convert_to_int(array):
    """Converts a string array to an array of integers."""
    for x in range(len(array)):
        array[x] = int(array[x])
    return array


def array_max_value(array):
    """Determines a max value and its position in array.

    Returns:
        - max - max value of an array
        - index - position of max value in given array
    """
    max = array[0]
    index = 0
    for x in range(len(array)-1):
        if max < array[x+1]:
            max = array[x+1]
            index = x+1
    return max, index


def array_min_value(array):
    """Determines a min value and its position in array.

    Returns:
        - min - min value of an array
        - index - position of min value in given array
    """
    min = array[0]
    index = 0
    for x in range(len(array) - 1):
        if min > array[x + 1]:
            min = array[x + 1]
            index = x+1
    return min, index


def merge_sort(inp_arr):
    """Merge sort algorithm."""
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        p = 0
        q = 0
        r = 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                inp_arr[r] = left_arr[p]
                p += 1
            else:
                inp_arr[r] = right_arr[q]
                q += 1

            r += 1

        while p < left_size:
            inp_arr[r] = left_arr[p]
            p += 1
            r += 1

        while q < right_size:
            inp_arr[r] = right_arr[q]
            q += 1
            r += 1
    return inp_arr


def bubble_sort(array):
    """Bubble sort algorithm."""
    n = len(array)
    for i in range(0, n):
        for j in range(i, n-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        for k in range(n-i, i):
            if array[k] < array[k-1]:
                temp = array[k]
                array[k] = array[k-1]
                array[k-1] = temp
    return array


def insertion_sort(array):
    """Insertion sort algorithm."""
    n = len(array)
    for i in range(0, n-1):
        j = i+1
        number = array[j]
        while j > 0 and number < array[j-1]:
            array[j] = array[j-1]
            j = j-1
        array[j] = number
    return array


def test_bubble_sort():
    """Unit test for bubble sort algorithm."""
    test_array = [12, -150, 0, -9, 16]
    sorted_array = [-150, -9, 0, 12, 16]
    assert bubble_sort(test_array) == sorted_array


def test_insertion_sort():
    """Unit test for insertion sort algorithm."""
    test_array = [125, -15, 30, -19, 160]
    sorted_array = [-19, -15, 30, 125, 160]
    assert insertion_sort(test_array) == sorted_array


def test_merge_sort():
    """Unit test for merge sort algorithm."""
    test_array = [813, -21, 5, -9, -16]
    sorted_array = [-21, -16, -9, 5, 813]
    assert merge_sort(test_array) == sorted_array
    

def test_min_value():
    """Unit test for function that determines min value of an array."""
    test_array = [81, 21, -5, -9, -16, 31, 0, 147, -4]
    assert array_min_value(test_array) == (-16, 4)


def test_max_value():
    """Unit test for function that determines max value of an array."""
    test_array = [81, 21, -5, -9, -16, 31, 0, 147, -4]
    assert array_max_value(test_array) == (147, 7)


def test_convert_to_int():
    """Unit test for function converting string array to int array."""
    test_array = ['1', '-19', '10', '-50', '34']
    int_array = [1, -19, 10, -50, 34]
    assert convert_to_int(test_array) == int_array