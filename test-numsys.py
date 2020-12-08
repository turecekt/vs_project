"""Testy převodník numerických soustav."""
from numsys import convertToBinary, convertToOctal, convertToHexadecimal, main

def test_main():
    """Otestuje zda-li funkce nepřijímá moc argumentů."""
    assert main("aaa") == "Too much arguments"
    """Otestuje zda-li funkce nepřijímá málo argumentů."""
    assert main("a") == "Too few arguments"
    """Otestuje zdali je volba převodu ve správném tvaru"""
    assert main("aa") == "Wrong dimension choice"
    """Otestuje zdali je vstup čísla k převodu ve správném tvaru"""
    assert main("1a") == "You must type in round number"
    """Otestuje zdali je vstup čísla k převodu ve správném tvaru"""
    assert main("11") == "1"


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
