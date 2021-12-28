#Překladač textu do morseova kodu a dekóder morseova kodu do textu

#Funkce pro definovani abecedy
def abeceda():

    # Abeceda pro překlad textu do orseovho kodu
    abeceda = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
               "k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
               "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---", "3":"...--",
               "4":"....-","5":".....","6":"-....","7":"--...","8":"---..", "9":"----.","0":"-----",",":"--..--",
               ".":".-.-.-","?":"..--..","/":"-..-.","-":"-....-","(":"-.--.",")":"-.--.-",":":"---...",";":"-.-.-.",
               "+":".-.-.","=":"-...-"}
               
    return abeceda

#Funkce pro překlad textu do morseovho kodu
def to_morse(vstup):
    morse_code = ""
    for pismeno in vstup:
        if pismeno.lower() in abeceda.keys():
            morse_code += abeceda[pismeno.lower()] + " "
        else:
            morse_code += pismeno.lower() + " "

        return morse_code  


abeceda = abeceda()

#vstupní formulár pro zadáni textu, kt. má být zakódován do morseovho kódu
text = input("Zadej text který chceš přenést do morseovky : ")

out = to_morse(text)
        
# Výstup překladače    
print(out)

import unittest   # Importování Unit testu

if __name__ == '__main__':
    unittest.main()
