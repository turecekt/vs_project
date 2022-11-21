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
    print("\n")


def decode():
    userInput = input()
    separatedString = userInput.split('/')
    for item in separatedString:
        if item not in morseCode:
            print("#", end='', flush=True)
        else:
            print(alphabet[morseCode.index(item)], end='', flush=True)
    print("\n")


def main():
    while True:
        print("Chcete přeložit:")
        print("1 - text do morseovky")
        print("2 - morseovka do textu")
        print("3 - ukončit program")

        menuInput = input()
        if menuInput == "1":
            print("Zadejte vstup:")
            encode()
        elif menuInput == "2":
            print("Zadejte vstup:")
            decode()
        elif menuInput == "3":
            break
        else:
            print("Špatné číslo")


if __name__ == '__main__':
    main()
