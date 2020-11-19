"""Testy převodník numerických soustav."""
from numsys import convertToBinary, convertToOctal, convertToHexadecimal


def test_convertToBinary():
    """Otestuje správnost převodu do dvojkové soustavy."""
    assert convertToBinary(20) == "10100"
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToBinary(-20) == \
        "number parameter cant be negative"
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToBinary(20.5) == \
        "number parameter must be round(int)"
    assert convertToBinary(-20.5) == \
        "number parameter must be round(int)"
    assert convertToBinary("asdk") == \
        "number parameter must be round(int)"


def test_convertToOctal():
    """Otestuje správnost převodu do osmičkové soustavy."""
    assert convertToOctal(20) == "24"
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToOctal(-20) == \
        "number parameter cant be negative"
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToOctal(20.5) == \
        "number parameter must be round(int)"
    assert convertToOctal(-20.5) == \
        "number parameter must be round(int)"
    assert convertToOctal("asdk") == \
        "number parameter must be round(int)"


def test_convertToHexadecimal():
    """Otestuje správnost převodu do šestnástkové soustavy."""
    assert convertToHexadecimal(185) == "B9"
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToHexadecimal(-20) == \
        "number parameter cant be negative"
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToHexadecimal(20.5) == \
        "number parameter must be round(int)"
    assert convertToHexadecimal(-20.5) == \
        "number parameter must be round(int)"
    assert convertToHexadecimal("asdk") == \
        "number parameter must be round(int)"
