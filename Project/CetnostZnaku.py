"""################POTOM SMAZAT
PyUnit
Kód musí obsahovat unit testy (pokrytí kódu testy by se mělo blížit 100%)
#Zdrojový kód musí projít kontrolním testem na githubu v sekci Actions (je nutné povolit). 
#Tzn. musí projít všechny unit testy a flake8
#Kód musí být okomentovaný (ideálně všechny entity)
#"""
#
#python -m venv c:\path\to\myenv
#""" cetnost znaku project
#by Radek Kratochvíl and Petr Slavík

#######################Informace o nejčastějším znaku#####################

def MaxZnak(vstup): 
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} 
        data = (vstup.replace(" ","")).upper()   
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for iChar in alpha:
            for sChar in vstup:
                if iChar == sChar:
                    charStore[sChar] += 1
                else:
                    charStore[sChar] = 1    
        res = max(charStore, key = charStore.get)
        print ("Znak s nejmensim poctem je: " + str(res))

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    charStore = {}   
                    print(charStore)                  
                    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    for iChar in alpha:
                        for sChar in vstup:
                            if iChar == sChar:
                                charStore[sChar] += 1
                            else:
                                charStore[sChar] = 1
                    res = max(charStore, key = charStore.get) 
                    print ("Znak s nejvetsim poctem je: " + str(res))            
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")            
    
    
#MaxZnak(input("File nebo text zakonceny #: "))


#def MaxZnak():
#    print ("The original string is : " + testStr)
#    all_freqMax = {}
#    for i in testStr:
#        if i in all_freqMax:
#         all_freqMax[i] += 1
#        else:
#            all_freqMax[i] = 1
#    res = max(all_freqMax, key = all_freqMax.get)
#    res = res.upper
#    print ("Znak s nejvetsim poctem je: " + str(res)) 
#
 #####################Informace o nejméně častém znaku#####################
def MinZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} 
        data = (vstup.replace(" ","")).upper()  
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for iChar in alpha:
            for sChar in data:
                if iChar == sChar:
                    charStore[iChar] += 1
                else:
                    charStore[iChar] = 1    
        res = min(charStore, key = charStore.get)
        print ("Znak s nejmensim poctem je: " + str(res))

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    charStore = {}                     
                    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    for iChar in alpha:
                        for sChar in data:
                            if iChar == sChar:
                                charStore[iChar] += 1
                                print(charStore)
                            else:
                                charStore[iChar] = 1
                    res = min(charStore, key = charStore.get) 
                    print ("Znak s nejmensim poctem je: " + str(res))            
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")            
    
    
MinZnak(input("File nebo text zakonceny #: "))
    
    
    
    
    
    
    
    #for characters in testStr.upper():
    #    print(charStore)
    #    if characters in charStore:
    #        charStore[characters] += 1
    #    else:
    #        charStore[characters] = 1
#
    #res = min(charStore, key = charStore.get)
    #print ("Znak s nejmensim poctem je: " + str(res)) 
   
#MinZnak("Je tu jen jedno A#")

#pridat vystup pole znaku kdyz nejmensi maji stejne





#
######################Informace o průměrné četnosti#####################
def PrumerKazdyZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ","")).upper()
        pocet_char = len(data)   
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for iChar in alpha:
            pocet = data.count(iChar)/pocet_char*100
            if data.count(iChar) > 0:
                print(iChar, "vyskyt je",f"{pocet:.2f}", "%")
    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    print("if valid",data)
                    print(data)
                    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    for iChar in alpha:
                        pocet = data.count(iChar)/pocet_char*100
                        if data.count(iChar) > 0:
                            print(iChar, "vyskyt je",f"{pocet:.2f}", "%")
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")

#PrumerKazdyZnak(input("File nebo text zakonceny #: "))


# #####################Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)#####################

def PocetKazdyZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ","")).upper()   
        alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for iChar in alpha:
            pocet = data.count(iChar)
            if data.count(iChar) > 0:
                print(iChar, "je",pocet)
    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                valid = data.endswith(endis)
                if valid:
                    print("if valid",data)
                    print(data)
                    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    for iChar in alpha:
                        pocet = data.count(iChar)
                        if data.count(iChar) > 0:
                            print(iChar, "je",pocet)
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")

#PocetKazdyZnak(input("File nebo text zakonceny #: "))
       
# 2 testy a to je jsou to neobyc znaky a nebo cislice a nebo odradkovani tak to bude test fail
#
#jen pro ukazku jestli funguje import CetnostZnaku.py
def secti(a,b):
    return a+b
