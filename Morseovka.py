"""Prevod textu na morseovku."""


"""Funkce rekurze pri zadani znaku, ktery neni v abecede"""


def is_input_correct(message):
    """
    Overi ze input je spravny.

    Attributes:
        message: Zprava
    Returns: True/False
    """
    for character in message:
        if character not in MORSE_CODE_DICT:
            return False
    return True


""" Uzivatel nejprve vlozi text, ktery chce prelozit do Morseovy abecedy."""


def load_message_to_encrypt():
    """
    Nacita text na preklad ze vstupu.

    Returns: zpravu ktera je ve velkych pismenach
    """
    message = input('Vloz text na preklad: ')
    message = message.upper()
    if not is_input_correct(message):
        return load_message_to_encrypt()
    else:
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
    Vyhleda slovnik a přidá odpovídající Morseovku.

    :param message: vyhleda hodnotu
    :return: vraci priprazeny kod k pismenu
    """
    sifra = ' '
    for pismeno in message:

        sifra += MORSE_CODE_DICT[pismeno] + ' '

    return sifra


def main():
    """Spusti program."""
    message_to_encrypt = load_message_to_encrypt()
    print(encrypt(message_to_encrypt))


if __name__ == '__main__':
    main()
