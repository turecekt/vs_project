# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:00:00 2022.

@author: BitterMug
"""

import unittest
import reakcniRychlost


def question(a, b, c):
    """Monkeypatch function.

    Returns:
    boolean: Wrong answer indicator.
    float: Reaction time indicator.
    """
    return False, 1.2


class tests(unittest.TestCase):
    """Set of tests for main myFunction function."""

    def test_myFunction_False(self):
        """Test myFunction with valid values."""
        temp = reakcniRychlost.question
        reakcniRychlost.question = question
        reakcniRychlost.myFunction()
        reakcniRychlost.question = temp


if __name__ == '__main__':
    unittest.main()
