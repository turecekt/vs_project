"""
Program pro preklad textu na morseovku a naopak.

1. priklad - input:
"sos"
1. ocekavany output:
"...|---|..."

2. priklad - input:
"Wikipedia is a free online encyclopedia"
2. ocekavany output:
".--|..|-.-|..|.--.|.|-..|..|.-||..|...||.-||..-.|.-.|.|.||---|-.|.-..|..|-.|.||.|-.|-.-.|-.--|-.-.|.-..|---|.--.|.|-..|..|.-"

"""

table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

def get_letter_by_value(search_value):
    """
    Vyhleda ve slovniku table odpovidajici hodnotu.

    :parametr search_value: je hodnota, ktera se ma vyhledat ve slovniku table.
    :return: vraci odpovidajici klic (pismeno) ze slovniku, jinak None
    """
    for key, value in table.items():
        if value == search_value:
            return key
    return None


text = input("Zadejte text: ").lower()
valid = True

# pokud prvni index je znak abecedy
is_alphabet = True
try:
    list(table.keys()).index(text[0])
except ValueError:
    is_alphabet = False

