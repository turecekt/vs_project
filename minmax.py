from os import path
import sys
import numpy as np
from typing import Tuple, List


def insert_sort(array: List[int]) -> None:
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current


def selection_sort(array: List[int]) -> None:
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


def bubble_sort(array: List[int]) -> None:
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def find_minimum(array: List[int]) -> Tuple[int, int]:
    min_index = 0
    min_elem = array[0]
    for i in range(1, len(array)):
        if array[i] < min_elem:
            min_index = i
            min_elem = array[i]
    return min_elem, min_index


def find_maximum(array: List[int]) -> Tuple[int, int]:
    max_index = 0
    max_elem = array[0]
    for i in range(1, len(array)):
        if array[i] > max_elem:
            max_index = i
            max_elem = array[i]
    return max_elem, max_index


def pseudo_generator():
    rng = np.random.default_rng()
    return rng.integers(100000, size=20)


def input_process(file_or_array: bool, number_of_arg: int):
    if number_of_arg - 1 == 0:
        print("the input is empty, just use pseudo generator")
        array = pseudo_generator()
    elif file_or_array:
        print("the input is an array of numbers")
        array = []
        for each in sys.argv[1:]:
            array.append(int(each))
    else:
        print("the input is a txt file")
        f = open(sys.argv[1], "r")
        array = []
        data = f.readline()
        data = data.split()
        for each in data:
            array.append(each)
    print(array)
    print(find_minimum(array))
    print(find_maximum(array))
    # bubble_sort(array)
    # selection_sort(array)
    insert_sort(array)
    print(array)


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
