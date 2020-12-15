"""Prevod textu na morseovku."""

def is_input_correct(message):
    for character in message:
        if character not in MORSE_CODE_DICT:
            return False
    return True


def load_message_to_encrypt():
    message = input('Vloz text na preklad: ')
    if not is_input_correct(message):
        return load_message_to_encrypt()
    else:
        message = message.upper()
        return message


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
                   '(': '-.--.', ')': '-.--.-', '!': '––...–',
                   ' ': '/'}


"""
Slovnik na preklad Morseovy abecedy
"""


def encrypt(message):
    """
    Vyhledá slovník a přidá odpovídající Morseovku.

    :param message: vyhleda hodnotu
    :return: vraci priprazeny kod k pismenu
    """
    sifra = ' '
    for pismeno in message:

        sifra += MORSE_CODE_DICT[pismeno] + ' '

    return sifra


"""
podminka

označuje různé znaky a označuje různá slova
"""

"""
vypíše šifru v morseově abecedě
"""

"""
na ukončení programu musí uživatel stisknout Enter
"""


def main():
    message_to_encrypt = load_message_to_encrypt()
    print(encrypt(message_to_encrypt))


# main()
