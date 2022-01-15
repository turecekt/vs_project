""" Unit testy """

from lib2to3.pgen2.literals import test
import unittest


class TEXT_DO_MORS(unittest.TestCase):

    def text_do_mors(self):
        """ Test Codovani jednoducheho textu. """
        source = "Studujem na UTB"
        dst = "... - ..- -.. ..- .--- . -- -. .- ..- - -..."
        self.assertEqual(TEXT_DO_MORS(source), dst)

    def text_do_mors(self):
        """ Test Codovani chybnych znaku. """
        source = "I@I"
        dst = "..{@}.."
        self.assertEqual(TEXT_DO_MORS(source), dst)

    def text_do_mors(self):
        """ Test Codovani prazdneho vstupu. """
        source = ""
        dst = ""
        self.assertEqual(TEXT_DO_MORS(source), dst)

class mors_do_text(unittest.TestCase):
    def mors_do_text(self):
        """ Test Decodovani jednoducheho textu. """
        source = ".--. .-. .. -.. .- .-.. .- ... --- -- .-- --- .-. -.- ..-. .-.. --- .--"
        dst = "Pridala som workflow".upper()
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Decodovani chybnych znaku. """
        source = "../---./.."
        dst = ""
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Decodovani prazdneho vstupu. """
        source = ""
        dst = ""
        self.assertEqual(mors_do_text(source), dst)

    def mors_do_text(self):
        """ Test Decodovani """
        source = " ... -.- ..- ... .- .-.. .- ... --- -- .--. -.-- - .... --- -. .- . .-.. -.-- -.. . -. ... - .- .-.. . ... -.- ..- ... .- -- -.. .- .-.. . .---"
        dst = "hello world".upper()
        self.assertEqual(mors_do_text(source), dst)

    def test_final(self):
        """ Test Codovani a Decodovani vstupu. """
        source = "Skusala som pythona cely den, stale skusam dalej?."
        dst = source.upper()
        self.assertEqual(mors_do_text(TEXT_DO_MORS(source)), dst)

if __name__ == '__main__':
    test()
