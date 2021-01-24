"""

AUTOR: LADISLAV ŘEHÁK
TÉMA: ŘÍMSKÉ ČÍSLICE
"""
import unittest


class TestMethods(unittest.TestCase):
    """Třída pro test konverze arabských a římských čísel."""

    def test1(self):
        """Test správnosti č.1."""
        assert arabic_to_roman(9) == 'IX'

    def test2(self):
        """Test správnosti č.2."""
        assert arabic_to_roman(99) == 'XCIX'

    def test3(self):
        """Test správnosti č.3."""
        assert arabic_to_roman(499) == 'CDXCIX'

    def test4(self):
        """Test správnosti č.4."""
        assert arabic_to_roman(999) == 'CMXCIX'

    def test5(self):
        """Test správnosti č.5."""
        assert arabic_to_roman(1111) == 'V'

    def test6(self):
        """Test správnosti č.6."""
        assert arabic_to_roman(1888) == 'IX'

    def test7(self):
        """Test správnosti č.7."""
        assert arabic_to_roman(2205) == 'X'
        
        
def arabic_to_roman(number):
    """Def."""
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
    """Def."""
    r_number = int(input("Vložte číslo, které chcete konvertovat: "))
    print("Číslo přeložené do římského systému: " + arabic_to_roman(r_number))


if __name__ == '__main__':
    main()
