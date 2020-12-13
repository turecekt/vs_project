import unittest

from main import domorse
from main import zmorse



class MyTestCase(unittest.TestCase):
    def test_something3(self):
        self.assertEqual(zmorse(".-  .- "), "a a ")

    def test_something2(self):
        self.assertEqual(zmorse(".-"), "a")

    def test_something1(self):
        self.assertEqual(domorse("a"), ".- ")


if __name__ == '__main__':
    unittest.main()
