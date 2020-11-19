"""Převodník numerických soustav."""


def convertToBinary(number):
    """Vrací zadané číslo převedené do dvojkové soustavy.

    Arguments:
    number - číslo určené pro převod do dvojkové soustavy
    Returns:
    convertedNumber - číslo převedené do dvojkové soustavy
    """
    if number < 0:
        return "number parameter cant be negative"
    if not isinstance(number, int):
        return "number parameter must be round(int)"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 2 == 0:
            convertedNumber = "0" + convertedNumber
        else:
            convertedNumber = "1" + convertedNumber
        remainder = int(remainder / 2)

    return convertedNumber


def convertToOctal(number):
    """Vrací zadané číslo převedené do osmičkové soustavy.

    Arguments:
    number - číslo určené pro převod do osmičkové soustavy
    Returns:
    convertedNumber - číslo převedené do osmičkové soustavy
    """
    if number < 0:
        return "number parameter cant be negative"
    if not isinstance(number, int):
        return "number parameter must be round(int)"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 8 == 0:
            convertedNumber = "0" + convertedNumber
        if remainder % 8 == 1:
            convertedNumber = "1" + convertedNumber
        if remainder % 8 == 2:
            convertedNumber = "2" + convertedNumber
        if remainder % 8 == 3:
            convertedNumber = "3" + convertedNumber
        if remainder % 8 == 4:
            convertedNumber = "4" + convertedNumber
        if remainder % 8 == 5:
            convertedNumber = "5" + convertedNumber
        if remainder % 8 == 6:
            convertedNumber = "6" + convertedNumber
        if remainder % 8 == 7:
            convertedNumber = "7" + convertedNumber
        remainder = int(remainder / 8)

    return convertedNumber


def convertToHexadecimal(number):
    """Vrací zadané číslo převedené do šestnástkové soustavy.

    Arguments:
    number - číslo určené pro převod do šestnástkové soustavy
    Returns:
    convertedNumber - číslo převedené do šestnástkové soustavy
    """
    if number < 0:
        return "number parameter cant be negative"
    if not isinstance(number, int):
        return "number parameter must be round(int)"

    convertedNumber = ""
    remainder = number
    while remainder > 0:
        if remainder % 16 == 0:
            convertedNumber = "0" + convertedNumber
        if remainder % 16 == 1:
            convertedNumber = "1" + convertedNumber
        if remainder % 16 == 2:
            convertedNumber = "2" + convertedNumber
        if remainder % 16 == 3:
            convertedNumber = "3" + convertedNumber
        if remainder % 16 == 4:
            convertedNumber = "4" + convertedNumber
        if remainder % 16 == 5:
            convertedNumber = "5" + convertedNumber
        if remainder % 16 == 6:
            convertedNumber = "6" + convertedNumber
        if remainder % 16 == 7:
            convertedNumber = "7" + convertedNumber
        if remainder % 16 == 8:
            convertedNumber = "8" + convertedNumber
        if remainder % 16 == 9:
            convertedNumber = "9" + convertedNumber
        if remainder % 16 == 10:
            convertedNumber = "A" + convertedNumber
        if remainder % 16 == 11:
            convertedNumber = "B" + convertedNumber
        if remainder % 16 == 12:
            convertedNumber = "C" + convertedNumber
        if remainder % 16 == 13:
            convertedNumber = "D" + convertedNumber
        if remainder % 16 == 14:
            convertedNumber = "E" + convertedNumber
        if remainder % 16 == 15:
            convertedNumber = "F" + convertedNumber
        remainder = int(remainder / 16)

    return convertedNumber


def test_convertToBinary():
    """Otestuje správnost převodu do dvojkové soustavy."""
    assert convertToBinary(20) == "10100"


def test_convertToBinaryNegativeParameter():
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToBinary(-20) == \
        "number parameter cant be negative"


def test_convertToBinaryParameterNotRound():
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToBinary(20.5) == \
        "number parameter must be round(int)"


def test_convertToOctal():
    """Otestuje správnost převodu do osmičkové soustavy."""
    assert convertToOctal(20) == "24"


def test_convertToOctalNegativeParameter():
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToOctal(-20) == \
        "number parameter cant be negative"


def test_convertToOctalParameterNotRound():
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToBinary(20.5) == \
        "number parameter must be round(int)"


def test_convertToHexadecimal():
    """Otestuje správnost převodu do šestnástkové soustavy."""
    assert convertToHexadecimal(185) == "B9"


def test_convertToHexadecimalNegativeParameter():
    """Otestuje zda-li funkce nepřijímá jako argument záporná čísla."""
    assert convertToHexadecimal(-20) == \
        "number parameter cant be negative"


def test_convertToHexadecimalParameterNotRound():
    """Otestuje zda-li funkce nepřijímá jako argument desetinná čísla."""
    assert convertToBinary(20.5) == \
        "number parameter must be round(int)"
