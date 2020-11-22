"""Toto je program pro nacteni bodu trojuhelniku v 2d prostoru.

Overi zda lze setrojit.
Jakou ma delku stran.
Jaky je jeho obvod a obsah.
Zda je nebo neni pravouhly.

"""
import math
A = [0, 0]
B = [0, 0]
C = [0, 0]
bc = [0, 0]
ab = [0, 0]
ac = [0, 0]
i = 0
check = False

""" Nacteni Bodu A"""
print("Zadej souradnice x a y pro bod A, danou souradnici vzdy potvrd enterem")
while check is False:
    A[i] = input()
    check = A[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")
check = False
i = i+1

while check is False:
    A[i] = input()
    check = A[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(A)
"""
"""nacteni bodu B"""
i = 0
check = False
print("Zadej souradnice x a y pro bod B, danou souradnici vzdy potvrd enterem")
while check is False:
    B[i] = input()
    check = B[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

check = False
i = i+1

while check is False:
    B[i] = input()
    check = B[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(B)
"""
"""nacteni bodu C"""
i = 0
check = False
print("Zadej souradnice x a y pro bod C, danou souradnici vzdy potvrd enterem")
while check is False:
    C[i] = input()
    check = C[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

check = False
i = i+1
while check is False:
    C[i] = input()
    check = C[i].isnumeric()
    if check is False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(C)
"""

""" vypocet stran"""
bc[0] = float(B[0]) - float(C[0])
bc[1] = float(B[1]) - float(C[1])
ac[0] = float(A[0]) - float(C[0])
ac[1] = float(A[1]) - float(C[1])
ab[0] = float(A[0]) - float(B[0])
ac[1] = float(A[1]) - float(B[1])
Sa = round(math.sqrt(bc[0]**2 + bc[1]**2))
Sb = round(math.sqrt(ac[0]**2 + ac[1]**2))
Sc = round(math.sqrt(ab[0]**2 + ab[1]**2))

"""test sestrojitelnosti"""
if Sa + Sb > Sc and Sa + Sc > Sb and Sb + Sc > Sa:
    print("Trojuhelnik lze setrojit")
    check = True
else:
    print("Trojuhelnik nelze setrojit")
    check = False
    pass

""" vypis hodnot trojuhelniku"""
if check is True:
    print("Delka strany a je: ", round(Sa))
    print("Delka strany b je: ", round(Sb))
    print("Delka strany c je: ", round(Sc))
    obvod = Sa+Sb+Sc
    s = obvod/2
    obsah = math.sqrt(s*(s-Sa)*(s-Sb)*(s-Sc))
    print("Obvod trojuhelniku je: ", round(obvod))
    print("Obsah trojuhelniku je: ", round(obsah))

    SbSc = Sb**2 + Sc**2
    SaSb = Sb**2 + Sa**2
    SaSc = Sa**2 + Sc**2

    if Sc**2 == SaSb or Sa**2 == SbSc or Sb**2 == SaSc:
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")
        pass
