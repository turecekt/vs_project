# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:07:17 2021
@author: zifca
"""

import unittest
from reakcniRychlost import calcOfEquations


class calcOfEquationsPlusSign(unittest.TestCase):
    """Set of tests for addition in calcOfEquations function."""

    def test_addPositiveNumbers(self):
        """Tests addition of two positive integers."""
        actual = calcOfEquations(5, 5, '+')
        self.assertEqual(actual, 10)

    def test_addNegativeNumbers(self):
        """Tests addition of two negative integers."""
        actual = calcOfEquations(-5, -5, '+')
        self.assertEqual(actual, -10)

    def test_addNegPosNumbers(self):
        """Tests addition of positive and negative integers."""
        actual = calcOfEquations(-5, 8, '+')
        self.assertEqual(actual, 3)

    def test_negativeZero(self):
        """Tests addition of negative zero."""
        actual = calcOfEquations(5, -0, '+')
        self.assertEqual(actual, 5)


class calcOfEquationsMinusSign(unittest.TestCase):
    """Set of tests for subtraction in calcOfEquations function."""

    def test_subPositiveNumbers(self):
        """Tests subtraction of two positive integers."""
        actual = calcOfEquations(5, 5, '-')
        self.assertEqual(actual, 0)

    def test_subPositiveNumbers2(self):
        """Tests subtraction of two positive integers.
        Ending with negative return.
        """

        actual = calcOfEquations(5, 8, '-')
        self.assertEqual(actual, -3)

    def test_subNegNumbers(self):
        """Tests subtraction of two negative integers."""
        actual = calcOfEquations(-8, -3, '-')
        self.assertEqual(actual, -5)

    def test_subNegNumbers2(self):
        """Tests subtraction of two negative integers.
        Ending with positive return.
        """

        actual = calcOfEquations(-3, -8, '-')
        self.assertEqual(actual, 5)

    def test_negativeZero(self):
        """Tests subtraction of negative zero."""
        actual = calcOfEquations(-3, -0, '-')
        self.assertEqual(actual, -3)


class calcOfEquationsMultiplicationSign(unittest.TestCase):
    """Set of tests for multiplication in calcOfEquations function."""

    def test_multiplyPositiveNumbers(self):
        """Tests multiplication of two positive integers."""
        actual = calcOfEquations(5, 5, '*')
        self.assertEqual(actual, 25)

    def test_multiplyPosNegNumbers(self):
        """Tests multiplication of negative and positive integers."""
        actual = calcOfEquations(-5, 5, '*')
        self.assertEqual(actual, -25)

    def test_multiplyNegNumbers(self):
        """Tests multiplication of two negative integers."""
        actual = calcOfEquations(-5, -5, '*')
        self.assertEqual(actual, 25)

    def test_multiplyZero(self):
        """Tests multiplication with zero integers."""
        actual = calcOfEquations(0, -5, '*')
        self.assertEqual(actual, 0)


class calcOfEquationsDivisionSign(unittest.TestCase):
    """Set of tests for division in calcOfEquations function."""

    def test_dividePositiveNumbers(self):
        """Tests division of two positive integers."""
        actual = calcOfEquations(5, 5, '/')
        self.assertEqual(actual, 1)

    def test_dividePosNegNumbers(self):
        """Tests division of positive and negative integers."""
        actual = calcOfEquations(-5, 5, '/')
        self.assertEqual(actual, -1)

    def test_divideNegNumbers(self):
        """Tests division of two negative integers."""
        actual = calcOfEquations(-5, -5, '/')
        self.assertEqual(actual, 1)

    def test_divideZero(self):
        """Tests division of zero."""
        actual = calcOfEquations(0, -5, '/')
        self.assertEqual(actual, 0)

    def test_divideZeroByZero(self):
        """Tests division by zero."""
        with self.assertRaises(ZeroDivisionError):
            calcOfEquations(0, 0, '/')


class calcOfEquationsError(unittest.TestCase):
    """Set of tests for error handling in calcOfEquations function."""

    def test_error(self):
        """Tests division by zero error."""
        with self.assertRaises(ZeroDivisionError):
            calcOfEquations(5, 0, '/')


if __name__ == '__main__':
    unittest.main()
