# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:21:11 2020

@author: pavel
"""

morse = {
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
    '0': '-----', 
    '1': '.----', 
    '2': '..---',
    '3': '...--', 
    '4': '....-', 
    '5': '.....',
    '6': '-....', 
    '7': '--...', 
    '8': '---..',
    '9': '----.', 
    "&": ".-...", 
    "'": ".----.",
    "@": ".--.-.", 
    ")": "-.--.-", 
    "(": "-.--.",
    ":": "---...", 
    ",": "--..--", 
    "=": "-...-",
    "!": "-.-.--", 
    ".": ".-.-.-", 
    "-": "-....-",
    "+": ".-.-.", 
    '"': ".-..-.", 
    "?": "..--..",
    "/": "-..-."
}

def encryption(message):

    encrypt = ''
    for letter in message:
        if letter != ' ':
            encrypt += morse[letter] + ' '
        else:
            encrypt += ' '
    return encrypt



def decryption(message):
    global i
    message += ' '
    decrypt = ''
    crtext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            crtext += letter
        else:
            i += 1
            if i == 2:
                decrypt += ' '
            else:
                decrypt += \
                    list(morse.keys())[list(morse.values()).index(crtext)]
                crtext = ''
    return decrypt



def main():

    message = input("Zadajte text, ktery chcete zasifrovat:")
    
    result = encryption(message.upper())
    print(result)



    message = input("Zadajte morseovu abecedu, kterou chcete odsifrovat:")
    
    result = decryption(message)
    print(result)

if __name__ == '__main__':
    main()