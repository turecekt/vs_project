import re


def is_number_int(number):
    return re.match(r"[+]?\d+(\.0*)?$", number) is not None


def number_conversion(number, base_system):         # max base value = 36
    result = ""
    if int(number) == 0:
        result += str(number)
    else:
        while number > 0:
            inter = int(number) % base_system
            if inter <= 9:
                result += str(inter)
            else:
                result += chr(ord('A') + inter - 10)
            number //= base_system

    result = result[::-1]
    return result
