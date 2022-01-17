"""Autori Petr Loukota a Natalie Vatterova."""


from cgi import test


text_do_mors = {'A': '.-',
                'B': '-...',
                'C': '-.-.',
                'D': '-..',
                'E': '.',
                'F': '..-.',
                'G': '--.',
                'H': '....',
                'I': '..',
                'J': '.---',
                'K': '-.-',
                'L': '.-..',
                'M': '--',
                'N': '-.',
                'O': '---',
                'P': '.--.',
                'Q': '--.-',
                'R': '.-.',
                'S': '...',
                'T': '-',
                'U': '..-',
                'V': '...-',
                'W': '.--',
                'X': '-..-',
                'Y': '-.--',
                'Z': '--..',
                '0': '-----',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.'}


"""Text."""
MORS_DO_TEXT = {}
for key, value in text_do_mors.items():
    MORS_DO_TEXT[value] = key


"""Text."""
def text_do_mors(zprava):
    mors = []
    for char in zprava:
        if char in text_do_mors:
            mors.append(text_do_mors[char])
    return " ".join(mors)


"""Text."""
def mors_do_text(zprava):
    zprava = zprava.split(" ")
    text = []
    for code in zprava:
        if code in MORS_DO_TEXT:
            text.append(MORS_DO_TEXT[code])
    return " ".join(text)


"""Text."""
def main():
    while True:
        response = input("Morseovku na text(1) Text na morseovku(2)?").upper()
        if response == "1" or response == "2":
            break

    if response == "1":
        print("Napiste morseovku (s mezerou mezi kazdym pismenem): ")
        mors = input("")
        text = mors_do_text(mors)
        print("Text prevedeny z morseovky je:  ")
        print(text)


    elif response == "2":
        print("Napište text: ")
        text = input("").upper()
        mors = text_do_mors(text)
        print(" Morseovka prevedena z textu je:  ")
        print(mors)


    return " ".join(text)


class TestMorseTranslator(test.TestCase):
    """Unit tests for all functions are here."""

    """Text."""
from Main import text_do_mors, mors_do_text, main


pole = "priklad"

"""Text."""
def test_main_chec_text_do_mors():
    text_do_mors(pole)


"""Text."""
def test_main_chec_mors_do_text():
    mors_do_text(pole)


"""Text."""
def test_mors_do_text1():
    mors1 = "... --- ..."
    assert mors_do_text
    ("S O S") == mors1


"""Text."""
def test_text_do_mors1():
    text1 = "S O S"
    assert text_do_mors
    ("... --- ...") == text1


"""Text."""
def test_main():
    response = "1"
    assert main
    ("Napiste morseovku (s mezerou mezi kazdym pismenem): ") == response


"""Text."""
def test_main2():
    response2 = "2"
    assert main
    ("Napište text: ") == response2


if __name__ == "__main__":
    test.main()