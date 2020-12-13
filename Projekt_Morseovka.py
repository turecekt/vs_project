# -*- coding: utf-8 -*-

# This program encodes and decodes latin alphabet to and from MorseCode

# mcipher -> stores translated from latin string
# dcipher -> strores translated from morsecode
# morsCharacter -> morse of single character
# i -> counts spaces betwees morse
# message -> string tob encoded or decoded

# Morsecode dictionary form Latin to Morse
LAT_MORSE_DICT = {'A':'.-',
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
              ',':'--..--',
              '.':'.-.-.-',
              '?':'..--..',
              '/':'-..-.',
              '-':'-....-',
              '(':'-.--.',
              ')':'-.--.-'}

#Funcion to decrypt the string from Latin to Morsecode
#each morse letter is devided by /
def encrypt(message):
  
   
    message = message.upper()
    mcipher = ''


    for letter in message:
        if letter != ' ':
            mcipher += LAT_MORSE_DICT[letter] + '/'
        else:
            mcipher += '/'
    return mcipher


#Funcion to decrypt the string from Morsecode to Latin letters
def decrypt(message):
    
    #Adding extra space at the end to acces the Last morsecode
    message += ' '
    dcipher = ''
    morsCharacter = ''
  
    for letter in message:
        if(letter != '-' and letter != '.' and letter != ' '):
            dcipher = 'Bad format'
            return dcipher

    for letter in message:
        if (letter != ' '):
            i = 0
            morsCharacter += letter
        else:
            i += 1
            if i == 2:
                dcipher += ' '
            else:
                dcipher += list(LAT_MORSE_DICT.keys())[list(LAT_MORSE_DICT.values()).index(morsCharacter)]
                morsCharacter = ''
    return dcipher



#Chooses type of the translation
def choice(choose):
   
    if choose == 1:
        vyberPrekladu = input("Your text: ")
        result = encrypt(vyberPrekladu)

    elif choose == 2:
        vyberPrekladu2 = input("Morse: ")
        result = decrypt(vyberPrekladu2)
    
    return result


#Definice main
def main():
    
    try:
        print("1 for Latin to Morse ")
        print("2 for Morse to Latin")
        a = int(input())
        volani = choice(a)
        print(volani)
    except ValueError:
        print("Musí být znak")


if __name__ == '__main__':
    main()
        
            
            
            
    