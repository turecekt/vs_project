PREVOD = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ',': '--..--',
        '.': '.-.-.-', '?': '..--..'}  # knihovna


def kodovani(p1):  # funkce kodování
    cipher = ""
    p1 = p1.upper()
    for letter in p1:
        if letter != ' ':
            cipher += PREVOD[letter] + ' '
        else:
            cipher += ' '
    return cipher.rstrip()


def dekodovani(p2):  # funkce dekodovani
    p2 = p2.upper() + ' '
    decipher = ''
    citext = ''
    for letter in p2:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(PREVOD.keys())[
                                    list(PREVOD.values()).index(citext)]
                citext = ''
    return decipher.rstrip()
