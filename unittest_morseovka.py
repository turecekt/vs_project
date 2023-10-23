"""Unit test pro morseovku."""
import unittest
from morseovka import encrypt, decrypt


class Unittest_morseovka(unittest.TestCase):
    """Trida pro spusteni unit testu."""

    def test_encrypt_pismeno(self):
        """Test prevodu pismene na kod."""
        self.assertEqual(encrypt("T"), "- ")

    def test_encrypt_veta(self):
        """Test prevodu vety na kod."""
        self.assertEqual(encrypt(
            "TESTOVACI VETA"), "- . ... - --- ...- .- -.-. ..  ...- . - .- ")

    def test_encrypt_cislo(self):
        """Test prevodu cisla na kod."""
        self.assertEqual(encrypt(
            "1234567890"), ".---- ..--- ...-- ....- ....."
            " -.... --... ---.. ----. ----- ")

    def test_decrypt_pismeno(self):
        """Test prevodu kodu na pismeno."""
        self.assertEqual(decrypt("-..-"), "X")

    def test_decrypt_text(self):
        """Test prevodu kodu na text."""
        self.assertEqual(decrypt(
            ".--. .-. . ...- --- -..  -. .-  ... .-.."
            " --- ...- ---  --..  -.- --- -.. ..-"),
            "PREVOD NA SLOVO Z KODU")
