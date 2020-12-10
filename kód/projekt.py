"""Proste projekt."""

import math

def zostrojenost(a, b, c):
    """Funkcia ktora zisti ci sa da trojuholnik zostrojit."""
    if (a + b > c and a + c > b and b + c > a):
        return 1
    else:
        return 0


def obvod(a, b, c):
    """Funkcia vypocita obvod."""
    return round(a+b+c, 4)


def obsah(a, b, c):
    """Funkcia vypocita obsah."""
    return round(a*(b*math.sin(math.acos((a**2 + b**2 - c**2)/(2*a*b))))/2, 4)


def pravouhlost(a, b, c):
    """Funkcia zisti ci je trojuholnik pravouhly."""
    if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        return 1
    else:
        return 0

def dlzkastrany(ax, ay, bx, by):
    """Funkcia pre vypocet dlzky strany trojuholnika."""
    return math.sqrt(((int(bx)-int(ax))**2)+((int(by)-int(ay))**2))


if __name__ == '__main__':
    xarray = []
    yarray = []
    for i in range(3):
        xarray.append(input('Zadaj x suradnicu bodu '))
        yarray.append(input('Zadaj y suradnicu bodu '))

    Ax = xarray[0]
    Ay = yarray[0]
    Bx = xarray[1]
    By = yarray[1]
    Cx = xarray[2]
    Cy = yarray[2]

    s1 = dlzkastrany(Ax, Ay, Bx, By)
    s2 = dlzkastrany(Ax, Ay, Cx, Cy)
    s3 = dlzkastrany(Bx, By, Cx, Cy)
    o = obvod(s1, s2, s3)
    S = obsah(s1, s2, s3)
    print(o)
    print(S)
    print('Strana AB ma dlzku:', round(dlzkastrany(Ax, Ay, Bx, By), 4))
    print('Strana AC ma dlzku:', round(dlzkastrany(Ax, Ay, Cx, Cy), 4))
    print('Strana BC ma dlzku:', round(dlzkastrany(Bx, By, Cx, Cy), 4))
