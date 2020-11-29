"""Main Function."""

# library imports
import sys


def convert_binary(input_number):
    """Convert decimal number to binary."""
    binar = ''
    if input_number == 0:
        binar = '0' + binar
    else:
        # Cycle and divide number that is higher than 0
        while input_number > 0:
            binar = str(input_number % 2) + binar
            input_number = input_number // 2
    # Returns converted binary number
    return binar


def test_convert_binary():
    """Test function convert_binary."""
    assert convert_binary(78) == "1001110"
    assert convert_binary(1) == "1"
    assert convert_binary(100) == "1100100"
    assert convert_binary(2020) == "11111100100"


def convert_octal(input_number):
    """Convert decimal number to octal."""
    text = ""
    k = []

    if input_number == 0:
        text = '0'

    while input_number > 0:
        # calc
        a = int(input_number % 8)

        # a add to array
        k.append(a)

        # calc
        input_number = (input_number - a) / 8

        # load array
        text = ""

    # turn the array
    for j in k[::-1]:
        text = text + str(j)

    return text


def test_convert_octal():
    """Test function convert decimal num to octal."""
    assert convert_octal(156) == "234"
    assert convert_octal(0) == "0"
    assert convert_octal(123456789) == "726746425"
    assert convert_octal(2020) == "3744"


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
        print(convert_binary(input_number))
    elif numeral_system_type_arg == "-o":
        print(convert_octal(input_number))
    elif numeral_system_type_arg == "-h":
        print(convert_hexadecimal(input_number))
    else:
        print("Unable to convert")


if __name__ == '__main__':
    main()
