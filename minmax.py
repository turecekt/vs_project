import sys
from os import path
from typing import Tuple, List, Optional
import numpy as np

# -----------------------------------
# This project contains three sorting algorithms,
# pseudo-random generator and functions to find minimum and maximum in array.
#
# Author: Lucie Šikudová
# -----------------------------------

"""
Implementation of insertion sort.
A simple sorting algorithm, efficient for small data sets.
Time complexity: O(n^2)
"""


def insert_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


"""
Implementation of sorting algorithm.
A simple comparison sorting algorithm
Time complexity: O(n^2)
"""


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array


"""
Implementation of bubble sort.
A simple comparing sorting algorithm.
This algorithm performs poorly in real world,
 it is used as an educational tool.
Time complexity: O(n^2)
"""


def bubble_sort(array: List[int]) -> List[int]:
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


"""
Implementation of function that finds the minimum in the array.
"""


def find_minimum(array: List[int]) -> Tuple[Optional[int], int]:
    if len(array) == 0:
        return None, -1
    min_index = 0
    min_elem = array[0]
    for i in range(1, len(array)):
        if array[i] < min_elem:
            min_index = i
            min_elem = array[i]
    return min_elem, min_index


"""
Implementation of function that finds the maximum in the array.
"""


def find_maximum(array: List[int]) -> Tuple[Optional[int], int]:
    if len(array) == 0:
        return None, -1
    max_index = 0
    max_elem = array[0]
    for i in range(1, len(array)):
        if array[i] > max_elem:
            max_index = i
            max_elem = array[i]
    return max_elem, max_index


"""
Function that generates array of (pseudo)random integers.
"""


def pseudo_generator():
    rng = np.random.default_rng()
    return rng.integers(100000, size=20)


"""
Function that process the user input.
"""


def input_process(file_or_array: bool, number_of_arg: int):
    # no input given, pseudo-random generator is used
    if number_of_arg - 1 == 0:
        print("the input is empty, just use pseudo generator")
        array = pseudo_generator()
    # input is an array of integers
    elif file_or_array:
        print("the input is an array of numbers")
        array = []
        for each in sys.argv[1:]:
            array.append(int(each))
    # input is a txt file with integers
    else:
        print("the input is a txt file")
        f = open(sys.argv[1], "r")  # open a file with "r" mode to read it
        array = []
        data = f.readline()  # read all integers
        data = data.split()  # split integers into n integers
        for each in data:
            array.append(each)  # make an array from the txt file


"""
Function to report wrong input.
"""


def wrong_input(input):
    print("wrong input entered")


if __name__ == "__main__":
    file_or_array = True
    # no arguments given
    if len(sys.argv) == 1:
        use_pseudo = True
    # at least 1 argument given
    else:
        # txt file
        if path.isfile(sys.argv[1]):
            file_or_array = False
        # non exist txt file
        elif sys.argv[1].find("txt") != -1:
            wrong_input(sys.argv[1])
            exit(0)
        # just a word without txt
        elif not sys.argv[1].isnumeric():
            wrong_input(sys.argv[1])
            exit(0)

    input_process(file_or_array, len(sys.argv))
