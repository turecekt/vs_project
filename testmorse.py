import unittest
import Morseovka

class Test_testmorse(unittest.TestCase):
    #test zakodovani textu
    def test_zakodovani(self):
        self.Morseovka.zakodovani('.-', '....', '---', '.---') == AHOJ
    #test dekodovani textu
    def test_dekodovani(self):
        self.Morseovka.dekodovani(AHOJ) == '.-' '....' '---' '.---'
    #test zakodovani prazdneho vstupu
    def test_zakodovani01(self):
        self.Morseovka.zakodovani("") == ""
    #test dekodovani prazdneho vstupu
    def test_dekodovani01(self):
        self.Morseovka.dekodovani("") == ""

if __name__ == '__main__':
    unittest.main()
