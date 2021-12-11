"""Library for morse alphabet."""
morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
                    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
                    'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
                    'r': '.-.', 's': '...', 't': '-',
                    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                    '9': '----.', ' ': '/', '': ''}

splitCharacter = ' '
errorMessage = "Morse code is not valid!"


"""This will convert letters into morse code"""


def letter2morse(letter: str) -> str:
    return morse[letter]


"""This will convert morse code into letters"""


def morse2letter(mor: str) -> str:
    return list(morse.keys())[list(morse.values()).index(mor)]


"""This will convert text into morse code"""


def text2morse(text: str) -> str:
    letters = list(text.lower())
    morseCode = ""
    for let in letters:
        if let in morse:
            morseCode += letter2morse(let) + splitCharacter
    return morseCode


"""This will convert morse code into text"""


def morse2text(morseText: str) -> str:
    arrayMorse = morseText.split(splitCharacter)
    text = ""
    for m in arrayMorse:
        if m in list(morse.values()):
            text += morse2letter(m)
        else:
            text = errorMessage
            break
    return text


"""Main method."""
if __name__ == "__main__":
    print(text2morse("Ahoj Kubo."))
    print(morse2text(".- .... --- .--- / -.- ..- -... ---"))
