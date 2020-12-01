"""Calculate triangle."""
import math


def lengthofside(jednaX, dveX, jednaY, dveY):
    """Calculate length of a side."""
    sa = jednaX - dveX
    sb = jednaY - dveY
    vysledek = math.sqrt(sa * sa + sb * sb)
    return vysledek


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
