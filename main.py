
nazev_souboru = 'povidka.txt'


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
print("Celkový počet znaků (bez mezer): ", len(uprav_text(nacti_text(nazev_souboru))))  # noqa


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


print("Četnosti jednotlivých znaků: ", zjisti_cetnosti(nazev_souboru))


def pocet_ruznych_znaku(slovnik):
    """ Funkce vrátí počet různých znaků.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - pocty - počet znaků"""

    pocty = len(slovnik)
    return pocty


print("Počet různých znaků: ", pocet_ruznych_znaku(zjisti_cetnosti(nazev_souboru))) # noqa


def nejcetnejsi_znaky(slovnik):
    """ Funkce vrátí nejčetnější znak.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - MaxDictVal - nejčetnější znak (string)"""

    MaxDictVal = max(slovnik, key=slovnik.get)
    return MaxDictVal


print("Nejčetnější znak: ", nejcetnejsi_znaky(zjisti_cetnosti(nazev_souboru)))


def nejmenecetne_znaky(slovnik):
    """ Funkce vrátí nejméně četný znak.

        Args:
            - slovnik - četnosti (dictionary)

        Returns:
            - MinDictVal - nejméně četný znak (string)"""

    MinDictVal = min(slovnik, key=slovnik.get)
    return MinDictVal


print("Nejméně četný znak: ", nejmenecetne_znaky(zjisti_cetnosti(nazev_souboru)))   # noqa
