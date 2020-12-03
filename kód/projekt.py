import math
xarray = [1,4,2]
yarray = [1,5,8]
'''for i in range(3):
    xarray.append(input('Zadaj x suradnicu bodu '))
    yarray.append(input('Zadaj x suradnicu bodu '))'''


Ax = xarray[0]
Ay = yarray[0] 
Bx = xarray[1]
By = yarray[1]
Cx = xarray[2]
Cy = yarray[2]

def dlzkastrany(ax,ay,bx,by):
    return math.sqrt(((int(bx)-int(ax))**2)+((int(by)-int(ay))**2))




print('Strana AB ma dlzku:',round(dlzkastrany(Ax,Ay,Bx,By),4),'\nStrana AC ma dlzku:',round(dlzkastrany(Ax,Ay,Cx,Cy),4),'\nStrana BC ma dlzku:',round(dlzkastrany(Bx,By,Cx,Cy),4))
#---------------------
def zostrojenost(a,b,c):
    if (a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

#---------------------
def obvod(a,b,c):
    return round(a+b+c,4)

def obsah(a,b,c):
    return round(a*(b*math.sin(math.acos((a**2 + b**2 - c**2)/(2*a*b))))/2,4)
#---------------------
def pravouhlost(a,b,c):
    if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        return True
    else:
        return False

print(obvod(dlzkastrany(Ax,Ay,Bx,By),dlzkastrany(Bx,By,Cx,Cy),dlzkastrany(Ax,Ay,Cx,Cy)))
print(obsah(dlzkastrany(Ax,Ay,Bx,By),dlzkastrany(Bx,By,Cx,Cy),dlzkastrany(Ax,Ay,Cx,Cy)))

#--------unit testy--------
def dlzkastrany_test():
    ax = 1
    ay = 1
    bx = -4
    by = 1
    vysledok = dlzkastrany(ax,ay,bx,by)
    ocakavanie = 5
    if vysledok == ocakavanie:
        return True
    else:
        return False

def zostrojenost_test():
    a = 4
    b = 8
    c = 2
    vysledok = zostrojenost(a,b,c)
    ocakavanie = False
    if vysledok == ocakavanie:
        return True
    else:
        return False

def pravouhlost_test():
    a = 4
    b = 5
    c = 3
    vysledok = pravouhlost(a,b,c)
    ocakavanie = True
    if vysledok == ocakavanie:
        return True
    else:
        return False

def obsah_test():
    a = 1
    b = 1
    c = 1
    vysledok = obsah(a,b,c)
    ocakavanie = 0.433
    if vysledok == ocakavanie:
        return True
    else:
        return False

def obvod_test():
    a = 45
    b = 45
    c = 40
    vysledok = obvod(a,b,c)
    ocakavanie = 130
    if vysledok == ocakavanie:
        return True
    else:
        return False
#-------------
print(dlzkastrany_test())
print(zostrojenost_test())
print(pravouhlost_test())
print(obsah_test())
print(obvod_test())
