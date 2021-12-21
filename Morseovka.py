"""komentar1."""
Morseovka = {'A': '.-', 'B': '-...',
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
             '0': '-----', ', ': '--..--', '.': '.-.-.-',
             '?': '..--..', '/': '-..-.', '-': '-....-',
             '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ' '
    for pismeno in message:
        if pismeno != ' ':
            cipher += Morseovka[pismeno] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(message):
    message += ' '
    decipher = ' '
    citext = ' '
    for pismeno in message:
        if (pismeno != ' '):
            i = 0
            citext += pismeno

        else:
            i += 1
            if i == 2:
                decipher += ' '

            else:
                decipher += list(Morseovka.keys())
                [list(Morseovka.values()).index(citext)]
                citext = ' '
    return decipher


def main():
    message = "test"
    result = encrypt(message.upper())
    print(result)

    message = "- . ... -"
    result = decrypt(message)
    print(result)


if __name__ == '__main__':
    main()
