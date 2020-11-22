"""Test convert functions."""
# library imports
import unittest

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


"""Unittest class for convert functions."""


class TestConvertion(unittest.TestCase):
    """Class testing convert functions."""

    def test_decimal_to_binary(self):
        """Function testing binary conversion."""
        self.assertEqual(decimalToBinary.convert(78), "1001110")
        self.assertEqual(decimalToBinary.convert(1234567890),
                         "1001001100101100000001011010010")

    def test_decimal_to_octal(self):
        """Function testing octal conversion."""
        self.assertEqual(decimalToOctal.convert(234), "352")
        self.assertEqual(decimalToOctal.convert(2781), "5335")

    def test_decimal_to_hexadecimal(self):
        """Function testing hexadecimal conversion."""
        self.assertEqual(decimalToHexadecimal.convert(100), "064")
        self.assertEqual(decimalToHexadecimal.convert("15119"), "03B0F")


if __name__ == '__main__':
    unittest.main()
