#!/usr/bin/env python

import random

# @author Daberger Jiri
# @description Counting response of user on easy math examples


def sum(a, b) -> int:
    # function return sum of two numbers
    return a + b


def subtraction(a, b) -> int:
    # function return difference of two numbers
    return a - b


def multiply(a, b) -> int:
    # function return multiple of two numbers
    return a * b


def division(a, b) -> float:
    # function return division of two numbers
    return round((a / b), 2)


def randomExample():
    """ Function for creating random math examples

    Parameters:
        operator (int): random number representing final operator of math example [1->+, 2->-, 3->*, 4->]
        a (int): random number <-10, 10>
        b (int): random number <10, 10>

    Returns: result of math expression

    """

    operator = random.randint(1, 4)
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    if operator == 4:
        if b == 0:
            randomExample()
        else:
            if b < 0:
                print(f"{a}/({b})")
            else:
                print(f"{a}/{b}")

            result = division(a, b)

    elif operator == 3:
        if b < 0:
            print(f"{a}*({b})")
        else:
            print(f"{a}*{b}")

        result = multiply(a, b)

    elif operator == 2:
        if b < 0:
            print(f"{a}+{b * (-1)}")
        elif b >= 0:
            print(f"{a}-{b}")
        result = subtraction(a, b)

    elif operator == 1:
        if b < 0:
            print(f"{a}{b}")
        elif b >= 0:
            print(f"{a}+{b}")
        result = sum(a, b)

    return result


print(randomExample())
