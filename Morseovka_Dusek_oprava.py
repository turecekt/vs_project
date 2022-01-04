"""
VARIABLE KEY.

'cipher' -> 'uloží string v morseove abecedě z anglického stringu.'
'decipher' -> 'uloží string v anglické abecedě z morseova stringu.'
'citext' -> 'uloží jeden charakter morseova kódu.'
'i' -> 'uloží string k encoded nebo decoded.'
"""

# Khihovna reprezentující morseovu abecedu
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '._..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '...-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Funkce k encryptování stringu
# pomocí morseovy abecedy
def encrypt(message):
    """Ecrypting string."""
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Prohledá knihovnu a přidá
            # korespudující morseuv kód
            # s mezerami k oddělení
            # morseova kódu od ostatních znaků
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 místo značí jinačí znak
            # a 2 místa značí různé slova
            cipher += ' '
    return cipher


# Funkce k decrypting string z morseovy abecedy do angličtiny
def decrypt(message):
    """Decrypting string."""
    # extra místo ke konci k přístupu morseovy abecedy
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # hledání volného místa
        if (letter != ' '):

            # čítač volných míst
            i = 0

            # uložení morseova kódu jednotlivého znaku
            citext += letter

        # v případě volného místa
        else:
            # if i = 1 indikování volného místa
            i += 1

            # if i = 2 indikévání nového slova
            if i == 2:

                # přidání volného místak separování slov
                decipher += ' '
            else:

                # přístup ke klíčům a jejím hodnotám (opačná encryption)
                decipher += list(MORSE_CODE_DICT.keys(
                ))[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


# Hard-coded driver funkce ke spuštění programu
def main():
    """Definition of main."""
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print(result)

    message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ..."
    result = decrypt(message)
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()


def test_main():
    """Definition of main."""
    message = "TEST PROBEHL USPESNE"
    result = encrypt(message.upper())
    print(result)

    message = "- . ... -  ..- ... .--. . ... -. ."
    result = decrypt(message)
    print(result)
