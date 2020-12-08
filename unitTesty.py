"""Unit testy programu minMax."""
import sys
from minMax import GetMinMax, bubblesort, selectionsort, insertionsort, vstup


def test_GetMinMax():
    """Test funkce minMax."""
    assert GetMinMax([3, 5, 8, 12, 5, 9, 10, 24, 22]) == print(
        "Minimum je cislo", 3, "na indexu", 0)
    print("Maximum je cislo", 24, "na indexu", 7)

    assert GetMinMax(
        [0, -5, 2]) == print("Minimum je cislo", -5, "na indexu", 1)
    print("Maximum je cislo", 2, "na indexu", 2)

    assert GetMinMax([-5, -5, 2, 3, 15]
                     ) == print("Minimum je cislo", -5, "na indexu", 0)
    print("Maximum je cislo", 15, "na indexu", 4)


def test_bubblesort():
    """Test algoritmu bubblesort."""
    assert bubblesort([3, 5, 8, 12, 5, 9, 10, 22]) == print(
        "Serazene pole:", [3, 5, 5, 8, 9, 10, 12, 22])
    assert bubblesort([3, -2]) == print("Serazene pole:", [3, -2])
    assert bubblesort([0, -5]) == print("Serazene pole:", [-5, 0])


def test_insertionsort():
    """Test algoritmu insertionsort."""
    assert insertionsort([3, 5, 8, 12, 5, 9, 10, 22]) == print(
        "Serazene pole:", [3, 5, 5, 8, 9, 10, 12, 22])
    assert insertionsort([3, -2]) == print("Serazene pole:", [3, -2])
    assert insertionsort([0, -5]) == print("Serazene pole:", [-5, 0])


def test_selectionsort():
    """Test algortimu selectionsort."""
    assert selectionsort([3, 5, 8, 12, 5, 9, 10, 22]) == print(
        "Serazene pole:", [3, 5, 5, 8, 9, 10, 12, 22])
    assert selectionsort([3]) == print("Serazene pole:", [3, -2])
    assert selectionsort([0, -5]) == print("Serazene pole:", [-5, 0])


def test_vstup():
    """Test pro funkcni vstup."""
    if len(sys.argv) == 2:
        assert vstup() == (True, [5, 2, 6, 6, 1, 65,
                                  2, 5, 65, 2, 6, 6, 2, 68, 45, 6, 3])
    elif len(sys.argv) > 2:
        cisla = []
        for i in range(1, len(sys.argv)):
            try:
                cisla.append(int(sys.argv[i]))
            except ValueError:
                assert vstup() == (False, [])
                break

        if cisla != []:
            assert vstup() == (True, cisla)


test_GetMinMax()
test_bubblesort()
test_insertionsort()
test_selectionsort()
test_vstup()
