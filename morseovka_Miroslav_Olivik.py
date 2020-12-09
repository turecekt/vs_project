# !/usr/bin/en v python3


# Jako první věc si msíme definovat abecedu, ke každému písmenu deklarujeme morseovo písmeno
SLOVNIK_MORSEOVKA = { ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--','4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..', '9': '----.',

                    '0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.', '-': '-....-','(': '-.--.', ')': '-.--.-'
                    }
# Dále definujeme první funkci - a to tedy funkci pro zakodovani textu díky prikazu def
def text_to_code():
# Jako první věc definujeme trext, ke kterému máme doplnit text pro kodovani
        text = input("Napište text, který hcete kodovat: ")
# Dále vytvoříme code, který nám říká, že text námi zadaný se automaticky převde na velké písmeno a to má ekvivalent i v morseove abecede a jejich znacich
        code = [SLOVNIK_MORSEOVKA[i.upper()] + " " for i in text if i.upper() in SLOVNIK_MORSEOVKA.keys()]
# Vytvoříme string k danemu code
        morseovka="".join(code)
# A string necháme přečíst
        print(morseovka)
                
# Stejný způsob použijeme i zde u dekodovani námi zadaného textu
def code_to_text():
        text = input("Napište kod, který chcete dekodovat: ")
# Vytvoříme zde to, že námi zadaný kod rozloží program na jednotlivé znaky morseovy abecedy a ty rozdělí a potom k těmto znakum přiřadi i písmena
        code = [k for i in text.split() for k,v in SLOVNIK_MORSEOVKA.items() if i==v]
        novytext = "".join(code)
# Opet nechame udělat string z code a necháme ho vypsat 
        print(novytext)


# Vypiseme menu pro vyber, co hceme aby program delal
print("""\n1 - TEXT KE KODOVÁNÍ \n2 - KÓD K ROZKÓDOVÁNÍ\n3 - KONEC\n""")

# Na zaver vypisime cyklus, ktery nám k menu ve stringu priradi i funkce
while True:
        try:
                vyber = int(input("TVŮJ VÝBĚR: "))
                if vyber == 1:
                        print(text_to_code())
                        break
                
                elif vyber == 2:
                        print (code_to_text())
                        break
                        
                elif vyber == 3:
                        print("UKONČUJI")
                        exit()
                     

# Zvolili jsme i fci else, která nám pokryje jakoukoliv jinou možnost než 1-3
                else:
                        print("NESPRÁVNÁ VOLBA, ZVOLTE ZNOVU")
        except:
                print("NESPRÁVNÁ VOLBA, ZVOLTE ZNOVU")

                
