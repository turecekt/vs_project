"""Functions for converting values."""
import re


def is_number_int(number):
    """Validate the value.

    Checks if the specified string contains values representing integers.
    Both integers and integers written in float form are recognized.
    :param number: String
    :return: Bool
    """
    return re.match(r"[-+]?\d+(\.0*)?$", number) is not None


def number_conversion(number, base_system):  # max base value = 36
    """Converts the selected number to the selected number system.

    This function uses conditional statements to convert a number
    to the selected number system.
    If the specified number is equal to 0, zero is automatically returned.
    If the number is other than zero, the result is calculated
    by successive division.
    :param number: String
    :param base_system: String
    :return: String
    """
    result = ""
    number = int(number)
    base_system = int(base_system)
    if number == 0:
        result += str(number)
    else:
        while number > 0:
            inter = number % base_system
            if inter <= 9:
                result += str(inter)
            else:
                result += chr(ord("A") + inter - 10)
            number //= base_system

    result = result[::-1]
    return result


def converter():
    """Input values.

    The function requires two input values - a number and a number system.
    It checks if the values are entered correctly
    (correct number of inputs and the "number" value is an integer).
    If incorrect values are entered, the function asks for new values.

    :return: None
    """
    number = input("Enter number in decimal base: ")
    base_system = input("Enter required base system: ")
    if is_number_int(number) is True:
        print("Result number is: ", number_conversion(number, base_system))
    else:
        print("You did not write right number. Try it again, dummy.")
        converter()
