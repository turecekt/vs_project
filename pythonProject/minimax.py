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