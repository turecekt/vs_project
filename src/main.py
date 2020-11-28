# Mapování písmen abecedy na znaky Morseovy abecedy
alphabet_morse = {
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
    "z": "--.."
}

# Mapování znaků Morseovy abecedy na písmena abecedy
morse_alphabet = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
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

# Podporované jazyky
languages = ["English", "Czech"]

# Funkce, která vypíše do konzole podporované jazyky
def printSupportLanguages():
    index = 1
    for language in languages:
        print(str(index) + " - " + language)
        index += 1

# Funkce, která zajišťuje správný výběr podporovaného jazyka
def language():
    print("Select languages:")
    printSupportLanguages()
    # Smyčka se opakuje, tak douho, dokud není vybrán správný jazyk
    while True:
        indexLanguageStr = input("Enter number of language: ")
        # Kontrola, jestli je uživatelský vstup číslo
        try:
            indexLanguageInt = int(indexLanguageStr) - 1
        except ValueError:
            print("Not an integer!")
            continue
        if (indexLanguageInt >= 0 and indexLanguageInt < len(languages)):
            return indexLanguageInt

# Funkce s logikou hlavní smyčky programu    
def mainLoop():
    # Menu (základní nastavení pro kódování a dekódování)
    print("Welcome to the translator!\n")
    lang = language()
    
# Spuštění hlavní smyčky
mainLoop()
