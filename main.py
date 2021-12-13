"""Program na kódování a dekódování Morseovy abecedy."""
# Slovník pro Morseovu abecedu.
morse_dict = {
    'A': '.-',   'B': '-...',
    'C': '-.-.', 'D': '-..',  'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---',  'P': '.--.', 'Q': '--.-',
    'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}


def code(text):
    """
    Funkce na přepsání písmen a čísel do morseovky.

    >>> code('123 45')
    '.---- ..--- ...-- | ....- .....'
    >>> code('Ahoj')
    '.- .... --- .---'
    >>> code('abeceda')
    '.- -... . -.-. . -.. .-'
    >>> code('Novy rok 2022')
    '-. --- ...- -.-- | .-. --- -.- | ..--- ----- ..--- ..---'
    """
    text = text.upper()
    ret = ""

    for letter in text:
        if letter in morse_dict:
            ret += morse_dict[letter] + " "
        else:
            ret += "| "
    return ret.strip()


def decode(text):
    """
    Funkce na přepsání morseovky na písmena a čísla.

    >>> decode('.... . .... .!')
    'Error'
    >>> decode('.--. . ... | -.- --- -.-. -.- .-')
    'PES KOCKA'
    >>> decode('-- --- .-. ... . | .- .-.. .--. .... .- -... . -')
    'MORSE ALPHABET'
    >>> decode('-.-. .. -.-. .- -.. .- ...-- ...-- ----- .----')
    'CICADA3301'
    """
    ret = ""

    letters = text.split(" ")
    for letter in letters:
        if letter == "|":
            ret += " "
        elif letter in morse_dict.values():
            ret += get_key(letter)
        else:
            return "Error"

    return ret.strip()


def get_key(val):
    """Překlad textu jendnoho písmene."""
    for key, value in morse_dict.items():
        if val == value:
            return key
    return ""


if __name__ == '__main__':
    """Hlavní funkce main. """

    print("Zvolte akci: ")
    choice = str(input("1 - Převod do Morseovky \n2 - Převod z Morseovky\n"))
    if(choice == "1" or choice == "2"):
        mess = str(input("Zadejte text k převodu: "))

    if choice == "1":
        print(f'Původni text: {mess} \nPřeložený text: {code(mess)}')
    elif choice == "2":
        if decode(mess) == "Error":
            print('Původní text není správně zakódován')
        else:
            print(f'Původni text: {mess} \nPřeložený text: {decode(mess)}')
    print('\nKonec Programu')


# Unit testy.
def test_code():
    """Unit test funkce Code."""
    assert code("51") == "..... .----"
    assert code("SOS") == "... --- ..."
    assert code("Zlin UTB") == "--.. .-.. .. -. | ..- - -..."
    assert code("Software") == "... --- ..-. - .-- .- .-. ."


def test_decode():
    """Unit test funkce Decode."""
    assert decode("..... .----") == "51"
    assert decode("... | ---") == "S O"
    assert decode("..--- .---- | ...- .- -. --- -.-. .") == "21 VANOCE"
    assert decode("'-.-' --- .-.. x") == "Error"

def test_get_key():
    """Unit test funkce Get_key."""
    assert get_key('.-..') == "L"
    assert get_key('...-') == "V"
    assert get_key('..-.') == "F"
    assert get_key('x-x') == ""
