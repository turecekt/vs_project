import sys


def main():
    input = []  # vytvori list input

    for x in sys.argv:  # nacte vsechny arumenty do listu input
        input.append(x)

    if len(input) == 1:  # tady se prida funkce na nahodne generovain cisel
        input = ''

    elif input[1] == "soubor-s-cisly.txt":  # funkce pro cteni ze souboru
        input = readfile()

    for y in input:  # docasne, vypise cisla
        print(y)


def readfile():  # funkce precte soubor a rozdeli skupiny znaku do listu
    file = open("soubor-s-cisly.txt", "r")  # otevre textovy soubor pro cteni
    text = file.read()  # ulozi obsah textoveho souboru do promenne
    output = []  # vytvoří list
    i = ''  # vytvoří promennou
    for j in text:  # projde kazdy znak ze souboru
        if j == ' ':
            output.append(i)  # prida vse z i do listu
            i = ''  # "vynuluje" i
        else:
            i = i + j  # prida aktualni znak k i
    if len(text) != 0:  # prida posledni cislo do listu
        output.append(i)

    return output


if __name__ == '__main__':  # umoznuje psani funkci pod main
    main()  # zavola main funkci
