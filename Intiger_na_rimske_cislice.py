"""
Adam Kopřiva.

Převod integru na římský zápis čísel docstring with a summary line,
and sume more text like here. Wow.
"""
import unittest

num_map = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
    ]


def num2roman(num):
    """´Převod čísla na římské číslo."""
    roman = ''

    while num > 0:
        for (i, r) in num_map:
            while num >= i:
                roman += r
                num -= i
                print(roman)

    return roman


num2roman(5)


class Testy(unittest.TestCase):
    """Zde jsou testy."""

    def test1(self):
        """
        Testik.

        It seems that it has to have THIS docstring with a summary line, a bla
        and sume more text like here. Wow.
        """
        assert num2roman(1) == 'I'

