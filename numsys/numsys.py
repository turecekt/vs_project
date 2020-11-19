##
# @mainpage ČÍSELNÉ SOUSTAVY
# @version 0.0.1
# @section intro Úvod
# Závěrečný projekt do předmětu Nástroje pro vývoj softwarových projektů
#
# @section assignment Zadání
# VSTUP
# - Kladné celé číslo v desítkové soustavě
# - Cílová soustava (2, 8, 16, apod.)
# - Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu
#   (parametricky, dotazy na uživatele, či jinak).
# VÝSTUP
# - Číslo v cílové číselné soustavě
#
##

##
# @file numsys.py
# @brief Převodník numerických soustav
# @author Matěj Mazáč <m_mazac@utb.cz>
#
# @section description Několik funkcí převádějících
# celá, kladná čísla z desítkové soustavy
#
##

##
# @brief Vrací zadané číslo převedené do dvojkové soustavy
# @param[in] number číslo určené pro převod do dvojkové soustavy
#
##
def convertToBinary(number):
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
        print(remainder)

    return convertedNumber


##
# @brief Vrací zadané číslo převedené do osmičkové soustavy
# @param[in] number číslo určené pro převod do osmičkové soustavy
#
##
def convertToOctal(number):
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


##
# @brief Vrací zadané číslo převedené do šestnáctkové soustavy
# @param[in] number číslo určené pro převod do šestnáctkové soustavy
#
##
def convertToHexadecimal(number):
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
    assert convertToBinary(20) == "10100"


def test_convertToBinaryNegativeParameter():
    assert convertToBinary(-20) == "number parameter cant be negative"


def test_convertToBinaryParameterNotRound():
    assert convertToBinary(20.5) == "number parameter must be round(int)"


def test_convertToOctal():
    assert convertToOctal(20) == "24"


def test_convertToOctalNegativeParameter():
    assert convertToOctal(-20) == "number parameter cant be negative"


def test_convertToOctalParameterNotRound():
    assert convertToBinary(20.5) == "number parameter must be round(int)"


def test_convertToHexadecimal():
    assert convertToHexadecimal(185) == "B9"


def test_convertToHexadecimalNegativeParameter():
    assert convertToHexadecimal(-20) == "number parameter cant be negative"


def test_convertToHexadecimalParameterNotRound():
    assert convertToBinary(20.5) == "number parameter must be round(int)"
