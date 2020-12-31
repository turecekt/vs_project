"""Otestovani kodu pomoci unit testů."""

from morseovka import prevodDoMorseovky
from morseovka import prevodZMorseovky


def test_prevodDoMorseovky():
    """Unit test pro zakodovani do morseovky."""
    assert prevodDoMorseovky("RADIM") == ".-. .- -.. .. -- "
    assert prevodDoMorseovky("13578") == ".---- ...-- ..... --... ---.."


def test_prevodZMorseovky():
    """Unit test pro dekodovani z morseovky."""
    assert prevodZMorseovky(
        ".-. .- -.. .. -- .---- ...-- ..... --... ---..") == "RADIM13578"
