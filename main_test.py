import unittest
from main import *


class TestKochFunction(unittest.TestCase):

    def test_koch_order_0(self):
        # Test for order 0
        expected_instructions = [('forward', 400)]  # Replace with the expected instructions for order 0

        generated_instructions = koch(400, 0)

        self.assertEqual(generated_instructions, expected_instructions)

    def test_koch_order_1(self):
        # Test for order 1
        expected_instructions = [('forward', 133.33333333333334), ('left', 60), ('forward', 133.33333333333334),
                                 ('left', -120), ('forward', 133.33333333333334), ('left', 60),
                                 ('forward', 133.33333333333334), ('left', 0)]

        generated_instructions = koch(400, 1)

        self.assertEqual(generated_instructions, expected_instructions)

    def test_koch_order_2(self):
        # Test for order 1
        expected_instructions = [('forward', 44.44444444444445), ('left', 60), ('forward', 44.44444444444445),
                                 ('left', -120), ('forward', 44.44444444444445), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 0), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 60), ('forward', 44.44444444444445),
                                 ('left', -120), ('forward', 44.44444444444445), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 0), ('left', -120),
                                 ('forward', 44.44444444444445), ('left', 60), ('forward', 44.44444444444445),
                                 ('left', -120), ('forward', 44.44444444444445), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 0), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 60), ('forward', 44.44444444444445),
                                 ('left', -120), ('forward', 44.44444444444445), ('left', 60),
                                 ('forward', 44.44444444444445), ('left', 0), ('left', 0)]

        generated_instructions = koch(400, 2)

        self.assertEqual(generated_instructions, expected_instructions)


class TestGetColorFunction(unittest.TestCase):

    def test_get_color_blue(self):
        self.assertEqual(getColor(1), "blue")

    def test_get_color_red(self):
        self.assertEqual(getColor(2), "red")

    def test_get_color_red(self):
        self.assertEqual(getColor(3), "green")

    def test_get_color_red(self):
        self.assertEqual(getColor(4), "yellow")

    def test_get_color_red(self):
        self.assertEqual(getColor(5), "black")

    def test_get_color_red(self):
        self.assertEqual(getColor(6), "white")


if __name__ == '__main__':
    unittest.main()
