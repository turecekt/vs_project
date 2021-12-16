#!/usr/bin/python3
# 14.12.2021
""" Codovani/Decodovani Morseovy abecedy. """

# mapa znaku morseovy abecedy
_chars = {
    'A':  ".-",    'N':  "-.",    '0':  "-----",   '\'': ".----.",
    'B':  "-...",  'O':  "---",   '1':  ".----",   '!':  "-.-.--",
    'C':  "-.-.",  'P':  ".--.",  '2':  "..---",   '/':  "-..-.",
    'D':  "-..",   'Q':  "--.-",  '3':  "...--",   '(':  "-.--.",
    'E':  ".",     'R':  ".-.",   '4':  "....-",   ')':  "-.--.-",
    'F':  "..-.",  'S':  "...",   '5':  ".....",   ':':  "---...",
    'G':  "--.",   'T':  "-",     '6':  "-....",   ';':  "-.-.-.",
    'H':  "....",  'U':  "..-",   '7':  "--...",   '+':  ".-.-.",
    'I':  "..",    'V':  "...-",  '8':  "---..",   '-':  "-....-",
    'J':  ".---",  'W':  ".--",   '9':  "----.",   '_':  "..--.-",
    'K':  "-.-",   'X':  "-..-",  '.':  ".-.-.-",  '"':  ".-..-.",
    'L':  ".-..",  'Y':  "-.--",  ',':  "--..--",  ' ':  ",",
    'M':  "--",    'Z':  "--..",  '?':  "..--..",  '\n': ",",
}

def atom(c):
    """ Codovani jednoho znaku do Morseovy abecedy. """
    try: return _chars[c.upper()]
    except: return '{'+ c +'}'

def mtoa(c):
    """ Decodovani jednoho znaku Morseovy abecedy. """
    try: return list(_chars.keys())[list(_chars.values()).index(c)]
    except: return '{'+ c +'}' if c else c

def tomorse(s):
    """ Codovani z textu do Morseovy abecedy. """
    return "/".join(atom(c) for c in list(s)) if s else ''

def frommorse(s):
    """ Decodovani z Morseovy abecedy do textu. """
    return "".join(mtoa(c) for c in \
        s.translate(str.maketrans('','',' \n')).split('/'))

if __name__ == "__main__":
    import sys
    # detekce argumentu se vstupem:
    if len(sys.argv) <= 1: s = sys.stdin.read()
    else: s = " ".join(sys.argv[1:])
    # detekce morseovy abecedy:
    print(tomorse(s) if s.strip(".-/, \n") else frommorse(s))

