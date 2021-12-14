"""
This is an example script.

It seems that it has to have THIS docstring with a summary line,
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
    """Return the pathname of the KOS root directory."""
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
    """
    Tady jsou testy

    It seems that it has to have THIS docstring with a summary line, a bl
    and sume more text like here. Wow.
    """
    def test1(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a bla
        and sume more text like here. Wow.
        """
        assert num2roman(1) == 'I'

    def test2(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a
        and sume more text like here. Wow.
        """
        assert num2roman(5) == 'V'

    def test3(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a bla
        and sume more text like here. Wow.
        """
        assert num2roman(50) == 'L'

    def test4(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a bl
        and sume more text like here. Wow.
        """
        assert num2roman(2) == 'II'

    def test5(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a blan
        and sume more text like here. Wow.
        """
        assert num2roman(3) == 'III'

    def test6(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a blan
        and sume more text like here. Wow.
        """
        assert num2roman(4) == 'IV'

    def test7(self):
        """
        This is an example script.

        It seems that it has to have THIS docstring with a summary line, a blan
        and sume more text like here. Wow.
        """
        assert num2roman(10) == 'X'
