from main import checkInputAndPrintRomanNumeral
import pytest

def test_parseToRomanNumeral_success():
    """Test for valid input and parsing to roman numerals"""
    assert checkInputAndPrintRomanNumeral("1994") == "MCMXCIV"

def test_parseToRomanNumeral_invalidInput():
    """Test for invalid input raising exception"""
    with pytest.raises(Exception):
        assert checkInputAndPrintRomanNumeral("invalidni text")
