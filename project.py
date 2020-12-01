"""@package docstring.

@file             project.py
@author           Ondrej Marecek <o_marecek@utb.cz>
@version          1.0
@brief            Morse Code Translator

@section LICENSE

This program is free to use....

@section DESCRIPTION

Morse code encryptor to and from morse code

"""

library = {'A': '.-', 'B': '-...',
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
           '(': '-.--.', ')': '-.--.-', ' ': '.....'}


def morseencrypt(txt):
    """Convert morse code to latin from user inserted txt."""
    """Test for morseencrypt function
    >>>morseencrypt('.-')
    'A'
    True"""
    translation = ''
    lib_encrypt = dict([(v, k) for k, v in library.items()])
    for x in txt:
        translation += lib_encrypt.get(x)
    return translation.strip()


def morsedecrypt(txt):
    """Convert latin to morse code from user inserted txt."""
    """ Test of morsedecrypt function
    >>> morsedecrypt('A')
    '.-'
    True"""
    translation = ''
    txt = txt.upper()
    for x in txt:
        translation += library.get(x) + ' '
    return translation.strip()


"""Menu section."""
pokracuj = True
while pokracuj:
    print("Menu: (Zadejte číslo, popřípadě zmáčkněte enter)")
    print("1: Překlad z morseovky do abecedy")
    print("2: Překlad z abecedy do morseovky")
    print("Pro ukončení programu zmáčkněte ENTER")
    print("********************************")
    print("Vyberte jednu z možností výše")
    vyber = input(":")
    if vyber == "":
        exit()
    else:
        print("Zadejte morseovku/text který chcete přeložit")
        text = input(":")
        if vyber == "1":
            print(morseencrypt(text))
            print("Chcete zpátky do menu a opakovat program? y/n")
            pokracuj = input().upper()
            if pokracuj == "N":
                pokracuj = False
            else:
                pokracuj = True
        elif vyber == "2":
            print(morsedecrypt(text))
            print("Chcete zpátky do menu a opakovat program? y/n")
            pokracuj = input().upper()
            if pokracuj == "N":
                pokracuj = False
            else:
                pokracuj = True
        else:
            exit()
else:
    exit()
