"""This module provides utility methods for triangle calculations."""

import math


def is_valid(a, b, c):
    """Check whether a triangle is valid.

    Parameters:
        a (float): side a
        b (float): side b
        c (float): side c

    Return:
        boolean: True if the triangle is valid, False otherwise
    """
    return a + b > c and a + c > b and b + c > a


def area(a, b, c):
    """Calculate the area of a triangle using Heron's formula.

    Parameters:
        a (float): side a
        b (float): side b
        c (float): side c

    Return:
        float: the area of the triangle
    """
    s = (a + b + c) / 2  # the semiperimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def is_right_angle(a, b, c):
    """Check whether a triangle is a right angle triangle or not.

    Parameters:
        a (float): side a
        b (float): side b
        c (float): side c

    Return (boolean):
        True if the triangle is right angle, False otherwise
    """
    pow_a = a ** 2
    pow_b = b ** 2
    pow_c = c ** 2
    return (math.isclose(pow_a, pow_b + pow_c)
            or math.isclose(pow_b, pow_a + pow_c)
            or math.isclose(pow_c, pow_a + pow_b))
