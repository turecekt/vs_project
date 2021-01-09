"""Triangle.

1. Information about constructability of the triangle.
2. Information about sides length.
3. Information about perimeter and content of the triangle.
4. Information about right angle of the triangle.
"""
import math


class Triangle:
    """Constructability triangle."""

    def __init__(self, ax, ay, bx, by, cx, cy):
        a = lengthOfSide("a", ax, bx)
        b = lengthOfSide("b", bx, by)
        c = lengthOfSide("c", cx, cy)

        if isConstructable(a, b, c):
            print("Trojúhelník je sestrojitelný.")
        else:
            print("Trojúhleník dle zadaných souřadnic nelze sestavit.")


def isConstructable(a, b, c):
    """Check triangle constructability.

    Return True if triangle is constructable
    >>> isConstructable(1, 1, 1)
    True
    """
    triangleIsConstructable = False

    if a + b > c and b + c > a and c + a > b:
        triangleIsConstructable = True

    return triangleIsConstructable


def lengthOfSide(sideName, x, y):
    """Compute lenght of side.

    Return lenght of side.
    >>> lengthOfSide(1, 1)
    2
    """
    sideLength = math.sqrt((x * x) + (y * y))
    print("Délka strany " + sideName + " je " + sideLength + ".")
