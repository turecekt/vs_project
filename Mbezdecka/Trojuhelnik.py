""" Toto je program pro nacteni bodu trojuhelniku v 2d prostoru
overeni zda lze setrojit
jakou ma delku stran
jaky je jeho obvod a obsah
zda je nebo neni pravouhly

"""
A = [0,0]
i = 0
check = False

print("Zadej souradnice pro bod A, danou souradnici vzdy potvrd enterem")
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