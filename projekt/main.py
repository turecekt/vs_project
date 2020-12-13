import math


def sestrojitelnost():
    '''
    Funkce zjistuje jestli lze sestrojit trojuhelnik

    Vraci:
    true = trojuhelnik lze sestrojit
    false = trojhelnik nelze sestrojit
    '''

    lze = sA + sB > sC and sB + sC > sA and sA + sC > sB

    return lze


def obsah():
    '''
    Funkce pocita obsah trojuhelniku

    Vraci float s vypocitanou hodnotou
    '''

    s = (sA + sB + sC) / 2

    S = math.sqrt(s * (s - sA) * (s - sB) * (s - sC))

    return S


def obvod():
    '''
    Funkce pocita obvod trojuhelniku

    Vraci float s vypocitanou hodnotou
    '''

    return sA + sB + sC


def pravouhelnost():
    '''
    Funkce zjistuje jesli je trojuhelnik pravouhly

    Vraci:
    true = trojuhelnik je pravouhlu
    false = trojuhelnik neni pravouhlu
    '''

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
    except Exception:
        print('Cisla byla zadana ve spatnem tvaru! Zadej pouze cela cisla.')
    else:
        sA = math.sqrt(((int(Bx) - int(Ax)) ** 2) + ((int(By) - int(Ay)) ** 2))
        sB = math.sqrt(((int(Cx) - int(Bx)) ** 2) + ((int(Cy) - int(By)) ** 2))
        sC = math.sqrt(((int(Ax) - int(Cx)) ** 2) + ((int(Ay) - int(Cy)) ** 2))

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

    input('Zmackni Enter k zavreni programu.')
