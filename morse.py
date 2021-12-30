"""Program pro překlad do morseovy abecedy a zpět."""

# Slovníky pro překlad do morseovy abecedy
DIR = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.',
                   '.': '.-.-.-', ',': '--..--', '-': '-....-', ':': '---...'}

# Záměna hodnot ve slovníku pro překlad z morseovy abecedy
DIR_Naopak = {value:key for key,value in DIR.items()}

def to_morse(retezec):
    """Funkce to_morse vrací vstupní řetězec převedený do morseovky.

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


def from_morse(retezec):
    """Funkce from_morse vrací vstupní řetězec převedený z morseovky.

    Argumenty:
        - retezec - Vstup funkce
    Vrací:
        - string - Výstup funkce
    """
    morse = retezec.split()
    # vstup se rozdělí na jednotlivé znaky které následně hledá ve slovníku
    preklad = []
    # přeložené znaky se ukládají do pole preklad

    for i in morse:
        if i in DIR_Naopak:
            preklad.append(DIR_Naopak[i])

            # vložený znak je nalezen ve slovníku a vložen na konec pole morse

    return "".join(preklad)


# Hlavní funkce


if __name__ == "__main__":
    operace = int(input("Vyberte si překlad:\n"
                        "1 - Do morseovky\n"
                        "2 - Z morseovky\n"))

    # Dle vybrané operace se následně provede překlad

    if operace == 1:
        vstup = input("Zadejte text k překladu do morseovky: ")
        preklad = to_morse(vstup.upper())
        print(preklad)

    elif operace == 2:
        vstup = input("Zadejte text k překladu z morseovky: ")
        preklad = from_morse(vstup)
        print(preklad)

    elif operace != 1 & operace != 2:
        print("Špatně zadaná operace")

    # V případě špatného výběru operace program končí


# Pytest pro převod do morseovky
def test_tomorse():
    """Funkce test_tomorse testuje zda funkce to_morse funguje správně."""
    assert to_morse('EA') == '. .-'
    assert to_morse('12') == '.---- ..---'
    assert to_morse('XYZ: 26, 3, 7') ==\
           '-..- -.-- --.. ---... ..--- -.... --..-- ...-- --..-- --...'


# Pytest pro převod z morseovky
def test_frommorse():
    """Funkce test_frommorse testuje zda funkce from_morse funguje správně."""
    assert from_morse('..... ----.') == '59'
    assert from_morse('. ..... --..-- -. --...') == 'E5,N7'
    assert from_morse('.---- ..--- ...-- -....- ....-'
                      ' ..... -.... -....- --... ---.. ----.') == '123-456-789'
