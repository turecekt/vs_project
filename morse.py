
"""
Skript pro kodovani/dekodovani Morseovy abecedy.

Vstup:
    message -> Vstupni retezec
Promenne:
    cipher -> Desifrovana zprava
    decipher -> Zasifrovana zprava
"""

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....',
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



def mainInput(message):

    for char in message:
        if char not in ".- ":
            return encrypt(message)
    return decrypt(message)


def test_mainInput():
    assert mainInput('univerzita') == '..- -. .. ...- . .-. --.. .. - .- '
    assert mainInput('- --- -- .- ...  -... .- - .-') == 'TOMAS BATA'


def encrypt(message):
    message = message.upper()           
    cipher = ''                         
    for letter in message:              
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher       


def test_encrypt():
    """Test zasifrovani."""
    assert encrypt('TURECEK') == '- ..- .-. . -.-. . -.- '



def decrypt(message):
    """Metoda pro desifrovani z morseovy abecedy na text."""
    message += ' '               # pro ukonceni posledniho Morse znaku
    decipher = ''                       # retezec, ktery bude funkce vracet
    citext = ''                         # pomocny retezec pro jeden znak Morse

    for letter in message:              # prochazi znaky vstupniho retezce
        # kdyz znak neni mezera, prida znak do pomocneho retezce citext:
        if (letter != ' '):
            i = 0                       # zaznamenava mezery v Morse kodu
            citext += letter
        # jinak (kdyz mezera):
        else:
            i += 1
            # pokud i == 2 >> konec slova -> prida mezeru do vystupu:
            if i == 2:
                decipher += ' '
            # jinak konec Morse znaku -> vyhleda znak ve slovniku
            # a prida prelozene pismeno do vystupu:
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''       # vycisti retezec pro znak

    return decipher                     # vraci rozsifrovany text

def test_decrypt():
    """Test desifrovani."""
    assert decrypt('- ..- .-. . -.-. . -.-') == 'TURECEK'

