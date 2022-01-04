"""
Adam Kopřiva.

Převod integru na římský zápis čísel
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


if __name__ == '__main__':
    num2roman(input('Zadejte číslo pro převod: '))


class Testy(unittest.TestCase):
    """Zde jsou testy."""

    def test1(self):
        """
        Testik.

        Zde se testuje správnost kodu
        """
        assert num2roman(1) == 'I'
