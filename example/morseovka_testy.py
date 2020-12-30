"""Otestovani kodu pomoci unit testů."""

from morseovka import *


def test_prevodDoMorseovky():
    """Unit test pro zakodovani do morseovky."""
    assert test_prevodDoMorseovky(
        "RADIM13578") == ".-. .- -.. .. -- .---- ...-- ..... --... ---.."


def test_prevodZMorseovky():
    """Unit test pro dekodovani z morseovky."""
    assert test_prevodZMorseovky(
        ".-. .- -.. .. -- .---- ...-- ..... --... ---..") == "RADIM13578"
