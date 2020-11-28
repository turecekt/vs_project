# Mapování písmen abecedy na znaky Morseovy abecedy
alphabetMorse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "ch": "----",
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
    "z": "--.."
}

# Mapování znaků Morseovy abecedy na písmena abecedy
morseAlphabet = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "----": "ch",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z"
}

# Mezera
space = " ";

# Funkce, která zajišťuje správný výběr překladu
def isAlphabetTranslation():
    print("Translate from:")
    print("1 - Alphabet")
    print("2 - Morse code")
    while True:
        # Kontrola, jestli je uživatelský vstup číslo
        try:
            index = int(input("Enter the translation number: "))
        except ValueError:
            print("Not an integer!")
            continue
        if (index == 1):
            return True
        elif (index == 2):
            return False
        else:
            continue

def alphabetTranslation(text):
    result = ""
    for char in text.lower():
        if char in alphabetMorse:
            result += alphabetMorse[char]
    return result

def morseCodeTranslation(text):
    return "MORSE CODE"

def translation(text, isAlphabet):
    return alphabetTranslation(text) if isAlphabet else morseCodeTranslation(text)

# Funkce s logikou hlavní smyčky programu    
def mainLoop(isRepeat):
    # Menu (základní nastavení pro kódování a dekódování)
    print("Welcome to the Translator!\n") if isRepeat == False else print("Translator\n")
    isAlphabet = isAlphabetTranslation()
    print()

    text = input("Enter text between \"\": ")
    print()
    
    print("Translation:")
    print(translation(text, isAlphabet))

isRepeat = False
exitCode = 'n'
    
# Spuštění hlavní smyčky
while exitCode != 'y':
    mainLoop(isRepeat)
    exitCode = input("\nDo you want exit program (y/n): ").lower()
    print()
    isRepeat = True
