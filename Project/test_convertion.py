# library imports
import unittest

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


class TestConvertion(unittest.TestCase):

    def test_decimal_to_binary(self):
        # self.assertEqual(decimalToBinary.convert("100"), "1100100")
        # self.assertEqual(decimalToBinary.convert("15119"), "11101100001111")
        pass

    def test_decimal_to_octal(self):
        # self.assertEqual(decimalToOctal.convert("100"), "144")
        # self.assertEqual(decimalToOctal.convert("15119"), "35417")
        pass

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimalToHexadecimal.convert(100), "064")
        self.assertEqual(decimalToHexadecimal.convert("15119"), "03B0F")


if __name__ == '__main__':
    unittest.main()
