import math

def sestrojitelnost(): 
    
    lze = sA + sB > sC and sB + sC > sA and sA + sC > sB

    return lze

def obsah():

    s = (sA + sB + sC) / 2

    S = math.sqrt(s * (s - sA) * (s - sB) * (s - sC))

    return S

def obvod():

    O = sA + sB + sC

    return O

def pravouhelnost():

    nejdelsi = max(sA, sB, sC)

    if nejdelsi == sC:
        je = sC ** 2 == sA ** 2 + sB ** 2
    elif nejdelsi == sB:
        je = sB ** 2 == sA ** 2 + sC ** 2
    elif nejdelsi == sA:
        je = sA ** 2 == sB ** 2 + sC ** 2

    return je

if __name__ == '__main__':
    print('Napis souradnici x bodu A: ')
    Ax = input()
    print('Napis souradnici y bodu A: ')
    Ay = input()
    print('Napis souradnici x bodu B: ')
    Bx = input()
    print('Napis souradnici y bodu B: ')
    By = input()
    print('Napis souradnici x bodu C: ')
    Cx = input()
    print('Napis souradnici y bodu C: ')
    Cy = input()

    try:
        int(Ax)
        int(Ay)
        int(Bx)
        int(By)
        int(Cx)
        int(Cy)
    except:
       print('Cisla byla zadana ve spatnem tvaru! Zadej pouze cela cisla.')
    else:
        int(Ax)
        int(Ay)
        int(Bx)
        int(By)
        int(Cx)
        int(Cy)

    sA = math.sqrt(((Bx - Ax) ** 2) + ((By - Ay) ** 2))
    sB = math.sqrt(((Cx - Bx) ** 2) + ((Cy - By) ** 2))
    sC = math.sqrt(((Ax - Cx) ** 2) + ((Ay - Cy) ** 2))

    if sestrojitelnost():
        print('Trojuhelnik lze sestrojit.')

        print('Strana A je dlouha: ', sA)
        print('Strana B je dlouha: ', sB)
        print('Strana C je dlouha: ', sC)

        print('Obsah je: ', obsah(), ' a obvod je: ', obvod())

        if pravouhelnost():
            print('Trojuhelnik je pravouhly.')
        else:
            print('Trojuhelnik neni pravouhly.')
    else:
        print('Trojuhelnik nelze sestrojit.')

    