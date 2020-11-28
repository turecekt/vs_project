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
morse_alphabet = {
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

# Funkce s logikou hlavní smyčky programu    
def mainLoop():
    # Menu (základní nastavení pro kódování a dekódování)
    print("Welcome to the translator!\n")
    isAlphabet = isAlphabetTranslation()
    
# Spuštění hlavní smyčky
mainLoop()
