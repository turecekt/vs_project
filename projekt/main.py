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


def encrypt(message):
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
    assert encrypt('E') == '. '


def decrypt(message):
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


#testovani decryptu
def test_decrypt():
    assert decrypt('.') == ('E')


def main():
    message = input("Zadejte zprávu v abc: ").upper()
    result = encrypt(message.upper())
    print(result)

    message = input("Zadejte zprávu v morseovce: ")
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
