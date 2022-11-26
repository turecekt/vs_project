import re


def is_number_int(number):
    return re.match(r"[-+]?\d+(\.0*)?$", number) is not None


def number_conversion(number, base_system):  # max base value = 36
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
    number = input("Enter number in decimal base: ")
    base_system = input("Enter required base system: ")
    if is_number_int(number) is True:
        print("Result number is: ", number_conversion(number, base_system))
    else:
        print("You did not write right number. Try it again, dummy.")
        converter()
