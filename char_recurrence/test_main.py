from unittest import TestCase

from char_recurrence.main import read_file, number_char


class Test(TestCase):
    def setUp(self):
        self.s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

    def test_read_file(self):
        # test for read_file method
        self.assertEqual(read_file(arg_len = 1, input_file = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"), self.s)
        self.assertNotEqual(read_file(arg_len = 1, input_file = "AHoj"), self.s)

    def test_number_char(self):
        self.assertEqual(73, number_char(self.s))
