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
    
# Vytvoření vstupu a následovné převedení vstupu na pole znaků
vstup = input('Zadejte text pro převod do Morseovky: ').upper()

rozdVstup = list(vstup)
# Vytvoření cyklu for pro převod zadaných znaků do morseovky
g = ""    
for prvek in rozdVstup:
    if prvek not in morseovka:
            print('Zadávané znaky můžou být jen písmena bez diakritiky a číslice') # Ošetření podmínek
            exit()
    for i in morseovka:
        if prvek == i:
            g = g + morseovka[i] + ' '
        

print(g) # Výstup      

 