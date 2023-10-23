"""Program Morseovka."""

"""Autoři: Richard Tomšů, Michal Jankůj."""


code_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
             "E": ".", "F": "..-.", "G": "--.", "H": "....",
             "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
             "M": "--", "N": "-.", "O": "---", "P": ".--.",
             "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
             "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
             "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---",
             "3": "...--", "4": "....-", "5": ".....",
             "6": "-....", "7": "--...", "8": "---..",
             "9": "----.", "0": "-----", "?": "..--..",
             ",": "--..--", ".": ".-.-.-", ";": "-.-.-.", "/": "-..-.",
             "=": "-...-", "-": "-....-", "'": ".----.",
             "(": "-.--.", ")": "-.--.-", ":": "---...",
             "_": "..--.-", "+": ".-.-.", "@": ".--.-.", " ": "/"}


def morse_code(line):
    """Funkce na kódováni morseovky.

    Jako vstupní parametr akceptuje string obsahující
    alfanumerické a bežné speciální znaky.
    Na výstupu funkce vrací string ve formě morseovy abecedy.
    """
    output = ""
    for letter in line:
        output += code_dict.get(letter, "") + " "
    return output[:-1]


def morse_decode(line):
    """Funkce na dekódovaní morseovky.

    Jako vstupní parametr akceptuje string obsahujíci
    znaky ".", "-", "/" a " ".
    Na výstupu funkce vrací string alfanumerických a
    běžných speciálních znaků.
    """
    output = ""
    for part in line.split():
        for key, value in code_dict.items():
            if value == part:
                output += key
    return output


if __name__ == '__main__':
    assert morse_code("KONTROLA") == "-.- --- -. - .-. --- .-.. .-"
    assert morse_code("KONTROLA KONTROLA") == \
           "-.- --- -. - .-. --- .-.. .- / -.- --- -. - .-. --- .-.. .-"
    assert morse_decode("-.- --- -. - .-. --- .-.. .-") == "KONTROLA"
    assert morse_decode("-.- --- -. - .-. --- .-.. .- "
                        "/ -.- --- -. - .-. --- .-.. .-") == \
           "KONTROLA KONTROLA"
