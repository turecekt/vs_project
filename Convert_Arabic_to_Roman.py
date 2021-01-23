"""
AUTOR: LADISLAV ŘEHÁK
TÉMA: ŘÍMSKÉ ČÍSLICE
"""


def arabic_to_roman(number):
    arabic = [1000, 900, 500, 400, 100,
              90, 50, 40, 10, 9, 5, 4, 1]

    roman = ["M", "CM", "D", "CD", "C", "XC",
             "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_number = ''
    i = 0
    while number > 0:
        for _ in range(number // arabic[i]):
            roman_number += roman[i]
            number -= arabic[i]
        i += 1
    return roman_number


def main():
    r_number = int(input("Vložte číslo, které chcete konvertovat: "))
    print("Číslo přeložené do římského systému: " + arabic_to_roman(r_number))


if __name__ == '__main__':
    main()
