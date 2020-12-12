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