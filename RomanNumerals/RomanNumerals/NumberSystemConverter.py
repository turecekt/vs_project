"""
NumberSystemConverter Package
----------------------------------
Contains functions for converting between numeric systems.
"""


def integerToRoman(integer):
    """
    Function for converting integers to Roman numbers.
    Converts any positive integer in range from 1 to 3999.

    :param name: integer - Number to be converted.
    :param type: int
    :return: str
    """

    # Checks if the input is None.
    if (integer is None):
        return "Input can not be None."

    # Checks if the input is really an integer in range 1-3999.
    if (not str(integer).isnumeric() or (integer < 1 or integer > 3999)):
        return "Input must be any positive integer from 1 to 3999."

    # Declaration of the variable "roman", which will represent
    # the value of the input integer in the system of Roman numerals.
    roman = ""

    # Filling variable "roman" with Roman numerals.
    while (integer > 0):

        if (integer >= 1000):
            integer -= 1000
            roman += "M"

        elif (integer >= 900):
            integer -= 900
            roman += "CM"

        elif (integer >= 500):
            integer -= 500
            roman += "D"

        elif (integer >= 400):
            integer -= 400
            roman += "CD"

        elif (integer >= 100):
            integer -= 100
            roman += "C"

        elif (integer >= 90):
            integer -= 90
            roman += "XC"

        elif (integer >= 50):
            integer -= 50
            roman += "L"

        elif (integer >= 40):
            integer -= 40
            roman += "XL"

        elif (integer >= 10):
            integer -= 10
            roman += "X"

        elif (integer >= 9):
            integer -= 9
            roman += "IX"

        elif (integer >= 5):
            integer -= 5
            roman += "V"

        elif (integer >= 4):
            integer -= 4
            roman += "IV"

        elif (integer >= 1):
            integer -= 1
            roman += "I"

    # Returns value of the input in the system of Roman numerals.
    return roman


def romanToInteger(roman):
    """
    Function for converting Roman numbers to integers.
    Converts any Roman number of valid format.

    :param name: roman - Number to be converted.
    :param type: str
    :return: int
    """

    # Checks if the input is None.
    if (roman is None):
        return "Input can not be None."

    # Make sure the input is a string.
    roman = str(roman)

    # Defining allowed characters.
    allowedChars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    # Checks if the input contains only allowed characters.
    for char in roman:
        if (char not in allowedChars):
            return "Contains illegal characters."

    # Declaration of the variable "parsed_roman", which will contain
    # individual numerals.
    parsed_roman = [roman[0]]

    # Counter initialization.
    i = 1

    # Filling variable "parsed_roman" with individual numerals.
    while i < len(roman):

        # "last_roman" represents the last numeral that was inserted
        # into "parsed_roman".
        last_roman = parsed_roman[len(parsed_roman) - 1]

        # "current_roman" represents next character from "roman".
        current_roman = roman[i]

        # If combination of "last_roman" and "current_roman" results
        # in a valid numeral, last numeral in "parsed_roman" is replaced
        # by this combination.
        if (valueOf(last_roman + current_roman) > 0):
            parsed_roman[len(parsed_roman) - 1] = last_roman + current_roman

        # If not, "current_roman" is added to "parsed_roman" like a new
        # last numeral.
        else:
            parsed_roman.append(current_roman)

        # Counter increment.
        i += 1

    # Declaration of the variable "integer", which will represent
    # the value of the input in the decimal system.
    integer = valueOf(parsed_roman[0])

    # Counter initialization.
    i = 1

    # Filling variable "integer" with its value.
    while i < len(parsed_roman):

        # "last_integer" represents the value of last numeral that was ad0ded.
        last_integer = valueOf(parsed_roman[i - 1])

        # "current_integer" represents the value that will be added
        # in the current step.
        current_integer = valueOf(parsed_roman[i])

        # If "last_integer" is greater than "current_integer" and highest
        # usable integer after "last_integer" is greater of equal to
        # "current_integer", it means, that "roman" is in correct format
        # and "current_integer" is added to "integer".
        if (last_integer > current_integer and
                getHighestUsableNumeralAfter(last_integer) >= current_integer):
            integer += current_integer

        # If not, error message is returned.
        else:
            return "Invalid format."

        # Counter increment.
        i += 1

    # Returns value of the input in the decimal system.
    return integer


