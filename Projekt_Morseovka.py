# -*- coding: utf-8 -*-

# This program encodes and decodes latin alphabet to and from MorseCode

# mcipher -> stores translated from latin string
# dcipher -> strores translated from morsecode
# mtext -> morse of single character
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
#Morsecode dictionary form Morse to Latin
MORSE_LATIN_DICT = {'.-':'A',
              '-...':'B',
              '-.-.':'C',
              '-..':'D',
              '.':'E',
              '..-.':'F',
              '--.':'G',
              '....':'H',
              '..':'I',
              '.---':'J',
              '-.-':'K',
              '.-..':'L',
              '--':'M',
              '-.':'N',
              '---':'O',
              '.--.':'.P',
              '--.-':'Q',
              '.-.':'R',
              '...':'S',
              '-':'T',
              '..-':'U',
              '...-':'V',
              '.--':'W',
              '-..-':'X',
              '-.--':'Y',
              '--..':'Z',
              '.----':'1',
              '..---':'2',
              '...--':'3',
              '....-':'4',
              '.....':'5',
              '-....':'6',
              '--...':'7',
              '---..':'8',
              '----.':'9',
              '-----':'0',
              '--..--':',',
              '.-.-.-':'.',
              '..--..':'?',
              '-..-.':'/',
              '-....-':'-',
              '-.--.':'(',
              '-.--.-':')'}

message = print("Text do Morse použij decrypt('TEXT'), Morse do Text použij decrypt('ZNAKY')")
message = input("Zde napiš svou zprávu:").upper()
# Function encrypts the message to Morsecode
def encrypt(message):
    mcipher = ''
    for letter in message:
        if letter != '':
            
            #Looking for right morsecode in dictionary and adding slash
            mcipher += LAT_MORSE_DICT[letter] + '/'
        else:
            # one space indicates different characters and two indicatates different words
            mcipher += '/'
            
    return mcipher

#Funcion to decrypt the string from Morsecode to latin
def decrypt(message):
    
    #Adding extra space at the end to acces the last morsecode
    message +=''
    
    dcipher = ''
    mtext = ''
    for letter in message:
        
        #Checks for space
        if (letter != ''):
            
            #Counter to keep track of space
            i = 0
            
            #Storing morse code of a single character
            mtext += letter
           
        #In case of space    
        else:
            
            #If i=1 that indicates a new character
            i += 1
            
            #If i=2 that indicates a new word
            if i == 2 :
                
                #Adding space to separate words
                dcipher +=''
            else:
                
                #accesing the keys using their values (reverse of encryption)
                dcipher += list(LAT_MORSE_DICT.keys())[list(LAT_MORSE_DICT.values()).index(mtext)]
                mtext = ''
                
                
                
    return dcipher

# Hard-coded driver function to run the program 
def main(): 
    message = "Vítej v mém dekodéru"
    result = encrypt(message.upper()) 
    print (result) 
  
    message = "Začni psát"
    result = decrypt(message) 
    print (result) 
    
# Executes the main function
    main()
        
            
            
            
    