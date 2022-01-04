import unittest
from minmax import find_maximum

# -------------------------------------------
# This file contains unit tests for function
# that finds maximum in array and its index.
#
# Author: Lucie Šikudová
# -------------------------------------------


class TestFindMaximum(unittest.TestCase):
    def test_small_sorted(self):
        self.assertEqual(find_maximum([1, 2, 3, 4, 5]), (5, 4))

    def test_small_unsorted(self):
        self.assertEqual(find_maximum
                         ([11, 15, 3, 29, 14, 39, 81, 45, 31]), (81, 6))

    def test_large_sorted(self):
        self.assertEqual(find_maximum([1, 3, 8, 12, 21,
                                       35, 39, 81, 113, 198, 265]), (265, 10))

    def test_sorting_large_unsorted(self):
        self.assertEqual(find_maximum
                         ([212, 28, 58, 25, 183, 197, 199, 127, 119, 97,
                           143, 136, 175, 185, 277]), (277, 14))

    def test_sorting_empty_array(self):
        self.assertEqual(find_maximum([]), (None, -1))
