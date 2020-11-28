"""Welcome to unit test for 'MorseCode' module."""

import pytest
from MorseCode import encode


@pytest.mark.parametrize("input,expected", [("h", "...."),
                         ("morseovka", "--|---|.-.|...|.|---|...-|-.-|.-"),
                         ("morseova abeceda je skupina symbolu",
                         "--|---|.-.|...|.|---|...-|.-||.-|-...|.|-.-.|.|"
                          "-..|.-||.---|.||...|-.-|..-|.--.|..|-.|.-||...|-."
                          "--|--|-...|---|.-..|..-"),
                         ("0123456789", "-----|.----|..---|...--|....-|.....|"
                          "-....|--...|---..|----.")])
def test_encrypt(input, expected):
    """Tests encode function."""
    assert(encode(input) == expected)
