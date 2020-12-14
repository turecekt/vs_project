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
morseovka_preklad = {
    '/': ' ',
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '----': 'CH',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}


def Txt_do_Morse(slovo):
    """Přeložení text do morse."""
    code = [morseABECEDA[i.upper()] + '' for i in slovo
            if i.upper() in morseABECEDA.keys()]
    morse = ''.join(code)
    print(morse)
    return morse


def Morse_do_Txt(morse):
    """Přeložení morse na text."""
    novy = morse.split('/')
    text = ""
    print(novy)
    for i in novy:
        if i in morseovka_preklad.keys():
            text = text + morseovka_preklad[i]
        if i == "":
            text = text + " "
    return text


print('''\n1- Prelozit text na Morseovku \n2- Prelozit Morseovku na text ''')

"""Vybrání možnosti překladu text do morse nebo morse na text."""
if __name__ == "__main__":
    while True:
        try:
            selection = int(input('Vyberte si co na co chcete prekladat: '))
            if selection == 1:
                slovo = input('Napiš slovo ')
                print(Txt_do_Morse(slovo))
                break
            elif selection == 2:
                slovo = input('Napiš morseovku ')
                print(Morse_do_Txt(slovo))
                break
            else:
                print('Spatna volba')
        except Exception:
            print('Spatna volba')


def test_Txt_do_Morse():
    """Předklad text na morse."""
    text = "AHOJ"
    assert Txt_do_Morse(text) == ".–/..../–––/.–––/"


def test_Morse_do_Txt():
    """Překlad morse na text."""
    code = ".---/.-/-.-//.---/./"
    assert Morse_do_Txt(code) == "JAK JE "
