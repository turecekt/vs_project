"""
Morseova sifra.

Program se postupne zepta na vstupy ve formatu ABC,
nebo v morseove sifre a nasledne prevede.
"""


MORSE_DICTIONARY = {'A': '.-', 'B': '-...',
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


# zasifrovani
def encrypt(message):
    """Zasifrovani zpravy.

    Vraceni vsech znaku v morseove sifre
    >>> encrypt('E')
    '. '
    """
    cipher = ''
    for letter in message:
        if letter != ' ':

            cipher += MORSE_DICTIONARY[letter] + ' '
        elif letter == '':
            cipher = ''
        else:
            cipher += ' '
    return cipher


# testovani spravnosti encryptu
def test_encrypt():
    """Test zasifrovani.

    Vraceni vsech znaku v morseove sifre
    >>> encrypt('E')
    '. '
    """
    assert encrypt('E') == '. '


# odsifrovavani
def decrypt(message):
    """Odsifrovani zpravy.

    Odsifrovani morseovky na text.
    >>> decrypt('.')
    'E'
    """
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        if letter != ' ':

            i = 0

            citext += letter

        else:

            i += 1

            if i == 2:

                decipher += ' '
            else:

                decipher += list(MORSE_DICTIONARY.keys())[
                    list(MORSE_DICTIONARY.values()).index(citext)]
                citext = ''

    return decipher


# testovani decryptu
def test_decrypt():
    """Testing decrypt.

    Odsifrovani morseovky na text.
    >>> decrypt('.')
    'E'
    """
    correctResult = 'EEEE'
    result = decrypt('. . . . ')
    assert result == correctResult

def test_decrypt_empty_string():
    """Testing decrypting with empty input."""
    correctResult = ''
    result = decrypt('')
    assert result == correctResult
# funkce main
def main():
    """Definovani funkce main.

    V mainu se prvne zavola input po encrypt potom
    zavola druhy input pro decrypt.
    """
    message = input("Zadejte zprávu v abc: ").upper()
    """Zprava.

    Pimena na velka.
    >>>input('e')
    'E'
    """
    result = encrypt(message.upper())
    print(result)

    message = input("Zadejte zprávu v morseovce: ")
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
