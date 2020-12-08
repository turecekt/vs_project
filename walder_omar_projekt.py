"""Number converter.

This is a Python converter for normal numbers
it converts it's input (in the form of a number)
and returns an output in the form of a Roman Numeral
"""


class Converter():
    """Convert number."""

    def convert(self, num):
        """Function returns a Roman Numeral based on the input, which is a full number.

        Args:
            - num - Input of the function

        Returns:
            - roman - The converter number
        """
        # Vytvoříme pole pro obyčejné čísla
        numbers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        # Vytvoříme pole pro Římské číslice
        romannumbers = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        # Vytvoříme string, který bude return a bude mít převedené římské číslice
        roman = ''
        # Vytvoříme číslo pro pozice v polích
        i = 0
        # Zadáme podmínku, že když bude input číslo 0, tak je metoda hotová a vrátí Římskou číslici
        while num > 0:
            # For cyclus, který nám vídělí input číslo číslem z pole čísel se zbytkem, projede to celé pole
            # dokud mu nezbyde žádný zbytek
            for x in range(num // numbers[i]):
                # Přídá číslo z pole s Římskými číslicemi do outputu
                roman += romannumbers[i]
                # Odečte od input čísla hodnotu, která již byla převedena
                num -= numbers[i]
            # Přidá číslu i 1, aby se pole dále projeli pro další převod
            i += 1
        # Vrátí Římskou číslici
        return roman


    def test_convert(self):
        """Function test_convert tests, if the method converts correctly.

        Prints a message depending on the result of the test
        """
        # Nastavíme si dvě testovací čísla
        num1 = 1
        num2 = 586
        # Nastavíme si jaký by měl vyjít výsledek
        result1 = 'I'
        result2 = 'DLXXXVI'
        # Otestujeme, jestli se hodnoty shodují s tím, jak mají vyjít
        num1_test = Converter().convert(num1)
        num2_test = Converter().convert(num2)
        # Nastavíme if, pro obě situace
        if result1 == num1_test and result2 == num2_test:
            # Jestli se hodnoty rovnají, napíše na konzoli, že metoda pracuje
            print("Metoda convert pracuje.")
        else:
            # Jestli se hodnoty nerovanjí, napíše na konzoli, že metoda nepracuje
            print("Metoda convert nepracuje!")
            exit()


if __name__ == '__main__':
    print('Running')

# Zavoláme metodu pro testování funkčnosti metody convert
Converter().test_convert()
print('')
# Vytvoříme promměnou opakovani, která bude 0, dokud uživatel nezadá správnou hodnotu
opakovani = 0
while opakovani == 0:
    try:
        # Vložíme do konzole otázku pro uživatele, aby zadal číslici pro převod
        numIn = int(input('Zadejte hodnotu pro převod: '))
        # Nastaví výsledek (vloženou hodnotu) jako argument pro metodu convert a výsledek vložíme na konzoli
        print(Converter().convert(numIn))
        # Opakování ukončíme
        opakovani += 1
    except:
        print('')
        # Když uživatel zadá špatně (string nebo prázdné) input, konzole vypíše že je to napsané špatně
        # a celý proces opakuje
        print('Hodnota byla zadána ve špatném tvaru')
        print('')
