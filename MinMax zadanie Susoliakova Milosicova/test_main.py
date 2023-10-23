"""Test funkcie na vykonanie pytestov."""

from sorts import buble_sort, merge_sort, insertion_sort, quick_sort
from main import main_program, vyber_algorythm, min_max_index
from main import main, chooseSorts


test_pole = [11, 3, 2, 1, 5, 7, 10, 6]
test_vysledok_pole = [1, 2, 3, 5, 6, 7, 10, 11]


def test_main_minmax():
    """Test funkcie na skontrolovanie min_max index pola."""
    min_max_index(test_pole)


def test_choice_buble_sort():
    """Test run buble sortu pre spravne zoradenie."""
    buble_sort(test_pole)
    assert (test_vysledok_pole == test_pole)


def test_choice_merge_sort():
    """Test run merge sortu pre spravne zoradenie."""
    merge_sort(test_pole, 0, len(test_pole) - 1)
    assert (test_vysledok_pole == test_pole)


def test_choice_insertion_sort():
    """Test run insertion sortu pre spravne zoradenie."""
    insertion_sort(test_pole)
    assert (test_vysledok_pole == test_pole)


def test_choice():
    """Test run quick sortu pre spravne zoradenie."""
    quick_sort(test_pole, 0, len(test_pole) - 1)
    assert (test_vysledok_pole == test_pole)


def test_main_program1():
    """Test run hlavnej funkce pre specificku volbou 1."""
    main_program(1)


def test_vyber_algorythm():
    """Test run funkce pre vyber sortov s danym polom\
        a specifickou volbou 3."""
    vyber_algorythm(3, test_pole)


def test_vyber_algorythm1():
    """Test run funkce pre vyber sortov s danym polom\
        a specifickou volbou 1."""
    vyber_algorythm(1, test_pole)


def test_vyber_algorythm2():
    """Test run funkce pre vyber sortov s danym polom\
        a specifickou volbou 2."""
    vyber_algorythm(2, test_pole)


def test_vyber_algorythm4():
    """Test run funkce pre vyber sortov s danym polom\
        a specifickou volbou 4."""
    vyber_algorythm(4, test_pole)


def test_vyber_algorythm5():
    """Test run funkce pre vyber sortov s danym polom\
        a specifickou volbou 5."""
    vyber_algorythm(5, test_pole)


def test_minmaxindex():
    """Test run funkce pre specificke pole v min max index funcii."""
    min_max_index(test_pole)


def test_run(monkeypatch):
    """Test run funkce pre volbu 5 a vystup Incorrect input."""
    monkeypatch.setattr('builtins.input', lambda _: 5)
    i = input("Enter your choice:")
    assert i == 5
    assert(main() == print("Incorrect input!"))


def test_run_mainSorts(monkeypatch):
    """Test run main sorts funkce pre volbu 5."""
    monkeypatch.setattr('builtins.input', lambda _: 5)
    i = input("Enter your choice:")
    assert i == 5
    assert(main() == print("Incorrect input!"))


def test_run_mainSorts_2(monkeypatch):
    """Test run main sorts funkce pre volbu 7."""
    monkeypatch.setattr('builtins.input', lambda _: 7)
    i = input("Enter your choice:")
    assert i == 7
    assert(chooseSorts() == 7)
