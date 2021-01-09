"""Triangle."""


class Triangle():
    """Constructability triangle"""


a = 0
b = 0
c = 0


def isConstructable():
    """Check triangle constructability
    Return True if thi triangle is constructable
    >>> isConstructable()
    true
    """

    triangleIsConstructable = True

    if a + b < c or b + c < a or c + a < b:
        triangleIsConstructable = False

    return triangleIsConstructable
