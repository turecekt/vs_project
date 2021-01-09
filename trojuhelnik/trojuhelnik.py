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
        """Triangle constructor."""
        print("Aplikace trojúhelník.")
        print("Informace o sestrojitelnosti trojúhelníku.")
        print("Pokud je to možné, tak obvodu, obsahu a pravoúhlosti.")

        a = lengthOfSide(ax, ay)
        b = lengthOfSide(bx, by)
        c = lengthOfSide(cx, cy)

        if isConstructable(a, b, c):
            p = perimeter(a, b, c)
            print("Obvod trojúhelníku je:")
            print(p)
            c = content(a, b, c)
            print("Obsah trojúhelníku je:")
            print(c)

        else:
            print("Trojúhleník dle zadaných souřadnic nelze sestavit.")


def isConstructable(a, b, c):
    """Check triangle constructability.

    Return True if triangle is constructable
    >>> isConstructable(1, 1, 1)
    True
    """
    triangleIsConstructable = False

    if (a > 0) and (b > 0) and (c > 0):
        if (a + b > c) and (b + c > a) and (c + a > b):
            triangleIsConstructable = True

    if triangleIsConstructable is True:
        print("Trojúhelník je sestrojitelný.")
        print("Délka strany a:")
        print(a)
        print("Délka strany b:")
        print(b)
        print("Délka strany c:")
        print(c)

    return triangleIsConstructable


def lengthOfSide(x, y):
    """Compute length of side.

    Return length of side.
    >>> lengthOfSide(1, 1)
    1.41421356237
    """
    sideLength = math.sqrt((x * x) + (y * y))
    return sideLength


def perimeter(a, b, c):
    """Compute perimeter of triangle.

    Return perimeter of triangle.
    >>> perimeter(1.41421356237, 1.41421356237, 1.41421356237)
    4.242640687119286
    """
    return a + b + c


def content(a, b, c):
    """Compute content of triangle.

    Return content of triangle.
    >>> content(1.41421356237, 1.41421356237, 1.41421356237)
    0.8660254037844389
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
