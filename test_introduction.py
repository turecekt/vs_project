# -*- coding: utf-8 -*-

import unittest
from reakcniRychlost import introduction


class introductionTest(unittest.TestCase):

    def test_introduction(self):
        with self.assertRaises(SystemExit) as ec:
            introduction()
        self.assertEqual(ec.exception.code, 0)


if __name__ == '__main__':
    unittest.main()
