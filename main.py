from unidecode import unidecode

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            ',', '.', '?', '-', '(', ')', ' ']

morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
             '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
             '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
             '--..--', '.-.-.-', '..--..', '-....-', '-.--.', '-.--.-', '']


def encode():
    userInput = unidecode(input()).upper()

    while not all(temp in alphabet for temp in userInput):
        print("Vstup obsahuje nepovolené znaky")
        print("Povolené znaky: [a-Z][0-9],.?()")
        print("Zadejte vstup znovu:")
        userInput = unidecode(input()).upper()

    for letter in userInput:
        print(morseCode[alphabet.index(letter)] + "/", end='', flush=True)


def decode():
    userInput = input()
    separatedString = userInput.split('/')
    for item in separatedString:
        if item not in morseCode:
            print("#", end='', flush=True)
        else:
            print(alphabet[morseCode.index(item)], end='', flush=True)

decode()


