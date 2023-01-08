"""Triangle program core definitions."""
import math


def trianglePerimeter(a, b, c):
    """Return perimeter."""
    return a + b + c


def triangleArea(a, b, c):
    """Return triangle area."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def constructability(a, b, c):
    """Return constructability."""
    return (a + b > c) and (b + c > a) and (c + a > b)


def triangleOrthogonality(leg1, leg2, hypotenuse):
    """Return orthogonality."""
    return math.pow(hypotenuse, 2) == math.pow(leg1, 2) + math.pow(leg2, 2)
