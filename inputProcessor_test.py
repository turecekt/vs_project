#!/usr/bin/env python3
"""Unittests for inputProcessor module."""

from inputProcessor import sideLength, inputPoint, getPoints, getSides
from unittest.mock import patch
import unittest


def test_sideLength():
    """Unittest for inputProcessor.sideLength."""
    assert sideLength((-2, 1), (-5, 5)) == 5


class TestInputPoint(unittest.TestCase):
    """Unittests for inputProcessor.inputPoints."""

    testInput = ["1", "-2.8"]

    @patch('builtins.input', side_effect=testInput)
    def test_inputPoint(self, mock_input):
        """Test inputPoints function with valid input."""
        expectedResult = [1.0, -2.8]
        actualResult = inputPoint("A")
        self.assertEqual(expectedResult, actualResult)

    testInputBadOK = ["lorem", "ipsum", "1.5", "lala", "-3"]

    @patch('builtins.input', side_effect=testInputBadOK)
    def test_inputPoint_badOK(self, mock_input):
        """Test inputPoints function with bad input corrected.

        Test inputPints function behaviour when user suplies
        invalid input and then corrected input.
        """
        expectedResult = [1.5, -3.0]
        actualResult = inputPoint("B")
        self.assertEqual(expectedResult, actualResult)

    testInputBad = ["lorem", "ipsum", "end", "1.5", "lala", "3"]

    @patch('builtins.input', side_effect=testInputBad)
    def test_inputPoint_bad(self, mock_input):
        """Test inputPoints function with bad input.

        Test inputPoints function behaviour when user suplies
        invalid input and doesn't correct it.
        """
        with self.assertRaises(SystemExit) as cm:
            inputPoint("C")

        self.assertEqual(cm.exception.code, 1)


class TestGetPoints(unittest.TestCase):
    """Unittests for inputProcessor.getPoints."""

    testPoints = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]

    @patch('inputProcessor.inputPoint', side_effect=testPoints)
    def test_getPoints(self, mock_inputPoint):
        """Test getPoints function with interactive input."""
        actualResult = getPoints("")
        self.assertEqual(actualResult, self.testPoints)

    def test_getPoints_args(self):
        """Test getPoints function with arguments input."""
        testArgs = ["example.py", "1", "-2.5", "3.8", "-4", "5", "0"]
        expectedResult = [[1.0, -2.5], [3.8, -4.0], [5.0, 0.0]]
        actualResult = getPoints(testArgs, debug=True)
        self.assertEqual(actualResult, expectedResult)


class TestGetSides(unittest.TestCase):
    """Unittests for inputProcessor.getSides."""

    testSides = [1.2, 2.3, 3.4]

    @patch('inputProcessor.sideLength', side_effect=testSides)
    @patch('inputProcessor.getPoints')
    def test_getSides(self, mock_getPoints, mock_sideLength):
        """Test getSides function."""
        actualResult = getSides("", debug=True)
        self.assertEqual(actualResult, self.testSides)
