"""################POTOM SMAZAT
PyUnit
Kód musí obsahovat unit testy (pokrytí kódu testy by se mělo blížit 100%)
Zdrojový kód musí projít kontrolním testem na githubu v sekci Actions (je nutné povolit). 
Tzn. musí projít všechny unit testy a flake8
Kód musí být okomentovaný (ideálně všechny entity)
"""


""" cetnost znaku project
by Radek Kratochvíl and Petr Slavík
"""

#####
#   Testovaci text vse hodit na UPPERCASE
testStr = "Testovaci text ktery je zakonceny #"
#
#   • Textový soubor (obsahující text bez diakritiky) jako parametr programu
#       vstup = ".\TopicPicker.txt"
#   nacist vstup 
#    pokud neni vstup tak vyzadat text od uzivatele zakonceny #
#def defVstup():
#    [1] vlozit cestu
#    [2] vlozit text
#   
######


#def FileInput(vstup):
#    return open(vstup)

 #####################Informace o celkovém počtu znaků#####################
def PocetZnak(vstup):
    vstupFile = open(vstup,"r")
    data = vstupFile.read().replace(" ","")
    pocet_char = len(data)
    print('Pocet znaku v celem txt souboru bez mezer :',pocet_char)

PocetZnak('.\TopicPicker.txt')

#####################Informace o nejčastějším znaku#####################

def MaxZnak():
    print ("The original string is : " + testStr)
    all_freqMax = {}
    for i in testStr:
        if i in all_freqMax:
         all_freqMax[i] += 1
        else:
            all_freqMax[i] = 1
    res = max(all_freqMax, key = all_freqMax.get)
    print ("The maximum of all characters in text is : " + str(res)) 

MaxZnak()



 #####################Informace o nejméně častém znaku#####################
def MinZnak():
    print ("The original string is : " + testStr)
    all_freqMin = {}
    for i in testStr:
        if i in all_freqMin:
         all_freqMin[i] += 1
        else:
            all_freqMin[i] = 1
    res = min(all_freqMin, key = all_freqMin.get)
    print ("The minimum of all characters in text is : " + str(res)) 
   
MinZnak()

#####################Informace o průměrné četnosti#####################
 
 
 
 
 #####################Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)#####################





#####Unit testy

#Neni zakonceno na #
#Neni soubor





#####
#
#   • V případě spuštění bez parametru musí program umět zpracovat text ze
#       standardního vstupu až po řádek obsahující ukončovací symbol #
######

#vstup = input('Write your paragraph,ends with #: ')
##asi bude foreach abeceda a pocet exception mezera zatim nevim asi tak neco
##asi na to bude nejaka vlastni pocitaci funkce kdyz to jde tak hezky pres .count(x)
#pocet = vstup.count('a')
#print(pocet)



