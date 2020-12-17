"""
Tento program zjistuje jestli lze sestrojit trojuhelnik.

Pokud ano, tak se vypocita delka jeho stran, obsah, obvod
a jestli je pravouhly.
Program prijima souradnice bodu A,B,C z konzole a vypisuje vysledky na konzoli.

Tvurce: Tomas Blaho
"""

from math import sqrt


# PyTest sekce ------------------------------
def test_obvod():
    """Test obvod()."""
    assert obvod(3, 4, 5) == 12
    assert obvod(5, 4, 3) == 12
    assert obvod(3, 5, 4) == 12


def test_obsah():
    """Test obsah()."""
    assert obsah(3, 4, 5) == 6
    assert obsah(5, 4, 3) == 6
    assert obsah(3, 5, 4) == 6


def test_pravouhelnost():
    """Test pravouhelnost()."""
    assert pravouhelnost(3, 4, 5) is True
    assert pravouhelnost(5, 4, 3) is True
    assert pravouhelnost(3, 5, 4) is True


def test_sestrojitelnost():
    """Test sestrojitelnost()."""
    assert sestrojitelnost(3, 4, 5) is True
    assert sestrojitelnost(5, 4, 3) is True
    assert sestrojitelnost(4, 5, 3) is True


def test_sA():
    """Test sA()."""
    assert sA(9, 12, 12, 16) == 5


def test_sB():
    """Test sB()."""
    assert sB(9, 12, 12, 16) == 5


def test_sC():
    """Test sC()."""
    assert sC(9, 12, 12, 16) == 5
# PyTest konec -----------------------------


def sestrojitelnost(a, b, c):
    """
    Funkce zjistuje jestli lze sestrojit trojuhelnik.

    Vraci:
    true = trojuhelnik lze sestrojit
    false = trojhelnik nelze sestrojit
    """
    lze = a + b > c and b + c > a and a + c > b

    return lze


def obsah(a, b, c):
    """
    Funkce pocita obsah trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    s = (a + b + c) / 2

    S = sqrt(s * (s - a) * (s - b) * (s - c))

    return S


def obvod(a, b, c):
    """
    Funkce pocita obvod trojuhelniku.

    Vraci:
    float s vypocitanou hodnotou
    """
    return a + b + c


def pravouhelnost(a, b, c):
    """
    Funkce zjistuje jesli je trojuhelnik pravouhly.

    Vraci:
    true = trojuhelnik je pravouhlu
    false = trojuhelnik neni pravouhlu
    """
    nejdelsi = max(a, b, c)

    if nejdelsi == c:
        je = c ** 2 == a ** 2 + b ** 2
    elif nejdelsi == b:
        je = b ** 2 == a ** 2 + c ** 2
    elif nejdelsi == a:
        je = a ** 2 == b ** 2 + c ** 2

    return je


def sA(ax, ay, bx, by):
    """
    Funkce pocita delku strany A.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(bx) - int(ax)) ** 2) + ((int(by) - int(ay)) ** 2))


def sB(bx, by, cx, cy):
    """
    Funkce pocita delku strany B.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(cx) - int(bx)) ** 2) + ((int(cy) - int(by)) ** 2))


def sC(ax, ay, cx, cy):
    """
    Funkce pocita delku strany C.

    Vraci:
    float s vypocitanou hodnotou
    """
    return sqrt(((int(ax) - int(cx)) ** 2) + ((int(ay) - int(cy)) ** 2))


if __name__ == '__main__':
    # Zkouska cisel jestli jsou ve spravnem tvaru.
    try:
        # Program pozaduje uzivatelsky vstup.
        Ax = int(input('Napis souradnici x bodu A: '))
        Ay = int(input('Napis souradnici y bodu A: '))
        Bx = int(input('Napis souradnici x bodu B: '))
        By = int(input('Napis souradnici y bodu B: '))
        Cx = int(input('Napis souradnici x bodu C: '))
        Cy = int(input('Napis souradnici y bodu C: '))
    except Exception:
        # Nejsou ve spravnem tvaru. Program skoci na konec.
        print('Cisla byla zadana ve spatnem tvaru! Zadej pouze cela cisla.')
    else:
        # Jsou ve spravnem tvaru.
        # Zde se pocita delka sran A, B, C.
        A = sA(Ax, Ay, Bx, By)
        B = sB(Bx, By, Cx, Cy)
        C = sC(Ax, Ay, Cx, Cy)

        # Vystup pozadovany v zadani.
        if sestrojitelnost(A, B, C):
            print('Trojuhelnik lze sestrojit.')

            print('Strana A je dlouha: ', A)
            print('Strana B je dlouha: ', B)
            print('Strana C je dlouha: ', C)

            print('Obsah je: ', obsah(A, B, C),
                  ' a obvod je: ', obvod(A, B, C))

            if pravouhelnost(A, B, C):
                print('Trojuhelnik je pravouhly.')
            else:
                print('Trojuhelnik neni pravouhly.')
        else:
            print('Trojuhelnik nelze sestrojit.')

    # Konec. Zde program ceka na uzivatelsky vstup k ukonceni.
    input('Zmackni Enter k zavreni programu.')
