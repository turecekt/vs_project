"""Testy pro převod číslených soustav."""
import soustavy
import pytest


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


def test_main():
    """Otestuje parsování argumentů"""
    # Test ukončení při příliš velkém množství argumentů
    with pytest.raises(SystemExit) as e:
        soustavy.main(["-h", 12, 15])
    assert e.type == SystemExit
    assert e.value.code == 1

    # Test správného zpracování argumentů
    soustavy.main(("-h", 22)) == hex(22)
