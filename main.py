"""Výpis morseovy abecedy."""

morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'}
"""
text -> promenna do ktere si ulozime
originalni text k prelozeni
cyklus for -> preklada pismeno ve zprave
podminka if    -> pokud pismeno ve zprave neni mezera
najdu si v poli morse_code
odpovidajici znak k pismenu a pridam mezeru
        else   -> pokud pismeno ve
        zprave je mezera pridam mezeru
"""


def zasifrovat(zprava):
    """Funkce zasifrovat -> slouzi k zasifrovani zpravy pomoci.
    
    morseovy abecedy funkce vraci zasifrovany text.
    """
    text = ''
    for pismeno in zprava:

        if pismeno != ' ':
            text += morse_code[pismeno] + ' '
        else:
            text += ' '
    return text
    
    
"""
zprava -> pridani mezery na konec zpravy k pristupu
poslednimu znaku morseovy abecedy
 ve zprave protoze index zacina na 0
prelozeny_text -> promenna
ve ktere je ulozeny finalni text z morseovy abecedy
i -> promenna
ktera nam kontroluje kolik je mezer ve zprave
podminka if     -> pokud ve zprave neni mezera
do promenne prelozit_text
pridam pismena z morseovy abecedy
         else   -> pokud ve zprave je mezera,
         pokud je i = 1 tak to znamena ze je ve zprave novy znak
         if     -> pokud i = 2 znamena to ze je ve
         zprave nove slovo a pridam do promenne prelozeny_text mezeru
"""


def odsifrovat(zprava):
    """Funkce odsifrovat -> slouzi k odsifrovani zpravy.

    pomoci morseovy abecedy funkce vraci odsifrovany text.
    """
    zprava += ' '

    prelozit_text = ''
    prelozeny_text = ''

    for pismeno in zprava:

        if (pismeno != ' '):
            i = 0

            prelozit_text += pismeno

        else:
            i += 1

            if i == 2:
                prelozeny_text += ' '

            else:

                prelozeny_text += list(morse_code.keys())[
                    list(morse_code.values()).index(prelozit_text)]
                prelozit_text = ''

    return prelozeny_text
    def testzasifrovat():
    """Unit test funkce zasifrovat."""
    zprava = "Ahoj svete"
    assert zasifrovat(zprava.upper()) == ".- .... --- .---  ... ...- . - . "