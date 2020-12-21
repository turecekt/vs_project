"""Unit Testovani Projekt_Morseovka."""

import unittest
from Projekt_Morseovka import encrypt
from Projekt_Morseovka import decrypt
from Projekt_Morseovka import choice


class Morseovka_Test(unittest.TestCase):
    """Unit test - Latin to Morse function."""


def test_encrypt_1():
    """Encrypting a word Morseovka."""
    assert(encrypt("ondra")) == "---/-./-../.-./.-/"

    """
    Unit test - Latin to Morse function
    """


def test_encrypt_2():
    """Encrypting number Morseovka."""
    assert(encrypt("1234")) == ".----/..---/...--/....-/"

    """
    Unit test - Morse to Latin function
    """


def test_decrypt_1():
    """Encrypting Morse to Latin Characters."""
    assert(decrypt("--- -. -.. .-. .-")) == "ONDRA"

    """
    Unit test - Morse to Latin Numbers function
    """


def test_decrypt_2():
    """Encrypting Morse to Latin Numbers."""
    assert (decrypt(".---- ..--- ...-- ....-")) == "1234"

    """
    Unit test - Choose translation function
    """


def test_choice_1():
    """Test of choosing translation."""
    assert (choice("1")) == "Your text: "
