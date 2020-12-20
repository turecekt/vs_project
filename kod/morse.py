# Zadefinovanie funkcie prekladacu
def prekladac(text):

    # Syntax pre prelozenie klasickej abecedy do Morseovej
    code = {' ': '| ', 'A': '.- ', 'B': '-... ',
            'C': '-.-. ', 'D': '-.. ', 'E': '. ',
            'F': '..-. ', 'G': '--. ', 'H': '.... ',
            'I': '.. ', 'J': '.--- ', 'K': '-.- ',
            'L': '.-.. ', 'M': '-- ', 'N': '-. ',
            'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
            'R': '.-. ', 'S': '... ', 'T': '- ',
            'U': '..- ', 'V': '...- ', 'W': '.-- ',
            'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
            '1': '.---- ', '2': '..--- ', '3': '...-- ',
            '4': '....- ', '5': '..... ', '6': '-.... ',
            '7': '--... ', '8': '---.. ', '9': '----. ',
            '0': '----- ', ',': '--..-- ', '.': '.-.-.- ',
            '?': '..--.. ', '/': '-..-. ', '-': '-....- ',
            '(': '-.--. ', ')': '-.--.- '}
    morse_code = ""

    # Prekladanie individualnych charakterov klasickej
    # abecedy do Morseoveho
    # kodu pomocou vyssie zadefinovanej syntaxe
    # a konvertacia malych pismen na velke
    for x in text:
        morse_code += code[x.upper()]
    return morse_code


if __name__ == '__main__':
    # Vyzadovanie vstupu od uzivatela prekladacu
    text = input("Zadajte text ktory chcete prelozit do Morseovky: ")

    text2 = prekladac(text)
    # Volanie funkcie prekladacu
    print("Text prelozeny do Morseovky vyzera takto: ", text2)
