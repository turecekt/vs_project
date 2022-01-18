import unittest
from main import kodovat, dekodovat

class Unittest_morseovka(unittest.TestCase):
    """Trida pro spusteni unit testu."""

    def test_kodovat_pismeno(self):
        """Test pro převod písmena na kod."""
        self.assertEqual(kodovat("A"), ".- ")

    def test_kodovat_veta(self):
        """Test pro převodu vety do morseovky"""
        self.assertEqual(kodovat(
            "MORSEOVKA"), "-- --- .-. ... . --- ...- -.- .- ")

    def test_kodovat_cislo(self):
        """Test pro převod číslic do morseovky."""
        self.assertEqual(kodovat(
            "1234567890"), ".---- ..--- ...-- ....- ....."
            " -.... --... ---.. ----. ----- ")

    def test_dekodovat_pismeno(self):
        """Test pro morseovky na pismeno."""
        self.assertEqual(dekodovat("-.--"), "Y")

    def test_dekodovat_text(self):
        """Test pro převod morseovky do textové věty."""
        self.assertEqual(dekodovat(
            ".--. .-. . ...- --- -..  -. .-  ... .-.."
            " --- ...- ---  --..  -.- --- -.. ..-"),
            "PREVOD NA SLOVO Z KODU")
