import unittest
from NumberSystemConverter import *

class Test_test_NumberSystemConverter(unittest.TestCase):

    def test_integerToRoman(self):

        wrongInputMessage = "Input must be any positive integer from 1 to 3999."

        roman = integerToRoman(0)
        self.assertEqual(roman, wrongInputMessage)

        roman = integerToRoman(4000)
        self.assertEqual(roman, wrongInputMessage)

        roman = integerToRoman(3.5)
        self.assertEqual(roman, wrongInputMessage)
        
        roman = integerToRoman(1789)
        self.assertEqual(roman, "MDCCLXXXIX")


    def test_romanToInteger(self):
        
        wrongInputMessage = "Obsahuje nepovolene znaky."
        
        integer = romanToInteger("1IV")
        self.assertEqual(integer, wrongInputMessage)


        wrongInputMessage = "Cislo je ve spatnem tvaru."
        
        integer = romanToInteger("IVI")
        self.assertEqual(integer, wrongInputMessage)

        integer = romanToInteger("CCCC")
        self.assertEqual(integer, wrongInputMessage)


if __name__ == '__main__':
    unittest.main()
