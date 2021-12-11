"""Kodovani a dekodovani z/do moseovky z/do textu."""

# Pridani slovniku
Morse_dictionary = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'ch': '----',
    'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-',
    'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/', '': ''
}


# Zalozeni funkci "encrypt" pro preklad z textu od morseovky
def encrypt(translate):
    """Prelozeni textu do
    morseovky."""
    # Do uvozovek se zadava text
    text = ''
    # Tento cyklus se obrati ke slovniku po kazdem stisknutim
    # tlacitek s pismeny a pak vypise zakodovany text
    for letter in translate:
        text += Morse_dictionary[letter] + ' '
    return text


def decrypt(translate):
    """Dekodovani morseovky do textu."""
    global n
    promena = ''
    translate += ' '
    word = ''

    # Zalozeni cyklu
    for letter in translate:

        # Pro rozlisovani slov ve vetach vytvorime cyklus
        if letter != ' ':
            # Globalni promena pro prepinani
            n = 0
            promena += letter

        # Jina podminka, jestli tam se objevi mezera
        else:
            # Ke globalni promene 'n' pripocitame 1 pro zvetseni
            n += 1
            # Pri n==2 se objevi slovo
            if n == 2:
                word += ' '
            else:
                # Ke vracene promene se pripocita key
                # pomoci prikazu 'values'
                # kde prikaz 'index' hleda
                # tecky a carky ve slovkinu
                word += list(Morse_dictionary.keys())[list(
                    Morse_dictionary.values()).index(promena)]
                promena = ''
    # Pak se vraci dekodovany text z morseovky
    return word


# Podminka pro spusteni programu


def main():
    """Vyber jedne z funkce programu a jeho spusteni.
    """
    choice = input("For Encrypt type '1' "
                   "\nFor Decrypt type '2': ")
    if choice == "1":
        translate = input("Add some text: ")
        result = encrypt(translate.lower())
        print(result)

    if choice == "2":
        print("Tip: Copy a code from the last word/sentence")
        translate = input("Add morse code: ")
        result = decrypt(translate)
        print(result)


if __name__ == '__main__':
    main()
