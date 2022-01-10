"""Authors: Radek Kratochvíl and Petr Slavík"""
import unittest
from CetnostZnaku import *


class TestCases(unittest.TestCase):

    def test_PocetZnak(self):                   ###    test počtu znaků ve vstupním textu, kdy povinný atribut #(hash) není brán jako znak    ###

        vstup = "AAAAAAAA#"
        self.assertEqual(PocetZnak(vstup), 8)


    def test_PocetZnak(self):                   ###    test počtu znaků ve vstupním souboru, kdy povinný atribut #(hash) není brán jako znak    ###

        vstup = "test_file.txt"
        self.assertEqual(PocetZnak(vstup),0)




    def test_MinZnak(self):                       ###   test informace o minimálním počtu znaků ve vstupním textu ###
    
        vstup = "Python ma jen jednou X Y Z a mozna jeste nejaka dalsi pismena #"        
        self.assertEqual(MinZnak(vstup), ['H', 'U', 'X', 'K', 'L', '#'])



    def test_MinZnakNoHash(self):               ###     test informace o minimálním počtu znaků ve vstupním textu bez povinného atributu #(hash)    ###

        vstup = ""
        self.assertEqual(MinZnak(vstup), 0)



    def test_MaxZnakText(self):                 ###     test informace o maximálním počtu znaků ve vstupním textu   ###

        vstup = "Python ma spustu AAAAAAA#"
        self.assertEqual(MaxZnak(vstup), ['A'])

    
    
    
    def test_MaxZnakFile(self):                 ###     test informace o maximálním počtu znaků ve vstupním souboru   ###
    
        vstup = "test_fileMax.txt"
        self.assertEqual(MaxZnak(vstup), ['A'])

    

    def test_MinZnakNoHashinFile(self):         ###     test informace o minimálním počtu znaků ve vstupním souboru bez povinného atributu #(hash)    ###
    
        vstup = "test_file.txt"
        self.assertEqual(MinZnak(vstup),0)

    """test funkce ktera vypise pocet kazdeho znaku z vlozeneho file"""
    def test_PocetKazdyZnakInFile(self):       
        vstup="test_filePocet.txt"
        self.assertEqual(PocetKazdyZnak(vstup),{'T': 5, 'E': 4, 'X': 1, 'P': 2, 'R': 1, 'O': 2, 'S': 1, 'F': 1, 'N': 2, 'C': 2, 'K': 2, 'A': 2, 'Z': 2, 'D': 1, 'Y': 1, '#': 1})

    """test funkce ktera vypise pocet kazdeho znaku z vlozeneho textu"""
    def test_PocetKazdyZnakInText(self):       
        vstup="Python max znaku#"
        self.assertEqual(PocetKazdyZnak(vstup),{'P': 1, 'Y': 1, 'T': 1, 'H': 1, 'O': 1, 'N': 2, 'M': 1, 'A': 2, 'X': 1, 'Z': 1, 'K': 1, 'U': 1, '#': 1})

if __name__ == '__main__':

    unittest.main()    