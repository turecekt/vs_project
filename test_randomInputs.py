"""
Created on Thu Dec 30 09:35:11 2021
@author: zifca
"""

import unittest
from reakcniRychlost import random_inputs


class randomInputs(unittest.TestCase):
    """Set of tests for randomInputs function."""

    def test_random_inputs_abIsInInterval(self):
        """ Tests if given values are in correct interval."""
        a, b, sgn = random_inputs()
        self.assertTrue(-10 <= a, b <= 10)

    def test_random_inputs_abIsInteger(self):
        """Tests if given values are integers."""
        a, b, sgn = random_inputs()
        self.assertTrue(isinstance(a, int)) \
            and self.assertTrue(isinstance(b, int))

    def test_sgn(self):
        """Tests if given sign is allowed."""
        a, b, sgn = random_inputs()
        self.assertTrue(sgn in ['+', '-', '*', '/'])


if __name__ == '__main__':
    unittest.main()
