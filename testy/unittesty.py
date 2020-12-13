"""Testování source."""
import unittest
import source_test


# Testovácí class
class TestMorseovky(unittest.TestCase):

    # PŘEVODY Z ABECEDY DO MORSEOVKY
    def test_1(self):
    """jen písmena všechna mala."""
        result = source_test.prevod("sos")
        self.assertEqual(result, "... --- ... ")

    def test_2(self):
        """jen písmena všechna velká."""
        result = source_test.prevod("AHOJ")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_3(self):
        """kombinace velkých a malých písmen."""
        result = source_test.prevod("AhOj")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_4(self):
        """jen čísla."""
        result = source_test.prevod("365")
        self.assertEqual(result, "...-- -.... ..... ")

    def test_5(self):
        """čísla a písmena."""
        result = source_test.prevod("Mam 20 let")
        self.assertEqual(result, "-- .- --   ..--- -----   .-.. . - ")

    # PŘEVODY Z MORSEOVKY DO ABECEDY
    def test_6(self):
        """jen písmena."""
        result = source_test.prevod(".- .... --- .---")
        self.assertEqual(result, "AHOJ")

    def test_7(self):
        """jen čísla."""
        result = source_test.prevod("...-- -.... .....")
        self.assertEqual(result, "365")

    def test_8(self):
        """čísla a písmena."""
        result = source_test.prevod("-- .- -- ..--- ----- .-.. . -")
        self.assertEqual(result, "MAM20LET")


if __name__ == '__main__':
    unittest.main()
