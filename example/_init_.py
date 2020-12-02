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
    """Otestuje správnost zadáváného parametru (musí být str)"""
    assert decrypt(10) == \
    "Parameter musí být (str)"


def test_encrypt():
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test") == "- . ... - "
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("20") == "..--- ----- "
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert encrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test12@") == "- . ... - .---- ..--- .--.-. "
    """Otestuje správnost zadáváného parametru (musí být str)"""
    assert encrypt(10) == \
    "Parameter musí být (str)"


def test_choice():
    """Otestuje správnost parametru volajícho funkce pro kódování/dekódování morseovky."""
    assert choice(0) == "Špatný formát zadávání"   
    """Otestuje správnost parametru (nesmí být záporný)."""
    assert choice(-20) == \
    "Parametr nesmí být záporný"
    """Otestuje správnost parametru (nesmí být str)."""
    assert choice("TEST") == \
    "Parametr musí být (int)"
