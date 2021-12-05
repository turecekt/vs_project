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
letter_u = "..-"
letter_w = ".--"
letter_x = "-..-"
letter_y = "-.--"
letter_z = "--.."
number_0 = "-----"
number_1 = ".----"
number_2 = "..---"
number_3 = "...--"
number_4 = "....-"
number_5 = "....."
number_6 = "-...."
number_7 = "--..."
number_8 = "---.."
number_9 = "----."


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
                    'Z':'--..',
                    '1':'.----', '2':'..---', 
                    '3':'...--', '4':'....-',
                    '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', 
                    '9':'----.', '0':'-----'
                    }

def split_to_letters(my_string):
    return list(my_string)

morseAlphNum = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_ch, letter_i, letter_j,
                letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t, letter_v, letter_u, 
                letter_w, letter_x, letter_y, letter_z, number_0, number_1, number_2, number_3, number_4, number_5, number_6, 
                number_7, number_8, number_9]

""" for letter in morseAlpNum:
    if letter == ".":
        print("yes we are there") """

msg = "type in the string consist of morse code or alphabet"

parser = argparse.ArgumentParser(description = msg)

parser.add_argument('MorseString', metavar='String', type=str, help='a string to decode/Ncode from/to morse code')

st = parser.parse_args()

errorObj = re.search(r'[^a-zA-Z0-9 \-.|]', st.MorseString, re.I)

if errorObj:
    print ("sys exit")
    sys.exit("please type in right characters")
else:
    print ("%s" %st.MorseString)
    

number_of_whitespaces = st.MorseString.count(" ")
number_of_separators = st.MorseString.count("|")
number_of_letters = len(st.MorseString)

print(number_of_letters)



""" /be careful about anything else than alphabet and dots and commas
    extremely careful for \ ""
    osetrit ze nesmi byt dva rozdelovace vedle sebe
    pozor na mezeru na konci a na zacatku
    rozlisit rozdelovace a pak pouzit podle toho urceny rozdelovac
    rozlisit jestli se jedna o decode nebo ncode
"""
separatorObj = re.search(r'[\|]+', st.MorseString)
whitespaceObj = re.search(r'[\s]+', st.MorseString)
morseObj = re.search(r'[.\-]', st.MorseString, re.I)
alphabetObj = re.search(r'[a-zA-Z0-9]', st.MorseString, re.I)

if separatorObj and whitespaceObj:
    sys.exit("please use only one way to split letters/words")

if morseObj and alphabetObj:
    sys.exit("please use only alphabet to Ncode or morse code to Decode")

if separatorObj:
    newString = re.sub(r'[\|\|]+', "|", st.MorseString)
    number_of_separators = newString.count("|")
    sep_number = number_of_separators
    splitString = newString.split("|")
elif whitespaceObj:
    newString = re.sub(r'[\s\s]+', " ", st.MorseString)
    number_of_whitespaces = newString.count(" ")
    sep_number = number_of_whitespaces
    splitString = newString.split()
else:
    sep_number = 0
    newString = st.MorseString
    splitString = newString.split()



if morseObj:
    letters = split_to_letters(st.MorseString)
    message = ""
    for i in range(number_of_letters):
        if i == 0 and (letters[i] == " " or letters[i] == "|"):
            sys.exit("please do not start with separators")
        if i == number_of_letters-1 and (letters[i] == " " or letters[i] == "|"):
            sys.exit("please do not end with separators")

    for j in range(sep_number + 1):
        print(splitString[j])
        if splitString[j] not in morseAlphNum:
            sys.exit("please fill in right morse code")
        else:
            message += list(MORSE_CODE_ALPHABET.keys())[list(MORSE_CODE_ALPHABET.values()).index(splitString[j])]
            # I was looking for some easy way to cooperate with the table ... I found this at (https://www.geeksforgeeks.org/morse-code-translator-python/) and changed for my code#
    print(message)



if alphabetObj:
    print("working on decode")
    st.MorseString = st.MorseString.upper()
    splitString = split_to_letters(st.MorseString)
    print(splitString)
    alpha_message = ""

    for i in range(number_of_letters):
        print(splitString[i])
        if i != 0:
                alpha_message += "|"
        else:
            if splitString[i] == " " or splitString[i] == "|":
                sys.exit("please do not start with separators")
        if splitString[i] != " " and splitString[i] != "|":
            alpha_message += MORSE_CODE_ALPHABET[splitString[i]]
    
    print ("alphabet message  :", alpha_message)