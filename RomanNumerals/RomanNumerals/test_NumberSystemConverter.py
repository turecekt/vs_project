import unittest
from NumberSystemConverter import NumberSystemConverter


class Test_test_NumberSystemConverter(unittest.TestCase):

    def test_integerToRoman(self):

        expectedValue = "Input can not be None."

        roman = NumberSystemConverter.integerToRoman(None)
        self.assertEqual(roman, expectedValue)

        expectedValue = "Input must be any positive integer from 1 to 3999."

        roman = NumberSystemConverter.integerToRoman(3.5)
        self.assertEqual(roman, expectedValue)

        expectedValue = "MDCLXVI"

        roman = NumberSystemConverter.integerToRoman(1666)
        self.assertEqual(roman, expectedValue)

        expectedValue = "CMXCIX"

        roman = NumberSystemConverter.integerToRoman(999)
        self.assertEqual(roman, expectedValue)

        expectedValue = "CDXLIV"

        roman = NumberSystemConverter.integerToRoman(444)
        self.assertEqual(roman, expectedValue)


    def test_romanToInteger(self):

        expectedValue = "Input can not be None."

        integer = NumberSystemConverter.romanToInteger(None)
        self.assertEqual(integer, expectedValue)

        expectedValue = "Contains illegal characters."

        integer = NumberSystemConverter.romanToInteger(1)
        self.assertEqual(integer, expectedValue)
        
        expectedValue = "Invalid format."

        integer = NumberSystemConverter.romanToInteger("MCXIIII")
        self.assertEqual(integer, expectedValue)

        integer = NumberSystemConverter.romanToInteger("IXI")
        self.assertEqual(integer, expectedValue)

        expectedValue = 3888

        integer = NumberSystemConverter.romanToInteger("MMMDCCCLXXXVIII")
        self.assertEqual(integer, expectedValue)

        expectedValue = 999

        integer = NumberSystemConverter.romanToInteger("CMXCIX")
        self.assertEqual(integer, expectedValue)

        expectedValue = 444

        integer = NumberSystemConverter.romanToInteger("CDXLIV")
        self.assertEqual(integer, expectedValue)


if __name__ == "__main__":
    unittest.main()
