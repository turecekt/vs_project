"""Výpočet vlastností trojuhelníka."""

"""Zaznamenat vstup z konzole"""
print("Zadejte souřadnice trojuhelníku\n")
A = (input("bod A - souřadnice x: "), input("bod A - souřadnice y: "))
B = (input("bod B - souřadnice x: "), input("bod B - souřadnice y: "))
C = (input("bod C - souřadnice x: "), input("bod C - souřadnice y: "))
Triangle = [A, B, C]
print("\nZadali jste Trojuhelník se souřadnicemi:")
print("A: ", A)
print("B: ", B)
print("C: ", C)


def is_valid(Triangle):
    """Funkce is_valid vyhodnotí je-li daný trojuhelník sestrojitelný.

    Jinak řečeno, zdali všechny body neleží na stejné přímce.

    >>> Triangle = [(0,0), (3,0), (0,4)]
    >>> is_valid(Triangle)
    True
    >>> Triangle = [(1,0), (1,7), (1,4)]
    >>> is_valid(Triangle)
    False
    """
    return True


def side_lengths(Triangle):
    """Funkce side_lengths vrací list délek stran trojuhelníku.

    >>> Triangle = [(0,0), (3,0), (0,4)]
    >>> side_lenghts(Triangle)
    [5,4,3]
    """
    sides = [1, 1, 1]
    return sides


def circumference(Triangle):
    """Funkce circumference vrací obvod trojuhelníku.

    >>> Triangle = [(0,0), (3,0), (0,4)]
    >>> circumference(Triangle)
    12
    """
    obvod = 5
    return obvod


def is_right(Triangle):
    """Funkce is_right vyhodnotí je-li daný trojuhelník pravoúhlý.

    >>> Triangle = [(0,0), (3,0), (0,4)]
    >>> is_right(Triangle)
    True
    """
    return False


def test_is_valid():
    """Test vyhodnocení bodů na jedné přímce jako False."""
    assert is_valid([(0, 0), (0, 4), (0, -2)]) is False
    assert is_valid([(0, 0), (3, 0), (0, -2)]) is True


def test_side_lengths():
    """Test výpočtu délek stran."""
    assert side_lengths([(0, 0), (3, 0), (0, 4)]) == [5, 4, 3]


def test_circumference():
    """Test výpočtu obvodu stran."""
    assert circumference([(0, 0), (3, 0), (0, 4)]) == 12


def test_is_right():
    """Test určení pravoúhlého trojuhelníku."""
    assert is_right([(0, 0), (3, 0), (0, 4)]) is True
    assert is_right([(0, 0), (3, 2), (1, 4)]) is False
