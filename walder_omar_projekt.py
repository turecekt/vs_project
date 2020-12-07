"""Number to Rome Numeral converter.

This is a Python converter for numbers, it converts it's input (form of a number)
and returns an output in the form of a Roman Numeral
"""


class Converter():
    """Convert number."""
    
    def convert(self, num):
        """Function convert returns a Roman Numeral based on argument num, which is a full number.

        Args:
            - num - Input of the function

        Returns:
            - roman - The converter number
        """
        #Vytvoříme pole pro obyčejné čísla
        numbers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        #Vytvoříme pole pro Římské číslice
        romannumbers = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        #Vytvoříme string, který bude return a bude mít převedené římské číslice
        roman = ''
        #Vytvoříme číslo pro pozice v polích
        i = 0
        #Zadáme podmínku, že když bude input číslo 0, tak je metoda hotová a vrátí Římskou číslici
        while num > 0:
            #For cyclus, který nám vídělí input číslo číslem z pole čísel se zbytkem, projede to celé pole
            #dokud mu nezbyde žádný zbytek
            for x in range(num // numbers[i]):
                #Přídá číslo z pole s Římskými číslicemi do outputu
                roman += romannumbers[i]
                #Odečte od input čísla hodnotu, která již byla převedena
                num -= numbers[i]
            #Přidá číslu i 1, aby se pole dále projeli pro další převod
            i += 1
        #Vrátí Římskou číslici
        return roman


    def test_convert(self):
        """Function test_convert tests, if the method converts correctly.

        Prints a message depending on the result of the test
        """
        num1 = 1
        num2 = 586
        result1 = 'I'
        result2 = 'DLXXXVI'
        num1_test = Converter().convert(num1)
        num2_test = Converter().convert(num2)
        if result1 == num1_test and result2 == num2_test:
            print("Metoda convert pracuje.")
        else:
            print("Metoda convert nepracuje!")


    def test_convertInput()
        """Function test_convertInput tests, if the input for the method convert is a number and isn't blank

        Prints a message depending on the result of the test
        """

if __name__ == '__main__':
    print('Running')

Converter().test_convert()
#Vložíme do konzole otázku pro uživatele, aby zadal číslici pro převod
print('Zadejte hodnotu pro převod:')
#Nastaví výsledek (vloženou hodnotu) jako promměnou, aby jsme s ní mohli pracovat
#numIn = int(input())
numIn = input()
#Vloženou hodnotu vložíme do metody convert, aby ji převedla
print(Converter().convert(numIn))
