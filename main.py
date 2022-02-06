def unique(pole_znaku):
    """
    Vrací pouze unikátní prvky pole.

    :param pole_znaku:
    """
    vystup = []
    for x in pole_znaku:
        if x not in vystup:
            vystup.append(x)
    return vystup


def celkovypocetznakuzadany(znaky):
    """
    Vrací celkový počet znaků ze zadaného textu \
    a zároveň naplňuje pole znaky, což jsou všechny zadané znaky.

    :param znaky:
    """
    while True:
        print("Zadejte text")
        slova = input()
        slova = slova.lower()
        if slova.isspace():
            continue
        else:
            break

    for znak in slova:
        if znak != " ":
            znaky.append(znak)
    return len(znaky)


def celkovypocetznakuzesouboru(znaky):
    """
      Vrací celkový počet znaků z textového souboru \
    a zároveň naplňuje pole znaky, což jsou všechny zadané znaky.

    :param znaky:
    """
    slova = open("Text.txt").read()
    slova = slova.lower()
    for znak in slova:
        if znak != " ":
            znaky.append(znak)
    return len(znaky)


def vyskytznaku(znaky):
    """
    Vrací pole čísel, které reprezenztuje \
    počet výskytů každého znaku z textu.

    :param znaky:
    """
    pocty_znaku = []
    for znak1 in znaky:
        nejcastejsi_znak = znak1
        kolikrat_se_znak_objevil = 0

        for znak2 in znaky:
            if nejcastejsi_znak == znak2:
                if znak2 == " ":
                    kolikrat_se_znak_objevil = 0
                else:
                    kolikrat_se_znak_objevil = kolikrat_se_znak_objevil + 1
        pocty_znaku.append(kolikrat_se_znak_objevil)
    return pocty_znaku


def nejcastejsiznak(znaky):
    """
    Vrací pole nejčastějších znaků v textu.

    :param znaky:
    """
    pocty_znaku = vyskytznaku(znaky)
    nejcastejsi_pocet = max(pocty_znaku)
    nejcastejsi_znaky = []
    for j in range(len(pocty_znaku)):
        if pocty_znaku[j] == nejcastejsi_pocet:
            nejcastejsi_znaky.append(znaky[j]+" ")
    nejcastejsi_znak = ""

    return nejcastejsi_znak.join(unique(nejcastejsi_znaky))


def nejmenecastyznak(znaky):
    """
    Vrací pole nejméně častých znaků z textu.

    :param znaky:
    """
    pocty_znaku = vyskytznaku(znaky)
    nejmene_casty_pocet = min(pocty_znaku)
    nejmene_caste_znaky = []
    for j in range(len(pocty_znaku)):
        if pocty_znaku[j] == nejmene_casty_pocet:
            nejmene_caste_znaky.append(znaky[j] + " ")
    nejmene_casty_znak = ""

    return nejmene_casty_znak.join(unique(nejmene_caste_znaky))


def prumernacetnostznaku(znaky):
    """
    Vrací průměrnou četnost z textu \
    (součet všech četností/součet všech znaků).

    :param znaky:
    """
    return sum(vyskytznaku(znaky)) / len(vyskytznaku(znaky))


def cetnostznakuabecedy(znaky):
    """
    Vrací pole abecedy. Ke každému písmenu v abecedě \
    je přiřazeno, kolikrát se vyskytuje v textu.

    :param znaky:
    """
    abeceda = ['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w',
               'x', 'y', 'z']
    pocet_znaku = [0] * len(abeceda)
    pole_abeceda_a_znaky = ["0"] * len(abeceda)

    for znak in znaky:
        for pismeno in abeceda:
            if znak == pismeno:
                pocet_znaku[abeceda.index(pismeno)] = \
                    pocet_znaku[abeceda.index(pismeno)] + 1
    for j in range(26):
        pole_abeceda_a_znaky[j] = str(abeceda[j]) + \
                                  " " + str(pocet_znaku[j]) + str(",")

    abeceda_a_znaky = " "
    return abeceda_a_znaky.join(pole_abeceda_a_znaky)


if __name__ == '__main__':
    vsechny_znaky = []

    while True:
        print("Chcete četnost z textového souboru nebo "
              "zadat text zde? text/zde ")
        volba = input()
        if volba == "text":
            print(celkovypocetznakuzesouboru(vsechny_znaky))
            break
        if volba == "zde":
            print(celkovypocetznakuzadany(vsechny_znaky))
            break
    print(nejcastejsiznak(vsechny_znaky))
    print(nejmenecastyznak(vsechny_znaky))
    print(round(prumernacetnostznaku(vsechny_znaky), 1))
    print(cetnostznakuabecedy(vsechny_znaky))
