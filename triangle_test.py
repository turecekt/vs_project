#!/usr/bin/env python3
"""Run triangle tests."""

import unittest
import triangle


# Test class
class SimpleTest(unittest.TestCase):
    """Very basic example test."""

    # Returns True or False.
    def testPerimeter1(self):
        """First test of valid STDIN input."""
        self.assertEqual(triangle.trianglePerimeter(3.0, 4.0, 5.0), 12.0)

    def testArea1(self):
        """First test of valid STDIN input."""
        self.assertEqual(triangle.triangleArea(3.0, 4.0, 5.0), 6.0)

    def testConst1(self):
        """First test of valid STDIN input."""
        self.assertEqual(triangle.constructability(3.0, 4.0, 5.0), True)

    def testOrthogon1(self):
        """First test of valid STDIN input."""
        self.assertEqual(triangle.triangleOrthogonality(3.0, 4.0, 5.0), True)


if __name__ == '__main__':
    unittest.main()
