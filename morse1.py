# coding=utf-8

"""
Snad už to bude fungovat.

Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
"""

def encrypt(zprava):
    encrypt = {'A':'.-', 'B':'-...',
               'C':'-.-.', 'D':'-..',
               'E':'.', 'F':'..-.',
               'G':'--.',
               'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-',
               'L':'.-..', 'M':'--',
               'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...',
               'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--',
               'X':'-..-', 'Y':'-.--',
               'Z':'--..', ' ': ''}
    result = ''
    if '' in zprava:
        result = ' '.join(encrypt[i] for i in zprava.upper())
    return result

"""
Snad už to bude fungovat.

Dvě funkce. Jedna pro zakódování(encrypt), jedna pro překlad(decrypt).
"""

def decrypt(text):
    decrypt = {'.-':'A', '-...':'B',
               '-.-.':'C', '-..':'D',
               '.':'E', '..-.':'F',
               '--.':'G', '....':'H',
               '..':'I', '.---':'J',
               '-.-':'K', '.-..':'L',
               '--':'M', '-.':'N',
               '---':'O', '.--.':'P',
               '--.-':'Q', '.-.':'R',
               '...':'S', '-':'T',
               '..-':'U', '...-':'V',
               '.--':'W', '-..-':'X',
               '-.--':'Y', '--..':'Z'}
    result = ''
    if '-' or '.' in text:
        result = ''.join(decrypt[i] for i in text.split())
    return result
