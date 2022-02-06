"""Unit testy pro soubor main.py."""

import unittest
from main import nejcastejsiznak
from main import nejmenecastyznak
from main import prumernacetnostznaku
from main import cetnostznakuabecedy
from main import unique
from main import vyskytznaku


class MyTestCase(unittest.TestCase):
    """
    Trida na unit testy.

    :param unittest.Testcas:
    """

    def test_if_valid_input_in_nejcastejsiznak_returns_valid_value(self):
        """
        Unit test pro funkci nejcastejsiznak.

        :param self:
        """
        text = "aaaabbbccdefgh"
        self.assertEqual(nejcastejsiznak(text), "a ")

    def test_if_valid_input_in_nejmenecastyznak_returns_valid_value(self):
        """
        Unite test pro funkci nejmenecastyznak.

        :param self:
        """
        text = "aaaabbbccdefgh"
        self.assertEqual(nejmenecastyznak(text), "d e f g h ")

    def test_if_valid_input_in_prumernacetnost_returns_valid_value(self):
        """
        Unit test na funkci prumernacetnostznaku.

        :param self:
        """
        text = "aaaabbbccdefgh"
        self.assertEqual((prumernacetnostznaku(text)), 2.4285714285714284)

    def test_if_valid_input_in_prumernacetnosti_returns_valid_value(self):
        """
        Unit test na funkci cetnostznakuabecedy.

        :param self:
        """
        text = "aaaabbbccdefgh"
        self.assertEqual(cetnostznakuabecedy(text),
                         "a 4, b 3, c 2, d 1, e 1,"
                         " f 1, g 1, h 1, i 0, j 0,"
                         " k 0, l 0, m 0, n 0, o 0,"
                         " p 0, q 0, r 0, s 0, t 0,"
                         " u 0, v 0, w 0, x 0, y 0,"
                         " z 0,")

    def test_if_valid_input_in_unique_returns_valid_value(self):
        """
        Unit test na funkci unique.

        :param self:
        """
        text = ["a", "a", "a", "a", "b", "b",
                "b", "c", "c", "d", "e", "f",
                "g", "h"]
        self.assertEqual((unique(text)), ["a", "b", "c", "d",
                                          "e", "f", "g", "h"])

    def text_if_valid_input_in_vyskytznaku_return_valid_value(self):
        """
        Testuje funkci vyskytznaku.

        :param self:
        """
        self.assertEqual(vyskytznaku(["a", "a", "a", "h"]),
                         ["3", "3", "3", "1"])


if __name__ == "main":
    unittest.main()
