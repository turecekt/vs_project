"""This module works with Roman Numerals.

The module supplies one function: toRoman(self, iArabicNum). For example,

>>> toRoman(self, 10)
X
"""


class roman_lib:
    """The main class for converting between Arabic Numbers and Roman Numerals.

    It can be upgraded in the future
    """

    def toRoman(self, iArabicNum):
        """Function converts Arabic Numbers to Roman Numerals.

        Args:

            iArabicNum (int): an integer

        Returns:

            str: a string of Roman Numerals
        """
        value = [1000, 900, 500, 400,
                 100, 90, 50, 40, 10,
                 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD",
                  "C", "XC", "L", "XL", "X",
                  "IX", "V", "IV", "I"]
        sRomanNum = ''
        i = 0
        while iArabicNum > 0:
            for x in range(iArabicNum // value[i]):
                sRomanNum += symbol[i]
                iArabicNum -= value[i]
            i += 1
        return sRomanNum

    def test_toRoman():
        """Function tests comvertion of Arabic Numbers to Roman Numerals.

        Args:

            None

        Returns:

            None
        """
        # all basic symbols are used exactly once
        assert (toRoman(0, 1444) == "MCDXLIV")
