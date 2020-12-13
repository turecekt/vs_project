import unittest

"""
    Importing the unittest module to test the program DC.py.
"""
from .Dragon import sides

"""
    Importing the sides function from the program DC.py
"""
from .Dragon import input_data

"""
    Importing the input_data function from the program DC.py
"""


class TestDragonCurve(unittest.TestCase):
    """Class for testing individual program functions DQ.py."""

    def test_sides2(self):
        """Function test, with the number of iterations equal to two."""
        q = sides(2)
        self.assertEqual(q, 'rrl')

    def test_sides3(self):
        """Function test, with the number of iterations equal to three."""
        q = sides(3)
        self.assertEqual(q, 'rrlrrll')

    def test_sider4(self):
        """Function test, with the number of iterations equal to four."""
        q = sides(4)
        self.assertEqual(q, 'rrlrrllrrrllrll')

    def test_sider5(self):
        """Function test, with the number of iterations equal to five."""
        q = sides(5)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrll')

    def test_sider6(self):
        """Function test, with the number of iterations equal to six."""
        q = sides(6)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrr'
                            'rlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider7(self):
        """Function test, with the number of iterations equal to seven."""
        q = sides(7)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrlllrrl'
                            'rrllrrrllrlllrrlrrlllrrllrll')

    def test_sider8(self):
        """Function test, with the number of iterations equal to eight."""
        q = sides(8)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrl'
                            'lrrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrl'
                            'llrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrlll'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlll'
                            'rrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider9(self):
        """Function test, with the number of iterations equal to nine."""
        q = sides(9)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrl'
                            'lrrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrl'
                            'llrrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrlll'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlll'
                            'rrlrrllrrrllrlllrrlrrlllrrllrll'
                            'rrrlrrllrrrllrllrrrlrrlllrrllrll'
                            'rrrlrrllrrrllrlllrrlrrlllrrllrllr'
                            'rrlrrllrrrllrllrrrlrrlllrrllrlllr'
                            'rlrrllrrrllrlllrrlrrlllrrllrlllr'
                            'rlrrllrrrllrllrrrlrrlllrrllrllrrr'
                            'lrrllrrrllrlllrrlrrlllrrllrlllrr'
                            'lrrllrrrllrllrrrlrrlllrrllrlllrrlr'
                            'rllrrrllrlllrrlrrlllrrllrll')

    def test_color1(self):
        q = input_data()
        self.assertEqual(type(q[0]), str)

    def test_color2(self):
        q = input_data()
        self.assertEqual(type(q[1]), str)


if __name__ == '__main__':
    unittest.main()
