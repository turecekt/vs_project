# 16.12.2021
""" Unit testy """

import unittest
from morse import frommorse, tomorse


class RunMorseTest(unittest.TestCase):

    def test_tomorse01(self):
        """ Test Codovani jednoducheho textu. """
        src = "hello world"
        dst = "...././.-../.-../---/,/.--/---/.-./.-../-.."
        self.assertEqual(tomorse(src), dst)

    def test_tomorse02(self):
        """ Test Codovani chybnych znaku. """
        src = "I@I"
        dst = "../{@}/.."
        self.assertEqual(tomorse(src), dst)

    def test_tomorse03(self):
        """ Test Codovani prazdneho vstupu. """
        src = ""
        dst = ""
        self.assertEqual(tomorse(src), dst)

    def test_frommorse01(self):
        """ Test Decodovani jednoducheho textu. """
        src = "...././.-../.-../---/,/.--/---/.-./.-../-.."
        dst = "hello world".upper()
        self.assertEqual(frommorse(src), dst)

    def test_frommorse02(self):
        """ Test Decodovani chybnych znaku. """
        src = "../---./.."
        dst = "I{---.}I"
        self.assertEqual(frommorse(src), dst)

    def test_frommorse03(self):
        """ Test Decodovani chybnych lomitek. """
        dst = "SOS"
        # vice lomitek mezi znaky
        src = "...//---///..."
        self.assertEqual(frommorse(src), dst)
        # lomitka na konci a na zacatku textu
        src = "/.../---/...///"
        self.assertEqual(frommorse(src), dst)

    def test_frommorse04(self):
        """ Test Decodovani prazdneho vstupu. """
        src = ""
        dst = ""
        self.assertEqual(frommorse(src), dst)

    def test_frommorse05(self):
        """ Test Decodovani vstupu se znaky ' ' a '\n'. """
        src = " ... ./. /\n.-../.-../---/, /.--/---/.-./.\n-../-..\n"
        dst = "hello world".upper()
        self.assertEqual(frommorse(src), dst)

    def test_final(self):
        """ Test Codovani a Decodovani vstupu. """
        src = "There is no elevator to success, you have to take the stairs."
        dst = src.upper()
        self.assertEqual(frommorse(tomorse(src)), dst)


if __name__ == '__main__':
    unittest.main()
