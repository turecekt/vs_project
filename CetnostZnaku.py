""" cetnost znaku project """
"""Authors: Radek Kratochvíl and Petr Slavík"""

"""Informace o celkovém počtu znaků"""
def PocetZnak(vstup): 
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} 
        data = (vstup.replace(" ", "")).upper()
        pocet_char = len(data)-1 
        return(pocet_char)
        #print ("Celkovy pocet znaku bez mezer je: " + str(pocet_char) )  

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ", "")
                pocet_char = len(data)-1 #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    return(pocet_char)
                    #print ("Celkovy pocet znaku bez mezer je: " + str(pocet_char) )                 

                else:
                    return(0)
                    #print("Vlozeny file nema ukonceni s #")
                             
    else:
        return(0)       
        #print("Vlozeny text neni ukonceny #")            
    
    
#PocetZnak(input("PocetZnak File nebo text zakonceny #: "))



"""Informace o nejčastějším znaku"""
""" Funkce sebere na vstupu soubor/text a provede nad nim kontrolu jestli je zakonceny znakem #
 Pokud je vstup validni tak provede pocet o nejcastejsim znaku a 
 v pripade ze je pocet stejny pro vice charakteru vrati pole nejcastejsich znaku
"""
def MaxZnak(vstup): 
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} # dictionary pro ulozeni znaku
        data = (vstup.replace(" ", "")).upper()   
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1    
        resMax = max(charStore.values())
        res = [key for key in charStore if charStore[key] == resMax]
        return(res)
        #print ("Znaky s nejvetsim poctem jsou: " + str(res)) 

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ", "")
                valid = data.endswith(endis)
                if valid:
                    charStore = {}  
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    resMax = max(charStore.values())
                    res = [key for key in charStore if charStore[key] == resMax]
                    return(res)
                    #print ("Znaky s nejvetsim poctem jsou: " + str(res))                  
                         
                else:
                    return(0)
                    #print("Vlozeny file nema ukonceni s #")
                             
    else:
        return(0)       
        #print("Vlozeny text neni ukonceny #")            
    
    
#MaxZnak(input("MaxZnak File nebo text zakonceny #: "))


"""Informace o nejméně častém znaku"""
def MinZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        charStore = {} 
        data = (vstup.replace(" ", "")).upper()   
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1    
        resMin = min(charStore.values())
        res = [key for key in charStore if charStore[key] == resMin]
        return(res)
        #print ("Znaky s nejmensim poctem jsou: " + str(res)) 

    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ", "")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    charStore = {}  
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    resMin = min(charStore.values())
                    res = [key for key in charStore if charStore[key] == resMin]
                    return(res)            
                else:
                    return(0)
                    #print("Vlozeny file nema ukonceni s #")
                             
    else:       
        return(0)
        #print("Vlozeny text neni ukonceny #")
    
    
#MinZnak(input("MinZnak File nebo text zakonceny #: "))
  

"""Informace o průměrné četnosti"""
def PrumerKazdyZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ", "")).upper()
        pocet_char = len(data)   
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for iChar in alpha:
            pocet = data.count(iChar)/pocet_char*100
            if data.count(iChar) > 0:
                print(iChar, "vyskyt je",f"{pocet:.2f}", "%")
    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ", "")
                pocet_char = len(data) #musime vynechat # a veskere nestandartni znaky
                valid = data.endswith(endis)
                if valid:
                    charStore = {} 
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    return(charStore)


                    print("if valid",data)
                    print(data)
                    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    for iChar in alpha:
                        pocet = data.count(iChar)/pocet_char*100
                        if data.count(iChar) > 0:
                            print(iChar, "vyskyt je",f"{pocet:.2f}", "%")
                else:
                    return(0)
                    #print("Vlozeny file nema ukonceni s #")
                             
    else:
        return(0)       
        print("Vlozeny text neni ukonceny #")

#PrumerKazdyZnak(input("File nebo text zakonceny #: "))


"""Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)"""
def PocetKazdyZnak(vstup):
    endis = "#"
    if vstup.endswith(endis):
        data = (vstup.replace(" ", "")).upper()   
        charStore = {}
        for sChar in data:
            if sChar in charStore:
                charStore[sChar] += 1
            else:
                charStore[sChar] = 1    
        return(charStore)
        #print(charStore)
    elif vstup.endswith('.txt'): #za predpokladu ze je vstup file input .txt
        with open(vstup) as text_file:
                data = text_file.read().upper().replace(" ", "")
                valid = data.endswith(endis)
                if valid:
                    charStore = {} 
                    for sChar in data:
                        if sChar in charStore:
                            charStore[sChar] += 1
                        else:
                            charStore[sChar] = 1    
                    return(charStore)
                else:
                    return(0)
                    #print("Vlozeny file nema ukonceni s #")
                             
    else:
        return(0)       
        #print("Vlozeny text neni ukonceny #")

#PocetKazdyZnak(input("PocetKazdyZnak File nebo text zakonceny #: "))