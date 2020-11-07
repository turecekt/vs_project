from unittest import TestCase

from char_recurrence.main import read_file, number_char, number_occurence


class Test(TestCase):
    def setUp(self):
        self.s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
        self.mylist = [('l', 1), ('o', 1), ('r', 1)]
    def test_read_file(self):
        # test for read_file method
        self.assertEqual(read_file(arg_len = 1,
                                   input_file = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"),
                         self.s)
        self.assertNotEqual(read_file(arg_len = 1, input_file = "AHoj"), self.s)

    def test_number_char(self):
        self.assertEqual(73, number_char(self.s))


    def test_number_occurence(self):
        self.assertNotEqual(self.mylist, number_occurence("Example"))   # Test with random word
        self.assertEqual(self.mylist, number_occurence("Lor"))          # Test if method create correct List
        self.assertEqual([('l', 1)], number_occurence("L"))             # Test if all word are lower case
        self.assertEqual([], number_occurence("žáš"))                   # Test for ignoring characters with accents
        self.assertEqual([], number_occurence("9_+"))                   # Test for ignoring characters with accents