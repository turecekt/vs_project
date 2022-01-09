"""
Autor: Radek Kratochvíl and Petr Slavík
"""
import unittest
from CetnostZnaku import *


class TestCases(unittest.TestCase):

    def test_PocetKazdyZnakFromFile(self):
        vstup="test_fileMax.txt"
        self.assertEqual(PocetKazdyZnak(vstup), )


if __name__ == '__main__':

    unittest.main()    