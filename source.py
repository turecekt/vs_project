#Funkce pro převod z Morseovky do abecedy a naopak
def prevod(vstup):

    # Vytvoření dictionary pro morseovku
    morseovka = {'1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' '}

    g = ""

    #Převedení z morseovky na text
    if vstup.startswith('.') or vstup.startswith('-'):
        
        #Rozdělení morseovky na jednotlivé kombinace
        rozdVstup = vstup.split(' ')

        #Vytvoření cyklu pro převod z morseovky na text
        for prvek in rozdVstup:
            if prvek not in morseovka.values():
                    print('Zadávané znaky nejsou písmena, či číslice, nebo znaky morseovky') # Ošetření vstupu
                    exit()
            for i in morseovka:
                if prvek == morseovka[i]:
                    g = g + i
            
        return g

    #Převedení z textu do morseovky
    else: 
        #Převedení textu na velká písmena
        vstupV = vstup.upper()

        #Převedení textu na pole znaků
        rozdVstup = list(vstupV)

        # Vytvoření cyklu for pro převod zadaných znaků do morseovky
            
        for prvek in rozdVstup:
            if prvek not in morseovka:
                    print('Zadávané znaky nejsou písmena, či číslice, nebo znaky morseovky') # Ošetření vstupu
                    exit()
            for i in morseovka:
                if prvek == i:
                    g = g + morseovka[i] + ' '

        return g

#vytvoření vstupu
print('--KODÉR A DEKODÉR MORSEOVKY--')
vstup = input('Zadejte text pro převod: ')

#výstup
print(prevod(vstup))

