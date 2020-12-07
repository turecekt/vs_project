"""Number to Rome Numeral converter.

This is a Python converter for numbers, it converts its input (form of a number)
and returns an output in the form of a Roman Numeral
"""


class Converter():
    """Convert number."""
    
    def convert(self, num):
        """Function convert returns a Roman Numeral based on argument num, which is a full number.

        Args:
            - num - Input of the function

        Returns:
            - output - Output of the function
        """
        numbers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        romannumbers = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman = ''
        i = 0
        while num > 0:
            for x in range(num // numbers[i]):
                roman += romannumbers[i]
                num -= numbers[i]
            i += 1
        return roman

if __name__ == '__main__':
    print('Running')

print('Zadejte hodnotu pro převod:')
numIn = int(input())
print(Converter().convert(numIn))
