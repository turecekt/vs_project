#zapninani programu
def start():
    once = True
    morse()

def morse():
    #inicializace pouze jednou na zacatku
    if (once):
        morseovka = { 'A':'.-', 'B':'-...',
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
        yep = input("If you want to see a summary of all available characters, press Y and Enter:")
        yep = yep.upper
        once = False
        if (yep == "Y"):
            print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
            input("Press Enter to continue..")

    decision = input("For encoding morse press 1, For decoding morse press 2, for exit press 3:")
    if (decision == "3"):
        print("Konec")
    else:
        if (decision == "1"):
            text = input("Enter text to encode:")
            encode(text)
            input("Press Enter to continue")
            morse()
        elif (decision == "2"):
            text = input("Enter morse code to decode, write / after every letter, write // after every word:")
            decode(text)
            input("Press Enter to continue")
            morse()
        else:
            print("Your input isn't 1 or 2")
            input("Press Enter to continue")
            morse()

# Slovnik obsahujici znaky morseovky
morseovka = { 'A':'.-', 'B':'-...',
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
 
# Funkce zakoduje do morseovky
def encode(zprava):
    try:
        zprava = zprava.upper()
        counter = 1
        kod = ''
        for pismeno in zprava:
            if pismeno != ' ':
                if counter < len(zprava):
                    # Najde ve slovniku odpovidajici kod pro jednotlive znaky
                    kod = kod + morseovka[pismeno] + '/'
                else:
                    kod = kod + morseovka[pismeno]
            else:
                # 1 / jsou ruzne znaky, 2 / ruzna slova
                kod += '/'
            counter = counter + 1
 
        return print(kod)
    # Pøi nedefinovaném vstupu se vypíše chybová hláška
    except KeyError: 
        print("Znak", pismeno, "není definovaný v morseovì abecedì")
        print("Definované znaky jsou: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ( )")
       

def decode(zprava):
    try:
        decodedMessage = ''
        message = zprava.split('//')
        counter = 1
   
        for word in message:
            letters = word.split('/')
            for letter in letters:
                if (letter != ''):
                    decodedMessage = decodedMessage + list(morseovka.keys())[list(morseovka.values()).index(letter)]
            if (counter < len(message)):
                decodedMessage = decodedMessage + ' '
            counter = counter + 1
        return   print(decodedMessage)
    except Exception: 
        print("Znak", letter, "není definovaný v morseovì abecedì")