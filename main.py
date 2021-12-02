
morse_dict = {
    'A':'.-',   'B':'-...',
    'C':'-.-.', 'D':'-..',  'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..',   'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---',  'P':'.--.', 'Q':'--.-',
    'R':'.-.',  'S':'...', 'T':'-',
    'U':'..-',  'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',

    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'
}

def code(text):
    """ Funkce na přepsání písmen a čísel do morseovky. """
    text = text.upper()
    ret = ""

    for letter in text:
        if letter in morse_dict:
            ret += morse_dict[letter] + " "
        else:
            ret += "| "
    return  ret.strip()

def decode(text):
    """ Funcke na přepsání morseovky na písmena a čísla. """
    ret = ""

    letters = text.split(" ")
    for l in letters:
        if l == "|":
            ret += " "
        elif l in morse_dict.values():
            ret += get_key(l)
        else:
            return "Error"

    return ret.strip()

def get_key(val):
    """Překlad textu jendnoho písmene"""
    for key, value in morse_dict.items():
        if val == value:
            return key
    return ""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """Hlavní funkce main"""
    print("Zvolte akci: ")
    choice = float(input("1 - Převod do Morseovky \n2 - Převod z Morseovky\n"))
    mess = str(input("Zadejte text k převodu: "))


    if choice == 1:
        print(f'Původni text: {mess} \nPřeložený text: {code(mess)}')
    elif choice == 2:
        if decode(mess) == "Error":
            print('Původní text není správně zakódován')
        else:
            print(f'Původni text: {mess} \nPřeložený text: {decode(mess)}')
    print('\nKonec Programu')



