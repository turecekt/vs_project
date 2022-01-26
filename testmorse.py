import unittest

class Test_testmorse(unittest.TestCase):
    #test zakodovani textu
    def test_zakodovani():
        assert Morseovka.zakodovani('.-', '....', '---', '.---') == AHOJ
    #test dekodovani textu
    def test_dekodovani():
        assert Morseovka.dekodovani(AHOJ) == '.-' '....' '---' '.---'
    #test zakodovani prazdneho vstupu
    def test_zakodovani01():
        assert Morseovka.zakodovani("") == ""
    #test dekodovani prazdneho vstupu
    def test_dekodovani01():
        assert Morseovka.dekodovani("") == ""

if __name__ == '__main__':
    unittest.main()