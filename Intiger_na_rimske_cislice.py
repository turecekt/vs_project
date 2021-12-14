# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import unittest
import math

class TestMethods(unittest.TestCase):
    
    
    def test1(self):
        assert integerToRoman(5) == 'I'

    def test2(self):
        assert integerToRoman(2) == 'II'

    def test3(self):
        assert integerToRoman(3) == 'III'
        
    def test4(self):
        assert integerToRoman(4) == 'IV'

    def test5(self):
        assert integerToRoman(5) == 'V'

    def test6(self):
        assert integerToRoman(6) == 'VI'
        
    def test7(self):
        assert integerToRoman(7) == 'VII'

    def test8(self):
        assert integerToRoman(8) == 'VIII'

    def test9(self):
        assert integerToRoman(9) == 'IX'
        
    def test10(self):
        assert integerToRoman(10) == 'X'

    def test11(self):
        assert integerToRoman(11) == 'XI'

    def test12(self):
        assert integerToRoman(12) == 'XII'

def integerToRoman(A):
    def test_integer_to_roman(self):
        self.fail()
   #
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

    div = 1
    while A >= div:
        div *= 10

    div /= 10

    res = ""

    while A:

        #
        lastNum = int(A / div)

        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                    romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
                    (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                    romansDict[div * 10])

        A = math.floor(A % div)
        div /= 10

    return res


# Vlozeni vstupu a vytisknuti vystupu
num1 = int(input("Enter num1: "))
print("Roman Numeral of Integer is:"
      + str(integerToRoman(num1)))


