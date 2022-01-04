from sorts import buble_sort, merge_sort, insertion_sort, quick_sort
from main import main_program, vyber_algorythm, min_max_index
from main import main, chooseSorts


test_pole = [11, 3, 2, 1, 5, 7, 10, 6]
test_vysledok_pole = [1, 2, 3, 5, 6, 7, 10, 11]


class Test_MainFunction2:
    def test_main_minmax(self):
        min_max_index(test_pole)


class Test_MainFunction:
    def test_choice(self):
        buble_sort(test_pole)
        assert (test_vysledok_pole == test_pole)


class Test_MergeSort:
    def test_choice(self):
        merge_sort(test_pole, 0, len(test_pole) - 1)
        assert (test_vysledok_pole == test_pole)


class Test_InsertionSort:
    def test_choice(self):
        insertion_sort(test_pole)
        assert (test_vysledok_pole == test_pole)


class Test_QuickSort:
    def test_choice(self):
        quick_sort(test_pole, 0, len(test_pole) - 1)
        assert (test_vysledok_pole == test_pole)


class Test_Main_Program1:
    def test_main_program1(self):
        main_program(1)


class Test_vyber_algorytm:
    def test_vyber_algorythm(self):
        vyber_algorythm(3, test_pole)


class Test_vyber_algorytm1:
    def test_vyber_algorythm1(self):
        vyber_algorythm(1, test_pole)


class Test_vyber_algorytm2:
    def test_vyber_algorythm2(self):
        vyber_algorythm(2, test_pole)


class Test_vyber_algorytm4:
    def test_vyber_algorythm4(self):
        vyber_algorythm(4, test_pole)


class Test_vyber_algorytm5:
    def test_vyber_algorythm5(self):
        vyber_algorythm(5, test_pole)


class Test_min_max_index:
    def test_minmaxindex(self):
        min_max_index(test_pole)


def test_run(monkeypatch):
    """Test run funkce."""
    monkeypatch.setattr('builtins.input', lambda _: 5)
    i = input("Enter your choice:")
    assert i == 5
    assert(main() == print("Incorrect input!"))


def test_run_mainSorts(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    i = input("Enter your choice:")
    assert i == 5
    assert(main() == print("Incorrect input!"))


def test_run_mainSorts_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 7)
    i = input("Enter your choice:")
    assert i == 7
    assert(chooseSorts() == 7)