def valueOf(roman_numeral):
    """
    Function for converting Roman numerals to integers.
    Converts any valid Roman numeral.
    If numeral is not valid, returns 0.

    :param name: roman_numeral - Numeral to be converted.
    :param type: str
    :return: int
    """

    if (roman_numeral == 'I'):
        return 1

    elif (roman_numeral == 'II'):
        return 2

    elif (roman_numeral == 'III'):
        return 3

    elif (roman_numeral == 'IV'):
        return 4

    elif (roman_numeral == 'V'):
        return 5

    elif (roman_numeral == 'IX'):
        return 9

    elif (roman_numeral == 'X'):
        return 10

    elif (roman_numeral == 'XX'):
        return 20

    elif (roman_numeral == 'XXX'):
        return 30

    elif (roman_numeral == 'XL'):
        return 40

    elif (roman_numeral == 'L'):
        return 50

    elif (roman_numeral == 'XC'):
        return 90

    elif (roman_numeral == 'C'):
        return 100

    elif (roman_numeral == 'CC'):
        return 200

    elif (roman_numeral == 'CCC'):
        return 300

    elif (roman_numeral == 'CD'):
        return 400

    elif (roman_numeral == 'D'):
        return 500

    elif (roman_numeral == 'CM'):
        return 900

    elif (roman_numeral == 'M'):
        return 1000

    elif (roman_numeral == 'MM'):
        return 2000

    elif (roman_numeral == 'MMM'):
        return 3000

    else:
        return 0


def getHighestUsableNumeralAfter(number):
    """
    Returns decimal value of highest usable Roman numeral after "number".

    :param name: number - Value of roman numeral.
    :param type: int
    :return: int
    """

    if (number is None):
        return 0

    if (not str(number).isnumeric()):
        return 0

    if (number >= 1000 and number <= 3000):
        return 900

    if (number == 900):
        return 90

    if (number == 500):
        return 300

    if (number >= 100 and number <= 400):
        return 90

    if (number == 90):
        return 9

    if (number == 50):
        return 30

    if (number >= 10 and number <= 40):
        return 9

    if (number == 9):
        return 0

    if (number == 5):
        return 3

    if (number >= 1 and number <= 4):
        return 0

    return 0


def coverage():

    integerToRoman(None)
    integerToRoman(0)
    integerToRoman(4000)
    integerToRoman(3.5)
    integerToRoman(1666)
    integerToRoman(999)
    integerToRoman(444)

    romanToInteger(None)
    romanToInteger(1)
    romanToInteger("p")
    romanToInteger("CCM")
    romanToInteger("XCL")
    romanToInteger("MD")

    valueOf(None)
    valueOf("I")
    valueOf("II")
    valueOf("III")
    valueOf("IV")
    valueOf("V")
    valueOf("IX")
    valueOf("X")
    valueOf("XX")
    valueOf("XXX")
    valueOf("XL")
    valueOf("L")
    valueOf("XC")
    valueOf("C")
    valueOf("CC")
    valueOf("CCC")
    valueOf("CD")
    valueOf("D")
    valueOf("CM")
    valueOf("M")
    valueOf("MM")
    valueOf("MMM")

    getHighestUsableNumeralAfter(1000)
    getHighestUsableNumeralAfter(900)
    getHighestUsableNumeralAfter(500)
    getHighestUsableNumeralAfter(100)
    getHighestUsableNumeralAfter(90)
    getHighestUsableNumeralAfter(50)
    getHighestUsableNumeralAfter(10)
    getHighestUsableNumeralAfter(9)
    getHighestUsableNumeralAfter(5)
    getHighestUsableNumeralAfter(1)
    getHighestUsableNumeralAfter(None)
    getHighestUsableNumeralAfter("I")
    getHighestUsableNumeralAfter(4000)


if __name__ == '__main__':
    coverage()
