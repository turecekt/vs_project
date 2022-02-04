MORSE_CODE_DICT = {
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
    ')': '-.--.-',
    }


def encryption(message):
    if len(message) == 0:
        return ''

    my_cipher = ''
    for myletter in message.upper():
        if myletter != ' ':
            my_cipher += MORSE_CODE_DICT[myletter] + ' '
        else:
            my_cipher += ' '
    return my_cipher.strip()


# This function is used to decrypt
# Morse code to English

def decryption(message):
    if len(message) == 0:
        return ''

    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:

        # checks for space

        if myletter != ' ':
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += \
                    list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mycitext)]  # noqa: E501
                mycitext = ''
    return decipher


def main():
    my_message = 'python-program'
    output = encryption(my_message)
    print(output)
    my_message = \
        '.--. -.-- - .... --- -. -....- .--. .-. --- --. .-. .- --'
    output = decryption(my_message)
    print(output)


# Executes the main function

if __name__ == '__main__':
    main()


def testEncryption():
    result = encryption('test')
    expected = '- . ... -'
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def testDecryption():
    result = decryption('- . ... -')
    expected = 'TEST'
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def test2Encryption():
    result = encryption('')
    expected = ''
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess


def test2Decryption():
    result = decryption('')
    expected = ''
    err_mess = "Expected:'" + expected + "', result:'" + result + "'"
    assert result == expected, err_mess
