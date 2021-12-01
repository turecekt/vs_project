"""Program pro překlad do morseovy abecedy a zpět."""

# Slovník pro překlad
DIR = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
       'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
       'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
       'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
       'Y': '-.--', 'Z': '--..',
       '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
       '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


# Překlad do morseovky
def morseovka(retezec):
    """Funkce morseovka převede vrací vstupní přetězec řevedený do morseovky.

    Argumenty:
        - retezec - Vstup funkce

    Vrací:
        - string - Výstup funkce
    """
    morse = []
    # přeložené znaky se ukládají do pole morse

    for i in retezec:
        if i in DIR:
            morse.append(DIR[i])

            # vložený znak je nalezen ve slovníku a vložen na konec pole morse

    return " ".join(morse)
    # přidání mezery na konec přeloženého znaku


# Hlavní funkce - input
def main():
    """Proměnné preklad je přidělen výsledek funkce morseovka.

    vstup.upper() = vložené písmeno je převedené na velký znak
    """
    vstup = input("Zadejte text: ")
    preklad = morseovka(vstup.upper())

    print(preklad)
    # Výstup přeloženého vstupu


if __name__ == "__main__":
    main()
