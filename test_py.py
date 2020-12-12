"""This module tests morsecode."""
import pytest
import morsecode


@pytest.mark.parametrize("input,expected",[("e", "."),
                         ("My name is Kate", "-- -.--  -. .- -- .  "
                          ".. ...  -.- .- - ."), ("?,.;/=-'():_+@",
                          "..--.. --..-- .-.-.- -.-.-. -..-. -...- "
                          "-....- .----. -.--. -.--.- ---... "
                          "..--.- .-.-. .--.-."), ("čáp!", "Č Á .--. !")])
def test_encode(input, expected):
    """Tests encode function."""
    assert(morsecode.encode_morse(input) == expected)


@pytest.mark.parametrize("input,expected", [("....", "H"),
                         ("?", ""),("-- --- .-. ... . --- "
                          "...- -.- .-", "MORSEOVKA")])
def test_decode(input, expected):
    """Tests decode_morse function."""
    assert(morsecode.decode_morse(input) == expected)
