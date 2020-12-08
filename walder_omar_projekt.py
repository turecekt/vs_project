"""Convert normal number to Roman numeral.

This is a Python converter for normal numbers
it converts it's input (in the form of a number)
and returns an output in the form of a Roman Numeral
"""


def convert(num):
    """Convert a normal number into a Roman numeral.

    This method convert its input (a number) and based on it
    returns it converted into Roman numerals

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
    # Vytvoříme string, který bude mít převedené římské číslice
    roman = ''
    # Vytvoříme číslo pro pozice v polích
    i = 0
    # Když bude input číslo 0, tak je metoda hotová a vrátí Římskou číslici
    while num > 0:
        # For cyclus, který vídělí input číslem, z pole numbers, se zbytkem
        # projede to celé pole dokud mu nezbyde žádný zbytek
        for x in range(num // numbers[i]):
            # Přídá číslo z pole s Římskými číslicemi do outputu
            roman += romannumbers[i]
            # Odečte od input čísla hodnotu, která již byla převedena
            num -= numbers[i]
        # Přidá číslu i 1, aby se pole dále projeli pro další převod
        i += 1
    # Vrátí Římskou číslici
    return roman


def test_convert():
    """Function tests, if the method converts correctly."""
    assert convert(1) == "I"
    assert convert(586) == "DLXXXVI"


def test_convertInput():
    """Function tests, if the input for convert is correct."""
    num = 250
    assert (num) != ""
    assert isinstance(num, int)


if __name__ == '__main__':
    # Vytvoříme promměnou opakovani, která bude 0
    # dokud uživatel nezadá správnou hodnotu
    opakovani = 0
    while opakovani == 0:
        # Vložíme do konzole otázku pro uživatele
        # aby zadal číslici pro převod
        numIn = int(input('Zadejte hodnotu pro převod: '))
        test_convertInput(numIn)
        # Nastaví výsledek (vloženou hodnotu) jako argument
        # pro metodu convert, výsledek vložíme na konzoli
        print(convert(numIn))
        # Opakování ukončíme
        opakovani += 1
