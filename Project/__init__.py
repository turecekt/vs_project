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
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1    
        res = max(charStore, key = charStore.get)
        print ("Znak s nejvetsim poctem je: " + str(res) )

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                print(data)
                if valid:
                    charStore = {}  
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    res = max(charStore, key = charStore.get)
                    print ("Znak s nejvetsim poctem je: " + str(res) )                 
                         
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")            
    
    
#MaxZnak(input("MaxZnak File nebo text zakonceny #: "))


#####################Informace o nejméně častém znaku#####################
def MinZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} 
        data = (vstup.replace(" ","")).upper()   
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1    
        res = min(charStore, key = charStore.get)
        print ("Znak s nejmensim poctem je: " + str(res))

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ","")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    charStore = {}  
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    #res = min(charStore, key = charStore.get)
                    res = min(charStore)
                    print (charStore.get) 
                    print(charStore)                               
                    print ("Znak s nejmensim poctem je: " + str(res))            
                else:
                    print("Vlozeny file nema ukonceni s #")
                             
    else:       
        print("Vlozeny text neni ukonceny #")            
    
    
MinZnak(input("MinZnak File nebo text zakonceny #: "))
    
 
 
    
    
    


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
