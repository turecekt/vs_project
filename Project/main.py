"""Main Function."""

# library imports
import sys

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


def main():
    """Get arguments from console, then call functions to convert number."""
    if len(sys.argv) == 3:  # get arguments from terminal
        numeral_system_type_arg = sys.argv[1]
        input_number = int(sys.argv[2])

    # TODO refactor else case
    else:
        numeral_system_type_arg = "not valid"
        input_number = 0

    # enables functionality for both lowercase and uppercase arguments
    numeral_system_type_arg = numeral_system_type_arg.lower()

    # choose what argument is used
    if numeral_system_type_arg == "-b":
        print(decimalToBinary.convert(input_number))
    elif numeral_system_type_arg == "-o":
        print(decimalToOctal.convert(input_number))
    elif numeral_system_type_arg == "-h":
        print(decimalToHexadecimal.convert(input_number))
    else:
        print("Unable to convert")


if __name__ == '__main__':
    main()
