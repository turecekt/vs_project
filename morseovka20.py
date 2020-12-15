import unittest

from main import odmorzeovky, domorzeovky


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(odmorzeovky("----."), '9')

    def test1(self):
        self.assertEqual(domorzeovky('9'), "----.")

    def test2(self):
        self.assertEqual(odmorzeovky("---.."), '8')

    def test3(self):
        self.assertEqual(domorzeovky('8'), "---..")

    def test4(self):
        self.assertEqual(odmorzeovky("--..."), '7')

    def test5(self):
        self.assertEqual(domorzeovky('7'), "--...")

    def test6(self):
        self.assertEqual(odmorzeovky("-...."), '6')

    def test7(self):
        self.assertEqual(domorzeovky('6'), "-....")

    def test8(self):
        self.assertEqual(odmorzeovky("....."), '5')

    def test9(self):
        self.assertEqual(domorzeovky('5'), ".....")

    def test10(self):
        self.assertEqual(odmorzeovky("....-"), '4')

    def test11(self):
        self.assertEqual(domorzeovky('4'), "....-")

    def test12(self):
        self.assertEqual(odmorzeovky("...--"), '3')

    def test13(self):
        self.assertEqual(domorzeovky('3'), "...--")

    def test14(self):
        self.assertEqual(odmorzeovky("..---"), '2')

    def test15(self):
        self.assertEqual(domorzeovky('2'), "..---")

    def test16(self):
        self.assertEqual(odmorzeovky(".----"), '1')

    def test17(self):
        self.assertEqual(domorzeovky('1'), ".----")

    def test00(self):
        self.assertEqual(odmorzeovky("-----"), '0')

    def test0(self):
        self.assertEqual(domorzeovky('0'), "-----")

    def test18(self):
        self.assertEqual(odmorzeovky("--.."), 'z')

    def test19(self):
        self.assertEqual(domorzeovky('z'), "--..")

    def test20(self):
        self.assertEqual(odmorzeovky("-.--"), 'y')

    def test21(self):
        self.assertEqual(domorzeovky('y'), "-.--")

    def test22(self):
        self.assertEqual(odmorzeovky("-..-"), 'x')

    def test23(self):
        self.assertEqual(domorzeovky('x'), "-..-")

    def test24(self):
        self.assertEqual(odmorzeovky(".--"), 'w')

    def test25(self):
        self.assertEqual(domorzeovky('w'), ".--")

    def test26(self):
        self.assertEqual(odmorzeovky("...-"), 'v')

    def test27(self):
        self.assertEqual(domorzeovky('v'), "...-")

    def test28(self):
        self.assertEqual(odmorzeovky("..-"), 'u')

    def test29(self):
        self.assertEqual(domorzeovky('u'), "..-")

    def test30(self):
        self.assertEqual(odmorzeovky("-"), 't')

    def test31(self):
        self.assertEqual(domorzeovky('t'), "-")

    def test32(self):
        self.assertEqual(odmorzeovky("..."), 's')

    def test33(self):
        self.assertEqual(domorzeovky('s'), "...")

    def test34(self):
        self.assertEqual(odmorzeovky(".-."), 'r')

    def test35(self):
        self.assertEqual(domorzeovky('r'), ".-.")

    def test36(self):
        self.assertEqual(odmorzeovky("--.-"), 'q')

    def test37(self):
        self.assertEqual(domorzeovky('q'), "--.-")

    def test38(self):
        self.assertEqual(odmorzeovky(".--."), 'p')

    def test39(self):
        self.assertEqual(domorzeovky('p'), ".--.")

    def test40(self):
        self.assertEqual(odmorzeovky("---"), 'o')

    def test41(self):
        self.assertEqual(domorzeovky('o'), "---")

    def test42(self):
        self.assertEqual(odmorzeovky("-."), 'n')

    def test43(self):
        self.assertEqual(domorzeovky('n'), "-.")

    def test44(self):
        self.assertEqual(odmorzeovky("--"), 'm')

    def test45(self):
        self.assertEqual(domorzeovky('m'), "--")

    def test46(self):
        self.assertEqual(odmorzeovky(".-.."), 'l')

    def test47(self):
        self.assertEqual(domorzeovky('l'), ".-..")

    def test48(self):
        self.assertEqual(odmorzeovky("-.-"), 'k')

    def test49(self):
        self.assertEqual(domorzeovky('k'), "-.-")

    def test50(self):
        self.assertEqual(odmorzeovky(".---"), 'j')

    def test51(self):
        self.assertEqual(domorzeovky('j'), ".---")

    def test52(self):
        self.assertEqual(odmorzeovky(".."), 'i')

    def test53(self):
        self.assertEqual(domorzeovky('i'), "..")

    def test54(self):
        self.assertEqual(odmorzeovky("...."), 'h')

    def test55(self):
        self.assertEqual(domorzeovky('h'), "....")

    def test56(self):
        self.assertEqual(odmorzeovky("--."), 'g')

    def test57(self):
        self.assertEqual(domorzeovky('g'), "--.")

    def test58(self):
        self.assertEqual(odmorzeovky("..-."), 'f')

    def test59(self):
        self.assertEqual(domorzeovky('f'), "..-.")

    def test60(self):
        self.assertEqual(odmorzeovky("."), 'e')

    def test61(self):
        self.assertEqual(domorzeovky('e'), ".")

    def test62(self):
        self.assertEqual(odmorzeovky("-.."), 'd')

    def test63(self):
        self.assertEqual(domorzeovky('d'), "-..")

    def test64(self):
        self.assertEqual(odmorzeovky("-.-."), 'c')

    def test65(self):
        self.assertEqual(domorzeovky('c'), "-.-.")

    def test66(self):
        self.assertEqual(odmorzeovky("-..."), 'b')

    def test67(self):
        self.assertEqual(domorzeovky('b'), "-...")

    def test68(self):
        self.assertEqual(odmorzeovky(".-"), 'a')

    def test69(self):
        self.assertEqual(domorzeovky('a'), ".-")


if __name__ == '__main__':
    unittest.main()
