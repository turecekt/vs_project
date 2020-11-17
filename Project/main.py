# library imports
import sys

# module imports
import decimalToBinary
import decimalToOctal
import decimalToHexadecimal


def pass_args(numeral_system, input_number):
    return numeral_system, input_number


def main():
    if len(sys.argv) == 3:  # get arguments from terminal
        numeral_system_type_arg = sys.argv[1]
        input_number = int(sys.argv[2])
    else:
        # raise TypeError
        numeral_system_type_arg = "not valid"
        input_number = 0

    if numeral_system_type_arg == "-b":
        print(decimalToBinary.convert(input_number))
    if numeral_system_type_arg == "-o":
        print(decimalToOctal.convert(input_number))
    if numeral_system_type_arg == "-h":
        print(decimalToHexadecimal.convert(input_number))
    else:
        pass
        # print("Unable to convert")


if __name__ == '__main__':
    main()
