import math

def sestrojitelnost(): 
    
    lze = sA + sB > sC and sB + sC > sA and sA + sC > sB

    return lze

if __name__ == '__main__':
    print('Napis souradnici x bodu A: ')
    Ax = int(input())
    print('Napis souradnici y bodu A: ')
    Ay = int(input())
    print('Napis souradnici x bodu B: ')
    Bx = int(input())
    print('Napis souradnici y bodu B: ')
    By = int(input())
    print('Napis souradnici x bodu C: ')
    Cx = int(input())
    print('Napis souradnici y bodu C: ')
    Cy = int(input())

    sA = math.sqrt(((Bx - Ax) ** 2) + ((By - Ay) ** 2))
    sB = math.sqrt(((Cx - Bx) ** 2) + ((Cy - By) ** 2))
    sC = math.sqrt(((Ax - Cx) ** 2) + ((Ay - Cy) ** 2))

    if sestrojitelnost():
        print('Trojuhelnik lze sestrojit.')
    else:
        print('Trojuhelnik nelze sestrojit.')

    print('Strana A je dlouha: ', sA)
    print('Strana B je dlouha: ', sB)
    print('Strana C je dlouha: ', sC)