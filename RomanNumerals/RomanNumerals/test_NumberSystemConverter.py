import unittest
from NumberSystemConverter import integerToRoman
from NumberSystemConverter import romanToInteger
from NumberSystemConverter import valueOf
from NumberSystemConverter import getHighestUsableNumeralAfter


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

        expectedValue = "MDCLXVI"

        roman = integerToRoman(1666)
        self.assertEqual(roman, expectedValue)

        expectedValue = "CMXCIX"

        roman = integerToRoman(999)
        self.assertEqual(roman, expectedValue)

        expectedValue = "CDXLIV"

        roman = integerToRoman(444)
        self.assertEqual(roman, expectedValue)


    def test_romanToInteger(self):

        expectedValue = "Input can not be None."

        integer = romanToInteger(None)
        self.assertEqual(integer, expectedValue)

        expectedValue = "Contains illegal characters."

        integer = romanToInteger(1)
        self.assertEqual(integer, expectedValue)

        integer = romanToInteger("P")
        self.assertEqual(integer, expectedValue)

        expectedValue = "Invalid format."

        integer = romanToInteger("CCM")
        self.assertEqual(integer, expectedValue)

        integer = romanToInteger("XCL")
        self.assertEqual(integer, expectedValue)

        expectedValue = 1500

        integer = romanToInteger("MD")
        self.assertEqual(integer, expectedValue)


    def test_valueOf(self):

        self.assertEqual(valueOf(None), 0)
        self.assertEqual(valueOf("I"), 1)
        self.assertEqual(valueOf("II"), 2)
        self.assertEqual(valueOf("III"), 3)
        self.assertEqual(valueOf("IV"), 4)
        self.assertEqual(valueOf("V"), 5)
        self.assertEqual(valueOf("IX"), 9)
        self.assertEqual(valueOf("X"), 10)
        self.assertEqual(valueOf("XX"), 20)
        self.assertEqual(valueOf("XXX"), 30)
        self.assertEqual(valueOf("XL"), 40)
        self.assertEqual(valueOf("L"), 50)
        self.assertEqual(valueOf("XC"), 90)
        self.assertEqual(valueOf("C"), 100)
        self.assertEqual(valueOf("CC"), 200)
        self.assertEqual(valueOf("CCC"), 300)
        self.assertEqual(valueOf("CD"), 400)
        self.assertEqual(valueOf("D"), 500)
        self.assertEqual(valueOf("CM"), 900)
        self.assertEqual(valueOf("M"), 1000)
        self.assertEqual(valueOf("MM"), 2000)
        self.assertEqual(valueOf("MMM"), 3000)


    def test_getHighestUsableNumeralAfter(self):

        self.assertEqual(getHighestUsableNumeralAfter(1000), 900)
        self.assertEqual(getHighestUsableNumeralAfter(900), 90)
        self.assertEqual(getHighestUsableNumeralAfter(500), 300)
        self.assertEqual(getHighestUsableNumeralAfter(100), 90)
        self.assertEqual(getHighestUsableNumeralAfter(90), 9)
        self.assertEqual(getHighestUsableNumeralAfter(50), 30)
        self.assertEqual(getHighestUsableNumeralAfter(10), 9)
        self.assertEqual(getHighestUsableNumeralAfter(9), 0)
        self.assertEqual(getHighestUsableNumeralAfter(5), 3)
        self.assertEqual(getHighestUsableNumeralAfter(1), 0)
        self.assertEqual(getHighestUsableNumeralAfter(None), 0)
        self.assertEqual(getHighestUsableNumeralAfter("I"), 0)
        self.assertEqual(getHighestUsableNumeralAfter(4000), 0)


#if __name__ == '__main__':
#    unittest.main()
