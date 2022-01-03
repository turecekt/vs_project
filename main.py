import pytest
import builtins


# Objekt morzeovka
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


# zapnutie programu
def main():
    once = True
    morse(once)


def morse(once):
    decision = input(
        "Pro překlad do morseovy abecedy stiskni 1, "
        "Pro překlad z morseovy abecedy stiskni 2, pro ukončení stiskni 0:")
    # preklad do morseovky  / z morseovky / ukonceni
    if decision == "0":
        print("Ukončování...")
    else:
        if decision == "1":  # preklad do morseovky
            text = input("Vlož text, který chceš přeložit do morseovy abecedy:")
            print(preloz_do_m(text, MorseovkaSeznam.dictionary))
            input("Stiskni Enter pro pokračování")
            morse(once)
        elif decision == "2":  # preklad z morseovky
            text = input(
                "Vlož text, který chceš přeložit z morseovy abecedy, "
                "napiš / za každám písmenkem a // za každým slovem:")
            print(preloz_z_m(text, MorseovkaSeznam.dictionary))
            input("Stiskni Enter pro pokračování")
            morse(once)
        else:  # spatny vstup
            print("Vložil jsi jiný znak než 1, 2 nebo 0")
            input("Stiskni Enter pro pokračování")
            morse(once)


# Funkcia preloží z morzeovky
def preloz_z_m(input_message, morseovka):
    try:
        prelozena_zprava = ''
        zprava = input_message.split('//')  # Do zpravy se uloží všechny slova
        counter = 1

        for word in zprava:
            pismena = word.split('/')  # Do Písmena uloží všechny písmena
            for pismeno in pismena:
                if pismeno != '':  # Pro každé písmeno se najde odpovídající skupina symbolů
                    prelozena_zprava = prelozena_zprava +\
                                       list(morseovka.keys())[list(morseovka.values()).index(pismeno)]
            if counter < len(zprava):  # Za každým slovem se udělá mezera mimo poslední
                prelozena_zprava = prelozena_zprava + ' '
            counter = counter + 1
        return prelozena_zprava
    except Exception:  # Pokud se nenajde skprávná skupina znaků vypíše se chybová hláška
        print("Chybný vstup: " + pismeno)
        return "Tento znak není definový v morseově abecedě"


# Funkcia preloží do morzeovky
def preloz_do_m(zprava, morseovka):
    try:
        zprava = zprava.upper()
        counter = 1
        code = ''
        for pismeno in zprava:
            if pismeno != ' ':
                if counter < len(zprava):
                    #  Najde v seznamu kod pro odpovídajici znak
                    code = code + morseovka[pismeno] + '/'
                else:
                    code = code + morseovka[pismeno]
            else:
                # 1  je pro znaky, 2 je pro slova
                code += '/'
            counter = counter + 1

        return code

    except KeyError:
        print("Chybný vstup: " + pismeno)
        return (
            # Při špatném vstupu se vypíše chybová hláška

            "Tento znak nezle využít, využij tyto znaky:"
            " A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - ")


if __name__ == '__main__':
    main()


def test_preloz_z_m():
    assert preloz_z_m(".-", MorseovkaSeznam.dictionary) == "A"


def test_preloz_do_m():
    assert preloz_do_m("A", MorseovkaSeznam.dictionary) == ".-"


def test_preloz_z_m_():
    assert preloz_z_m("$", MorseovkaSeznam.dictionary) == "Tento znak není definový v morseově abecedě"


def test_preloz_do_m_():
    assert preloz_do_m("%", MorseovkaSeznam.dictionary) == \
           "Tento znak nezle využít, využij tyto znaky:" \
           " A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 , . ? / - "


def test_morse():
    set_keyboard_input(["0"])
    morse(True)
    output = get_display_output()
    assert output == [
        "Pro překlad do morseovy abecedy stiskni 1, Pro překlad z morseovy abecedy stiskni 2, pro ukončení stiskni 0:",
        "Ukončování..."]


inner_values = []
print_values = []


def vstup(s):
    print_values.append(s)
    return inner_values.pop(0)


def start_vstupu_vystupu():
    global inner_values, print_values

    inner_values = []
    print_values = []

    builtins.input = vstup
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(vstupy):
    global inner_values

    start_vstupu_vystupu()
    inner_values = vstupy
