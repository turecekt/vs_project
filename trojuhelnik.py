import math

def delkaStrany(x1, y1, x2, y2):
    """Calculate the length of a side of a triangle.

    Return the length of the side rounded to 2 decimal places
    >>> delkaStrany(10, 10, 5, 5) == 7.07
    True
    >>> delkaStrany(6, 4, 2, 3)
    4.12
    """
    str1 = x2-x1
    str2 = y2-y1
    str1 = math.pow(str1, 2)
    str2 = math.pow(str2, 2)
    st = round(math.sqrt(str1+str2), 2)
    return st

print("Zadejte souřadnice pro bod A na ose X: ")
ax = float(input())
print("Zadejte souřadnice pro bod A na ose Y: ")
ay = float(input())
print("Zadejte souřadnice pro bod B na ose X: ")
bx = float(input())
print("Zadejte souřadnice pro bod B na ose Y: ")
by = float(input())
print("Zadejte souřadnice pro bod C na ose X: ")
cx = float(input())
print("Zadejte souřadnice pro bod C na ose Y: ")
cy = float(input())
stra = delkaStrany(cx, cy, bx, by)
print("Délka strany a: " + str(stra) + " cm")
strb = delkaStrany(ax, ay, cx, cy)
print("Délka strany b: " + str(strb) + " cm")
strc = delkaStrany(bx, by, ax, ay)
print("Délka strany c: " + str(strc) + " cm")
if stra + strb > strc and strb + strc > stra and strc + stra > strb:
    print("Trojúhelník je sestrojitelný")
else:
    print("Trojúhelník není sestrojitelný")
obvod = stra + strb + strc
print("Obvod trojúhelníku je " + str(obvod) + " cm")
s = (stra + strb + strc) / 2
m = s * (s - stra) * (s - strb) * (s - strc)
if m >= 0:
    obsah = math.sqrt(m)
    print("Obsah trojúhelníku je " + str(obsah) + " cm")
else:
    print("Obsah nelze vypočítat (záporné číslo pod odmocninou")
if math.pow(2, stra) == math.pow(2, strb) + math.pow(2, strc) or math.pow(2, strb) == math.pow(2, strc) + math.pow(2, stra) or math.pow(2, strc) == math.pow(2, stra) + math.pow(2, strb):
    print("Trojúhelník je pravoúhlý")
else:
    print("Trojúhelník není pravoúhlý")