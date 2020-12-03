"""Unit testy na kontrolu hlavních funkcí."""
import unittest
import source.main


class TestSifrovani(unittest.TestCase):
    """Sloka testů na funkci sifrovani_morse."""

    def test_sifrovani_1(self):
        """Test testující string o jednom slově."""
        expected1 = "- . ... - ..--- "
        self.assertEqual(source.main.sifrovani_morse("test1"), expected1)

    def test_sifrovani_2(self):
        """Test testující string o více slovech."""
        expected2 = "-.. .-. .-- .... -.-- / - . ... - "
        self.assertEqual(source.main.sifrovani_morse("druhy test"), expected2)


class TestDesifrovani(unittest.TestCase):
    """Sloka testů na funcki desifrovani_morse."""

    def test_desifrovani_1(self):
        """Test testující dešifrování stringu o dvou slovech."""
        expected3 = "TEST PROSEL"
        self.assertEqual(source.main.desifrovani_morse
                         ("- . ... - / .--. .-. --- ... . .-.. "),
                         expected3)

    def test_desifrovani_2(self):
        """Test testující dešifrování stringu s více slovy a čísly."""
        expected4 = "TEST DOKONCEN 415 3 5 7"
        self.assertEqual(source.main.desifrovani_morse
                         ("- . ... - / -.. --- -.- --- -. -.-. . -. / "
                          "..... ..--- -.... / ....- / -.... / ---.. "),
                         expected4)
