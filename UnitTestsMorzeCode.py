import unittest
from main import encrypt
from main import decrypt


class MyTestCase(unittest.TestCase):
    def testTextToMorseCode(self):
        self.assertEqual(encrypt("Hello world!"), ".... . .-.. .-.. --- .-- --- .-. .-.. -.. --..-- ")

    def testTextToEnglish(self):
        self.assertEqual(decrypt('.... . .-.. .-.. --- .-- --- .-. .-.. -.. --..--'), 'HELLOWORLD!')

    def testErrorsToMorseCode(self):
        self.assertEqual(encrypt("абвгд"), "Invalid data")

    def testErrorsToEnglish(self):
        self.assertEqual(decrypt('...........................'), 'Invalid data')

if __name__ == '__main__':
    unittest.main()