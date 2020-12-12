"""Project for AK1VS.
Author: Matúš Juhasz.
"""
from unittest import TestCase

from char_recurrence.main import read_file, number_char, number_occurence


class Test(TestCase):
    """Testing class for methods."""
    def setUp(self):
        """Set variables for testing."""
        self.s = "Lorem Ipsum is simply dummy text of " \
                 "the printing and typesetting industry"
        self.mylist = [('l', 1), ('o', 1), ('r', 1)]

    def test_read_file(self):
        """Test for read_file method."""
        self.assertEqual(read_file(arg_len=1,
                                   input_file="Lorem Ipsum is simply "
                                              "dummy text of the printing "
                                              "and typesetting industry"),
                         self.s)
        self.assertNotEqual(read_file(arg_len=1, input_file="AHoj"), self.s)

    def test_number_char(self):
        """Test if method return correct lenght of word."""
        self.assertEqual(73, number_char(self.s))

    def test_number_occurence(self):
        """Testing method for correct number of occurrence.

        #1 Test if method create correct List.
        #2 Test if all word are lower case.
        #3 Test for ignoring characters with accents.
        #4 Test for ignoring characters with accents.
        """
        self.assertNotEqual(self.mylist, number_occurence("Example"))
        self.assertEqual(self.mylist, number_occurence("Lor"))
        self.assertEqual([('l', 1)], number_occurence("L"))
        self.assertEqual([], number_occurence("žáš"))
        self.assertEqual([], number_occurence("9_+"))
