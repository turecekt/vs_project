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


def letter2morse(letter):
    return morse[letter]


def morse2letter(mor):
    return list(morse.keys())[list(morse.values()).index(mor)]


def text2morse(text: str):
    letters = list(text.lower())
    morse = ""
    for let in letters:
        morse += letter2morse(let) + splitCharacter
    return morse


def morse2text(morseText):
    arrayMorse = morseText.split(splitCharacter)
    text = ""
    for m in arrayMorse:
        text += morse2letter(m)
    return text


"""Main method."""
if __name__ == "__main__":
    print(text2morse("Ahoj Kubo"))
    print(morse2text(".- .... --- .--- / -.- ..- -... ---"))
