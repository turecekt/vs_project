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