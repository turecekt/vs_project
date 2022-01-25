import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_if_valid_input_in_nejcastejsiznak_returns_valid_value(self):
        text = "aaaabbbccdefgh"
        self.assertEqual(nejcastejsiznak(text), "a ")

    def test_if_valid_input_in_nejmenecastyznak_returns_valid_value(self):
        text = "aaaabbbccdefgh"
        self.assertEqual(nejmenecastyznak(text), "d e f g h ")

    def test_if_valid_input_in_prumernacetnost_returns_valid_value(self):
        text = "aaaabbbccdefgh"
        self.assertEqual((prumernacetnostznaku(text)), 2.4285714285714284)

    def test_if_valid_input_in_prumernacetnosti_returns_valid_value(self):
        text = "aaaabbbccdefgh"
        self.assertEqual(cetnostznakuabecedy(text), "a 4, b 3, c 2, d 1, e 1, f 1, g 1, h 1, i 0, j 0, k 0, l 0, m 0, n 0, o 0, p 0, q 0, r 0, s 0, t 0, u 0, v 0, w 0, x 0, y 0, z 0,")

    def test_if_valid_input_in_unique_returns_valid_value(self):
        text = ["a", "a", "a", "a", "b", "b", "b", "c", "c", "d", "e", "f", "g", "h"]
        self.assertEqual((unique(text)), ["a", "b", "c", "d", "e", "f", "g", "h"])

    def text_if_valid_input_in_vyskytznaku_return_valid_value(self):
        self.assertEqual(vyskytznaku(["a", "a", "a", "h"]), ["3", "3", "3", "1"])

if __name__ == '__main__':
    unittest.main()