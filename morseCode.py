"""

this is module to Ncode alphabet messages to morse code and vice versa

module contains "asserts" alphanum chars as morse code strings also my added separators codes 

also contains multiple functions:

split_to_letters()
myArgParser()
checkConditions()
morseDecode()
morseNcode()

"""


import argparse
import re
import sys
import pytest

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
    """
    function split_to_letters returns list of characters from string

    Args:
        -my_string - Input string 
    
    Returns:
        - list of separated characters
    """

    return list(my_string)

morseAlphNum = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_ch, letter_i, letter_j,
                letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t, letter_v, letter_u, 
                letter_w, letter_x, letter_y, letter_z, number_0, number_1, number_2, number_3, number_4, number_5, number_6, 
                number_7, number_8, number_9, space, separator]

def myArgParser(args):
    """
    function myArgParser returns obj with parsed argument (which should be string)
    also checks if the string contains valid characters (alphanumeric chars, dots, dashes, verticals[as separators])
    takes argument from command line

    Args:
        -args - Command line argument
    
    Returns:
        - st.MorseString - input string
    """
    msg = "type in the string consist of morse code or alphanumeric characters"

# this had to be because python (more like unix) doesnt take double dash as a string but it expects something to go after ... so I had to check for it
    if args == '--':
        sys.exit("M")
    else:
        parser = argparse.ArgumentParser(description = msg)
        parser.add_argument('MorseString', metavar='String', type=str, help='a string to decode/Ncode from/to morse code')

    st = parser.parse_args()

    errorObj = re.search(r'[^a-zA-Z0-9 \-\.\|]', st.MorseString, re.I)

    if errorObj:
        sys.exit("please type in right characters")

    return st.MorseString


def checkConditions(st):
    """
    function checkConditions returns lengths of string which is already stripped to characters without separators and string with separators
    also returns string which is stripped
    it checks if is used only whitespaces or verticals and also if you want to only Ncode or Decode ... you cant do both at the same time
    then magic with verticals and spaces happens  

    Args:
        -st - input string 

    Returns:
        -len_basic_string - number of characters in string
        -len_splitString - number of characters in stripped string
        -splitString - stripped string (without separators)
    """
    separatorObj = re.search(r'[\|]+', st)
    whitespaceObj = re.search(r'[\s]+', st)
    morseObj = re.search(r'[.\-]', st, re.I)
    alphabetObj = re.search(r'[a-zA-Z0-9]', st, re.I)


    if separatorObj and whitespaceObj:
        sys.exit("please use only one way to split letters/words")

    if morseObj and alphabetObj:
        sys.exit("please use only alphabet to Ncode it or morse code to Decode it")

    if separatorObj:
        st = re.sub(r'\|\|\|+', "||", st)
        newString = re.sub(r'\|\|', "|----....|", st)
        splitString = newString.split("|")
    elif whitespaceObj:
        newString = re.sub(r'\s\s', " ....---- ", st)
        splitString = newString.split()
    else:
        newString = st
        splitString = newString.split()
    
    len_splitString = len(splitString)
    len_basic_string = len(split_to_letters(st))

    return len_splitString, len_basic_string, splitString


def morseDecode(len_splitString, len_basic_string, splitString, st):
    """
    function morseDecode returns printed Decoded message from morse code
    it goes through the string and checks if you start or end with separators (not valid)
    also it checks if you use valid morse code which is written above 

    Args:
        -st - input string
        -len_basic_string - number of characters in none stripped input string
        -len_splitString - number of substrings in stripped input string
        -splitString - stripped input string into substrings from alphabet
    
    Returns:
        - message - returns the decoded message

    """

    letters = split_to_letters(st)
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
    return message

