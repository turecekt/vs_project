import unittest
import math


class TestMethods(unittest.TestCase):

    def test1(self):
        assert integerroman(1) == 'I'

    def test878(self):
        assert integerroman(0) == ''

    def test871(self):
        assert integerroman(-1) == ''
        
    def test879(self):
        assert integerroman(4000) == ''

    def test2(self):
        assert integerroman(2) == 'II'

    def test3(self):
        assert integerroman(3) == 'III'

    def test4(self):
        assert integerroman(4) == 'IV'

    def test5(self):
        assert integerroman(5) == 'V'

    def test6(self):
        assert integerroman(6) == 'VI'

    def test7(self):
        assert integerroman(7) == 'VII'

    def test8(self):
        assert integerroman(8) == 'VIII'

    def test9(self):
        assert integerroman(9) == 'IX'

    def test10(self):
        assert integerroman(10) == 'X'

    def test11(self):
        assert integerroman(11) == 'XI'

    def test12(self):
        assert integerroman(12) == 'XII'

    def test13(self):
        assert integerroman(13) == 'XIII'

    def test14(self):
        assert integerroman(14) == 'XIV'

    def test15(self):
        assert integerroman(15) == 'XV'

    def test16(self):
        assert integerroman(16) == 'XVI'

    def test17(self):
        assert integerroman(17) == 'XVII'

    def test18(self):
        assert integerroman(18) == 'XVIII'

    def test19(self):
        assert integerroman(19) == 'XIX'

    def test20(self):
        assert integerroman(20) == 'XX'

    def test21(self):
        assert integerroman(21) == 'XXI'

    def test22(self):
        assert integerroman(22) == 'XXII'

    def test23(self):
        assert integerroman(23) == 'XXIII'

    def test24(self):
        assert integerroman(24) == 'XXIV'

    def test25(self):
        assert integerroman(25) == 'XXV'

    def test26(self):
        assert integerroman(26) == 'XXVI'

    def test27(self):
        assert integerroman(27) == 'XXVII'

    def test28(self):
        assert integerroman(28) == 'XXVIII'

    def test29(self):
        assert integerroman(29) == 'XXIX'

    def test30(self):
        assert integerroman(30) == 'XXX'

    def test31(self):
        assert integerroman(31) == 'XXXI'

    def test32(self):
        assert integerroman(32) == 'XXXII'

    def test33(self):
        assert integerroman(33) == 'XXXIII'

    def test34(self):
        assert integerroman(34) == 'XXXIV'

    def test35(self):
        assert integerroman(35) == 'XXXV'

    def test36(self):
        assert integerroman(36) == 'XXXVI'

    def test37(self):
        assert integerroman(37) == 'XXXVII'

    def test38(self):
        assert integerroman(38) == 'XXXVIII'

    def test39(self):
        assert integerroman(39) == 'XXXIX'

    def test40(self):
        assert integerroman(40) == 'XL'

    def test50(self):
        assert integerroman(41) == 'XLI'

    def test51(self):
        assert integerroman(42) == 'XLII'

    def test52(self):
        assert integerroman(43) == 'XLIII'

    def test53(self):
        assert integerroman(44) == 'XLIV'

    def test54(self):
        assert integerroman(45) == 'XLV'

    def test55(self):
        assert integerroman(46) == 'XLVI'

    def test56(self):
        assert integerroman(47) == 'XLVII'

    def test57(self):
        assert integerroman(48) == 'XLVIII'

    def test58(self):
        assert integerroman(49) == 'XLIX'

    def test59(self):
        assert integerroman(50) == 'L'

    def test60(self):
        assert integerroman(51) == 'LI'

    def test61(self):
        assert integerroman(52) == 'LII'

    def test62(self):
        assert integerroman(53) == 'LIII'

    def test63(self):
        assert integerroman(54) == 'LIV'

    def test64(self):
        assert integerroman(55) == 'LV'

    def test65(self):
        assert integerroman(56) == 'LVI'

    def test66(self):
        assert integerroman(57) == 'LVII'

    def test67(self):
        assert integerroman(58) == 'LVIII'

    def test68(self):
        assert integerroman(59) == 'LIX'

    def test69(self):
        assert integerroman(60) == 'LX'

    def test70(self):
        assert integerroman(61) == 'LXI'

    def test71(self):
        assert integerroman(62) == 'LXII'

    def test72(self):
        assert integerroman(63) == 'LXIII'

    def test73(self):
        assert integerroman(64) == 'LXIV'

    def test74(self):
        assert integerroman(65) == 'LXV'

    def test75(self):
        assert integerroman(66) == 'LXVI'

    def test76(self):
        assert integerroman(67) == 'LXVII'

    def test77(self):
        assert integerroman(68) == 'LXVIII'

    def test78(self):
        assert integerroman(69) == 'LXIX'

    def test79(self):
        assert integerroman(70) == 'LXX'


def integerroman(a):

    romansdict = \
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
    while a >= div:
        div *= 10

    div /= 10

    res = ""

    while a:

        #
        lastnum = int(a / div)

        if lastnum <= 3:
            res += (romansdict[div] * lastnum)
        elif lastnum == 4:
            res += (romansdict[div] +
                    romansdict[div * 5])
        elif 5 <= lastnum <= 8:
            res += (romansdict[div * 5] +
                    (romansdict[div] * (lastnum - 5)))
        elif lastnum == 9:
            res += (romansdict[div] +
                    romansdict[div * 10])

        a = math.floor(a % div)
        div /= 10

    return res


# Vlozeni vstupu a vytisknuti vystupu
num1 = int(input("Enter num1: "))
print("Roman Numeral of Integer is:"
      + str(integerroman(num1)))


if __name__ == '__main__':
    unittest.main()
