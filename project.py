"""Tohle vezme input od uzivatele."""
userInp = input('Zadejte cele cislo na preklad :')
# Tohle prevede input od uzivatele na int aby to program mohl zpracovat


userInp = int(userInp)


class romanNum:
    """Vytvorime class romanNum kde vlozime funckci na preklad."""

    def intToRom(self, userInp):
        """Vezme input a prevede na rimske."""
        # Nadefinujeme si cisla na ktere pak budem odkazovat
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        # Nadefinujeme si symboly na ktere pak budem odkazovat
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        # Vytvorim transNum ktery zatim bude mit value prazdneho stringu

        transNum = ''

        # While loopem loopnu syb a val, priradim hodnotu k transNum
        # ktera odpovida danemu user inputu (userInp)

        i = 0

        while userInp > 0:
            for _ in range(userInp // val[i]):
                transNum += syb[i]
                userInp -= val[i]
            i += 1
        # Vratim transNum
        return transNum
# Do konzole vypisu prevedenou hodnotu userInp.
# V kozoli se ukaze hodnota cisla ktere zadal user v rimskych cislicih
print(romanNum().intToRom(userInp))

import unittest
from project import romanNum

class testOutput(unittest.TestCase):
    def test_deset(self):
        translator = romanNum()
        userInp = 10
        expected_output = 'X'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_nul(self):
        translator = romanNum()
        userInp = 0
        expected_output = ''
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_tisicJedna(self):
        translator = romanNum()
        userInp = 1001
        expected_output = 'MI'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def test_devetDevetDevet(self):
        translator = romanNum()
        userInp = 999
        expected_output = 'CMXCIX'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def dvaTisiceJedna(self):
        translator = romanNum()
        userInp = 2001
        expected_output = 'MMI'
        self.assertEqual(translator.intToRom(userInp), expected_output)

    def jedenact(self):
        translator = romanNum()
        userInp = 1
        expected_output = 'XI'
        self.assertEqual(translator.intToRom(userInp), expected_output)



if __name__ == '__main__':
    unittest.main()

