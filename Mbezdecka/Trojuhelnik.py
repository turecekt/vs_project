"""Toto je program pro nacteni bodu trojuhelniku v 2d prostoru.

Overi zda lze setrojit.
Jakou ma delku stran.
Jaky je jeho obvod a obsah.
Zda je nebo neni pravouhly.

"""


def nacteni_bodu():
    """Nacteni Bodu."""
    print("Zadej souradnice bodu, danou souradnici vzdy potvrd enterem")
    nc = [0, 0]
    nc[0] = input()
    nc[1] = input()
    return nc


def vypocet_strany(A, B):
    """Vypocet strany.

    >>> vypocet_strany([1, 3], [3, 5])
    2.828
    >>> import math
    >>> math.sqrt(float(4**2) + float(3**2))
    5.0
    """
    import math
    ab = [0, 0]
    ab[0] = float(A[0]) - float(B[0])
    ab[1] = float(A[1]) - float(B[1])
    S = float(math.sqrt(float(ab[0]**2) + float(ab[1]**2)))
    return round(S, 3)


def sestrojitelny(Sa, Sb, Sc):
    """Test sestrojitelnosti.

    >>> sestrojitelny( 4.243, 5.099, 2.828)
    Trojuhelnik lze setrojit
    True
    >>> sestrojitelny( 0, 5.099, 2.828)
    Trojuhelnik nelze setrojit
    False
    """
    if Sa + Sb > Sc and Sa + Sc > Sb and Sb + Sc > Sa:
        print("Trojuhelnik lze setrojit")
        return True
    else:
        print("Trojuhelnik nelze setrojit")
        return False


def obvod(Sa, Sb, Sc):
    """Vypocet obvodu trojuhelniku.

    >>> obvod(4.243, 5.099, 2.828)
    12.17
    """
    return Sa+Sb+Sc


def svypocet(Sa, Sb, Sc):
    """Pomocny vypocet pro obsah.

    >>> svypocet(4.243, 5.099, 2.828)
    6.085
    """
    return obvod(Sa, Sb, Sc)/2


def obsah(Sa, Sb, Sc):
    """Vypocet osahu trojuhelniku.

    >>> obvod(4.243, 5.099, 2.828)
    12.17
    """
    s = svypocet(Sa, Sb, Sc)
    return math.sqrt(s*(s-Sa)*(s-Sb)*(s-Sc))


def pravouhly(Sa, Sb, Sc):
    """Test zda se jedna o pravouhly trojuhelnik.

    >>> pravouhly(4.243, 5.099, 2.828)
    True
     >>> pravouhly(2.243, 5.099, 2.828)
     False
    """
    SbSc = round(Sb**2 + Sc**2)
    SaSb = round(Sa**2 + Sb**2)
    SaSc = round(Sa**2 + Sc**2)
    if round(Sc**2) == SaSb or round(Sa**2) == SbSc or round(Sb**2) == SaSc:
        return True
    else:
        return False


if __name__ == '__main__':
    """ Hlavni telo programu."""

    import math
    A = ['0', '0']
    B = ['0', '0']
    C = ['0', '0']
    check = False
    A = nacteni_bodu()
    B = nacteni_bodu()
    C = nacteni_bodu()
    Sa = vypocet_strany(B, C)
    Sb = vypocet_strany(A, C)
    Sc = vypocet_strany(A, B)
    check = sestrojitelny(Sa, Sb, Sc)
    if check is True:
        print("Delka strany a je: ", round(Sa, 3))
        print("Delka strany b je: ", round(Sb, 3))
        print("Delka strany c je: ", round(Sc, 3))
        print("Obvod trojuhelniku je: ", round(obvod(Sa, Sb, Sc), 3))
        print("Obsah trojuhelniku je: ", round(obsah(Sa, Sb, Sc), 3))
        if pravouhly(Sa, Sb, Sc) is True:
            print("Trojuhelnik je pravouhly")
        else:
            print("Trojuhelnik neni pravouhly")
            pass
    else:
        pass
