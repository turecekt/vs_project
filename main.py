"""
Integer to Roman numerals converter by Dominik Vanduch.

This console app was written to take integer and convert it into a Roman
numeral system as a term project for AP1VS.
"""


def int_to_roman(number):
    """
    Convert integer to Roman numeral system.

    Tests for this function:
    >>> int_to_roman(10)
    'X'
    >>> int_to_roman(468)
    'CDLXVIII'
    >>> int_to_roman(967)
    'CMLXVII'
    """
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]

    dictionary = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]

    roman_num = ''
    i = 0

    while number > 0:
        for _ in range(number // values[i]):
            roman_num += dictionary[i]
            number -= values[i]
        i += 1
    return roman_num


unconverted = int(input("Enter a number to be converted: "))

converted = int_to_roman(unconverted)

print(converted)
