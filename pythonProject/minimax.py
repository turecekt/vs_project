"""MinMax Projekt AP1VS.

Závìreèný zápoètový projekt MinMax v Pythonu Tomáš Uhøík
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