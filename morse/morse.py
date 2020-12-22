"""Morse encoder/decoder."""
from unidecode import unidecode

morseList = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..",
             'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
             'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
             'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
             'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
             'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
             'y': "-.--", 'z': "--..", '1': ".----", '2': "..---",
             '3': "...--", '4': "....-", '5': ".....", '6': "-....",
             '7': "--...", '8': "---..", '9': "----.", '0': "-----",
             '.': ".-.-.-", ',': "--..--", ':': "---...", '?': "..--..",
             '-': "-....-", '/': "-..-.", '@': ".--.-.", '=': "-...-",
             ' ': "/"}


def morse_code(var_inp):
    """
    Morse encoder.

    Returns encoded string
    """
    var_inp = var_inp.lower()
    var_inp = unidecode(var_inp)
    strInpMorse = ""

    for char_inp in var_inp:
        strInpMorse += morseList[char_inp] + " "

    strInpMorse = strInpMorse[:-1]

    return strInpMorse


def morse_decode(var_inp2):
    """
    Morse decoder.

    Returns decoded string
    """
    var_inp2 = var_inp2 + " "
    strInpMorse = ""
    tmpWord = ""
    charCnt = 1

    for char_inp in var_inp2:
        if char_inp != ' ':
            tmpWord += char_inp
        else:
            strInpMorse += list(morseList.keys())[list(morseList.values()).index(tmpWord)]
            tmpWord = ''

        charCnt += 1

    return strInpMorse


if __name__ == '__main__':
    print('Morse Encoder/Decoder')
    print('d for decode')
    print('e for encode')
    print('Enter what you want to do: ')
    strChoice = input()
    if strChoice == 'e':
        print('Enter text to encode: ')
        strInp = input()
        strInpOrg = strInp
        var = morse_code(strInp)
        print(var)
    elif strChoice == 'd':
        print('Enter text to decode: ')
        strInp = input()
        strInpOrg = strInp
        var = morse_decode(strInp)
        print(var)
    else:
        print('Wrong choice...')
        print('Exiting...')
