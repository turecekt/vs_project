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
        pass

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimalToHexadecimal.convert(100), "064")
        self.assertEqual(decimalToHexadecimal.convert("15119"), "03B0F")


if __name__ == '__main__':
    unittest.main()
