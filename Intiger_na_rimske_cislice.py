import unittest

class Testy(unittest.TestCase):

    def test1(self):
        assert num2roman(1) == 'I'

    def test2(self):
        assert num2roman(5) == 'V'

    def test3(self):
        assert num2roman(50) == 'L'

    def test2(self):
        assert num2roman(2) == 'II'

    def test3(self):
        assert num2roman(3) == 'III'

    def test4(self):
        assert num2roman(4) == 'IV'

    def test5(self):
        assert num2roman(10) == 'X'


num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
                print(roman)

    return roman


num2roman(5)
