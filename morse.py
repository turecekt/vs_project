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


def encode(userInput):
    cypher = ""
    while not all(temp in alphabet for temp in userInput):
        print("Vstup obsahuje nepovolené znaky")
        print("Povolené znaky: [a-Z][0-9],.?()")
        print("Zadejte vstup znovu:")
        userInput = unidecode(input()).upper()

    for letter in userInput:
        cypher += morseCode[alphabet.index(letter)] + "/"
    return cypher


def decode(userInput):
    cypher = ""
    separatedString = userInput.split('/')
    for item in separatedString:
        if item not in morseCode:
            cypher += "#"
        else:
            cypher += alphabet[morseCode.index(item)]

    return cypher


def main():
    while True:
        print("Chcete přeložit:")
        print("1 - text do morseovky")
        print("2 - morseovka do textu")
        print("3 - ukončit program")

        menuInput = input()
        if menuInput == "1":
            print("Zadejte vstup:")
            userInput = unidecode(input()).upper()
            print(encode(userInput))
        elif menuInput == "2":
            print("Zadejte vstup:")
            userInput = input()
            print(decode(userInput))
        elif menuInput == "3":
            break
        else:
            print("Špatné číslo")


if __name__ == '__main__':
    main()
