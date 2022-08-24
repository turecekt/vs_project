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
    for pismena in text: 
        if pismena != " ": #kontrola mista
            zakodovany_text = zakodovany_text + MORSE_CODE_DICT.get(pismena) #vyhleda slovnik a prida odpovidajici znak + mezeru
        else:
            zakodovany_text += " " #pridani mezery
    return(zakodovany_text) #vypis zakodovany text


def dekodovani(text): #funkce pro dekodovani
    text += " " #pridani mezery
    key_list = list(MORSE_CODE_DICT.keys()) #pro pristup ke klicum
    val_list = list(MORSE_CODE_DICT.values())
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
                normal = normal + key_list[val_list.index(kod)] #pristup ke klicum pomoci jejich hodnot
                kod = ""
    return(normal) #vypis dekodovany text

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

#test zakodovani textu
def test_zakodovani():
    assert zakodovani('.-') == 'a'

#test dekodovani textu
def test_dekodovani():
    assert dekodovani('a') == '.-'

if __name__ == '__main__':
    unittest.main()
