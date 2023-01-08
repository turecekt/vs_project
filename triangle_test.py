#!/usr/bin/env python3
"""Run triangle tests."""

import unittest
# from io import StringIO
# from unittest.mock import patch
# import main


#  Test class
# class SimpleTest(unittest.TestCase):
#     """Very basic example test."""

#  Returns True or False.
#     def test(self):
#         """First test of valid STDIN input."""
#        test_args = ['.\\main.py', '1', '1', '3', '3', '3', '1']
#         expectedStdout = """Lengths of the sides of the triangle are:
# 2.8284271247461903, 2.0, 2.0
# Perimeter of the triangle is: 6.82842712474619
# Area of the triangle is: 1.9999999999999991
# """
#         #  Test evaluation
#         with patch('sys.stdout', new_callable=StringIO) as fakeStdout:
#             main.main()
#             self.assertEqual(fakeStdout.getvalue(), expectedStdout)


if __name__ == '__main__':
    unittest.main()
