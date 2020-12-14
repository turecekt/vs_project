"""Prevod textu na morseovku."""

message = input('Vloz text na preklad')
""" Uzivatel nejprve vlozi text, ktery chce prelozit do Morseovy abecedy."""

message = message.upper()
"""
Slovnik Morseovy abecedy je ve formatu uppercase,

V pripade zadani vety v lowercase, prepise vetu na uppercase
"""

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


"""
Slovnik na preklad Morseovy abecedy
"""


def encrypt(message):
    """
    Vyhledá slovník a přidá odpovídající Morseovku.

    :param message: vyhleda hodnotu
    :return: vraci priprazeny kod k pismenu
    """
    sifra = ''
    for pismeno in message:
        if pismeno != ' ':

            sifra += MORSE_CODE_DICT[pismeno] + ' '
        else:

            sifra += ' '

        return sifra


"""
podminka

označuje různé znaky a označuje různá slova
"""

print(encrypt(message))
"""
vypíše šifru v morseově abecedě
"""

input()
"""
na ukončení programu musí uživatel stisknout Enter
"""
