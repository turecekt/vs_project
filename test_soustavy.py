"""Testy pro převod číslených soustav."""

import soustavy


def test_toOctal():
    """Testuje převod na oktály."""
    assert oct(45) == soustavy.toOctal(45)
    assert oct(300197) == soustavy.toOctal(300197)


def test_toBin():
    """Testuje převod na binárku."""
    assert bin(985).lower() == soustavy.toBin(985).lower()
    assert bin(9876543210).lower() == soustavy.toBin(9876543210).lower()


def test_toHex():
    """Testuje převod na hexadecimální soustavu."""
    assert hex(1263).lower() == soustavy.toHex(1263).lower()
    assert hex(9876543210).lower() == soustavy.toHex(9876543210).lower()
