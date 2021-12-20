
"""
Program pro kodovani a dekodovani morseovy abecedy.
Vypracoval: Petr kraus

"""
# definice morseovy abecedy
morseDictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....',
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


def EncodeMorse(message):
    """Funkce pro zasifrovani do morseovky"""
    message.upper()                          # prevede vstup na velka pismena
    code = ''                                # string ktery bude funkci vracet
    for letter in message:
        if letter != ' ':
            code += morseDictionary[letter] + ' '
        else:
            code += ' '
    return code


def DecodeMorse(message):
    """Funkce pro desifrovani z morseovky"""
    message += ' '
    deCode = ''                              # string ktery bude funkci vracet
    tempText = ''                            # docasny string pro jeden znak
    for letter in message:
        if (letter != ' '):
            i = 0                            # zaznamenavani mezery
            tempText += letter
        else:
            i += 1
            if i == 2:
                deCode += ' '
            else:
                deCode += list(morseDictionary.keys())
                [list(morseDictionary.values()).index(tempText)]
                tempText = ''
    return deCode


def Input(message):
    """Funkce pro input morseovky"""
    for char in message:
        if char not in ".- ":
            return EncodeMorse(message)
    return DecodeMorse(message)


def TestEncode():
    """Test zakodovani."""
    assert EncodeMorse('HELLO') == '.... . .-.. .-.. --- '


def TestDecode():
    """Test dekodovani."""
    assert DecodeMorse('.... . .-.. .-.. --- ') == 'HELLO'


def TestInput():
    """Overeni ze funkce vola správnou funkci."""
    assert Input('univerzita') == '..- -. .. ...- . .-. --.. .. - .- '
    assert Input('- --- -- .- ...  -... .- - .-') == 'TOMAS BATA'


demoText = 'Hello world'
print('"' + demoText + '" \nse prelozi jako:\n"' + Input(demoText) + '"')
demoMorse = '.... --- .-- .- .-. . -.-- --- ..-'
print('"' + demoMorse + '" \nse prelozi jako:\n"' + Input(demoMorse) + '"')
