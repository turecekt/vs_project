"""Slovník z latinky do Morseovy abecedy."""
dict = {'A': '.-',       'B': '-...',
        'C': '-.-.',     'D': '-..',      'E': '.',
        'F': '..-.',     'G': '--.',      'H': '....',
        'I': '..',       'J': '.---',     'K': '-.-',
        'L': '.-..',     'M': '--',       'N': '-.',
        'O': '---',      'P': '.--.',     'Q': '--.-',
        'R': '.-.',      'S': '...',      'T': '-',
        'U': '..-',      'V': '...-',     'W': '.--',
        'X': '-..-',     'Y': '-.--',     'Z': '--..',
        '1': '.----',    '2': '..---',    '3': '...--',
        '4': '....-',    '5': '.....',    '6': '-....',
        '7': '--...',    '8': '---..',    '9': '----.',
        '0': '-----',    ',': '--..--',   '.': '.-.-.-',
        '?': '..--..',   '/': '-..-.',    '-': '-....-',
        '(': '-.--.',    ')': '-.--.-'}

def encrypt(vstup):
    """Encrypt string text.
    Return string in morse code
    >>> encrypt('A')
    .-
    >>> encrypt('7') == '--... '
    True.
    """
    vystup = ''

    for letter in vstup:

        if letter in dict:
            vystup += dict[letter] + ' '

        elif letter == ' ':
            vystup += ' '

        else:
            # necharakterizovaný znak
            vystup += '?'

    return vystup

def decrypt(vstup):
    """Decrypt string in morse code.
    Return string text
    >>> decrypt('.-')
    A
    >>> decrypt('--...') == '7 '
    True.
    """
    vstup += ' '
    vystup = ''
    citext = ''

    for letter in vstup:

        if (letter != ' '):
            i = 0
            citext += letter

        # v prípade medzery
        else:
            i += 1

            if i == 2:
                vystup += ' '

            else:
                vystup += list(dict.keys())[list(dict.values()).index(citext)]
                citext = ''

    return vystup


def main():
    """Funkce zabezpečí loop celého programu."""
    x = input("Ak chceš kódovať, stlač K.\nAk chceš dekódovať, stlač D.\n")

    if x == "k":
        k = input("Zadaj text na preklad do morzeovky: \n")
        k = k.upper()
        print(encrypt(k))

    elif x == "d":
        d = input("Zadaj morzeovku na preklad na text: \n")
        d = d.upper()
        print(decrypt(d))

    else:
        print("Zadaj K alebo D!")

    print()
    print()
    main()


main()