#!/usr/bin/env python

import random

# Author: Daberger Jiri <j_daberger@utb.cz>
# Description: Counting response of user on easy math examples

from time import perf_counter


def sum(a, b) -> int:
    """
    Args:
        a: int
        b: int

    Returns: sum of two numbers (int)
    """
    return a + b


def subtraction(a, b) -> int:
    """
    Args:
        a: int
        b: int

    Returns: difference of two numbers (int)
    """
    return a - b


def multiply(a, b) -> int:
    """
    Args:
        a: int
        b: int

    Returns: multiple of two numbers (int)
    """
    return a * b


def division(a, b) -> float:
    """
    Args:
        a: int
        b: int

    Returns: division of two numbers (double)
    """
    if b == 0:
        return False
    return round((a / b), 2)


def randomExample():
    """
    Function for creating random math examples
    Parameters:
        operator (int): random number for operator [1; 2; 3; 4]
        a (int): random number <-10, 10>
        b (int): random number <10, 10>

    Returns: result of math expression
    """

    operator = random.randint(4, 4)
    a = random.randint(-1, 1)
    b = random.randint(-1, 1)

    if operator == 4:
        if b < 0:
            print(f"{a}/({b})")
        else:
            print(f"{a}/{b}")

        result = division(a, b)
        if result is False:
            return randomExample()

    # part of code for multiply
    elif operator == 3:
        if b < 0:
            print(f"{a}*({b})")
        else:
            print(f"{a}*{b}")

        result = multiply(a, b)

    # part of code for substraction
    elif operator == 2:
        if b < 0:
            print(f"{a}+{b * (-1)}")
        elif b >= 0:
            print(f"{a}-{b}")
        result = subtraction(a, b)

    # part of code for sum
    elif operator == 1:
        if b < 0:
            print(f"{a}{b}")
        elif b >= 0:
            print(f"{a}+{b}")
        result = sum(a, b)

    return result


def compareResults(pc, user) -> bool:
    """
    Function which compare two values,
    right result of math example and user answer

    Args:
        pc: Right result of math example
        user: Answer of user

    Returns: true or false
    """
    try:
        if float(pc) == float(user):
            return True
    except ValueError:
        return False
    return False


def average(times) -> float:
    """ Method for counting average time of user reply
    Args:
        times: List of times

    Returns: average time (double)
    """
    av = 0
    for x in times:
        av += x
    av /= len(times)
    return round(av, 2)


"""
Unit tests for all functions
"""


def test_sum():
    assert sum(2, 2) == 4


def test_subtraction():
    assert subtraction(5, 2) == 3


def test_multiply():
    assert multiply(4, 8) == 32


def test_division():
    assert division(0, 1) == 0


def test_average():
    assert average([1, 2, 6]) == 3


def test_compareResults():
    assert compareResults(4, 4)


def test_RandomExample():
    res = randomExample()
    assert (100 >= res >= -100 or res is False)


points = 0
i = 0
times = list()
repetition = 5

while i < repetition:
    start = perf_counter()

    pc = randomExample()
    user = input("Your answer: ")

    stop = perf_counter()
    times.append(stop - start)

    if compareResults(pc, user):
        points += 1

    else:
        print(f"Your answer is wrong! Right answer is {pc}")

    i += 1

print(f"\nYou got {points} of {repetition} points")
print(f"Average time is {average(times)} seconds")
