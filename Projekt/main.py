import pytest

#Objekt morseovka
class MorseDictionary:
    dictionary = { 'A':'.-', 'B':'-...',
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

#zapninani programu
def main():
    once = True
    morse(once)

def morse(once):
    if (once):
        yep = input("If you want to see a summary of all available characters, press Y and Enter:")
        yep = yep.upper()
        once = False
        if (yep == "Y"):#pokud y, vypise mozne znaky
            print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
            input("Press Enter to continue..")
    decision = input("For encoding morse press 1, For decoding morse press 2, for exit press 3:") #co chces delat / dekodovat / zakodovat
    if (decision == "3"):
        print("Goodbye")
    else:
        if (decision == "1"): #dekodovani
            text = input("Enter text to encode:")
            print(encode(text,MorseDictionary.dictionary))
            input("Press Enter to continue")
            morse(once)
        elif (decision == "2"): #rozkodovani
            text = input("Enter morse code to decode, write / after every letter, write // after every word:")
            print(decode(text,MorseDictionary.dictionary))
            input("Press Enter to continue")
            morse(once)
        else: #spatnej input
            print("Your input isn't 1 or 2")
            input("Press Enter to continue")
            morse(once)

# Funkce zakoduje do morseovky
def encode(message,morseCode):
    try:
        message = message.upper()
        counter = 1
        code = ''
        for letter in message:
            if letter != ' ':
                if counter < len(message):
                    # Najde ve slovniku odpovidajici kod pro jednotlive znaky
                    code = code + morseCode[letter] + '/'
                else:
                    code = code + morseCode[letter]
            else:
                # 1 / jsou ruzne znaky, 2 / ruzna slova
                code += '/'
            counter = counter + 1
 
        return code
    # Pøi nedefinovaném vstupu se vypíše chybová hláška
    except KeyError: 
        print("Wrong character " + letter)
        return ("Character is not defined in morse code. These characters are defined: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ")

# Funkce dekóduje z morseovky
def decode(inputMessage,morseCode):
    try:
        decodedMessage = ''
        message = inputMessage.split('//') # Do message se uloží všechny slova
        counter = 1
   
        for word in message:
            letters = word.split('/') # Do letters se uloží všechny písmena
            for letter in letters:
                if (letter != ''): # Pro každé písmeno se najde odpovídající klíè v dictionary morseCode
                    decodedMessage = decodedMessage + list(morseCode.keys())[list(morseCode.values()).index(letter)]
            if (counter < len(message)): # Krom posledního slova, se za každým slovem pøipíše mezera
                decodedMessage = decodedMessage + ' '
            counter = counter + 1
        return decodedMessage
    except Exception: # Při nenalezení hodnoty v dictionary se vypíše chybová hláška
        print("Wrong character: " + letter)
        return ("Character is not defined in morse code")

if __name__ == '__main__':
        main()

def test_decode():
    assert decode(".-",MorseDictionary.dictionary) == "A"

def test_encode():
    assert encode("A",MorseDictionary.dictionary) == ".-"

def test_decode2():
    assert decode("@",MorseDictionary.dictionary) == "Character is not defined in morse code"

def test_encode2():
    assert encode("@",MorseDictionary.dictionary) == "Character is not defined in morse code. These characters are defined: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - "

def test_morse():
    set_keyboard_input(["Y", "", "3"])
    morse(True)
    output = get_display_output()
    assert output == ["If you want to see a summary of all available characters, press Y and Enter:",
                      "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )",
                      "Press Enter to continue..",
                      "For encoding morse press 1, For decoding morse press 2, for exit press 3:",
                      "Goodbye"]
import builtins

inner_values = []
print_values = []

def vstup(s):
    print_values.append(s)
    return inner_values.pop(0)

def vstup_vystup_start():
    global inner_values, print_values

    inner_values = []
    print_values = []

    builtins.input = vstup
    builtins.print = lambda s: print_values.append(s)

def get_display_output():
    global print_values
    return print_values

def set_keyboard_input(vstupy):
    global inner_values

    vstup_vystup_start()
    inner_values = vstupy