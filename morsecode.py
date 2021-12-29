"""

Překladač textu do morseova kodu a dekóder morseova kodu do textu.
Kod obsahuje i výběrové menu pro překlad na text nebo morseovku.

"""

# Funkce pro definovani abecedy
def abeceda():

    # Abeceda pro překlad textu do morseovho kodu
    abeceda = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", 
               "k": "-.-", "l": ".---", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", 
               "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", 
               "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ",": "--..--", 
               ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", ":": "---...", ";": "-.-.-.", 
               "+": ".-.-.", "=": "-...-"}
               
    return abeceda

abeceda = abeceda()

# Funkce pro překlad textu do morseovho kodu
def to_morse(vstup):
    morse_code = ""
    for pismeno in vstup:
        if pismeno.lower() in abeceda.keys():
            morse_code += abeceda[pismeno.lower()] + " "
        else:
            morse_code += pismeno.lower() + " "

    return morse_code

# Fuknce pro překlad morseovky na text    
def from_morse(vstup):

    vstup += ' '
 
    text = ''
    bvstup = ''
    for pismeno in vstup:
 
        if (pismeno != ' '):
 
            i = 0
 
            bvstup += pismeno
 
        else:
            i += 1
 
            if i == 2 :
 
                text += ' '
            else:
 
                text += list(abeceda.keys())[list(abeceda.values()).index(bvstup)]
                bvstup = ''
 
    return text

# Menu pro překlad textu na morseovku nebo morseovky na text
def main():

    menu = input("Vyber si :\n\n 1. Chcem zakódovať text do morzeovky (Zadaj číslo 1).\n 2. Chcem dekódovať text z morzeovky (Zadaj číslo 2).\n 3. Ukončiť program (Zadaj ľubovolný znak alebo čísla od 3 do 9)\n\n  - Zadajte svoju voľbu : ")
    if menu == "1" :
        text = input("\n  -- Zadej text který chceš přenést do morseovky : ")
        vypis = "\n  --- Preklad : " + to_morse(text)
    elif menu == "2":
        text = input("\n  -- Zadej text který chceš přenést z morseovky : ")
        vypis = "\n  --- Preklad : " + from_morse(text)
    else:
        vypis = "\n --- Ukončili ste program --- "
    print(vypis)
    
    

# Importování Unit testu    
import unittest   

if __name__ == '__main__':
    main()
    unittest.main()

   

def test_to():
    # Test překladu textu do morseovky
    assert(to_morse("ahoj")) == ".- .... --- .--- "


def test_from():
    # Test překladu morseovky na text
    assert(from_morse("--.. -.. .- .-. . -.-.")) == "zdarec"
    
