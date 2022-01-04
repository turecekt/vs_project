"""find minimum unit tests."""
import unittest
from minmax import find_minimum

# -------------------------------------------
# This file contains unit tests for function
# that finds minimum in array and its index.
#
# Author: Lucie Šikudová
# -------------------------------------------


"""
class for finding minimum in array unit tests
compares result of the function and the expected output
"""


class TestFindMinimum(unittest.TestCase):
    """
        public class for finding minimum unit test
    """

    def test_small_sorted(self):
        """
        Check the correctness of find minimum with sorted small array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(find_minimum([1, 2, 3, 4, 5]), (1, 0))

    def test_small_unsorted(self):
        """
        Check the correctness of find minimum with unsorted small array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(find_minimum
                         ([11, 15, 3, 29, 14, 39, 81, 45, 31]), (3, 2))

    def test_large_sorted(self):
        """
        Check the correctness of find minimum with sorted large array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(find_minimum([1, 3, 8, 12, 21,
                                       35, 39, 81, 113, 198, 265]), (1, 0))

    def test_sorting_large_unsorted(self):
        """
        Check the correctness of find minimum with unsorted large array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(find_minimum
                         ([212, 28, 58, 25, 183, 197, 199, 127, 119, 97,
                           143, 136, 175, 185, 277]), (25, 3))

    def test_sorting_empty_array(self):
        """
        Check the correctness of find minimum with empty array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(find_minimum([]), (None, -1))
