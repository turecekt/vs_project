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
        """Triangle constructor.

        >>> test=Triangle(1, 1, 1, 1, 1, 1)
        Aplikace trojúhelník.
        Informace o sestrojitelnosti trojúhelníku.
        Pokud je to možné, tak obvodu, obsahu a pravoúhlosti.
        Trojúhelník je sestrojitelný.
        Délka strany a:
        1.41
        Délka strany b:
        1.41
        Délka strany c:
        1.41
        Obvod trojúhelníku je:
        4.23
        Obsah trojúhelníku je:
        0.86
        Trojúhelník je pravoúhlý:
        NE
        >>> test=Triangle(0, 0, 0, 0, 0, 0)
        Aplikace trojúhelník.
        Informace o sestrojitelnosti trojúhelníku.
        Pokud je to možné, tak obvodu, obsahu a pravoúhlosti.
        Trojúhleník dle zadaných souřadnic nelze sestavit.
        """
        print("Aplikace trojúhelník.")
        print("Informace o sestrojitelnosti trojúhelníku.")
        print("Pokud je to možné, tak obvodu, obsahu a pravoúhlosti.")

        a = lengthOfSide(ax, ay)
        b = lengthOfSide(bx, by)
        c = lengthOfSide(cx, cy)

        if isConstructable(a, b, c):
            print("Trojúhelník je sestrojitelný.")
            print("Délka strany a:")
            print(a)
            print("Délka strany b:")
            print(b)
            print("Délka strany c:")
            print(c)
            print("Obvod trojúhelníku je:")
            print(perimeter(a, b, c))
            print("Obsah trojúhelníku je:")
            print(content(a, b, c))
            print("Trojúhelník je pravoúhlý:")
            print(hasRightAngle(a, b, c))
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

    return triangleIsConstructable


def lengthOfSide(x, y):
    """Compute length of side.

    Return length of side.
    >>> lengthOfSide(1, 1)
    1.41
    """
    return round(math.sqrt((x * x) + (y * y)), 2)


def perimeter(a, b, c):
    """Compute perimeter of triangle.

    Return perimeter of triangle.
    >>> perimeter(1.41, 1.41, 1.41)
    4.23
    """
    return round(a + b + c, 2)


def content(a, b, c):
    """Compute content of triangle.

    Return content of triangle.
    >>> content(1.41, 1.41, 1.41)
    0.86
    """
    s = tempContent(a, b, c)
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)


def tempContent(a, b, c):
    """Temporary number to compute.

    Return temporary number.
    >>> tempContent(1.41, 1.41, 1.41)
    2.115
    """
    return round((a + b + c) / 2, 3)


def hasRightAngle(a, b, c):
    """Compute right angle of triangle.

    Return True if the triangle has right angle.
    >>> hasRightAngle(3, 4, 5)
    'ANO'
    >>> hasRightAngle(1, 1, 1)
    'NE'
    """
    sides = [a, b, c]
    sides.sort(reverse=True)
    if sides[0] * sides[0] == (sides[1] * sides[1]) + (sides[2] * sides[2]):
        return "ANO"
    else:
        return "NE"
