import math

inp = input('Zadaj body s ciarkou a body oddel medzerou: ')
array = inp.split(' ')

A = array[0].split(',')
B = array[1].split(',')
C = array[2].split(',')

a = math.sqrt(((int(B[0])-int(A[0]))**2)+((int(B[1])-int(A[1]))**2))
b = math.sqrt(((int(C[0])-int(A[0]))**2)+((int(C[1])-int(A[1]))**2))
c = math.sqrt(((int(C[0])-int(B[0]))**2)+((int(C[1])-int(B[1]))**2))

print('Strana AB ma dlzku:',round(a,4),'\nStrana AC ma dlzku:',round(b,4),'\nStrana BC ma dlzku:',round(c,4))
#---------------------
if (a + b > c and a + c > b and b + c > a):
    print('Da sa zostrojit')
else:
    print('neda sa zostrojit')
#---------------------
print('Obvod = ',round(a+b+c,4),'Obsah = ',round(a*(b*math.sin(math.acos((a**2 + b**2 - c**2)/(2*a*b))))/2,4))
#---------------------
if(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
    print('Je pravouhly')
else:
    print('Neni pravouhly')
