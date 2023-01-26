'''Hlavní modul funkcí pro hlavní část kódu'''
PREVOD = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ',': '--..--',
        '.': '.-.-.-', '?': '..--..'}
'''Slovník písmen a jejich zápisu v morseově abecedě'''


def kodovani(p1):
    '''Funkce kodovani'''
    cipher = ""
    '''Příjem programu'''
    p1 = p1.upper()
    '''Zadefinování'''
    for letter in p1:
        '''Cyklus'''
        if letter != ' ':
            '''Pokud se nejedná o mezeru'''
            cipher += PREVOD[letter] + ' '
            '''Převeď dle slovníku'''
        else:
            '''Jinak'''
            cipher += ' '
            '''Kóduj jako mezeru'''
    return cipher.rstrip()
    '''Odpověď programu'''


def dekodovani(p2):
    '''Funkce dekodovani'''
    p2 = p2.upper() + ' '
    '''Zadefinování'''
    decipher = ''
    '''Program přijme zprávu uživatele'''
    citext = ''
    '''Program vytvoří překlad dle zprávy uživatele'''
    for letter in p2:
        '''Cyklus pro překlad písmena'''
        if (letter != ' '):
            '''Pokud se nejedná o mezeru'''
            i = 0
            '''Začátek cyklu'''
            citext += letter
            '''Přiřadíme písmeno'''
        else:
            '''Pokud se jedná o mezeru'''
            i += 1
            '''Cyklus pokračuje'''
            if i == 2:
                '''Pokud cyklus nic nenašel'''
                decipher += ' '
                '''Program přidá mezeru'''
            else:
                '''Pokud cyklus něco našel'''
                decipher += list(PREVOD.keys())[
                                    list(PREVOD.values()).index(citext)]
                '''Převádíme písmeno do morseovy abecedy'''
                citext = ''
                '''Překlad'''
    return decipher.rstrip()
    '''Odpověď programu'''
