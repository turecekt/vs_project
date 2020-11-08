"""Toto je program pro nacteni bodu trojuhelniku v 2d prostoru
overeni zda lze setrojit
jakou ma delku stran
jaky je jeho obvod a obsah
zda je nebo neni pravouhly
"""
A = [0, 0]
B = [0, 0]
C = [0, 0]
i = 0
check = False

""" Nacteni Bodu A"""
print("Zadej souradnice x a y pro bod A, danou souradnici vzdy potvrd enterem")
while check == False:
    A[i] = input()
    check = A[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")
    
check = False   
i = i+1
while check == False:
    A[i] = input()
    check = A[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(A)
"""
"""nacteni bodu B"""
i = 0
check = False
print("Zadej souradnice x a y  pro bod B, danou souradnici vzdy potvrd enterem")
while check == False:
    B[i] = input()
    check = B[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")
    
check = False   
i = i+1
while check == False:
    B[i] = input()
    check = B[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(B)
"""
"""nacteni bodu C"""
i = 0
check = False
print("Zadej souradnice x a y  pro bod C, danou souradnici vzdy potvrd enterem")
while check == False:
    C[i] = input()
    check = C[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")
    
check = False   
i = i+1
while check == False:
    C[i] = input()
    check = C[i].isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(C)
"""

""" vypocet stran"""
import  math
Sa = round(math.sqrt((float(B[0]) - float(C[0]))**2 + (float(B[1]) - float(C[1]))**2))
Sb = round(math.sqrt((float(A[0]) - float(C[0]))**2 + (float(A[1]) - float(C[1]))**2))
Sc = round(math.sqrt((float(A[0]) - float(B[0]))**2 + (float(A[1]) - float(B[1]))**2))

"""test sestrojitelnosti"""
if Sa + Sb > Sc and Sa + Sc> Sb and Sb + Sc > Sa:
    print("Trojuhelnik lze setrojit")
    check= True
else:
    print("Trojuhelnik nelze setrojit")
    check= False
    pass

""" vypis hodnot trojuhelniku"""
if check == True:
    print("Delka strany a je: ",round(Sa))
    print("Delka strany b je: ",round(Sb))
    print("Delka strany c je: ",round(Sc))
    obvod = Sa+Sb+Sc
    s = obvod/2
    obsah =math.sqrt(s*(s-Sa)*(s-Sb)*(s-Sc))
    print("Obvod trojuhelniku je: ",round(obvod))
    print("Obsah trojuhelniku je: ",round(obsah))
   
    if Sc**2 == Sb**2 + Sc**2 or Sa**2 == Sb**2 + Sc**2 or Sb**2 == Sa**2 + Sc**2:
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")
        pass