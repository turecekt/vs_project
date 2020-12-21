"""PROJECT MORSECODE TRANSLATOR."""

"""This program encodes and decodes latin alphabet
to and from MorseCode.

""""dcipher -> strores translated from morsecode."""
"""morsCharacter -> morse of single character."""
"""i -> counts spaces betwees morse."""
"""message -> string tob encoded or decoded."""

"""Morsecode dictionary form Latin to Morse."""
LAT_MORSE_DICT = {'A': '.-',
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
                  ',': '--..--',
                  '.': '.-.-.-',
                  '?': '..--..',
                  '/': '-..-.',
                  '-': '-....-',
                  '(': '-.--.',
                  ')': '-.--.-'}


"""
Funcion decrypts the string from Latin to Morsecode
each morse character is devided by /, words by //.
Args: Words in Latin dictionary
Returns: Morse code
"""


def encrypt(message):

    message = message.upper()
    mcipher = ''

    for letter in message:
        if letter != ' ':
            mcipher += LAT_MORSE_DICT[letter] + '/'
        else:
            mcipher += '/'
    return mcipher


"""
"Funcion to decrypt the string from Morsecode to Latin letters
Args: Morse symbols
Returns: Latin characters
"""


def decrypt(message):

    message += ' '
    dcipher = ''
    morsCharacter = ''

    for letter in message:
        if(letter != '-' and letter != '.' and letter != ' '):
            dcipher = 'Bad format'
            return dcipher

    for letter in message:
        if (letter != ' '):
            i = 0
            morsCharacter += letter
        else:
            i += 1
            if i == 2:
                dcipher += ' '
            else:
                dcipher += list(LAT_MORSE_DICT.keys())
                [list(LAT_MORSE_DICT.values()).index(morsCharacter)]
                morsCharacter = ''
    return dcipher


"""
Chooses type of the translation
Args: 1 fof ecnrypting Latin to MorseCode
      2 for decrypting MorseCode to Latin Characters
Returns: waiting for user input
"""


def choice(choose):

    if choose == 1:
        chooseTranslate = input("Your text: ")
        result = encrypt(chooseTranslate)

    elif choose == 2:
        choosTranslate2 = input("Morse: ")
        result = decrypt(choosTranslate2)

    return result


"""
Main definition
"""


def main():

    try:
        print("1 for Latin to Morse ")
        print("2 for Morse to Latin")
        a = int(input())
        volani = choice(a)
        print(volani)
    except ValueError:
        print("Must be symbol")


if __name__ == '__main__':
    main()
