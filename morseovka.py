Slovnik_morse = {   'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-'
                }
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    PrekladEncrypt = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            PrekladEncrypt += Slovnik_morse[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            PrekladEncrypt += ' '
 
    return PrekladEncrypt
 
# Function to decrypt the string
# from morse to english
def decrypt(message):
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    PrekladDecrypt = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                PrekladDecrypt += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                PrekladDecrypt += list(Slovnik_morse.keys())[list(Slovnik_morse
                .values()).index(citext)]
                citext = ''
 
    return PrekladDecrypt
 
# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print (result)
 
    message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decrypt(message)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()