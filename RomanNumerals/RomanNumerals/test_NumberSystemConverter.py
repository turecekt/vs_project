import unittest
from NumberSystemConverter import *

class Test_test_NumberSystemConverter(unittest.TestCase):

    def test_integerToRoman(self):

        wrongInputMessage = "Input must be any positive integer from 1 to 3999."

        roman = NumberSystemConverter.integerToRoman(0)
        self.assertEqual(roman, wrongInputMessage)

        roman = NumberSystemConverter.integerToRoman(4000)
        self.assertEqual(roman, wrongInputMessage)

        roman = NumberSystemConverter.integerToRoman(3.5)
        self.assertEqual(roman, wrongInputMessage)
        
        roman = NumberSystemConverter.integerToRoman(1789)
        self.assertEqual(roman, "MDCCLXXXIX")


    def test_romanToInteger(self):
        
        wrongInputMessage = "Obsahuje nepovolene znaky."
        
        integer = NumberSystemConverter.romanToInteger("1IV")
        self.assertEqual(integer, wrongInputMessage)


        wrongInputMessage = "Cislo je ve spatnem tvaru."
        
        integer = NumberSystemConverter.romanToInteger("IVI")
        self.assertEqual(integer, wrongInputMessage)

        integer = NumberSystemConverter.romanToInteger("CCCC")
        self.assertEqual(integer, wrongInputMessage)


if __name__ == '__main__':
    unittest.main()
