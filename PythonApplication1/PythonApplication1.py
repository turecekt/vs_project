MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):

    """
    Kodujeme naše slovo.
     
    >>>encrypt("neco")
    "-. . -.-. ---"
    """
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
 
    return cipher.strip()
 


def main():
    message = "neco"
    result = encrypt(message.upper())
    print (result)
    print (message)
 

if __name__ == '__main__':
    main()
    

def test_answers ():
    assert encrypt ("sos")=="... --- ..."
    assert encrypt ("neco")=="-. . -.-. ---"
