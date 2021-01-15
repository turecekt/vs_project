# coding=utf-8

"""
Hlavní program.

Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
"""


def encrypt(zprava):
    """Vytvoření slovníku a funkce pro zakódování zprávy."""
    encrypt = {'A': '.-', 'B': '-...',
               'C': '-.-.', 'D': '-..',
               'E': '.', 'F': '..-.',
               'G': '--.',
               'H': '....', 'I': '..',
               'J': '.---', 'K': '-.-',
               'L': '.-..', 'M': '--',
               'N': '-.', 'O': '---',
               'P': '.--.', 'Q': '--.-',
               'R': '.-.', 'S': '...',
               'T': '-', 'U': '..-',
               'V': '...-', 'W': '.--',
               'X': '-..-', 'Y': '-.--',
               'Z': '--..', ' ': ''}
    result = ''
    if '' in zprava:
        result = ' '.join(encrypt[i] for i in zprava.upper())
    return result


def decrypt(text):
    """Vytvoření slovníku pro překlad z morseova kódu a funkce pro překlad."""
    decrypt = {'.-': 'A', '-...': 'B',
               '-.-.': 'C', '-..': 'D',
               '.': 'E', '..-.': 'F',
               '--.': 'G', '....': 'H',
               '..': 'I', '.---': 'J',
               '-.-': 'K', '.-..': 'L',
               '--': 'M', '-.': 'N',
               '---': 'O', '.--.': 'P',
               '--.-': 'Q', '.-.': 'R',
               '...': 'S', '-': 'T',
               '..-': 'U', '...-': 'V',
               '.--': 'W', '-..-': 'X',
               '-.--': 'Y', '--..': 'Z'}
    result = ''
    if '-' or '.' in text:
        result = ''.join(decrypt[i] for i in text.split())
    return result

def main():
    """Výběr ze dvou možností."""
    moznost = input("Zakodovat(1) Preloz(2)")
    if moznost == "1":
        preloz = input("")
        result = encrypt(preloz.lower())
        print(result)
        input("")

    if moznost == "2":
        preloz = input(" ")
        result = decrypt(preloz)
        print(result.capitalize())
        input("")


if __name__ == '__main__':
    main()
