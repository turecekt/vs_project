"""
Tento program zjistuje jestli lze sestrojit trojuhelnik.

Pokud ano, tak se vypocita delka jeho stran, obsah, obvod
a jestli je pravouhly.
Program prijima souradnice bodu A,B,C z konzole a vypisuje vysledky na konzoli.

Tvurce: Tomáš Blaho
"""

import math


def sestrojitelnost(A, B, C):
    """
    Funkce zjistuje jestli lze sestrojit trojuhelnik.

    Vraci:
    true = trojuhelnik lze sestrojit
    false = trojhelnik nelze sestrojit
    """
    lze = A + B > C and B + C > A and A + C > B

    return lze


def obsah(A, B, C):
    """
    Funkce pocita obsah trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    s = (A + B + C) / 2

    S = math.sqrt(s * (s - A) * (s - B) * (s - C))

    return S


def obvod(A, B, C):
    """
    Funkce pocita obvod trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    return A + B + C


def pravouhelnost(A, B, C):
    """
    Funkce zjistuje jesli je trojuhelnik pravouhly.

    Vraci:
    true = trojuhelnik je pravouhlu
    false = trojuhelnik neni pravouhlu
    """
    nejdelsi = max(A, B, C)

    if nejdelsi == C:
        je = C ** 2 == A ** 2 + B ** 2
    elif nejdelsi == B:
        je = B ** 2 == A ** 2 + C ** 2
    elif nejdelsi == sA:
        je = A ** 2 == B ** 2 + C ** 2

    return je


if __name__ == '__main__':
    # Program pozaduje uzivatelsky vstup.
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

    # Zkouska cisel jestli jsou ve spravnem tvaru.
    try:
        int(Ax)
        int(Ay)
        int(Bx)
        int(By)
        int(Cx)
        int(Cy)
    except Exception:
        # Nejsou ve spravnem tvaru. Program skoci na konec.
        print('Cisla byla zadana ve spatnem tvaru! Zadej pouze cela cisla.')
    else:
        # Jsou ve spravnem tvaru.
        # Zde se pocita delka sran A, B, C.
        # Toto se bude pozdeji pouzivat ve funkcich.
        sA = math.sqrt(((int(Bx) - int(Ax)) ** 2) + ((int(By) - int(Ay)) ** 2))
        sB = math.sqrt(((int(Cx) - int(Bx)) ** 2) + ((int(Cy) - int(By)) ** 2))
        sC = math.sqrt(((int(Ax) - int(Cx)) ** 2) + ((int(Ay) - int(Cy)) ** 2))

        # Vystup pozadovany v zadani.
        if sestrojitelnost(A = sA, B = sB, C = sC):
            print('Trojuhelnik lze sestrojit.')

            print('Strana A je dlouha: ', sA)
            print('Strana B je dlouha: ', sB)
            print('Strana C je dlouha: ', sC)

            print('Obsah je: ', obsah(A = sA, B = sB, C = sC), ' a obvod je: ', obvod(A = sA, B = sB, C = sC))

            if pravouhelnost(A = sA, B = sB, C = sC):
                print('Trojuhelnik je pravouhly.')
            else:
                print('Trojuhelnik neni pravouhly.')
        else:
            print('Trojuhelnik nelze sestrojit.')

    # Zde program ceka na uzivatelsky vstup k ukonceni.
    input('Zmackni Enter k zavreni programu.')
