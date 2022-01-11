# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:00:00 2022.

@author: BitterMug
"""

import unittest
import reakcniRychlost


def autoInput():
    """Monkeypatch function.

    Simulates User input.
    Returns:
    int: User input.
    """
    return 5

def autoInputErr():
    """Monkeypatch function.

    Simulates incorect User input.
    Returns:
    str: Incorect user input.
    """
    return "a"

class tests_question(unittest.TestCase):
    """Set of tests for question function."""

    def test_question_correct(self):
        """Test correct answer handling."""
        reakcniRychlost.user_input = autoInput
        reakcniRychlost.question(2, 3, "+")

    def test_question_wrong(self):
        """Test incorrect answer handling."""
        reakcniRychlost.user_input = autoInput
        reakcniRychlost.question(2, 0, "+")

    def test_question_err(self):
        """Test error answer handling."""
        reakcniRychlost.user_input = autoInputErr
        with self.assertRaises(ValueError):
            reakcniRychlost.question(2, 0, "+")


if __name__ == '__main__':
    unittest.main()
