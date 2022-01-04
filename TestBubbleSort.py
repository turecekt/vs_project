"""unit test for bubble sort."""
from minmax import bubble_sort
import unittest

# -----------------------------------
# This file contains unit tests for bubble sort algorithm.
#
# Author: Lucie Šikudová
# -----------------------------------

"""
class for bubble sort unit tests
compares result of the function and the expected output
"""


class TestBubbleSort(unittest.TestCase):
    """public class for bubble sort unit test."""

    def test_sorting_small_sorted(self):
        """
        Check the correctness of bubble sort with sorted small array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorting_small_unsorted(self):
        """
        Check the correctness of bubble sort with unsorted small array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(bubble_sort([11, 15, 3, 29, 14, 39, 81, 45, 31]),
                         [3, 11, 14, 15, 29, 31, 39, 45, 81])

    def test_sorting_large_sorted(self):
        """
        Check the correctness of bubble sort with sorted large array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(bubble_sort
                         ([1, 3, 8, 12, 21, 35, 39, 81, 113, 198, 265]),
                         [1, 3, 8, 12, 21, 35, 39, 81, 113, 198, 265])

    def test_sorting_large_unsorted(self):
        """
        Check the correctness of bubble sort with unsorted large array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(bubble_sort
                         ([212, 28, 58, 25, 183, 197, 199, 127,
                           119, 97, 143, 136, 175, 185, 277]),
                         [25, 28, 58, 97, 119, 127, 136, 143, 175,
                          183, 185, 197, 199, 212, 277])

    def test_sorting_empty_array(self):
        """
        Check the correctness of bubble sort with empty array.

        :return: AssertionError if error, otherwise nothing
        """
        self.assertEqual(bubble_sort([]), [])
