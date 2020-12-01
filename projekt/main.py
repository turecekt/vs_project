"""Calculate triangle."""
import math


def lengthofside(jednaX, dveX, jednaY, dveY):
    """Calculate length of a side."""
    sa = jednaX - dveX
    sb = jednaY - dveY
    vysledek = math.sqrt(sa * sa + sb * sb)
    return vysledek


def constructability(Jedna, Dva, Tri):
    """Return if the triangle can be constructed."""
    if Jedna + Dva > Tri and Dva + Tri > Jedna and Jedna + Tri > Dva:
        return 'Trojúhelník je sestrojitelný'
    else:
        return 'Trojůhelník není sestrojitelný'


def biggest(stranaJedna, stranaDva, stranaTri):
    """Return the biggest number."""
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
    """Check if the triangle has a right angle."""
    if C * C == A * A + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif A * A == C * C + B * B:
        return 'Trojúhelník je pravoúhlý'
    elif B * B == C * C + A * A:
        return 'Trojúhelník je pravoúhlý'
    else:
        return 'Trojúhelník není pravoúhlý'


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

print(a)
print(b)
print(c)
print(constructability(a, b, c))
print("Největší strana má délku", biggest(a, b, c))
print(rightangle(c, a, b))
