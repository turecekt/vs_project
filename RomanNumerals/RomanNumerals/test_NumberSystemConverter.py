import unittest
from NumberSystemConverter import integerToRoman
from NumberSystemConverter import romanToInteger


class Test_test_NumberSystemConverter(unittest.TestCase):

    def test_integerToRoman(self):

        errorMessage = "Input can not be None."

        roman = integerToRoman(None)
        self.assertEqual(roman, errorMessage)

        errorMessage = "Input must be any positive integer from 1 to 3999."

        roman = integerToRoman(0)
        self.assertEqual(roman, errorMessage)

        roman = integerToRoman(4000)
        self.assertEqual(roman, errorMessage)

        roman = integerToRoman(3.5)
        self.assertEqual(roman, errorMessage)

        roman = integerToRoman(1789)
        self.assertEqual(roman, "MDCCLXXXIX")

    def test_romanToInteger(self):

        errorMessage = "Input can not be None."

        integer = romanToInteger(None)
        self.assertEqual(integer, errorMessage)

        errorMessage = "Contains illegal characters."

        integer = romanToInteger("1IV")
        self.assertEqual(integer, errorMessage)

        errorMessage = "Invalid format."

        integer = romanToInteger("IVI")
        self.assertEqual(integer, errorMessage)

        integer = romanToInteger("CCCC")
        self.assertEqual(integer, errorMessage)


if __name__ == '__main__':
    unittest.main()
