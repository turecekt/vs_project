from sorts import buble_sort
from sorts import merge_sort
from sorts import insertion_sort
from sorts import quick_sort
from main import main_program
from main import vyber_algorythm

test_pole = [11, 3, 2, 1, 5, 7, 10, 6]
test_vysledok_pole = [1, 2, 3, 5, 6, 7, 10, 11]


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


class Test_Main_Program:
    def test_main_program(self):
        main_program(3)


class Test_vyber_algorytm:
    def test_vyber_algorythm(self):
        vyber_algorythm(5, test_pole)
