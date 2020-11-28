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
def getLanguageIndex():
    print("Select languages:")
    printSupportLanguages()
    # Smyčka se opakuje, tak douho, dokud není vybrán správný jazyk
    while True:
        # Kontrola, jestli je uživatelský vstup číslo
        try:
            index = int(input("Enter number of language: ")) - 1
        except ValueError:
            print("Not an integer!")
            continue 
        if (index >= 0 and index < len(languages)):
            return index

# Funkce, která zajišťuje správný výběr překladu
def isLanguageTranslation():
    print("Translate from:")
    print("1 - Language")
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

# Funkce s logikou hlavní smyčky programu    
def mainLoop():
    # Menu (základní nastavení pro kódování a dekódování)
    print("Welcome to the translator!\n")
    languageIndex = getLanguageIndex()
    print()
    isLangTranslation = isLanguageTranslation()
    
# Spuštění hlavní smyčky
mainLoop()
