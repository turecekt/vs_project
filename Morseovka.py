import unittest

#Definování morseovky
MORSE_CODE_DICT = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}

def zakodovani(text): #funkce pro zakodovani
    zakodovany_text = "" #zakodovany text = string
    for pismena in text.upper(): 
        if pismena != " ": #kontrola mista
            zakodovany_text += MORSE_CODE_DICT[pismena] + ' ' #vyhleda slovnik a prida odpovidajici znak + mezeru
        else:
            zakodovany_text += " " #pridani mezery
    return zakodovany_text #vypis zakodovany text


def dekodovani(text): #funkce pro dekodovani
    global prostor
    text += " " 
    kod = "" 
    normal = ""
    for pismena in text:
        if pismena != " ": #kontrola mista
            kod += pismena #ukladani morseovky po znaku
            prostor = 0 #prostor
        else:
            prostor += 1 #pokud je rovno 1 oznacuje pismeno
            if prostor == 2: #pokud je rovno 2 oznacuje nove slovo
                normal += " " #pridani mezery
            else:
                normal += \
                    list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(kod)] #pristup ke klicum pomoci jejich hodnot
                kod = ""
    return normal  #vypis dekodovany text

def main():

    sifrovani = input('Morse Encoder/Decoder\n'
                      ' d for decode \n'
                      ' e for encode \n'
                      'Enter what you want to do: \n')
    if sifrovani == 'e':
        text_k_zakodovani = input('Enter text to encode: \n').upper()
        print(zakodovani(text_k_zakodovani))
    elif sifrovani == 'd':
        text_k_dekodovani = input('Enter text to decode: \n')
        print(dekodovani(text_k_dekodovani))
    else:
        print('Wrong choice...\nExiting...')


if __name__ == '__main__':
    main()

#test zakodovani znaku
def test_zakodovani():
    vstup = source.zakodovani('.-')
    self.assertEqual(vstup, 'a')

#test zakodovani textu
def test_zakodovani01(self):
    vstup = source.zakodovani("test")
    self.assertEqual(vstup, "- . ... - ")

#test zakodovani cisel
def test_zakodovani02(self):
    vstup = source.zakodovani("1, 2, 3, 4")
    self.assertEqual(vstup, ".---- --..--  "
                            "..--- --..--  ...-- --..--  ....- ")

#test dekodovani znaku
def test_dekodovani():
    vstup = source.dekodovani('a')
    self.assertEqual(vstup, '.-')

#test dekodovani textu
def test_dekodovani01(self):
    vstup = source.dekodovani("- . ... -")
    self.assertEqual(vstup, "TEST")

#test dekodovani cisel
def test_dekodovani02(self):
    vstup = source.dekodovani("----- -----  .----  ..---  ...--  ....-")
    self.assertEqual(vstup, "00 1 2 3 4")

if __name__ == '__main__':
    unittest.main()
