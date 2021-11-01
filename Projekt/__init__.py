

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
def zakodovat(zprava):
    kod = ''
    for pismeno in zprava:
        if pismeno != ' ':
 
            # Najde ve slovniku odpovidajici kod pro jednotlive znaky
            kod = kod + morseovka[pismeno] + ' '
        else:
            # 1 mezera jsou ruzne znaky, 2 mezery ruzna slova
            kod += ' '
 
    return kod
 
# Funkce dekoduje z morseovky
def dekodovat(zprava):