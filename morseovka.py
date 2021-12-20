"""Aplikace, ktera umoznuje prelozit text do morseovky a zpet."""

# Vytvoreni slovniku znaku
Slovnik_morse = {
                    'A': '.-',
                    'B': '-...',
                    'C': '-.-.',
                    'D': '-..',
                    'E': '.',
                    'F': '..-.',
                    'G': '--.',
                    'H': '....',
                    'I': '..',
                    'J': '.---',
                    'K': '-.-',
                    'L': '.-..',
                    'M': '--',
                    'N': '-.',
                    'O': '---',
                    'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.',
                    'S': '...',
                    'T': '-',
                    'U': '..-',
                    'V': '...-',
                    'W': '.--',
                    'X': '-..-',
                    'Y': '-.--',
                    'Z': '--..',
                    '1': '.----',
                    '2': '..---',
                    '3': '...--',
                    '4': '....-',
                    '5': '.....',
                    '6': '-....',
                    '7': '--...',
                    '8': '---..',
                    '9': '----.',
                    '0': '-----',
                    ', ': '--..--',
                    '.': '.-.-.-',
                    '?': '..--..',
                    '/': '-..-.',
                    '-': '-....-',
                    '(': '-.--.',
                    ')': '-.--.-'
                    }


def encrypt(message):
    """Funkce pro prevedeni textu do morse code."""
    PrekladEncrypt = ''
    for letter in message:
        if letter != ' ':
            PrekladEncrypt += Slovnik_morse[letter] + ' '
        else:
            PrekladEncrypt += ' '

    return PrekladEncrypt


def decrypt(message):
    """Funkce pro prevedeni morse code do textu."""
    message += ' '
    PrekladDecrypt = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                PrekladDecrypt += ' '
            else:
                PrekladDecrypt += list(Slovnik_morse.keys())[list(
                    Slovnik_morse.values()).index(citext)]
                citext = ''

    return PrekladDecrypt


if __name__ == '__main__':
    """Funkce, ktera umoznuje vybrat typ prevodu."""

    vyber = input("Pro sifrovani stiskni 's' pro desifrovani stiskni 'd'")
    if vyber == "s":
        message = input("Zadej text nebo slovo pro prelozeni do morse code: ")
        result = encrypt(message.upper())
        print(result)
    if vyber == "d":
        message = input("Zadej morse code pro prelozeni do textu: ")
        result = decrypt(message.upper())
        print(result)
