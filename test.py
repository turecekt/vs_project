from unittest import TestCase
import functions


class Test_Encode(TestCase):
    def test_encryptShortWord(self):
        self.assertEqual('--.. -.- --- ..- ... -.- .-',
                         functions.kodovani('ZKOUSKA'))

    def test_encryptLongWord(self):
        self.assertEqual('.- -. --- ..--..',
                         functions.kodovani('ANO?'))

    def test_encryptSentence(self):
        inp = "NEBO NE."
        expect_out = "-. . -... ---  -. . .-.-.-"
        self.assertEqual(expect_out, functions.kodovani(inp))


class Test_Decipher(TestCase):
    def test_decryptShortWord(self):
        self.assertEqual('ZKOUSKA',
                         functions.dekodovani('--.. -.- --- ..- ... -.- .-'))

    def test_decryptLongWord(self):
        self.assertEqual('ANO?', functions.dekodovani(".- -. --- ..--.."))

    def test_decryptSentence(self):
        inp = "-. . -... ---  -. . .-.-.-"
        expect_out = "NEBO NE."
        self.assertEqual(expect_out, functions.dekodovani(inp))
