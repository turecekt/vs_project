"""Test."""
import unittest

from main import odmorzeovky, domorzeovky


class MyTestCase(unittest.TestCase):
    """Testy."""

    def test(self):
        """Test z morse."""
        self.assertEqual(odmorzeovky("----."), '9')

    def test1(self):
        """Test do morse."""
        self.assertEqual(domorzeovky('9'), " ----. ")
    def test(self):
        """Test z morse."""
        self.assertEqual(odmorzeovky("---.."), '8')

    def test1(self):
        """Test do morse."""
        self.assertEqual(domorzeovky('a'), " ---.. ")

if _name_ == '_main_':
    unittest.main()
