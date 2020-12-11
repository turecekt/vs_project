#zde budeme delat nas projekt
#TODO: potreba udelat komentare
#TODO: udelat funkci toMorse, ktera prevede text do morseovky
#TODO: udelat funkci toWord, která prevede morseovku do slov
#TODO: udelat nacitani vstupu vyber zda chce uzivatel kodovat nebo dekodovat
#TODO: udelat testy

def toMorse(message):
    Morseovka={
        #Pismena
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        #Cisla
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Specialniznaky
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
    vysledek = ""
    for c in message:
        vysledek += Morseovka.get(c,";") + " "
    if(vysledek.find(";") != -1):
        vysledek = "chybne zadany vstup"        
    return vysledek


def toWord(morseMessage):
    Morseovka={
        #Pismena
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        #Cisla
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Specialniznaky
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
    vysledek = ""
    for x in morseMessage:
        vysledek = Morse.message.split(" ")
        vysledek += Morseovka.get(x,";")
    if(vysledek.find(";") != -1):
        vysledek = "chybne zadany vstup"        
    return vysledek

def testToMorse():
    pass


def testToWord():
    pass


def main():
    #zde bude nacitani vstupu a vyber zda se bude kodovat nebo dekodovat
    print('Zadej co chces prelozit do morseovky: ')
    a = input()
    a.lower()
    d = toMorse(a)
    print(d)
    b = input("zadej text v morseovce: ")
    print(toWord(b))



if __name__ == '__main__':
    main()



