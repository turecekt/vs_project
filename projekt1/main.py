"""
Tento Program slouží k překládání textu do morseovy abecedy a zpět.
Uživatel zadá libovolný text do konzole, algoritmus rozpozná jestli je
na vstupu zadána zpráva v morseově abecedě nebo pomocí znaků klasické abecedy.
Uživatel může zadat velká i malá písmena bez diakritiky, čísla i jiné znaky.
Na výstupu uživatel získá zašifrovaný nebo rozšifrovaný text.
"""
# Knihovna Morseovy Abecedy
import string

MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


# Funkce, která zajištuje zašifrování prostého textu do Morseovy abecedy
def zasifrovani(zprava):
    sifra = ''
    for pismeno in zprava:
        if pismeno != ' ':  # Pokud je ve zprávě písmeno,
            sifra += MORSE_CODE[pismeno] + ' '  # program vloží příslušný kod z Morseovy abecedy
        else:

            sifra += ' '  # Pokud je ve zprávě mezera, program vloží mezeru mezi znaky

    return sifra  # Funkce vrátí přeloženou zprávu


# Funkce která zajištuje rozšifrování textu z Morseovy abecedy
def rozsifrovani(zprava):
    zprava += ' '  # Přidána mezera na konec zprávy,

    text = ''
    citext = ''  # Vymazání uložené zprávy
    for pismeno in zprava:

        if pismeno != ' ':  # Podmínka kontrolující mezery ve zprávě

            i = 0  # Počítadlo mezer

            citext += pismeno  # Ukládání morseovky po jednom znaku


        else:
            # Pokud i=1, znamená to nový znak
            # Pokud i=2, znamená to nové slovo
            i += 1

            if i == 2:
                # Přidání mezery k oddělení slov
                text += ' '
            else:
                # Přístup ke knihovně morseovy abecedy přes hodnoty znaku
                text += list(MORSE_CODE.keys())[
                            list(MORSE_CODE.values()).index(citext)
                        ]
                citext = ''

    return text  # Funkce vrátí přeloženou zprávuS


def main():
    print("Vlož text (bez diakritiky):")  # Vypsání zprávy na konzoli
    zprava = input()  # Načtení zprávy z konzole a přiřazení
    if zprava[0] in (".", "-"):  # Pokud zpráva začíná "." nebo "-" program zavolá funkci rozsifrovani
        result = rozsifrovani(zprava)
    else:  # Pokud zprána nezačíná "." nebo "-" znamená to že je zpráva napsáná klasickou abecedou a program zavolá funkci zasifrovani
        zprava = zprava.upper()  # Převede zprávu z konzole na velká písmena
        result = zasifrovani(zprava)

    print(result)  # Program vypíše výsledek na konzoli


def testMorseDoTextu(zprava):
    zprava = "SOS"
    zprava = zprava.upper()
    result = zasifrovani(zprava)
    assert result == "... --- ..", "SOS je ... --- ..."


# Ukončení main funkce
if __name__ == '__main__':
    main()
