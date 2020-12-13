"""Testování source."""
import unittest
import source_test
# Testovácí class


class TestMorseovky(unittest.TestCase):
    """Tato class funguje pro testování našeho source."""

    # PŘEVODY Z ABECEDY DO MORSEOVKY
    def test_1(self):
        """Jen písmena všechna malá."""
        result = source_test.prevod("sos")
        self.assertEqual(result, "... --- ... ")

    def test_2(self):
        """Jen písmena všechna velká."""
        result = source_test.prevod("AHOJ")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_3(self):
        """Kombinace velkých a malých písmen."""
        result = source_test.prevod("AhOj")
        self.assertEqual(result, ".- .... --- .--- ")

    def test_4(self):
        """Jen čísla."""
        result = source_test.prevod("365")
        self.assertEqual(result, "...-- -.... ..... ")

    def test_5(self):
        """Čísla a písmena."""
        result = source_test.prevod("Mam 20 let")
        self.assertEqual(result, "-- .- --   ..--- -----   .-.. . - ")

    # PŘEVODY Z MORSEOVKY DO ABECEDY
    def test_6(self):
        """Jen písmena."""
        result = source_test.prevod(".- .... --- .---")
        self.assertEqual(result, "AHOJ")

    def test_7(self):
        """Jen čísla."""
        result = source_test.prevod("...-- -.... .....")
        self.assertEqual(result, "365")

    def test_8(self):
        """Čísla a písmena."""
        result = source_test.prevod("-- .- -- ..--- ----- .-.. . -")
        self.assertEqual(result, "MAM20LET")

    def test_9(self):
        """Čísla, písmena."""
        result = source_test.prevod("-.. -. . ... -.- .- .--- . .--. ."
                                    " -.- -. -.-- -.. . -. .- .--- . ..--- "
                                    "---.. ... - ..- .--. -. ..-")
        self.assertEqual(result, "DNESKAJEPEKNYDENAJE28STUPNU")

    def test_10(self):
        """Nepovolené znaky na začátku."""
        result = source_test.prevod("?ahoj")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')

    def test_11(self):
        """Nepovolené znaky uprostřed."""
        result = source_test.prevod("ah?oj")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')

    def test_12(self):
        """Nepovolené znaky na konci."""
        result = source_test.prevod("ahoj?")
        self.assertEqual(result, 'Zadaná nesprávná kombince znaků')


if __name__ == '__main__':
    unittest.main()
