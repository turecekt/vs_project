import numpy as np


def celkovypocetznakuzadany(znaky):
    slova = input()
    for znak in slova:
        if znak != " ":
            znaky.append(znak)
    return len(znaky)


def celkovypocetznakuzesouboru(znaky):
    slova = open("Text.txt").read()
    for znak in slova:
        if znak != " ":
            znaky.append(znak)
    return len(znaky)


def vyskytznaku(znaky):
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
    pocty_znaku = vyskytznaku(znaky)
    nejcastejsi_pocet = max(pocty_znaku)
    nejcastejsi_znaky = []
    for j in range(len(pocty_znaku)):
        if pocty_znaku[j] == nejcastejsi_pocet:
            nejcastejsi_znaky.append(znaky[j]+" ")
    nejcastejsi_znak = ""

    return nejcastejsi_znak.join(np.unique(nejcastejsi_znaky))


def nejmenecastyznak(znaky):
    pocty_znaku = vyskytznaku(znaky)
    nejmene_casty_pocet = min(pocty_znaku)
    nejmene_caste_znaky = []
    for j in range(len(pocty_znaku)):
        if pocty_znaku[j] == nejmene_casty_pocet:
            nejmene_caste_znaky.append(znaky[j] + " ")
    nejmene_casty_znak = ""

    return nejmene_casty_znak.join(np.unique(nejmene_caste_znaky))


def prumernacetnostznaku(znaky):
    return sum(vyskytznaku(znaky)) / len(vyskytznaku(znaky))


def cetnostznakuabecedy(znaky):
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
    print("Chcete četnost z textového souboru nebo zadat text zde? text/zde ")
    while True:
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
