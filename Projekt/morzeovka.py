"""Modul pro prekladani textu z morzeovky do abecedy a opacne."""


abeceda = {'1': '.----', '2': '..---', '3': '...--', '4': '....-',
           '5': '.....', '6': '-....', '7': '--...', '8': '---..',
           '9': '----.', '0': '-----', 'a': '.-', 'b': '-...',
           'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
           'h': '....', 'ch': '----', 'i': '..', 'j': '.---', 'k': '-.-',
           'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
           'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', ' ': '',
           'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

morzeovka = {'.----': '1', '..---': '2', '...--': '3', '....-': '4',
             '.....': '5', '-....': '6', '--...': '7', '---..': '8',
             '----.': '9', '-----': '0',  '.-': 'a', '-...': 'b',
             '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
             '....': 'h', '----': 'ch', '..': 'i', '.---': 'j',
             '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
             '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
             '..-': 'u', '...-': 'v',  '.--': 'w', '-..-': 'x', '-.--': 'y',
             '--..': 'z', ' ': ''}


def ab2mor(zprava):
    """
    Prelozeni z abecedy do morzeovky.

    Vrati zadany text v morzeovce
    >>> ab2mor("a1")
    '.- .---- '
    """
    c = ""
    for i in str(zprava.lower()):
        try:
            c += abeceda[i] + " "
        except KeyError:
            print("Text neni validni")
            break
    return c


def mor2ab(zprava):
    """
    Prelozeni z morzeovky do abecedy.

    Vrati zadany text v abecede
    >>> mor2ab("....- ....")
    '4h'
    """
    znak = ""
    vystup = ""
    x = 1
    for i in str(zprava):
        if x == len(zprava):
            znak += str(i)
            try:
                vystup += morzeovka[znak]
            except KeyError:
                print("Text neni validni")
                break
            break
        elif i == " ":
            try:
                vystup += morzeovka[znak]
            except KeyError:
                print("Text neni validni")
                break
            znak = ""
            x += 1
        elif i == "." or i == "-":
            znak += str(i)
            x += 1
        else:
            print("Text neni validni")
            break
    return vystup


if __name__ == "__main__":
    print("Vyberte moznost: \n1. Prelozeni z morzeovky",
          "\n2. Prelozeni do morzeovky")
    user_input = input(": ")
    if user_input == "1":
        print("Zadejte zpravu v morzeovce")
        text_input = input(": ")
        print("Prelozena zprava:", mor2ab(text_input))
    elif user_input == "2":
        print("Zadejte zpravu pro prelozeni do morzeovky")
        text_input = input(": ")
        print("Prelozena zprava:", ab2mor(text_input))
    else:
        print("Neplatny vyber")


def test_ab2mor():
    """Testy prelozeni do morzeovky jenom pismena."""
    assert(ab2mor("abcd")) == ".- -... -.-. -.. "


def test_mor2ab():
    """Testy prelozeni z morzeovky jenom cisla."""
    assert(mor2ab("....- --...")) == "47"


def test_ab2mor_no_input():
    """Testy prelozeni bez inputu."""
    assert(ab2mor("")) == ""


def test_ab2mor_numbers():
    """Testy prelozeni do morzeovky jenom cisla."""
    assert(ab2mor("123")) == ".---- ..--- ...-- "
