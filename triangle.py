"""Triangle program core definitions."""
import math


def sideLength(point1, point2):
    """Return lenghts of sides."""
    return math.sqrt(
                     math.pow((int(point2[0]) - int(point1[0])), 2)
                     + math.pow((int(point2[1]) - int(point1[1])), 2)
                    )


def trianglePerimeter(a, b, c):
    """Return perimeter."""
    return a + b + c


def triangleArea(a, b, c):
    """Return triangle area."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def constructability(a, b, c):
    """Return constructability"""
    return (a + b > c) and (b + c > a) and (c + a > b)

def triangleOrthogonality(leg1, leg2, hypotenuse):
    """Return orthogonality"""
    return math.pow(hypotenuse, 2) == math.pow(leg1, 2) + math.pow(leg2, 2)
