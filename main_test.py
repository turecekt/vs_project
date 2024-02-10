"""This is the "main_test" module.

Contains unit tests for main.py
"""

import unittest
from main import *


class TestKochFunction(unittest.TestCase):
    """Unit tests for the Koch function in the main module checks correctness of instructions"""

    def test_koch_order_0(self):
        """This test checks if the Koch function returns the expected instructions for order 0."""
        expected_instructions = [('forward', 400)]

        generated_instructions = koch(400, 0)

        self.assertEqual(generated_instructions, expected_instructions)

    def test_koch_order_1(self):
        """This test checks if the Koch function returns the expected instructions for order 1."""
        expected_instructions = [('forward', 133.33333333333334), ('left', 60), ('forward', 133.33333333333334),
                                 ('left', -120), ('forward', 133.33333333333334), ('left', 60),
                                 ('forward', 133.33333333333334), ('left', 0)]

        generated_instructions = koch(400, 1)

        self.assertEqual(generated_instructions, expected_instructions)

    def test_koch_order_2(self):
        """This test checks if the Koch function returns the expected instructions for order 2."""
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

    def test_koch_order_3(self):
        """This test checks if the Koch function returns the expected instructions for order 3."""
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

        generated_instructions = koch(400, 3)

        self.assertNotEqual(generated_instructions, expected_instructions)

    def test_koch_order_4(self):
        """This test checks if the Koch function returns the expected instructions for order 4."""
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

        generated_instructions = koch(400, 4)

        self.assertNotEqual(generated_instructions, expected_instructions)


class TestGetColorFunction(unittest.TestCase):
    """Unit tests for the getColor function in the main module."""

    def test_get_color_blue(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'blue' for the input value 1.
        """
        self.assertEqual(getColor(1), "blue")

    def test_get_color_red(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'red' for the input value 2.
        """
        self.assertEqual(getColor(2), "red")

    def test_get_color_red(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'green' for the input value 3.
        """
        self.assertEqual(getColor(3), "green")

    def test_get_color_red(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'yellow' for the input value 4.
        """
        self.assertEqual(getColor(4), "yellow")

    def test_get_color_red(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'black' for the input value 5.
        """
        self.assertEqual(getColor(5), "black")

    def test_get_color_red(self):
        """Test for color 'blue'.

        Checks if the getColor function returns 'white' for the input value 6.
        """
        self.assertEqual(getColor(6), "white")


if __name__ == '__main__':
    unittest.main()
