"""
Morseovka.

Tenhle kolekce nám umožňuje pracovat s písmeny,
číslicemi a několik unikátních znaků,
které pomocí funkcí lze kódovat a dekódovat.
Písmena v kolekci mají hodnotu key, znaky value.
"""
List = {
         'A': '.-',
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
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',
         '0': '-----',
         ', ': '--..--',
         '.': '.-.-.-',
         '?': '..--..',
         '/': '-..-.',
         '-': '-....-',
         '(': '-.--.',
         ')': '-.--.-'
         }


def Kodovat(text):
    """Funkce dekoduje textový řetezec do morseovky."""
    Ktext = ""
    for pismena in text:
        """Pokud není mezera"""
        if text != " ":
            Ktext = Ktext + List.get(pismena) + " "
            """Pokud mezera je"""
        else:
            Ktext += " "
    return Ktext
    print(Ktext)


def Dekodovat(text):
    """Funkce dekoduje morseovy text do textového řetezce."""
    text += " "
    """Proměnné je přiřazen klíč"""
    Klic = list(List.keys())
    """Proměnné je přiřazena hodnota"""
    Hodnota = list(List.values())
    m = ""
    """Výsledná proměnná"""
    Ntext = ""
    for pismena in text:
        if pismena != " ":
            m += pismena
            """Proměnná počítá mezery"""
            i = 0
        else:
            i += 1
            """Nové písmeno"""
            if i == 2:
                """Přidání mezery"""
                Ntext += " "
            else:
                Ntext = Ntext + Klic[Hodnota.index(m)]
                m = ""
    return Ntext
    print(Ntext)


def main():
    """"""
    Ktext = "Neandertalec"
    Detext = "-. . .- -. -.. . .-. - .- .-.. . -.-."
    """Proměnná výsledek překládá na velké písmena"""
    Vysledek = Kodovat(Ktext.upper())
    DVysledek = Dekodovat(Detext)
    print(Vysledek)
    print(DVysledek)


if __name__ == '__main__':
    main()


def test_Kodovat():
    """
    testováni převodu textového řetezce do morseovky.
    """
    assert Kodovat("FLAKE8") == "..-. .-.. .- -.- . ---.. "


def test_Dekodovat():
    """
    Testování převodu morseova kodu do textového řetezce.
    """
    assert Dekodovat("..-. .-.. .- -.- . ---..") == "FLAKE8"
