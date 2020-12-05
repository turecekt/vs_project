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

    soubor = open(nazev_souboru, encoding='utf-8')
    obsah = soubor.read()
    soubor.close()
    print("kolikátý je to znak: ",obsah.find("#"))
    ukoncovaciZnak = obsah.find("#")
    if ukoncovaciZnak == 0:
        obsah = ""
    elif ukoncovaciZnak < 0:
        obsah = obsah
    else:
        obsah = obsah[0:ukoncovaciZnak]

    return obsah

def test_nacti_text():
    assert (nazev_souboru) == 'Ahoj'  

def secti(a, b):
    return a + b

def test_secti():
    assert secti(1, 2) == 5
    

# print ("ukončovací znak: ",ukoncovaciZnak)
print("základní text: ",nacti_text(nazev_souboru))

def uprav_text(text):
    str = text.lower()
    str = str.replace(" ","")
    return str
print("upravený text: ",uprav_text(nacti_text(nazev_souboru)))

pripraveny_text = uprav_text(nacti_text(nazev_souboru))
count = {}
for x in pripraveny_text:
    if x in count.keys():
        count[x] +=1
        
    else:
        count[x] = 1

print(count)

for x in count.keys ():
    print("znak",x ,"se v textu vyskytuje: ",count[x])

print("Počet různých znaků: ",len(count))

MaxDictVal = max(count, key=count.get)
print("Nejčetnější znak:",MaxDictVal)

# MinDictVal = min(count, key=count.get)
# print("Nejméně četný znak:",MinDictVal)


# def nejmeneCetnyZnak(poctyZnaku):
#     MinDictVal = min(poctyZnaku, key=poctyZnaku.get)
#     return MinDictVal

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
