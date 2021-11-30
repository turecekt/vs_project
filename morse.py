DIR = {'A': '.-', 'B': '-...',
       'C': '-.-.', 'D': '-..', 'E': '.',
       'F': '..-.', 'G': '--.', 'H': '....',
       'I': '..', 'J': '.---', 'K': '-.-',
       'L': '.-..', 'M': '--', 'N': '-.',
       'O': '---', 'P': '.--.', 'Q': '--.-',
       'R': '.-.', 'S': '...', 'T': '-',
       'U': '..-', 'V': '...-', 'W': '.--',
       'X': '-..-', 'Y': '-.--', 'Z': '--..',
       '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
       '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def morseovka(cislo):

    morse = []
    for i in cislo:
        if i in DIR:
            morse.append(DIR[i])
    return " ".join(morse)


def main():
    vstup = input("Zadejte text: ")
    preklad = morseovka(vstup.upper())
    print(preklad)


if __name__ == "__main__":
    main()

