"""Random math examples.

Author: Daberger Jiri <j_daberger@utb.cz>
Description: Counting response of user on easy math examples
"""

import random
from time import perf_counter


def sum(a, b) -> int:
    """Sum function.

    Args:
        a: int
        b: int

    Returns: sum of two numbers (int)
    """
    return a + b


def subtraction(a, b) -> int:
    """Subtraction function.

    Args:
        a: int
        b: int

    Returns: difference of two numbers (int)
    """
    return a - b


def multiply(a, b) -> int:
    """Multiply function.

    Args:
        a: int
        b: int

    Returns: multiple of two numbers (int)
    """
    return a * b


def division(a, b) -> float:
    """Division function.

    Args:
        a: int
        b: int

    Returns: division of two numbers (double)
    """
    if b == 0:
        return False
    return round((a / b), 2)


def randomExample():
    """For creating random math examples.

    Parameters:
        operator (int): random number for operator [1; 2; 3; 4]
        a (int): random number <-10, 10>
        b (int): random number <10, 10>

    Returns: result of math expression
    """
    operator = random.randint(1, 4)
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

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
    """Compare results function.

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
    """For counting average time of user reply.

    Args:
        times: List of times

    Returns: average time (double)
    """
    av = 0
    for x in times:
        av += x
    av /= len(times)
    return round(av, 2)


def test_sum():
    """Unit test for sum function."""
    assert sum(2, 2) == 4
    assert sum(2, -2) == 0
    assert sum(5, 8) == 13
    assert sum(0, 0) != -5


def test_subtraction():
    """Unit test for subtraction function."""
    assert subtraction(5, 2) == 3
    assert subtraction(-7, -2) != 9
    assert subtraction(2, 0) == 2
    assert subtraction(-2, 2) == -4


def test_multiply():
    """Unit test for multiply function."""
    assert multiply(4, 8) == 32
    assert multiply(4, 0) == 0
    assert multiply(4, -1) == -4
    assert multiply(2, 8) != 31


def test_division():
    """Unit test for division function."""
    assert division(0, 1) == 0
    assert division(8, 1) == 8
    assert division(10, 5) == 2
    assert division(10, 2) != 2


def test_average():
    """Unit test for average function."""
    assert average([1, 2, 6]) == 3
    assert average([2, 2, 2]) == 2
    assert average([5, 4, 3]) == 4
    assert average([1, 1, 1]) == 1


def test_compareResults():
    """Unit test for compareResults function."""
    assert compareResults(4, 4)
    assert compareResults(0, 0)
    assert compareResults(8, 8)
    assert not compareResults(5, 2)


def test_RandomExample():
    """Unit test for RandomExample function."""
    res = randomExample()
    assert (100 >= res >= -100 or res is False)


def startProgram():
    """Call this function will start the program."""
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


print("Welcome to my generator of math examples! \n")
# startProgram()
