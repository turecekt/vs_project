morseABECEDA = {
    ' ': '/',
    'A': '.–/',
    'B': '–.../',
    'C': '–.–./',
    'D': '–../',
    'E': './',
    'F': '..–./',
    'G': '––./',
    'H': '..../',
    'CH': '––––/',
    'I': '../',
    'J': '.–––/',
    'K': '–.–/',
    'L': '.–../',
    'M': '––/',
    'N': '–./',
    'O': '–––/',
    'P': '.––./',
    'Q': '––.–/',
    'R': '.–./',
    'S': '.../',
    'T': '−/',
    'U': '..–/',
    'V': '...–/',
    'W': '.––/',
    'X': '–..–/',
    'Y': '–.––/',
    'Z': '––../'
}

ABECEDAmorse = {
    '/': ' ',
    '.–': 'A',
    '–...': 'B',
    '–.–.': 'C',
    '–..': 'D',
    '.': 'E',
    '..–.': 'F',
    '––.': 'G',
    '....': 'H',
    '––––': 'CH',
    '..': 'I',
    '.–––': 'J',
    '–.–': 'K',
    '.–..': 'L',
    '––': 'M',
    '–.': 'N',
    '–––': 'O',
    '.––.': 'P',
    '––.–': 'Q',
    '.–.': 'R',
    '...': 'S',
    '−': 'T',
    '..–': 'U',
    '...–': 'V',
    '.––': 'W',
    '–..–': 'X',
    '–.––': 'Y',
    '––..': 'Z'
}

def Txt_do_Morse():
    txt = input('Napiste text, ktery se ma prelozit do Morseovky:')
    code = [morseABECEDA[i.upper()] + '' for i in txt if i.upper() in morseABECEDA.keys()]
    morse = ''.join(code)
    print(morse)

def Morse_do_Txt():
    txt = input('Napiste Morseovku ktera se ma prekladat na text:')
    novy = txt.split('/')
    code = [ABECEDAmorse[i] + '' for i in novy if i in ABECEDAmorse.keys()]
    morse = ''.join(code)
    print(morse)


print('''\n1- Prelozit text na Morseovku \n2- Prelozit Morseovku na text ''')


while True:
    try:
        selection = int(input('Vyberte si co na co chcete prekladat:'))
        if selection == 1:
            print((Txt_do_Morse()))
            break
        elif selection == 2:
            print(Morse_do_Txt())
            break
        else:
            print('Spatna volba')
    except:
        print('Spatna volba')


def test_prekladslov():

    assert prekladslov("AHOJ") == " .–/..../–––/.–––/"
    assert prekladslov('DOMOV') == "–../–––/––/–––/...–/"
    assert prekladslov("DNES JE HEZKE POCASI") == "–../–././...//.–––/.//...././––../–.–/.//.––./–––/–.–./.–/.../../"
