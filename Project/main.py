"""Main Function."""

# library imports
import sys

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


def convert_hexadecimal(input_number):
    """Convert decimal number to hexadecimal."""
    input_number = int(input_number)
    x = (input_number % 16)  # modulo
    chars = "0123456789ABCDEF"
    rest = input_number / 16  # rest after division

    # if rest equals zero, return characters where index is x
    if rest == 0:
        return chars[x]
    # if rest is not zero, use method "convert" recursively
    return convert_hexadecimal(rest) + chars[x]


def test_convert_hexadecimal():
    """Test function convert_hexadecimal."""
    if sys.version_info > (3, 0):
        assert convert_hexadecimal(100) == "064"
    else:
        assert convert_hexadecimal(100) == "64"


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
        print(convert_hexadecimal(input_number))
    else:
        print("Unable to convert")


if __name__ == '__main__':
    main()
