""" Morseova abeceda """

MORSEUVA_ABECEDA = {
                    ' ': '/', 'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '@': '.--.-.',
                    '  ': '|', '=': '-...-'
                }

#"""def sifrovani()"""
 #   """Šifrovaní textu do morseovky"""

#"""def desifrovani()"""
 #   """Dešifrování textu z moreovky"""
    



"""Výběrové menu"""
print('''\n Vyber možnost: 
             1 - Šifrování do morseovy abecedy
             2 - Dešifrování morseovy abecedy
             3 - konec''')

volba = int(input("Zadej možnost 1-3: "))
if volba == 1:
    print("výběr šifrování")
elif volba == 2:
    print("výběr dešifrování")
elif volba == 3:
     print("ukončení programu")
else:
    print("špatná volba bude opakování menu") 
