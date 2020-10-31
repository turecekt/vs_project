""" Toto je program pro nacteni bodu trojuhelniku v 2d prostoru
overeni zda lze setrojit
jakou ma delku stran
jaky je jeho obvod a obsah
zda je nebo neni pravouhly

"""
check = False

print("Zadej souradnice pro bod A, danou souradnici vzdy potvrd enterem")
while check == False:
    xA = input()
    check = xA.isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")
    
check = False   
while check == False:
    xB = input()
    check = xB.isnumeric()
    if check == False:
        print("Nezadal jsi ciselnou hodnotu!! Zkus to znovu")

"""uzivatelsky test nacteni
print(xA, xB)
"""