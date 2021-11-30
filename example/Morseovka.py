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