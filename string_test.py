"""Unittest pro prekladac morseovky."""

import unittest

SLOVNIK_MORSEOVKA = {"A": ".-", "B": "-...",
                     "C": "-.-.", "D": "-..", "E": ".",
                     "F": "..-.", "G": "--.", "H": "....",
                     "I": "..", "J": ".---", "K": "-.-",
                     "L": ".-..", "M": "--", "N": "-.",
                     "O": "---", "P": ".--.", "Q": "--.-",
                     "R": ".-.", "S": "...", "T": "-",
                     "U": "..-", "V": "...-", "W": ".--",
                     "X": "-..-", "Y": "-.--", "Z": "--..",
                     "1": ".----", "2": "..---", "3": "...--",
                     "4": "....-", "5": ".....", "6": "-....",
                     "7": "--...", "8": "---..", "9": "----.",
                     "0": "-----", ", ": "--..--", ".": ".-.-.-",
                     "?": "..--..", "/": "-..-.", "-": "-....-",
                     "(": "-.--.", ")": "-.--.-"}


class TestMorseovka(unittest.TestCase):
    """Tato trida funguje jako testovaci trida."""

    def test_3(texttocode):
        """Testovani prekladu do morseovky."""
        text = str(input="Ahoj")
        [SLOVNIK_MORSEOVKA[i.upper()]
         + " " for i in text if i.upper() in SLOVNIK_MORSEOVKA.keys()]
        texttocode.assertTrue("-. --- -. . ")
        texttocode.assertFalse("--. --. .. .")
        texttocode.assertThat(morseovka="-. --- -. . ")

    def test_1(self):
        """Testovani zvetsovani pismen."""
        self.asserEqual("abc".upper(), "ABC")
        self.assertTrue("ABC".isupper())
        self.assertFalse("Abc".isupper())

    def test_2(self):
        """Prevod na rozlozeni textu."""
        s = "miroslav olivik"
        self.assertEqual(s.split(), ["miroslav", "olivik"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "main":
    unittest.main()
