# library imports
import unittest

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


class TestConvertion(unittest.TestCase):

    def test_decimal_to_binary(self):
        pass

    def test_decimal_to_octal(self):
        self.assertEqual(decimalToOctal.convert(234), "352")
        self.assertEqual(decimalToOctal.convert(2781), "5335")

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimalToHexadecimal.convert(100), "64")
        self.assertEqual(decimalToHexadecimal.convert("15119"), "3B0F")


if __name__ == '__main__':
    unittest.main()
