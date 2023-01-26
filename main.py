from functions import *


if __name__ == '__main__':
    while (True):
        n1 = input("Chcete-li kódovat text do Morseovy abecedy, stiskněte k."
                   " Chcete-li dekódovat text v Morseově abecedě, "
                   "stiskněte d. Po zmáčknutí jiného "
                   "tlačítka bude program ukončen.")
        # "k" or "d" or "n" or "K" or "K" or "N"
        if n1 in ["k", "K"]:
            p1 = input("Zadejte text (bez diakritiky), který chcete zakódovat "
                       "do Morseovy abecedy. Kromě písmen je možné používat"
                       " pouze tečku, čárku a otazník.")
            result = kodovani(p1)
            print(result)
        elif n1 in ['d', 'D']:
            p2 = input("Zadejte kod v Morseově abecedě za použití mezer,"
                       " teček a pomlček.")
            result = dekodovani(p2)
            print(result)
        else:
            break
