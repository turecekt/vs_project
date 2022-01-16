###Unit testy.###
import unittest


class RunMorseTest(unittest.TestCase):

    def TEXT_DO_MORS(self):
        """ Test Kodovani jednoducheho textu. """
        src = "Studujem na UTB"
        dst = "... - ..- -.. ..- .--- . -- -. .- ..- - -..."
        self.assertEqual(TEXT_DO_MORS(src), dst)

    def TEXT_DO_MORS(self):
        """ Test Kodovani chybnych znaku. """
""" Unit testy """

from lib2to3.pgen2.literals import test
import unittest


class TEXT_DO_MORS(unittest.TestCase):

    def text_do_mors(self):
        """ Test Kodovani jednoducheho textu. """
        source = "Studujem na UTB"
        dst = "... - ..- -.. ..- .--- . -- -. .- ..- - -..."
        self.assertEqual(TEXT_DO_MORS(source), dst)

    def text_do_mors(self):
        """ Test Kodovani chybnych znaku. """
        source = "I@I"
        dst = "..{@}.."
        self.assertEqual(TEXT_DO_MORS(source), dst)

    def text_do_mors(self):
        """ Test Kodovani prazdneho vstupu. """
        source = ""
        dst = ""
        self.assertEqual(TEXT_DO_MORS(source), dst)

class mors_do_text(unittest.TestCase):
    def mors_do_text(self):
        """ Test Dekodovani jednoducheho textu. """
        source = ".--. .-. .. -.. .- .-.. .- ... --- -- .-- --- .-. -.- ..-. .-.. --- .--"
        dst = "Pridala som workflow".upper()
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Dekodovani chybnych znaku. """
        source = "../---./.."
        dst = ""
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Dekodovani prazdneho vstupu. """
        source = ""
        dst = ""
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Dekodovani """
        source = " ... -.- ..- ... .- .-.. .- ... --- -- .--. -.-- - .... --- -. .- . .-.. -.-- -.. . -. ... - .- .-.. . ... -.- ..- ... .- -- -.. .- .-.. . .---"
        dst = "hello world".upper()
        self.assertEqual(mors_do_text(source), dst)

    def test_final(self):
        """ Test Kodovani a Dekodovani vstupu. """
        source = "Skusala som pythona cely den, stale skusam dalej?."
        dst = source.upper()
        self.assertEqual(mors_do_text(TEXT_DO_MORS(source)), dst)

if __name__ == '__main__':
    test()