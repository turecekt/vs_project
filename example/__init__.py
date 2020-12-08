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
    """Funkce načítá znak ze souboru po znak "#". Soubor zavře.

    Args:
        - nazev_souboru - Soubor formátu .txt, který chceme načítst

    Returns:
        - obsah - Vrací string """

    soubor = open(nazev_souboru, encoding='utf-8')
    obsah = soubor.read()
    soubor.close()
    # print("kolikátý je to znak: ", obsah.find("#"))
    ukoncovaciZnak = obsah.find("#")
    if ukoncovaciZnak < 0:
        obsah = obsah
        return obsah
    elif ukoncovaciZnak > 0:
        obsah = obsah[0:ukoncovaciZnak]
        return obsah
    else:
        print("v souboru je ukončovací znak hned na začátku")


print("Text: ", nacti_text(nazev_souboru))


def uprav_text(text):
    """ Funkce převádí písmena na málá, odstraní mezery.

        Args:
            - text - Vstup je string, který chceme upravit

        Returns:
            - text - Vrací upravený string """

    str = text.lower()
    str = str.replace(" ", "")
    return str


# print("Upravený text: ", uprav_text(nacti_text(nazev_souboru)))
print("Celkový počet znaků (bez mezer): ", len(uprav_text(nacti_text(nazev_souboru))))


def zjisti_cetnosti(text):
    """ Funkce z textu zjistí četnosti jednotlivých znaků.

        Args:
            - text - String ve kterém zjišťujeme četnosti znaků

        Returns:
            - count - Vrací četnosti (dictionary)"""

    pripraveny_text = uprav_text(nacti_text(text))
    count = {}
    for x in pripraveny_text:
        if x in count.keys():
            count[x] += 1

        else:
            count[x] = 1
    return(count)


print(zjisti_cetnosti(nazev_souboru))


def pocet_ruznych_znaku(slovnik):
    """ Funkce vrátí počet různých znaků.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - pocty - počet znaků"""

    pocty = len(slovnik)
    return pocty


print("Počet různých znaků: ", pocet_ruznych_znaku(zjisti_cetnosti(nazev_souboru)))


def nejcetnejsi_znaky(slovnik):
    """ Funkce vrátí nejčetnější znak.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - MaxDictVal - nejčetnější znak (string)"""

    MaxDictVal = max(zjisti_cetnosti(nazev_souboru), key=zjisti_cetnosti(nazev_souboru).get)
    return MaxDictVal


print("Nejčetnější znak: ", nejcetnejsi_znaky(zjisti_cetnosti(nazev_souboru)))


def nejmenecetne_znaky(slovnik):
    """ Funkce vrátí nejméně četný znak.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - MinDictVal - nejméně četný znak (string)"""

    MinDictVal = min(zjisti_cetnosti(nazev_souboru), key=zjisti_cetnosti(nazev_souboru).get)
    return MinDictVal


print("Nejméně četný znak: ", nejmenecetne_znaky(zjisti_cetnosti(nazev_souboru)))


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
