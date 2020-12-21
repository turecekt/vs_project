"""Testy na funkci Morseovka"""

import pytest
import morseovka.py


class TestSifrovani(unittest.TestCase):
        """"Testy na funkci Morseovka_na_Text."""""

    def test_sifrovani_1(self):
        """Test testujici string o jednom slove."""

        expected1 = "- . ... - ..--- "
        self.assertEqual(morseovka.Text_na_Morseovku("test1"), expected1)

    def test_sifrovani_2(self):
        """Test testujici string o vice slovech."""

        expected2 = "-.. .-. .-- .... -.-- / - . ... - "
        self.assertEqual(morseovka.Text_na_Morseovku("druhy test"), expected2)


class TestDesifrovani(unittest.TestCase):
        """Testy na funkci Morseovka_na_Text."""

    def test_desifrovani_1(self):
        """Test testujici desifrovani stringu o dvou slovech."""

        expected3 = "TEST PROSEL"
        self.assertEqual(morseovka.Morseovka_na_Text
                         ("- . ... - / .--. .-. --- ... . .-.. "),
                         expected3)

    def test_desifrovani_2(self):
        """Test testujici desifrovani stringu s vice slovy a cisly."""

        expected4 = "TEST DOKONCEN 415 3 5 7"
        self.assertEqual(morseovka.Morseovka_na_Text
                         ("- . ... - / -.. --- -.- --- -. -.-. . -. / "
                          "..... ..--- -.... / ....- / -.... / ---.. "),
                         expected4)
