# Function for converting integers to Roman numerals.
# Converts any positive Integer in range from 1 to 3999.
def integerToRoman(integer):

    # Checks if the input is really an integer in range 1-3999.
    # If not, function returns error message.
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

    # Returns value of the input integer in the system of Roman numerals.
    return roman


def romanToInteger(roman):

    allowedChars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for char in roman:

        if (char not in allowedChars):
            return "Obsahuje nepovolene znaky."

    parsed_roman = [roman[0]]

    i = 1
    while i < len(roman):

        last_roman = parsed_roman[len(parsed_roman) - 1]
        current_roman = roman[i]

        if (valueOf(last_roman + current_roman) > 0):
            parsed_roman[len(parsed_roman) - 1] = last_roman + current_roman

        else:
            parsed_roman.append(current_roman)

        i += 1

    integer = valueOf(parsed_roman[0])

    i = 1
    while i < len(parsed_roman):

        last_integer = valueOf(parsed_roman[i - 1])
        current_integer = valueOf(parsed_roman[i])

        if (last_integer > current_integer):

            if (getHighestUsableInteger(last_integer) >= current_integer):
                integer += current_integer

            else:
                return "Cislo je ve spatnem tvaru."

        else:
            return "Cislo je ve spatnem tvaru."

        i += 1

    return integer


def valueOf(roman_number):
    if (roman_number == 'I'):
        return 1

    elif (roman_number == 'II'):
        return 2

    elif (roman_number == 'III'):
        return 3

    elif (roman_number == 'IV'):
        return 4

    elif (roman_number == 'V'):
        return 5

    elif (roman_number == 'IX'):
        return 9

    elif (roman_number == 'X'):
        return 10

    elif (roman_number == 'XX'):
        return 20

    elif (roman_number == 'XXX'):
        return 30

    elif (roman_number == 'XL'):
        return 40

    elif (roman_number == 'L'):
        return 50

    elif (roman_number == 'XC'):
        return 90

    elif (roman_number == 'C'):
        return 100

    elif (roman_number == 'CC'):
        return 200

    elif (roman_number == 'CCC'):
        return 300

    elif (roman_number == 'CD'):
        return 400

    elif (roman_number == 'D'):
        return 500

    elif (roman_number == 'CM'):
        return 900

    elif (roman_number == 'M'):
        return 1000

    elif (roman_number == 'MM'):
        return 2000

    elif (roman_number == 'MMM'):
        return 3000

    else:
        return 0


def getHighestUsableInteger(number):
    if (number >= 1000 and number <= 3000):
        return 900

    elif (number == 900):
        return 90

    elif (number == 500):
        return 300

    elif (number >= 100 and number <= 400):
        return 90

    elif (number == 90):
        return 9

    elif (number == 50):
        return 30

    elif (number >= 10 and number <= 40):
        return 9

    elif (number == 9):
        return 0

    elif (number == 5):
        return 3

    elif (number >= 1 and number <= 4):
        return 0

    else:
        return 0
