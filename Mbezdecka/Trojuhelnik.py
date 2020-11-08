""" Toto je program pro nacteni bodu trojuhelniku v 2d prostoru
overeni zda lze setrojit
jakou ma delku stran
jaky je jeho obvod a obsah
zda je nebo neni pravouhly

"""
A = [0,0]
B = [0,0]
C = [0,0]

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
i = (B[0] - C[0])**2 + (B[1] - C[1])**2
stra = math.sqrt(i)
i = (A[0] - C[0])**2 + (A[1] - C[1])**2
strb = math.sqrt(i)
i = (A[0] - B[0])**2 + (A[1] - B[1])**2
strc = math.sqrt(i)

"""test sestrojitelnosti"""
if stra + strb > strc and stra + strc > strb and strb + strc > stra
    print("Trojuhelnik lze setrojit)