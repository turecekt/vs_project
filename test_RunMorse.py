"""Zacatek Unit testu."""
import unittest
from RunMorse import encrypt
from RunMorse import decrypt


class RunMorseTest(unittest.TestCase):
    """Spusteni testu."""

    def test_encrypt(self):
        """Unittest 'encrypt' textu s mezerami."""
        self.assertEqual(
            encrypt("there is some text"),
            "- .... . .-. . / .. ... / "
            "... --- -- . / - . -..- - ")

    def test_decrypt(self):
        """Unittest 'decrypt' morseovky."""
        self.assertEqual(
            decrypt(". .-.. -.. -.. .- "
                    "-. ... ..- .-. .. -. "),
            "elddansurin ")

    def test_decrypt1(self):
        """Unittest 'decrypt' morseovky s mezerami."""
        self.assertEqual(decrypt(
            "- .... . / -- .- - .-. .. -..- "),
            "the matrix ")


if __name__ == '__main__':
    unittest.main()
