#!/usr/bin/env python3
"""Run triangle tests."""

import unittest
from io import StringIO
from unittest.mock import patch
import triangle


#  Test class
class SimpleTest(unittest.TestCase):
    """Very basic example test."""

    #  Returns True or False.
    def test(self):
        """First test of valid STDIN input."""
        test_args = ['.\\main.py', '1', '2', '3', '4', '5', '6']
        test_output = """Points are ('1', '2') ('3', '4') ('5', '6')
Lengths of the sides of the triangle are:
2.8284271247461903, 2.8284271247461903, 5.656854249492381
Perimeter of the triangle is: 11.313708498984761
Area of the triangle is: 0.0
"""
        #  Test evaluation
        with patch('sys.stdout', new_callable=StringIO) as f:
            triangle.start(test_args)
            self.assertEqual(f.getvalue(), test_output)


if __name__ == '__main__':
    unittest.main()
