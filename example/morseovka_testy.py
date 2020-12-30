"""Otestovani kodu pomoci unit testů."""

import morseovka


def test_prevodDoMorseovky():
    """Unit test pro zakodovani do morseovky."""
    assert prevodDoMorseovky(
        "RADIM13578") == ".-. .- -.. .. -- .---- ...-- ..... --... ---.."


def test_prevodZMorseovky():
    """Unit test pro dekodovani z morseovky."""
    assert prevodZMorseovky(
        ".-. .- -.. .. -- .---- ...-- ..... --... ---..") == "RADIM13578"
