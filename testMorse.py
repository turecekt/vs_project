"""Morse tests."""
import Morseovka


def test_morse_enc0():
    """
    Encoding Test 0.

    Input:"Ahoj"
    Output:" .- .... --- .--- "
    """
    assert Morseovka.encrypt("Ahoj".upper()) == " .- .... --- .--- "


def test_morse_enc1():
    """
    Encoding Test 1.

    Input:"SOS"
    Output:" ... --- ... "
    """
    assert Morseovka.encrypt("SOS".upper()) == " ... --- ... "


def test_morse_enc2():
    """
    Encoding Test 2.
_
    Input:"jak se mas?"
    Output:" .--- .- -.- / ... . / -- .- ... ..--.. "
    """
    assert Morseovka.encrypt("jak se mas?".upper()) == " .--- .- -.- / ... . / -- .- ... ..--.. "


def test_morse_enc3():
    """
    Encoding Test 3.

    Input:"-.("
    Output:" -....- .-.-.- -.--. "
    """
    assert Morseovka.encrypt("-.(") == " -....- .-.-.- -.--. "


def test_is_input_correct_unsupported_characters():
    assert not Morseovka.is_input_correct("**")


def test_is_input_correct_correct_input():
    assert Morseovka.is_input_correct("AHOJ.")
