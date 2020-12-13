"""Kodovani a dekodovaní morseovy text."""

"""Abeceda potřebná na překlad na Morse"""
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

"""Abeceda potřebná na překlad na text"""
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
    """Přeložení text do morse."""
    txt = input('Napiste text, ktery se ma prelozit do Morseovky:')
    code = [morseABECEDA[i.upper()] + '' for i in txt
            if i.upper() in morseABECEDA.keys()]
    morse = ''.join(code)
    print(morse)


def Morse_do_Txt():
    """Přeložení morse na text."""
    txt = input('Napiste Morseovku ktera se ma prekladat na text:')
    novy = txt.split('/')
    code = [ABECEDAmorse[i] + '' for i in novy if i in ABECEDAmorse.keys()]
    morse = ''.join(code)
    print(morse)


print('''\n1- Prelozit text na Morseovku \n2- Prelozit Morseovku na text ''')

"""Vybrání možnosti překladu text do morse nebo morse na text."""
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
    except Exception:
        print('Spatna volba')


def test_prekladslov(prekladslov):
    """Předklad text na morse."""
    assert prekladslov("AHOJ") == " .–/..../–––/.–––/"
    assert prekladslov('DOMOV') == "–../–––/––/–––/...–/"
    assert prekladslov("DNES JE HEZKE POCASI") == \
           "–../–././...//.–––/.//...././––../–.–/.//.––./–––/–.–./.–/.../../"


def test_predkladmorse(predkladmorse):
    """Překlad morse na text."""
    assert predkladmorse("−/–––/––/.//.–––/.–/–.–//.–––/./") == "TOMEJAKJE"
    assert predkladmorse("–././.–./.–/–..//.––./.–./.–/–.–./..–/.–––/..–/") \
           == "NERADPRACUJU"
    assert predkladmorse(".–./–.––/–.–./..../.–.././/–././–.../–––//.––."
                         "/–––/––/.–/.–../..–/") == "RYCHLENEBOPOMALU"