import pytest
from sorts import buble_sort

test_pole = [3,2,1]
test_vysledok_pole = [1,2,3]

test_volba1 = 1
test_volba2 = 1

class Test_MainFunction:
    def test_choice(self):
        buble_sort(test_pole)
        assert (test_vysledok_pole == test_pole)