"""Unit test for MorseCode."""
import unittest
from morse import MorseCodeTranslator


class TestMorseCodeTranslator(unittest.TestCase):
    """Unit tests."""
    # Morse code to text
    def test_morse_to_text_no_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ""
        expected_output = "You must provide a string of text to translate"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_numbers(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_punctuation(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".-... .--.-. -.--.- -.--. -...- -.-.-- -....- .-.-. ..--.."
        x = "&@)(=!-+?"
        self.assertEqual(translator.translate_morse(morse), x)

    def test_morse_to_text_not_strict(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.translate_morse(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Unable to translate morse code(4spaces)."
        )
        self.assertEqual(
            translator.translate_morse(morse, strict=True), expected_output
        )

    # Text to morse code
    def test_text_to_morse_no_text(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = ""
        expected_output = "You must provide a morse code string to translate"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_text_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_numbers_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "1234567890"
        exp_out = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        self.assertEqual(translator.translate_text(text), exp_out)

    def test_punctuation_to_morse(self):
        """Unit tests."""
        translator = MorseCodeTranslator()
        text = "&@)(=!-+?"
        x = ".-... .--.-. -.--.- -.--. -...- -.-.-- -....- .-.-. ..--.."
        self.assertEqual(translator.translate_text(text), x)


if __name__ == "__main__":
    unittest.main()
