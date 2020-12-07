"""This is the "example" module.

The example module supplies one function, compute().  For example,

>>> compute(3)
3
"""


def compute(x):
    """Functon compute returns evaluation of expression using argument x.

    Args:
        - x - Input of the function

    Returns:
        - output - Output of the function
    """
    return x * x - 2 * x

nazev_souboru = 'basnicka.txt'

def nacti_text(nazev_souboru):
    """Funkce načte text ze souboru. Pokud je přítomen znak "#", načte text jen po tento znak. Soubor zavře.

    Args:
        - nazev_souboru - Soubor formátu .txt, který chceme načítst

    Returns:
        - obsah - Vrací string """
    
    soubor = open(nazev_souboru, encoding='utf-8')
    obsah = soubor.read()
    soubor.close()
    print("kolikátý je to znak: ",obsah.find("#"))
    ukoncovaciZnak = obsah.find("#")
    if ukoncovaciZnak < 0:
        obsah = obsah
        return obsah
    elif ukoncovaciZnak > 0:
        obsah = obsah[0:ukoncovaciZnak]
        return obsah
    else: 
        print ("v souboru je ukončovací znak hned na začátku")


print("základní text: ",nacti_text(nazev_souboru))

def uprav_text(text):
    """ Funkce upravuje text: převede všechna písmena na málá a odstraní mezery mezi slovy.

        Args:
            - text - Vstup je string, který chceme upravit
        
        Returns
            - text - Vrací upravený string """

    str = text.lower()
    str = str.replace(" ","")
    return str

print("upravený text: ",uprav_text(nacti_text(nazev_souboru)))


def zjisti_cetnosti (text):
    pripraveny_text = uprav_text(nacti_text(text))
    count = {}
    for x in pripraveny_text:
        if x in count.keys():
            count[x] +=1
            
        else:
            count[x] = 1    
    return(count)

print(zjisti_cetnosti(nazev_souboru))

# for x in count.keys ():
#     print("znak",x ,"se v textu vyskytuje: ",count[x])


def pocet_ruznych_znaku(slovnik):
    pocty = len(slovnik)
    return pocty

print ("z metody počet různých znaků: ",pocet_ruznych_znaku(zjisti_cetnosti(nazev_souboru)))
    
def nejcetnejsi_znaky(slovnik):
    MaxDictVal = max(zjisti_cetnosti(nazev_souboru), key=zjisti_cetnosti(nazev_souboru).get)
    return MaxDictVal
print("Nejčetnější znaky z metody: ", nejcetnejsi_znaky(zjisti_cetnosti(nazev_souboru)))

def nejmenecetne_znaky(slovnik):
    MinDictVal = min(zjisti_cetnosti(nazev_souboru), key=zjisti_cetnosti(nazev_souboru).get)
    return MinDictVal
print("Nejméně četné znaky z metody: ", nejmenecetne_znaky(zjisti_cetnosti(nazev_souboru)))

# MaxDictVal = max(count, key=count.get)
# print("Nejčetnější znak:",MaxDictVal)

# MinDictVal = min(count, key=count.get)
# print("Nejméně četný znak:",MinDictVal)




# def kolikZnakuJeVtextu(obsah,nejmeneCetnyZnak):
#     return obsah.count(nejmeneCetnyZnak(poctyZnaku)
                       

    
# print("Nejméně četný znak FUNKCE:",nejmeneCetnyZnak(count))

#  for x in count.keys ():
#     if count[x] == 2:
#         print("jen písmena",x)
#     else:
#         print("nefunguje") 



# Ještě pořešit:
#     - jak vypsat všechny nejméně četné znaky
#         ještě získat hodnotu nejméně četného znaku a potom vypsat
#         jen ty nejméně četné
#     - když text nebude obsahovat #, tak neodečítat -1    --- hotovo
#     - průměrná četnost

# VSTUP
# • Textový soubor (obsahující text bez diakritiky) jako parametr programu
# • V případě spuštění bez parametru musí program umět zpracovat text ze
# standardního vstupu až po řádek obsahující ukončovací symbol #
# VÝSTUP
# • Informace o celkovém počtu znaků
# • Informace o nejčastějším znaku
# • Informace o nejméně častém znaku
# • Informace o průměrné četnosti
# • Informace o četnosti jednotlivých znaků abecedy (bez diakritiky)
