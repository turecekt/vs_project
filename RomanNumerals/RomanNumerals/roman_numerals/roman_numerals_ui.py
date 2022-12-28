"""Contains Roman Numerals UI."""

from pickle import TRUE
from roman_numerals.number_system_converter import (
        NumberSystemConverter as converter)


def roman_numerals_ui():
    """
    UI for converting integers to roman numbers and back.

    Converts any positive integer in range from 1 to 3999, and
    any roman number of valid format.
    """
    # Defining a constant.
    WRONG_INPUT_MESSAGE = "wrong input"

    # Main loop.
    while (TRUE):
        # Print of menu options.
        print()
        print("1 - integer to roman")
        print("2 - roman to integer")
        print("0 - exit")

        # Waiting for input.
        user_input = input("input: ")

        # If input is not numeric, wrong input message is printed
        # and loop continues.
        if (not user_input.isnumeric()):
            print(WRONG_INPUT_MESSAGE)
            continue

        # Converts input to integer.
        user_input = int(user_input)

        # If input is 1, function asks for integer to convert.
        if (user_input == 1):
            integer = input("integer = ")

            # If input is not numeric, wrong input message is printed
            # and loop continues.
            if (not integer.isnumeric()):
                print(WRONG_INPUT_MESSAGE)
                continue

            # Convert input to roman number.
            roman = converter.integer_to_roman(int(integer))

            # Print of converted number.
            print("roman = " + roman)

        # If input is 2, function asks for roman number to convert.
        elif (user_input == 2):
            roman = input("roman = ")

            # Convert input to integer.
            roman = converter.roman_to_integer(roman)

            # Print of converted number.
            print("integer = " + str(roman))

        # If input is 0, function ends.
        elif (user_input == 0):
            return

        # If input is something else, wrong input message is printed.
        else:
            print(WRONG_INPUT_MESSAGE)
