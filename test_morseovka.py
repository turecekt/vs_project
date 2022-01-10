"""Testy na funkci Morseovka."""


from morseovka import sifrovani, desifrovani


def test_sifrovani1():
    """Test testujici string o jednom slove."""
    ocekavanyVysledek = '- . ... -'
    assert sifrovani
    ('test') == ocekavanyVysledek


def test_sifrovani2():
    """Test testujici string o vice slovech."""
    ocekavanyVysledek2 = '--.. -.- --- ..- ... -.- .- / - . ... -..-'
    assert sifrovani
    ("zkouska testu") == ocekavanyVysledek2

