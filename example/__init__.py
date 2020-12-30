"""Projekt MORSEOVKA - Radim Žaluda

Zadani:

Vytvořte program, který umí kódovat i dekódovat Morseovu abecedu.
VSTUP
• Textový řetězec
• Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu.
VÝSTUP
• Zakódovaná, případně dekódovaná morseovka

"""
MORSEOVKA = {                           #prevodni slovnik (dictionary)
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
}
import sys                                              #import sys modulu
def prevodDoMorseovky(vstup):                           #Deklarace funkce prevodDoMorseovky s parametrem vstup
    vystup = ""                                         #nastaveni prommene na prazdny retezec
    for znak in vstup:                                  #for cyklus pro prochazeni jednotlivych znaku zadaneho vstupniho rezetezce
            vystup = vystup + MORSEOVKA[znak] + "/"     #nacitani znaku do promenne vystup s pripojenim lomitka (pro lepsi citelnost morseovy abecedy na konzoli)
    print(vystup)                                       #zobrazeni zadaneho textoveho retezce v morseove abecede

def prevodZMorseovky(vstup):                            #deklarace funkce prevodZMorseovky s parametrem vstup
        vstup += ' '                                    #pridani mezery na konec vstupniho retezce(Morseovy abecedy)
        vystup = ''                                     #nastaveni prommene na prazdny retezec
        pomocna = ''                                    #nastaveni prommene na prazdny retezec
        for znak in vstup:                              #for cyklus pro prochazeni jednotlivych znaku vstupního retezce(Morseovy abecedy)
            if (znak != ' '):
                i = 0
                pomocna += znak                         #ulozeni nalazeneho znaku abecedy do pomocne promenne
            else:
                i += 1                                  #inkrementace i o +1
                if i == 2:                              #pokud se nachazeji dve po sobe jdouci mezery...
                    vystup += ' '                       #...pridame do promenne na konec dalsi
                else:
                    vystup += list(MORSEOVKA.keys())[list(MORSEOVKA.values()).index(pomocna)] #pomoci seznamu (znaky postupne nactene) a ulozeni prevedeneho textu z Morseovy abecedy do promenne vystup
                    pomocna = ''                        #vynulovani pomocne promenne
        print(vystup)


volba = input("Zmáčkni klávesu 1 pro zakódování do Morseovy abecedy nebo zmáčkni klávesu 2 pro dekódování z Morseovy abecedy:  ")
if volba == '1':                                                                #podminkou if - elif (stisknutim klavesy 1 nebo 2) se uzivatele zeptame, zda-li chce text zakodovat nebo dekodovat
    vstup = input( "Zadej text pro převod do Morseovy abecedy: ").upper()       #nacteni vstupu od uzivatele z klavesnice a ulozeni do promenne vstup + pouziti metody upper pro převod na velka pismena(kvuli prevodni tabulce)
    prevodDoMorseovky(vstup)

elif volba == '2':                                                              #podminkou if - elif (stisknutim klavesy 1 nebo 2) se uzivatele zeptame, zda-li chce text zakodovat nebo dekodovat
    vstup = input("Zadej znaky morseovy abecedy pro převod : ")                 #nacteni vstupu od uzivatele z klavesnice a ulozeni do promenne vstup
    prevodZMorseovky(vstup)

else:
    sys.exit("nezvolil jsi správnou klávesu (1 nebo 2), program končí")         #Pokud uzivatel nestikne 1 nebo 2 informuje jej o tom a ukonci program pomoci sys.exit metody