def morseNcode(len_splitString, len_basic_string, st):
    """
    function morseNcode ncodes the alphabet message to the morse code it uses verticals as separators
    also it goes through the string and checks if you start or end with separators
    then it checks if the character is separator if not it replaces alphanum chars with morse chars

    Args:
        -st - input string
        -len_basic_string - number of characters in none stripped input string
        -len_splitString - number of substrings in stripped input string

    Returns:
        -ncode_message - morse coded message 

    """

    st = st.upper()
    splitString = split_to_letters(st)
    ncode_message = ""

    for i in range(len_basic_string):
        if i != 0:
                ncode_message += "|"
        else:
            if splitString[i] == " " or splitString[i] == "|":
                sys.exit("please do not start with separators")
        if i == len_basic_string-1 and (splitString[i] == " " or splitString[i] == "|"):
            sys.exit("please do not end with separators")
        if splitString[i] != " " and splitString[i] != "|":
            ncode_message += MORSE_CODE_ALPHABET[splitString[i]]
            
    return ncode_message

#flake
#pak fork dokoncit

def main():
    """ Main function where the program runs and all the functions are called"""
    myStr = myArgParser(sys.argv[1])

    separatorObj = re.search(r'[\|]+', myStr)
    whitespaceObj = re.search(r'[\s]+', myStr)
    morseObj = re.search(r'[.\-]', myStr, re.I)
    alphabetObj = re.search(r'[a-zA-Z0-9]', myStr, re.I)


    len_splitString, len_basic_string, splitString = checkConditions(myStr)

    if morseObj:
        message = morseDecode(len_splitString, len_basic_string, splitString, myStr)
    elif alphabetObj:
        message = morseNcode(len_splitString, len_basic_string, myStr)

    print(message)

if __name__ == '__main__':
    main()

def testParser():
    parser = myArgParser("hello")
    assert(parser == myArgParser(sys.argv[1]))
    parser = myArgParser("---")
    assert(parser == myArgParser(sys.argv[1]))


def testSplitToLetters():
    assert split_to_letters("....") == ['.', '.', '.', '.']
    assert split_to_letters("aaaa") == ['a', 'a', 'a', 'a']

def testCheckConditions():
    assert(checkConditions("ahoj H") == (2, 6, ['ahoj', 'H']))
    assert(checkConditions("....    ....") == (4, 12, ['....', '....----', '....----', '....']))

def testMorseDecode():
    num_substring, basic_str_len, splitString = checkConditions(".... ....")
    assert(morseDecode(num_substring, basic_str_len, splitString, ".... ....") == "HH")
    num_substring, basic_str_len, splitString = checkConditions("....||-...|-.--|-..|.-..|..||...-||..-|.-..|..|-.-.|..||-.-.|---|..-|.--.|-.-|---|...-|-.--|-.-.|....||----.|-----")
    assert(morseDecode(num_substring, basic_str_len, splitString, "....||-...|-.--|-..|.-..|..||...-||..-|.-..|..|-.-.|..||-.-.|---|..-|.--.|-.-|---|...-|-.--|-.-.|....||----.|-----") == "H|BYDLI|V|ULICI|COUPKOVYCH|90")

def testMorseNcode():
    num_substring, basic_str_len, splitString = checkConditions("hello")
    assert(morseNcode(num_substring, basic_str_len, "hello") == "....|.|.-..|.-..|---")
    num_substring, basic_str_len, splitString = checkConditions("hello there")
    assert(morseNcode(num_substring, basic_str_len, "hello there") == "....|.|.-..|.-..|---||-|....|.|.-.|.")
    num_substring, basic_str_len, splitString = checkConditions("ulice coupkovych 8")
    assert(morseNcode(num_substring, basic_str_len, "ulice coupkovych 8") == "..-|.-..|..|-.-.|.||-.-.|---|..-|.--.|-.-|---|...-|-.--|-.-.|....||---..")

""" 
def testMyArgParser():
    
    assert isinstance(parser, ArgumentParser)
    assert isinstance(parser, list)
    args = {_.dest: _ for _ in parser._actions if isinstance(_, _StoreAction)}

    assert args.keys() == {"MorseString"}
    assert args["MorseString"].type == str
    assert args["MorseString"].help == 'a string to decode/Ncode from/to morse code'
    assert args["MorseString"].metavar == 'String'
    assert args["MorseString"] == argv[1] """