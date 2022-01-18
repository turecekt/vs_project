import unittest
from main import kodovat, dekodovat
"""
Tenhle kolekce nám umožňuje pracovat s písmeny,
 číslicemi a několik unikátních znaků,
 které pomocí funkcí lze kódovat a dekódovat.
Písmena v kolekci mají hodnotu key, znaky value.
"""
List = {
         'A':'.-',
         'B':'-...',
         'C':'-.-.',
         'D':'-..',
         'E':'.',
         'F':'..-.',
         'G':'--.',
         'H':'....',
         'I':'..',
         'J':'.---',
         'K':'-.-',
         'L':'.-..',
         'M':'--',
         'N':'-.',
         'O':'---',
         'P':'.--.',
         'Q':'--.-',
         'R':'.-.',
         'S':'...',
         'T':'-',
         'U':'..-',
         'V':'...-',
         'W':'.--',
         'X':'-..-',
         'Y':'-.--',
         'Z':'--..',
         '1':'.----',
         '2':'..---',
         '3':'...--',
         '4':'....-',
         '5':'.....',
         '6':'-....',
         '7':'--...',
         '8':'---..',
         '9':'----.',
         '0':'-----',
         ', ':'--..--',
         '.':'.-.-.-',
         '?':'..--..',
         '/':'-..-.',
         '-':'-....-',
         '(':'-.--.',
         ')':'-.--.-'
         }


def kodovat(text):
    """    Funkce přiřazuje z kolekce písmen danné znaky.
    Do funkce je vložena podmínka v případě, kdy v textu bude
    mezera.
    """
    ktext = ''
    for pismeno in text:
        if pismeno != ' ':
            ktext += List[pismeno] + ' '
        else:
            ktext += ' '

    return ktext


def dekodovat(text):
    """Funkce přiřazuje hodnoty z kolekce do písmen"""
    text += ' '
    dtext = ''
    citext = ''
    for letter in text:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                dtext += ' '
            else:
                dtext += list(List.keys())[list(
                    List.values()).index(citext)]
                citext = ''
               
    return dtext

if __name__ == '__main__':
    """Funkce, ktera umoznuje vybrat typ prevodu."""

    vyber = input("stiskni '1' pro kodovani textu"
                  ", stiskni '2' pro dekodovani textu: ")
    if vyber == "1":
        message = input("Zadej text, ktery chceš přeložit do morseovky: ")
        result = kodovat(message.upper())
        print(result)
    if vyber == "2":
        message = input("Zadej morseový kod, ktery chceš přeložit do textu: ")
        result = dekodovat(message.upper())
        print(result)
class Unittest_morseovka(unittest.TestCase):
    """Trida pro spusteni unit testu."""

    def test_kodovat_pismeno(self):
        """Test pro převod písmena na kod."""
        self.assertEqual(kodovat("A"), ".- ")

    def test_kodovat_veta(self):
        """Test pro převodu vety do morseovky"""
        self.assertEqual(kodovat(
            "MORSEOVKA"), "-- --- .-. ... . --- ...- -.- .- ")

    def test_kodovat_cislo(self):
        """Test pro převod číslic do morseovky."""
        self.assertEqual(kodovat(
            "1234567890"), ".---- ..--- ...-- ....- ....."
            " -.... --... ---.. ----. ----- ")

    def test_dekodovat_pismeno(self):
        """Test pro morseovky na pismeno."""
        self.assertEqual(dekodovat("-.--"), "Y")

    def test_dekodovat_text(self):
        """Test pro převod morseovky do textové věty."""
        self.assertEqual(dekodovat(
            ".--. .-. . ...- --- -..  -. .-  ... .-.."
            " --- ...- ---  --..  -.- --- -.. ..-"),
            "PREVOD NA SLOVO Z KODU")
