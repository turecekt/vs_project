"""Importovani knihovny unittest."""
import unittest


class TestMethods(unittest.TestCase):
    """Trida urcena k testovani cisel a k nim prirazenym hodnot."""

    def test1(self):
        """Kontrola správné hodnoty."""
        self.assertEqual(prevod(1), "I")
        self.assertEqual(prevod(5), "V")
        self.assertEqual(prevod(10), "X")
        self.assertEqual(prevod(50), "L")
        self.assertEqual(prevod(100), "C")
        self.assertEqual(prevod(500), "D")
        self.assertNotEqual(prevod(1000), "D")


"""Prevod na rimske cislo."""


def prevod(cislo):
    """Prevod promenne cislo.

    >>> prevod(1)
    'I'
    """
    """Seznamy znaku a jejich hodnot."""
    hodnota = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    znak = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
            "IV", "I"]
    """Vystup prevodu na rimske cislo."""
    rimske_cislo = ''
    """Promenna urcujici pozici v seznamech."""
    pozice = 0
    while cislo > 0:
        """Hodnota vydeli celociselne se zaokrouhlenim dolu vstup."""
        a = (cislo // hodnota[pozice])
        b = 0
        for b in range(a):
            rimske_cislo = rimske_cislo + znak[pozice]
            cislo = cislo - hodnota[pozice]
        pozice = pozice + 1
    return rimske_cislo


if __name__ == '__main__':
    unittest.main(exit=False)
    cislo = int(input("Zadej čislo: "))
    if cislo < 0:
        print("Číslo nemůže bý záporné")
    elif cislo == 0:
        print("Číslo nesmí být nula")
    else:
        print(prevod(cislo))
