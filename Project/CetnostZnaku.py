""" cetnost znaku project
by Radek Kratochvíl and Petr Slavík
"""

#####
#
#   • Textový soubor (obsahující text bez diakritiky) jako parametr programu
#
######
vstup = ".\TopicPicker.txt"

#def FileInput(vstup):
#    return open(vstup)



vstupFile = open("TopicPicker.txt","r")
 #####################Informace o celkovém počtu znaků#####################
data = vstupFile.read().replace(" ","")
num_of_char = len(data)
print('Number of characters in text file without spaces:',num_of_char)


#####################Informace o nejčastějším znaku#####################




 #####################Informace o nejméně častém znaku#####################


 #####################Informace o průměrné četnosti#####################
 
 
 
 
 
 
 
 
 #####################Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)#####################


#print(vstupFile.read())
#characters=0
#for line in vstupFile:
#    line = line.strip("\#")
#
#    words= line.split()
#    count_words += len(words)
#    count_char += len(line)
#
#    vstupFile.close()
#
#    print("nm_char:",count_char)
#


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



