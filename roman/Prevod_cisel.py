"""Prevod na rimske cislo."""


def prevod(cislo):
    """Prevod promenne cislo.

    >>> prevod(1)
    I
    """
    """Seznamy znaku a jejich hodnot."""
    hodnota = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    znak = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",
            "I"]
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
    print(prevod(int(input("Zadej číslo: "))))
