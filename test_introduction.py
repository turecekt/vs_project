# -*- coding: utf-8 -*-

import unittest
from reakcniRychlost import introduction


class introductionTest(unittest.TestCase):
        
    def test_exception(self):
        try:
            introduction()
        except ExceptionType:
            self.fail("introduction() raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()
