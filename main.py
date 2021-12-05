"""Morse script."""
znaky = {
        """
        Definice pole morseovky.
        """
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----'
}

def encodovani(vstup):
    """
    Encodovani do morseovky
    Funkce bere parametr vstup, kterym je string 
    Funkce prochazi pole znak, zaroven transformuje vstup stringu na velka pismena.
    Pokud znak neni prazdny. Hleda funkce shodny znak morseovky v poli abecedy.
    Postupne tak sklada morseuv kod.
    Funkce vraci morseovku.
    """
    zprava = ''
    i = 0
    for znak in vstup.upper():
        if znak != ' ':
            zprava += znaky[znak]
            if len(vstup)-1 != i:
                zprava+= ' '
        i += 1
    return zprava


def decodovani(vstup):
    """
    Dekodovani z morseovky
    Funkce bere parametr vstup, kterym je string??...
    Funkce kontroluje, zda vstup neni prazdny
    Do promene pismeno vklada pomoci iterace kazdy prvek ze stringu/ pole vstupu
    Funkce prohledava pole znak a hleda shodu morseovky s abecednim predpisem v poli. Pokud se shoduji, vypise dany znak abecedy
    Funkce pasivne osetruje chyby v pripadnem prekladu.
    Funkce vraci desifrovanou zpravu.
    """
    try:
        vstup += " "
        desifrovanaZprava = ''
        pismeno = ''
        i = 0
        for letter in vstup:
            if (letter != ' '):
                i = 0
                pismeno += letter
            else:
                i += 1
                if i == 2:
                    desifrovanaZprava += ' '
                else:
                    desifrovanaZprava += list(znaky.keys())[list(znaky.values()).index(pismeno)]
                    pismeno = ''
        return desifrovanaZprava
    except ValueError:
        return "Chyba, Nelze přeložit!"

