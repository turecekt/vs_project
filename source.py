#Funkce pro převod
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

    #Převedení textu na velká písmena
    vstupV = vstup.upper()

    #Převedení textu na pole znaků
    rozdVstup = list(vstupV)

    # Vytvoření cyklu for pro převod zadaných znaků do morseovky
    g = ""    
    for prvek in rozdVstup:
        if prvek not in morseovka:
                print('Zadávané znaky můžou být jen písmena bez diakritiky a číslice') # Ošetření podmínek
                exit()
        for i in morseovka:
            if prvek == i:
                g = g + morseovka[i] + ' '

    return g

#UNIT TEST 1
def unitTest1():
    result = "... --- ... "
    s = "sos"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 2
def unitTest2():
    result = "...-- -.... ..... "
    s = "365"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 3
def unitTest3():
    result = "...- . .-.. .. -.- --- ... - "
    s = "vEliKoSt"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 4
def unitTest4():
    result = "-.-. .. ... .-.. --- ....- ..--- "
    s = "Cislo42"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")

#UNIT TEST 5
def unitTest5():
    result = ".- .... --- .---   .--- .- -.-   ... .   -- .- ..."
    s = "Ahoj jak se mas"
    test = prevod(s)
    if result == test:
        return print("OK")
    else:
        return print("NOT OK")




#vytvoření vstupu
vstup = input('Zadejte text pro převod do Morseovky: ')

#výstup
print(prevod(vstup))

