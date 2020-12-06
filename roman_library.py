"""This module works with Roman Numerals.

The module supplies one function: toRoman(self, iArabicNum). For example,

>>> toRoman(10)
X
"""


class roman_lib:
    """The main class for converting between Arabic Numbers and Roman Numerals.

    It can be upgraded in the future
    """

    def toRoman(iArabicNum):
        """Convert Arabic Numbers to Roman Numerals.

        Args:
            iArabicNum (int): an integer
        Returns:
            sRomanNum (str): a string of Roman Numerals
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
