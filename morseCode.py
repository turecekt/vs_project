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
space = "....----"
separator = "----...."


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
                    '9':'----.', '0':'-----',
                    ' ':'....----', '|':'----....'
                    }

def split_to_letters(my_string):
    return list(my_string)

morseAlphNum = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_ch, letter_i, letter_j,
                letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t, letter_v, letter_u, 
                letter_w, letter_x, letter_y, letter_z, number_0, number_1, number_2, number_3, number_4, number_5, number_6, 
                number_7, number_8, number_9, space, separator]


def myArgParser():
    msg = "type in the string consist of morse code or alphabet"

    args = sys.argv[1]
    if args == '--':
        sys.exit("M")
    else:
        parser = argparse.ArgumentParser(description = msg)
        parser.add_argument('MorseString', metavar='String', type=str, help='a string to decode/Ncode from/to morse code')

    st = parser.parse_args()

    errorObj = re.search(r'[^a-zA-Z0-9 \-\.\|]', st.MorseString, re.I)

    if errorObj:
        sys.exit("please type in right characters")

    """ 
        extremely careful for \ ""
    """
    return st


def checkConditions(st):

    if separatorObj and whitespaceObj:
        sys.exit("please use only one way to split letters/words")

    if morseObj and alphabetObj:
        sys.exit("please use only alphabet to Ncode it or morse code to Decode it")

    if separatorObj:
        st.MorseString = re.sub(r'\|\|\|+', "||", st.MorseString)
        newString = re.sub(r'\|\|', "|----....|", st.MorseString)
        splitString = newString.split("|")
    elif whitespaceObj:
        newString = re.sub(r'\s\s', " ....---- ", st.MorseString)
        splitString = newString.split()
    else:
        newString = st.MorseString
        splitString = newString.split()
    
    len_splitString = len(splitString)
    len_basic_string = len(split_to_letters(st.MorseString))

    return len_splitString, len_basic_string, splitString

def morseNcode(len_basic_string, len_splitString, splitString):
    if morseObj:
        letters = split_to_letters(st.MorseString)
        message = ""
        for i in range(len_basic_string):
            if i == 0 and (letters[i] == " " or letters[i] == "|"):
                sys.exit("please do not start with separators")
            if i == len_basic_string-1 and (letters[i] == " " or letters[i] == "|"):
                sys.exit("please do not end with separators")


        for j in range(len_splitString):
            if splitString[j] not in morseAlphNum:
                sys.exit("please fill in right morse code")
            else:
                message += list(MORSE_CODE_ALPHABET.keys())[list(MORSE_CODE_ALPHABET.values()).index(splitString[j])]
                # I was looking for some easy way to cooperate with the table ... I found this at (https://www.geeksforgeeks.org/morse-code-translator-python/) and changed for my code#

        print(message)

def morseDecode(len_basic_string, len_splitString):
    if alphabetObj:
        st.MorseString = st.MorseString.upper()
        splitString = split_to_letters(st.MorseString)
        alpha_message = ""

        for i in range(len_basic_string):
            if i != 0:
                    alpha_message += "|"
            else:
                if splitString[i] == " " or splitString[i] == "|":
                    sys.exit("please do not start with separators")
            if i == len_basic_string-1 and (splitString[i] == " " or splitString[i] == "|"):
                sys.exit("please do not end with separators")

            if splitString[i] != " " and splitString[i] != "|":
                alpha_message += MORSE_CODE_ALPHABET[splitString[i]]

        print ("alphabet message  :", alpha_message)

st = myArgParser()

separatorObj = re.search(r'[\|]+', st.MorseString)
whitespaceObj = re.search(r'[\s]+', st.MorseString)
morseObj = re.search(r'[.\-]', st.MorseString, re.I)
alphabetObj = re.search(r'[a-zA-Z0-9]', st.MorseString, re.I)

len_splitString, len_basic_string, splitString = checkConditions(st)


morseNcode(len_basic_string, len_splitString, splitString)
morseDecode(len_basic_string, len_splitString)