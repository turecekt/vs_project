# Python program to implement Morse Code Translator

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'cipher_char' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
"""

# Dictionary representing the morse code chart
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
                   '(': '-.--.', ')': '-.--.-', '=': '-...-',
                   '': '', '+': '.-.-.', ':': '---...'}


def encrypt(message):
    """Function encrypt() encrypts given text into Morse Code.

        Args:
            - message - Given text to encrypt

        Returns:
            - cipher - Encrypted given text
        """
    cipher = ""
    formatted_message = str(message).upper()

    for letter in formatted_message:
        if letter != " ":

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += " "

    # shorten the string of the last char
    st = str(cipher)
    st = st[:-1]
    return st


# Function to decrypt the string from morse to greek alphabet
def decrypt(message):
    """Function decrypt() decrypts given text from Morse Code into greek alphabet.

        Args:
            - message - Given text to decrypt

        Returns:
            - decipher - Decrypted text
        """
    # extra space added at the end to access the
    # last morse code
    i = 0
    decipher_message = ""
    message += " "

    decipher = ""
    cipher_char = ""
    for letter in message:

        # checks for space
        if letter != " ":

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            cipher_char += letter

            # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += " "
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT
                                 .keys())[list(MORSE_CODE_DICT
                                               .values()).index(cipher_char)]
                cipher_char = ""

        decipher_message = str(decipher).upper()

    return decipher_message
