"""Welcome to unit test for 'MorseCode' module

"""
import pytest
from MorseCode import encode


@pytest.mark.parametrize("input,expected", [("h", "...."),
                         ("morseovka", "--|---|.-.|...|.|---|...-|-.-|.-")])
def test_encrypt(input, expected):
    assert(encode(input) == expected)
