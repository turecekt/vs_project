"""
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
    """
    Funkce přiřazuje z kolekce písmen danné znaky.
    Do funkce je vložena podmínka v případě, kdy v textu bude
    mezera.
    """
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
    """Funkce přiřazuje hodnoty z kolekce do písmen"""
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
    """Do proměnné Ktext vložíme text, který chceme kódovat,
     do proměnné Detext vložíme znaky Morseovy abecedy,
    zavoláním funkcí, program vypíše výsledky."""
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
    Prvni test kontroluje, zda opravdu funkce Kodovat převádí
    textovy řetězec do šifrovaného textu.
    """

    assert Kodovat("FLAKE8") == "Kontrola"



def test_Dekodovat():

    """
    Druhá test kontroluje, zda funkce Dekodovat převádí
    šifrovaný text do textového řetězce.
    """

    assert Dekodovat("..-. .-.. .- -.- . ---..") == "FLAKE8"
