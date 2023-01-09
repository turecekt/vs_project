"""Triangle program core definitions."""
import math


def trianglePerimeter(a, b, c):
    """:return: Perimeter of the triangle."""
    return a + b + c


def triangleArea(a, b, c):
    """:return: Area of the triangle."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def constructability(a, b, c):
    """:return: Constructability of the triangle."""
    return (a + b > c) and (b + c > a) and (c + a > b)


def triangleOrthogonality(leg1, leg2, hypotenuse):
    """:return: Orthogonality of the triangle."""
    return math.pow(hypotenuse, 2) == math.pow(leg1, 2) + math.pow(leg2, 2)
