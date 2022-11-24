"""Coding and decoding."""

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            ',', '.', '?', '-', '(', ')', ' ']

morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
             '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...',
             '---..', '----.', '-----',
             '--..--', '.-.-.-', '..--..', '-....-', '-.--.', '-.--.-', '']


def encode(encodeInput):
    """
    Encode normal alphabet to morse code.

    :param encodeInput: text to translate(string)
    """
    cypher = ""
    while not all(temp in alphabet for temp in encodeInput):
        encodeInput = input('Vstup obsahuje nepovolené znaky\n'
                            'Povolené znaky: [a-Z][0-9],.?()\n'
                            'Zadejte vstup znovu:\n').upper()

    for letter in encodeInput:
        cypher += morseCode[alphabet.index(letter)] + "/"
    return cypher


def decode(decodeInput):
    """
    Decode morse code to normal alphabet.

    :param decodeInput: text to decode(string)
    """
    cypher = ""
    separatedString = decodeInput.split('/')
    for item in separatedString:
        if item in morseCode:
            cypher += alphabet[morseCode.index(item)]
        else:
            cypher += "#"

    return cypher


def mainMenu(x):
    """
    Give number to user menu.

    :param x: input to menu(int)
    """
    if x == "1":
        userInput = input('Zadejte vstup:\n').upper()
        print(encode(userInput))
    elif x == "2":
        userInput = input('Zadejte vstup:\n')
        print(decode(userInput))
    elif x == "3":
        exit()
    else:
        print("Špatné číslo")
    return x


if __name__ == '__main__':
    """Console UI of the main function."""

    while True:
        menuInput = input('Chcete přeložit:\n'
                          '1 - text do morseovky\n'
                          '2 - morseovka do textu\n'
                          '3 - ukončit program\n')
        mainMenu(menuInput)
