"""MinMax Projekt AP1VS.

Závìreènı zápoètovı projekt MinMax v Pythonu Tomáš Uhøík
"""
import random
import sys
import pytest


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