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
A[0] = input()
A[1] = input()


"""nacteni bodu B"""

print("Zadej souradnice x a y pro bod B, danou souradnici vzdy potvrd enterem")
B[0] = input()
B[1] = input()


"""nacteni bodu C"""

print("Zadej souradnice x a y pro bod C, danou souradnici vzdy potvrd enterem")
C[0] = input()
C[1] = input()

""" vypocet stran"""
bc[0] = float(B[0]) - float(C[0])
bc[1] = float(B[1]) - float(C[1])
ac[0] = float(A[0]) - float(C[0])
ac[1] = float(A[1]) - float(C[1])
ab[0] = float(A[0]) - float(B[0])
ab[1] = float(A[1]) - float(B[1])

Sa = float(math.sqrt(float(bc[0])**2 + float(bc[1]**2)))
Sb = float(math.sqrt(float(ac[0]**2) + float(ac[1]**2)))
Sc = float(math.sqrt(ab[0]**2 + ab[1]**2))

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
    print("Delka strany a je: ", round(Sa, 3))
    print("Delka strany b je: ", round(Sb, 3))
    print("Delka strany c je: ", round(Sc, 3))
    obvod = Sa+Sb+Sc
    s = obvod/2
    obsah = math.sqrt(s*(s-Sa)*(s-Sb)*(s-Sc))
    print("Obvod trojuhelniku je: ", round(obvod, 3))
    print("Obsah trojuhelniku je: ", round(obsah, 3))

    SbSc = Sb**2 + Sc**2
    SaSb = Sa**2 + Sb**2
    SaSc = Sa**2 + Sc**2
    round(SbSc)
    round(SaSb)
    round(SaSc)

    if round(Sc**2) == SaSb or round(Sa**2) == SbSc or round(Sb**2) == SaSc:
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")
        pass
