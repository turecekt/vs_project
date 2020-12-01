"""Převodník morseové soustavy."""

from morse import encrypt, decrypt, choice


def test_decrypt():
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... -") == "TEST"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("..--- -----") == "20"
    """Otestuje zda funkce překládá znaky mimo morseovu abecedu."""
    assert decrypt("AWEGWRHGWRh") == "Špatný formát zadávání"
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert decrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... - .---- ..--- .--.-.") == "TEST12@"


def test_encrypt():
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test") == "- . ... - "
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("20") == "..--- ----- "
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert encrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test12@") == "- . ... - .---- ..--- .--.-. "


def test_choice():
    """Ověření parametru pro volání definicí."""
    assert choice(0) == "Špatný formát zadávání"
