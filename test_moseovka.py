"""Test."""
import unittest

from morseovka import odmorzeovky, domorzeovky


class MyTestCase(unittest.TestCase):
    """Testy."""

    def test(self):
        """Test z morse."""
        self.assertEqual(odmorzeovky("----."), '9')

    def test2(self):
        """Test do morse."""
        self.assertEqual(domorzeovky('9'), " ----. ")

    def test3(self):
        """Test z morse."""
        self.assertEqual(odmorzeovky("---.."), '8')

    def test4(self):
        """Test do morse."""
        self.assertEqual(domorzeovky('a'), " ---.. ")


if __name__ == '__main__':
    unittest.main()
