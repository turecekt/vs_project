def int_to_roman(number):
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
    while  number > 0:
        for _ in range(number // values[i]):
            roman_num += dictionary[i]
            number -= values[i]
        i += 1
    return roman_num


print(int_to_roman(int(input("Enter a number to be converted to Roman numeral system: "))))