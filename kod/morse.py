"""Syntax pre prelozenie klasickej abecedy do Morseovej."""
code = {' ': '|', 'A': '.-', 'B': '-...',
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
        '0': '-----', ',': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'}

"""Zadefinovanie funkcie prekladacu do Morse Kodu."""


def encryptor(text):
    """Zadefinovanie premennej."""
    encrypted_text = ""

    """Prekladanie individualnych charakterov klasickej
    abecedy do Morseoveho
    kodu pomocou vyssie zadefinovanej syntaxe
    a konvertacia malych pismen na velke."""
    for x in text:
        encrypted_text += code[x.upper()] + ' '
    return encrypted_text


"""Zadefinovanie funkcie prekladacu z Morse Kodu."""


def decryptor(text):
    """Zadefinovanie premennej a ziskanie klucu a
    hodnoty zo slovniku."""
    text += " "
    key_list = list(code.keys())
    value_list = list(code.values())
    morse = ""
    normal = ""
    """Preklad individualnych Morseovych znakov
    do regularnej abecedy vratane podmienok pre
    oddelovanie."""
    for x in text:
        if x != " ":
            morse += x
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                normal += " "
            else:
                normal = normal + key_list[value_list.index(morse)]
                morse = ""
    """Vypis textu"""
    print("\nText prelozeny z Morseovky je:", normal)


"""Otvorenie dialogu, uzivatel pomocou klavesy 1 a 2
zvoli, ci chce prekladat z, alebo do Morseoveho kodu."""
if __name__ == '__main__':
    ch = input("\nAk chcete prekladat text do Morseovky, stlačte '1'."
               "\n\nAk chcete preložiť Morse Code stlačte '2'.\n")
    if ch == '1':
        text_to_encrypt = input("Zadajte text, ktorý chcete "
                                "preložiť do Morseovky: ")
        encryptor(text_to_encrypt)
        text2 = encryptor(text_to_encrypt)
        print("\nText prelozeny do Morseovky je:", text2)
    else:
        text_to_decrypt = input("Zadajte text, ktorý chcete "
                                "preložiť z Morseovky: ")
        decryptor(text_to_decrypt)
