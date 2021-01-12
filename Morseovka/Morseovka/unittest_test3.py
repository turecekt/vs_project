"""Unittesty."""

import unittest
from Morseovka import TextToMorse
from Morseovka import MorseToText


# text na Moresuv kod
class Test(unittest.TestCase):
    """Vytvoreni classu unittest."""

    def test_prelozeni(self):
        """Test prevodu textu do kodu morse."""
        self.assertEqual(TextToMorse('asd'), ' .- ... -..')

    def test_spravnych_symbolu(self):
        """Test na zobrazeni spatnych symbolu."""
        self.assertEqual(TextToMorse('!`@#$%^&()+='), 'nespravne znaky')

    def test_prazdneho_pole(self):
        """Test na kontrolu prazdneho pole."""
        self.assertEqual(TextToMorse(''), 'prazdne pole')


# Moresuv kod na text
class Test1(unittest.TestCase):
    """Vytvoreni classu unittest."""

    def test_prelozeni(self):
        """Test na prelozeni kodu morse do textu."""
        self.assertEqual(MorseToText(['...', '---', '...']), 'sos')

    def test_textu_v_sp(self):
        """Test na srovnani morse kodu se slovnikem."""
        self.assertEqual(MorseToText(['----------']),
                         'chyba pri zadavani znaku')

    def test_spravnych_symbolu(self):
        """Test na zobrazeni spatnych symbolu."""
        self.assertEqual(MorseToText(['!@#$%^&()+']), 'nespravne znaky')

    def test_prazdneho_pole(self):
        """Test na kontrolu prazdneho pole."""
        self.assertEqual(MorseToText(''), 'prazdne pole')


if __name__ == '__main__':
    unittest.main()
