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
        
    def test13(self):
        assert integerToRoman(13) == 'XIII'

    def test14(self):
        assert integerToRoman(14) == 'XIV'

    def test15(self):
        assert integerToRoman(15) == 'XV'
        
    def test16(self):
        assert integerToRoman(16) == 'XVI'

    def test17(self):
        assert integerToRoman(17) == 'XVII'

    def test18(self):
        assert integerToRoman(18) == 'XVIII'
        
    def test19(self):
        assert integerToRoman(19) == 'XIX'

    def test20(self):
        assert integerToRoman(20) == 'XX'

    def test21(self):
        assert integerToRoman(21) == 'XXI'
        
    def test22(self):
        assert integerToRoman(22) == 'XXII'

    def test23(self):
        assert integerToRoman(23) == 'XXIII'

    def test24(self):
        assert integerToRoman(24) == 'XXIV'
    
    def test25(self):
        assert integerToRoman(25) == 'XXV'

    def test26(self):
        assert integerToRoman(26) == 'XXVI'
        
    def test27(self):
        assert integerToRoman(27) == 'XXVII'

    def test28(self):
        assert integerToRoman(28) == 'XXVIII'

    def test29(self):
        assert integerToRoman(29) == 'XXIX'
        
    def test30(self):
        assert integerToRoman(30) == 'XXX'

    def test31(self):
        assert integerToRoman(31) == 'XXXI'

    def test32(self):
        assert integerToRoman(32) == 'XXXII'
        
    def test33(self):
        assert integerToRoman(33) == 'XXXIII'

    def test34(self):
        assert integerToRoman(34) == 'XXXIV'

    def test35(self):
        assert integerToRoman(35) == 'XXXV'

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


