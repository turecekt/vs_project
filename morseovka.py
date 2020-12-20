# -*- coding: utf-8 -*-

# This program encodes and decodes latin alphabet to and from MorseCode

# Morsecode dictionary
MORSE_DICT = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '-.-',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.---',
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
              ',': '--..--',
              '.': '.-.-.-',
              '?': '..--..',
              '/': '-..-.',
              '-': '-....-',
              '(': '-.--.',
              ')': '-.--.-'}

# Function to encrypt the string
# according to the morse code dictionary
def encrypt(message):
    cipher = ' '
    for letter in message:
        if letter != ' ':
            
            # Looking for corresponding morsecode in dictionary and adding space
            cipher += MORSE_DICT[letter] + ' '
        else:
            # one space indicates different characters and two indicatates different words
            cipher += ' '
            
    return cipher

# Funcion to decrypt the string from Morsecode to latin
def decrypt(message):
    
    # Adding extra space at the end to acces the last morsecode
    message +=' '
    
    decipher = ' '
    citext = ' '
    for letter in message:
        
        # Checks for space
        if (letter != ' '):
            
            # Counter to keep track of space
            i = 0
            
            # Storing morse code of a single character
            citext += letter
           
        # In case of space    
        else:
            
            # If i=1 that indicates a new character
            i += 1
            
            # If i=2 that indicates a new word
            if i == 2 :
                
                # Adding space to separate words
                decipher +=' '
            else:
              
                # accesing the keys using their values (reverse of encryption)
                decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                citext = ' '
    return decipher
