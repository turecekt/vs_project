import argparse
import re
import sys

letter_a = ".-"
letter_b = "-..."
letter_c = "-.-."
letter_d = "-.."
letter_e = "."
letter_f = "..-."
letter_g = "--."
letter_h = "...."
letter_ch = "----"
letter_i = ".."
letter_j = ".---"
letter_k = "-.-"
letter_l = ".-.."
letter_m = "--"
letter_n = "-."
letter_o = "---"
letter_p = ".--."
letter_q = "--.-"
letter_r = ".-."
letter_s = "..."
letter_t = "-"
letter_v = "...-"
letter_w = ".--"
letter_x = "-..-"
letter_y = "-.--"
letter_z = "--.."

MORSE_CODE_ALPHABET = { 
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 
                    'E':'.', 'F':'..-.',
                    'G':'--.', 'H':'....',
                    'CH':'----','I':'..',
                    'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 
                    'N':'-.', 'O':'---', 
                    'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 
                    'T':'-', 'U':'..-', 
                    'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 
                    'Z':'--..'
                    #'1':'.----', '2':'..---', '3':'...--',
                    #'4':'....-', '5':'.....', '6':'-....',
                    #'7':'--...', '8':'---..', '9':'----.',
                    #'0':'-----'
                    }

morseAlphabet = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_ch, letter_i, letter_j, letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t, letter_v, letter_w, letter_x, letter_y, letter_z]

for letter in morseAlphabet:
    if letter == ".":
        print("yes we are there")

msg = "type in the string consist of morse code or alphabet"

parser = argparse.ArgumentParser(description = msg)

parser.add_argument('MorseString', metavar='String', type=str, help='a string to decode/Ncode from/to morse code')

st = parser.parse_args()

errorObj = re.search(r'[^a-zA-Z \-.|]', st.MorseString, re.I)

if errorObj:
    print ("sys exit")
    sys.exit("please type in right characters")
else:
    print ("%s" %st.MorseString)
    

"""print("%s" %st)"""
print("string %s" %letter_a)

number_of_whitespaces = st.MorseString.count(" ")
number_of_separators = st.MorseString.count("|")

print(number_of_whitespaces)



""" /be careful about anything else than alphabet and dots and commas
    extremely careful for \ ""
    dont allow both .-- 
    || and whitespaces are allowed in both
    osetrit ze nesmi byt dva rozdelovace vedle sebe
"""

""" upper() """

morseObj = re.search(r'[ .\-|]', st.MorseString, re.I)

if morseObj:
    print ("working on morse")
    # bez skrz string a podle oddelovacu rozdel "pismena" 
    splitString = st.MorseString.split()
    message = ""
    
    for i in range(number_of_whitespaces + 1):
        print(splitString[i])
        if splitString[i] not in morseAlphabet:
            print("please fill in right morse code")
            #sys.exit()
        else:
            message += list(MORSE_CODE_ALPHABET.keys())[list(MORSE_CODE_ALPHABET.values()).index(splitString[i])]
            # I was looking for some easy way to cooperate with the table ... I found this at (https://www.geeksforgeeks.org/morse-code-translator-python/) and changed for my code#
    
    print (message)

alphabetObj = re.search(r'[a-zA-Z |]', st.MorseString, re.I)

if alphabetObj:
    print("working on decode")
    splitString = st.MorseString.split()
    alpha_message = ""

    for i in range(number_of_whitespaces + 1):
        print(number_of_whitespaces)
        print(splitString[i])
        if splitString[i] not in morseAlphabet:
            print("wrong if statement")
            #sys.exit()
        else:
            alpha_message += MORSE_CODE_ALPHABET[splitString[i]]
            # I was looking for some easy way to cooperate with the table ... I found this at (https://www.geeksforgeeks.org/morse-code-translator-python/) and changed for my code#
    
    print (alpha_message)
    