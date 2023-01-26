"""Hlavní modul."""
from functions import kodovani, dekodovani
'''Importujeme funkce z jiného kódu'''

if __name__ == '__main__':
    '''Podminka'''
    while (True):
        '''Pokud pravda pak:'''
        n1 = input("Chcete-li kódovat text do Morseovy abecedy, stiskněte k."
                   " Chcete-li dekódovat text v Morseově abecedě, "
                   "stiskněte d. Po zmáčknutí jiného "
                   "tlačítka bude program ukončen.")
        '''Dotaz programu a příjem odpovědi uživatele'''
        if n1 in ["k", "K"]:
            '''Odpověď uživatele - 1. možnost'''
            p1 = input("Zadejte text (bez diakritiky), který chcete zakódovat "
                       "do Morseovy abecedy. Kromě písmen je možné používat"
                       " pouze tečku, čárku a otazník.")
            '''Instrukce programu a příjem odpovědi uživatele'''
            result = kodovani(p1)
            '''Odpověď programu podle funkce v jiném kódu'''
            print(result)
            '''Vytisknutí odpovědi programu'''
        elif n1 in ['d', 'D']:
            '''Odpověď uživatele - 2. možnost'''
            p2 = input("Zadejte kod v Morseově abecedě za použití mezer,"
                       " teček a pomlček.")
            '''Instrukce programu a příjem odpovědi'''
            result = dekodovani(p2)
            '''Odpověď programu podle funkce v jiném kódu'''
            print(result)
            '''Vytisknutí odpovědi programu'''
        else:
        '''Odpověď uživatele - jiné než 1. nebo 2. možnost'''
            break
            '''Konec programu'''
