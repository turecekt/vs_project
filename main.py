import unittest

"""Prevod arabskeho cisla na rimske. VS_Project."""


# funkce pro prevod arabskeho cisla na rimska
def prevod(cislo):
    """Prevede cislo na rimsky string."""
    # rimska cisla
    rimska = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    # arabska cisla
    arabska = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    rimska_cislice = ''
    i = 0
    # zacneme loop dokud neni cislo 0
    while cislo > 0:
        # do stringu zapiseme ekvivalent arabskeho cisla rimskym
        # a ubereme z puvodniho cisla
        for _ in range(cislo // arabska[i]):
            rimska_cislice += rimska[i]
            cislo -= arabska[i]
        i += 1
    # vracime hotovy string
    return rimska_cislice


# try/except je zde kvuli moznosti nezadani cisla
try:
    print("Rimska cislice: ", prevod(int(input("Zadej cislo: "))))
except Exception as ex:
    print("Spatne zadana hodnota! Hodnota musi byt cislo!")


class Test(unittest.TestCase):
    def doTest(self):
        self.assertEqual(prevod(1), "I")
        self.assertEqual(prevod(10), "X")
        self.assertEqual(prevod(24), "XXIV")
