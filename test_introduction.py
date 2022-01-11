# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:00:00 2022.

@author: BitterMug
"""

import unittest
from reakcniRychlost import introduction


class introductionTest(unittest.TestCase):
    """Set of tests for introduction function."""

    def test_exception(self):
        """Test for any errors running introduction function."""
        introduction()


if __name__ == '__main__':
    unittest.main()
