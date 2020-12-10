MORSE_CODE = {'A': '.-', 'B': '-...',
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


def zasifrovani(zprava):
    sifra = ''
    for pismeno in zprava:
        if pismeno != ' ':

            sifra += MORSE_CODE[pismeno] + ' '
        else:

            sifra += ' '

    return sifra


def rozsifrovani(zprava):
    zprava += ' '

    text = ''
    citext = ''
    for pismeno in zprava:

        if pismeno != ' ':

            i = 0

            citext += pismeno


        else:

            i += 1

            if i == 2:

                text += ' '
            else:

                text += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(citext)]
                citext = ''

    return text


def main():
    print("Vlož text (bez diakritiky):")
    zprava = input()
    # zprava = "sos"

    if zprava[0] in (".", "-"):
        result = rozsifrovani(zprava)
    else:
        zprava = zprava.upper()
        result = zasifrovani(zprava)

    # result = zasifrovani(zprava)
    print(result)


# print(result)

# zprava = "sos"
# result = zasifrovani(zprava.upper())
# print(result)

# zprava = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
# result = rozsifrovani(zprava)
# print(result)


if __name__ == '__main__':
    main()
