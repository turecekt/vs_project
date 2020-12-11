"""Unit testy."""

import unittest

import morse


class Test(unittest.TestCase):
    """Class tests."""

    def test_sifrovani(self):
        """Unit test pro sifrovaci funkci."""
        test = morse.sifrovani("test")
        self.assertEqual(test, "- . ... - ")

    def test_sifrovani_1(self):
        """Unit test pro sifrovaci funkci."""
        test = morse.sifrovani("1, 2, 3, 4")
        self.assertEqual(test, ".---- --..--  "
                               "..--- --..--  ...-- --..--  ....- ")

    def test_sifrovani_2(self):
        """Unit test pro sifrovaci funkci."""
        self.assertEqual(morse.sifrovani("text s mezerami"),
                         "- . -..- -  ...  -- . --.. . .-. .- -- .. ")

    def test_sifrovani_3(self):
        """Unit test pro sifrovaci funkci."""
        self.assertEqual(morse.sifrovani(",? )( !"),
                         "--..-- ..--..  -.--.- -.--.  -.-.-- ")

    def test_desifrovani(self):
        """Unit test pro desifrovaci funkci."""
        self.assertEqual(morse.desifrovani("- . ... -"), "TEST")

    def test_desifrovani_1(self):
        """Unit test pro desifrovaci funkci."""
        self.assertEqual(morse.desifrovani("----- -----  "
                                           ".----  ..---  ...--  ....-"),
                         "00 1 2 3 4")

    def test_desifrovani_2(self):
        """Unit test pro desifrovaci funkci."""
        self.assertEqual(morse.desifrovani(".-.-.- --..-- ..--"
                                           ".. -.-.-- -.--.- -.--. -..-."),
                         ".,?!)(/")


if __name__ == '__main__':
    unittest.main()
