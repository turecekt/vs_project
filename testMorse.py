"""Morse tests."""
import Morseovka


def test_morse_enc0():
    """
    Test 1.

    Input:"Ahoj"
    Output:" .- .... --- .--- "
    """
    assert Morseovka.encrypt("Ahoj".upper()) == " .- .... --- .--- "


def test_morse_enc1():
    """
    Test 2.

    Input:"SOS"
    Output:" ... --- ... "
    """
    assert Morseovka.encrypt("SOS".upper()) == " ... --- ... "


def test_morse_enc2():
    """
    Test 3.

    Input:"jak se mas?"
    Output:" .--- .- -.- / ... . / -- .- ... ..--.. "
    """
    assert Morseovka.encrypt("jak se mas?".upper()) ==\
           " .--- .- -.- / ... . / -- .- ... ..--.. "


def test_morse_enc3():
    """
    Encoding Test 4.

    Input:"-.("
    Output:" -....- .-.-.- -.--. "
    """
    assert Morseovka.encrypt("-.(") == " -....- .-.-.- -.--. "


def test_is_input_correct_unsupported_characters():
    """Definuje nepodporovane znaky"""
    assert not Morseovka.is_input_correct("**")
