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
        vysledek += Morseovka[c] + " "
    return vysledek


def toWord(morseMessage):
    pass

def testToMorse():
    pass

def testToWord():
    pass

def main():
    #zde bude nacitani vstupu a vyber zda se bude kodovat nebo dekodovat
    a = "ahoj"
    d = toMorse(a)

    print(d)


if __name__ == '__main__':
    main()

