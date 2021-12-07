"""Array."""

MorseCodeArray = {'A': '.-', 'B': '-...', ' ': '',
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
                  '0': '-----', ', ': '.-.-.-', '.': '......',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', '!': '--..--'}


# Metoda šifrování v Morseovu abecedu
"""Functions."""


def encrypt(userText):
    """Convert English text to Morse code."""
    userText = userText.upper()
    error = 'Invalid data'
    cipher = ''
    errorcountencrypt = 0
    for letter in userText:
        if letter in MorseCodeArray:
            if (letter != ' '):
                if letter == ' ':
                    cipher += MorseCodeArray[letter]
                else:
                    cipher += MorseCodeArray[letter] + ' '
            else:
                cipher += ''
        else:
            errorcountencrypt = errorcountencrypt + 1
    if errorcountencrypt == 0:
        return cipher
    else:
        return error


# Metoda dešifrování z Morseovou abecedy

def decrypt(userText):
    """Convert Morse code to English text."""
    error = 'Invalid data'
    userText += ' '
    decipher = ''
    citext = ''
    errorcountdecrypt = 0
    for letter in userText:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            if citext in MorseCodeArray.values():
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(MorseCodeArray.keys())
                    [list(MorseCodeArray.values()).index(citext)]
                    citext = ''
            else:
                errorcountdecrypt = errorcountdecrypt + 1
    if errorcountdecrypt == 0:
        return decipher
    else:
        return error


def main():
    """Print text and receive data from the keyboard."""
    print('Enter "M" for Morse Code, to decode into English insert "E"')
    count = input()
    count = count.lower()
    if count == "m":
        print("Insert Eng text:")
        userText = input()
        result = encrypt(userText)
        print(result)
    elif count == "e":
        print("Insert Morze code:")
        userText = input()
        result = decrypt(userText)
        print(result)
    else:
        print("Invalid data")


if __name__ == '__main__':
    main()
