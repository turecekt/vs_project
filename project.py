'''Morse code translator'''
library = {'A': '.-', 'B': '-...',
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
                    '(':'-.--.', ')':'-.--.-', ' ':'.....'}

# Translating morse code to latin
def morseEncrypt(txt):
    translation = ''
    # Swaping keys from library:
    lib_encrypt = dict([(v, k) for k, v in library.items()])
    # Morse code output will be splitted with space
    txt = txt.split(' ')
    for x in txt:
        translation += lib_encrypt.get(x)
    return translation.strip()
# Translating latin to morse code:
def morseDecrypt(txt):
    translation = ''
    txt = txt.upper()
    for x in txt:
        translation += library.get(x) + ' '
    return translation.strip()

pokracuj = True
while pokracuj:
    print("Menu: (Zadejte číslo, popřípadě zmáčkněte enter)")
    print("1: Překlad z morseovky do abecedy")
    print("2: Překlad z abecedy do morseovky")
    print("Pro ukončení programu zmáčkněte ENTER")
    print("********************************")
    print("Vyberte jednu z možností výše")
    vyber = input(":")
    if vyber == "":
        exit()
    else:
        print("Zadejte morseovku/text který chcete přeložit")
        text = input(":")
        if vyber =="1":
            print(morseEncrypt(text))
            print("Chcete zpátky do menu a opakovat program? y/n")
            pokracuj = input().upper()
            if pokracuj == "N":
                pokracuj = False
            else:
                pokracuj = True
        elif vyber =="2":
            print(morseDecrypt(text))
            print("Chcete zpátky do menu a opakovat program? y/n")
            pokracuj = input().upper()
            if pokracuj == "N":
                pokracuj = False
            else:
                pokracuj = True
        else:
            exit()
else:
    exit()




