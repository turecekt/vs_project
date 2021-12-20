"""Unit Tests Code."""

import unittest
from main import encrypt
from main import decrypt


class MyTestCase(unittest.TestCase):
    """Class of Unit Tests."""

    def testTextToMorseCode(self):
        """Checking Morse Code Encoding."""
        self.assertEqual(encrypt("Hello world!"),
                         ".... . .-.. .-.. --- .-- --- .-. .-.. -.. --..-- ")

    def testTextToEnglish(self):
        """Checking Endlish Encoding."""
        self.assertEqual(decrypt
                         (".... . .-.. .-.. --- .-- --- .-. .-.. -.. --..--"),
                         "HELLOWORLD!")

    def testErrorsToMorseCode(self):
        """Error checking when encoding Morse code."""
        self.assertEqual(encrypt("абвгд"), "Invalid data")

    def testErrorsToEnglish(self):
        """Error checking when encoding English."""
        self.assertEqual(decrypt('..........................'), 'Invalid data')


if __name__ == '__main__':
    unittest.main()
