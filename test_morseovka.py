"""Testy na funkci Morseovka."""

import morseovka


def test_sifrovani1():
    """Test testujici string o jednom slove."""
    expected1 = "- . ... -"
    assert morseovka.sifrovani
    ("test") == expected1


def test_sifrovani():
    """Test testujici string o vice slovech."""
    expected2 = "-.. .-. .-- .... -.-- / - . ... -"
    assert morseovka.sifrovani
    ("druhy test") == expected2


def test_desifrovani1():
    """Test testujici desifrovani stringu o dvou slovech."""
    expected3 = "TEST PROSEL"
    assert morseovka.desifrovani
    ("- . ... - / .--. .-. --- ... . .-.. ") == expected3


def test_desifrovani():
    """Test testujici desifrovani stringu s cisly."""
    expected4 = "TEST 415 3 5 7"
    assert morseovka.desifrovani
    ("- . ... - / ....- .---- ..... / ...-- / ..... / --...") == expected4
