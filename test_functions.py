"""Hlavní modul - Unit testy pro program."""
from unittest import TestCase
import functions
'''Vkládáme TestCase a funkce z jiného kódu'''


class Test_Encode(TestCase):
    """Vytvoření třídy pro kódování."""

    def test_encryptQWERTZU(self):
        """Kódování písmen QWERTZU."""
        self.assertEqual('--.- .-- . .-. - --.. ..-',
                         functions.kodovani('QWERTZU'))
        '''Výsledek a příklad'''

    def test_encryptIOPASDF(self):
        """Kódování písmen IOPASDF."""
        self.assertEqual('.. --- .--. .- ... -.. ..-.',
                         functions.kodovani('IOPASDF'))
        '''Výsledek a příklad'''

    def test_encryptCVBNM(self):
        """Kódování písemn CVBNM a mezery s tečkou."""
        self.assertEqual('-.-. ...- -... -. --  .-.-.-',
                         functions.kodovani('CVBNM .'))

    def test_encryptGHJKLYX(self):
        """Kódování písmen GHJKLYX."""
        inp = "GHJKLYX"
        '''Příklad'''
        expect_out = "--. .... .--- -.- .-.. -.-- -..-"
        '''Výsledek'''
        self.assertEqual(expect_out, functions.kodovani(inp))
        '''Srovnání'''


class Test_Decipher(TestCase):
    """Vytvoření třídy pro dekódování."""

    def test_decryptQWERTZU(self):
        """Dekódování písmen QWERTZU."""
        self.assertEqual('QWERTZU',
                         functions.dekodovani('--.- .-- . .-. - --.. ..-'))
        '''Výsledek a příklad'''

    def test_decryptIOPASDF(self):
        """Dekódování písmen IOPASDF."""
        self.assertEqual('IOPASDF',
                         functions.dekodovani(".. --- .--. .- ... -.. ..-."))
        '''Výsledek a příklad'''

    def test_decryptCVBNM(self):
        """Dekódování písmen CVBNM a mezery s tečkou."""
        self.assertEqual('CVBNM .',
                         functions.dekodovani('-.-. ...- -... -. --  .-.-.-'))
        '''Výsledek a příklad'''

    def test_decryptGHJKLYX(self):
        """Dekódování písemn GHJKLYX."""
        inp = "--. .... .--- -.- .-.. -.-- -..-"
        '''Příklad'''
        expect_out = "GHJKLYX"
        '''Výsledek'''
        self.assertEqual(expect_out, functions.dekodovani(inp))
        '''Srovnání'''
