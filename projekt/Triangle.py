"""Calculate triangle."""
import math


def lengthofside(jednaX, dveX, jednaY, dveY):
    """Calculate length of a side."""
    sa = jednaX - dveX
    sb = jednaY - dveY
    vysledek = math.sqrt(sa * sa + sb * sb)
    return vysledek


def constructability(Jedna, Dva, Tri):
    """Return if the triangle can be constructed.

    >>> constructability(5, 4, 3)
    'Trojúhelník je sestrojitelný'
    >>> constructability(500, 4, 3)
    'Trojůhelník není sestrojitelný'
    """
    if Jedna + Dva > Tri and Dva + Tri > Jedna and Jedna + Tri > Dva:
        return 'Trojúhelník je sestrojitelný'
    else:
        return 'Trojůhelník není sestrojitelný'


def biggest(stranaJedna, stranaDva, stranaTri):
    """Return the biggest number.

    >>> biggest(1, 2, 3)
    3
    >>> biggest(50.1, 94.20, 4/2)
    94.2
    """
    big = stranaJedna
    if big > stranaDva:
        if big > stranaTri:
            return big
        else:
            return stranaTri
    elif stranaDva > stranaTri:
        return stranaDva
    else:
        return stranaTri


def rightangle(C, A, B):
    """Check if the triangle has a right angle.

    >>> rightangle(5, 4, 3)
    'Trojúhelník je pravoúhlý'
    >>> rightangle(500, 2, 1)
    'Trojúhelník není pravoúhlý'
    """
    if C * C == A * A + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif A * A == C * C + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif B * B == C * C + A * A:
        return 'Trojúhelník je pravoúhlý'
    else:
        return 'Trojúhelník není pravoúhlý'


def perimeter(A, B, C):
    """Count the perimeter of triangle.

    >>> perimeter(2, 5, 3)
    10
    """
    o = A + B + C
    return o


def area(A, B, C):
    """Calculate area of triangle."""
    s = perimeter(A, B, C) / 2
    S = math.sqrt(s*(s-A)*(s-B)*(s-C))
    return S


if __name__ == '__main__':
    try:
        Ax = float(input("Napiš pozici x bodu A:"))
        Ay = float(input("Napiš pozici y bodu A:"))
        Bx = float(input("Napiš pozici x bodu B:"))
        By = float(input("Napiš pozici y bodu B:"))
        Cx = float(input("Napiš pozici x bodu C:"))
        Cy = float(input("Napiš pozici y bodu C:"))
    except ValueError:
        print("Nebylo zadano číslo")

    a = lengthofside(Cx, Bx, Cy, By)
    b = lengthofside(Ax, Cx, Ay, Cy)
    c = lengthofside(Bx, Ax, By, Ay)

    print("Délka strany a je: ", a)
    print("Délka strany b je: ", b)
    print("Délka strany c je: ", c)
    print(constructability(a, b, c))
    print("Největší strana má délku", biggest(a, b, c))
    print(rightangle(c, a, b))
    print("Obvod trojúhelníku je: ", perimeter(a, b, c))
    print("Obsah trojúhelníku je: ", area(a, b, c))
