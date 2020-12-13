MORSEUV_SLOVNIK = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}

def Text_na_Morseovku():
    text = input('Napis text pro Morseovo sifrovani : ')
    kod = [MORSEUV_SLOVNIK[i.upper()] + ' ' for i in text if i.upper() in MORSEUV_SLOVNIK.keys()]
    morseovka=''.join(kod)
    print(morseovka)

def Morseovka_na_Text():
    text = input('Napis Morseuv kod pro desifrovani do textu: ')
    kod = [j for i in text.split() for j,k in MORSEUV_SLOVNIK.items() if i==k]
    text2 = ''.join(kod)
    print(text2)