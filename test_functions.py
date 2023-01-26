from unittest import TestCase
import functions


class Test_Encode(TestCase):
    def test_encryptShortWord(self):
        self.assertEqual('--.- .-- . .-. - --.. ..-',
                         functions.kodovani('QWERTZU'))

    def test_encryptLongWord(self):
        self.assertEqual('.. --- .--. .- ... -.. ..-.',
                         functions.kodovani('IOPASDF'))

    def test_encryptLongWord(self):
        self.assertEqual('-.-. ...- -... -. --  .-.-.-',
                         functions.kodovani('CVBNM .'))

    def test_encryptSentence(self):
        inp = "GHJKLYX"
        expect_out = "--. .... .--- -.- .-.. -.-- -..-"
        self.assertEqual(expect_out, functions.kodovani(inp))


class Test_Decipher(TestCase):
    def test_decryptShortWord(self):
        self.assertEqual('QWERTZU',
                         functions.dekodovani('--.- .-- . .-. - --.. ..-'))

    def test_decryptLongWord(self):
        self.assertEqual('IOPASDF',
                         functions.dekodovani(".. --- .--. .- ... -.. ..-."))

    def test_decryptShortWord(self):
        self.assertEqual('CVBNM .',
                         functions.dekodovani('-.-. ...- -... -. --  .-.-.-'))

    def test_decryptSentence(self):
        inp = "--. .... .--- -.- .-.. -.-- -..-"
        expect_out = "GHJKLYX"
        self.assertEqual(expect_out, functions.dekodovani(inp))
