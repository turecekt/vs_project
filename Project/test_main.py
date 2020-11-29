import main
import sys


def test_convert_binary():
    """Test function convert_binary."""
    assert main.convert_binary(78) == "1001110"
    assert main.convert_binary(1) == "1"
    assert main.convert_binary(100) == "1100100"
    assert main.convert_binary(2020) == "11111100100"


def test_convert_octal():
    """Test function convert decimal num to octal."""
    assert main.convert_octal(156) == "234"
    assert main.convert_octal(0) == "0"
    assert main.convert_octal(123456789) == "726746425"
    assert main.convert_octal(2020) == "3744"


def test_convert_hexadecimal():
    """Test function convert_hexadecimal."""
    if sys.version_info > (3, 0):
        assert main.convert_hexadecimal(0) == "0"
        assert main.convert_hexadecimal(100) == "064"
        assert main.convert_hexadecimal(15119) == "03B0F"
    else:
        assert main.convert_hexadecimal(0) == "0"
        assert main.convert_hexadecimal(100) == "64"
        assert main.convert_hexadecimal(15119) == "03B0F"