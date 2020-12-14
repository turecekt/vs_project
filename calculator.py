"""Functions for simple mathematical operations with two numbers.

The operations are addition, subtraction, multiplication and division.
"""


def add(x, y):
    """Find the addition of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a addition of two numbers.
    """
    return x + y


def subtract(x, y):
    """Find the subtraction of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a subtraction of two numbers.
    """
    return x - y


def multiply(x, y):
    """Find the multiplication of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a multiplication of two numbers.
    """
    return x * y


def divide(x, y):
    """Find the division of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a division of two numbers.

    Raise Value error when second number is 0.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
