import unittest
from NumberSystemConverter import integerToRoman
from NumberSystemConverter import romanToInteger
from NumberSystemConverter import valueOf


class Test_test_NumberSystemConverter(unittest.TestCase):

    def test_integerToRoman(self):

        expectedValue = "Input can not be None."

        roman = integerToRoman(None)
        self.assertEqual(roman, expectedValue)

        expectedValue = "Input must be any positive integer from 1 to 3999."

        roman = integerToRoman(0)
        self.assertEqual(roman, expectedValue)

        roman = integerToRoman(4000)
        self.assertEqual(roman, expectedValue)

        roman = integerToRoman(3.5)
        self.assertEqual(roman, expectedValue)

        expectedValue = "MDCCLXXXIX"

        roman = integerToRoman(1789)
        self.assertEqual(roman, expectedValue)

    def test_romanToInteger(self):

        expectedValue = "Input can not be None."

        integer = romanToInteger(None)
        self.assertEqual(integer, expectedValue)

        expectedValue = "Contains illegal characters."

        integer = romanToInteger("1IV")
        self.assertEqual(integer, expectedValue)

        expectedValue = "Invalid format."

        integer = romanToInteger("IVI")
        self.assertEqual(integer, expectedValue)

        integer = romanToInteger("CCCC")
        self.assertEqual(integer, expectedValue)

    def test_valueOf(self):

        expectedValue = 0

        integer = valueOf(None)
        self.assertEqual(integer, expectedValue)

        integer = valueOf(1)
        self.assertEqual(integer, expectedValue)

        integer = valueOf("P")
        self.assertEqual(integer, expectedValue)

        integer = valueOf("i")
        self.assertEqual(integer, expectedValue)

        integer = valueOf("CCCC")
        self.assertEqual(integer, expectedValue)

        integer = valueOf("IC")
        self.assertEqual(integer, expectedValue)

        integer = valueOf("CX")
        self.assertEqual(integer, expectedValue)

        expectedValue = 90

        integer = valueOf("XC")
        self.assertEqual(integer, expectedValue)


if __name__ == '__main__':
    unittest.main()
