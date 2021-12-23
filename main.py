import pytest


# Objekt morseovka
class MorseovkaSeznam:
    dictionary = {'A': '.-', 'B': '-...',
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


# zapninani programu
def main():
    once = True
    morse(once)


def morse(once):
    decision = input(
        "Pro překlad do morseovy abecedy stiskni 1, Pro překlad z morseovy abecedy stiskni 2, pro ukončení stiskni 0:")  # preklad do morseovky  / z morseovky / ukonceni
    if decision == "0":
        print("Ukončování...")
    else:
        if decision == "1":  # preklad do morseovky
            text = input("Vlož text, který chceš přeložit do morseovy abecedy:")
            print(Preloz_do_m(text, MorseovkaSeznam.dictionary))
            input("Stiskni Enter pro pokračování")
            morse(once)
        elif decision == "2":  # preklad z morseovky
            text = input(
                "Vlož text, který chceš přeložit z morseovy abecedy, napiš / za každám písmenkem a // za každým slovem:")
            print(Preloz_z_m(text, MorseovkaSeznam.dictionary))
            input("Stiskni Enter pro pokračování")
            morse(once)
        else:  # spatny vstup
            print("Vložil jsi jiný znak než 1, 2 nebo 0")
            input("Stiskni Enter pro pokračování")
            morse(once)


# Funkce přeloží z morseovky
def Preloz_z_m(inputMessage, Morseovka):
    try:
        PrelozenaZprava = ''
        zprava = inputMessage.split('//')  # Do zpravy se uloží všechny slova
        counter = 1

        for word in zprava:
            Pismena = word.split('/')  # Do Písmena uloží všechny písmena
            for Pismeno in Pismena:
                if Pismeno != '':  # Pro každé písmeno se najde odpovídající skupina symbolů
                    PrelozenaZprava = PrelozenaZprava + list(Morseovka.keys())[list(Morseovka.values()).index(Pismeno)]
            if counter < len(zprava):  # Za každým slovem se udělá mezera mimo poslední
                PrelozenaZprava = PrelozenaZprava + ' '
            counter = counter + 1
        return PrelozenaZprava
    except Exception:  # Pokud se nenajde skprávná skupina znaků vypíše se chybová hláška
        print("Chybný vstup: " + Pismeno)
        return "Tento znak není definový v morseově abecedě"


# Funkce přeloží do morseovky
def Preloz_do_m(zprava, Morseovka):
    try:
        zprava = zprava.upper()
        counter = 1
        code = ''
        for Pismeno in zprava:
            if Pismeno != ' ':
                if counter < len(zprava):
                    #  Najde v seznamu kod pro odpovídajici znak
                    code = code + Morseovka[Pismeno] + '/'
                else:
                    code = code + Morseovka[Pismeno]
            else:
                # 1  je pro znaky, 2 je pro slova
                code += '/'
            counter = counter + 1

        return code

    except KeyError:
        print("Chybný vstup: " + Pismeno)
        return (
            # Při špatném vstupu se vypíše chybová hláška

            "Tento znak nezle využít, využij tyto znaky: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ")


if __name__ == '__main__':
    main()
