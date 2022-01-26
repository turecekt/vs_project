import unittest
import Morseovka

class Test_testmorse(unittest.TestCase):
    #test zakodovani textu
    def test_zakodovani(self):
        assert Morseovka.zakodovani('.-', '....', '---', '.---') == AHOJ
    #test dekodovani textu
    def test_dekodovani(self):
        assert Morseovka.dekodovani(AHOJ) == '.-' '....' '---' '.---'
    #test zakodovani prazdneho vstupu
    def test_zakodovani01(self):
        assert Morseovka.zakodovani("") == ""
    #test dekodovani prazdneho vstupu
    def test_dekodovani01(self):
        assert Morseovka.dekodovani("") == ""

if __name__ == '__main__':
    unittest.main()
