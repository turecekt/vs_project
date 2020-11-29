"""Modul obshaujici tridu translatoru Morseovi abecedy."""


class Translator:
    """Trida zverejnujici funkce pro kodovani/dekodovani Morseovi abecedy."""

    def __init__(self):
        """Konstruktor tridy.

        Definuje Morseovu abecedu.
        """
        self.abeceda = {'A': '.-',
                        'B': '-...',
                        'C': '-.-.',
                        'D': '-..',
                        'E': '-',
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
                        '9': '----.',
                        '.': '.-.-.-.',
                        ',': '--..--',
                        '?': '..--..',
                        '!': '--..-',
                        ';': '-.-.-.',
                        ':': '---...',
                        '(': '--...',
                        ')': '-.--.-',
                        ' ': '.-..-.',
                        '-': '-....-',
                        '_': '..--.-',
                        '@': '.--.-.'}

    def decodeChar(self, enc):
        """Metoda dekoduje znak z Morseovi abecedy do alfabeticke.

        Args:
            - enc - Zakodovany znak.

        Returns:
            - Dekodovany znak, pripadne ?, pokud se nepovede dekodovat.
        """
        for key, value in self.abeceda.items():
            if (value == enc):
                return str(key)
        return '?'

    def encodeChar(self, dec):
        """Metoda kodujici znak z alfabeticke abecedy do Morseovi.

        Args:
            - dec - Znak k zakodovani.

        Returns:
            - Zakodovany znak, pripadne zakodovany ?,
              pokud se nepovede zakodovat.
        """
        for key, value in self.abeceda.items():
            if (key == dec.upper()):
                return str(value)
        return '..--..'

    def encode(self, txt):
        """Metoda kodujici string z alfabeticke abecedy do Morseovi.

        Args:
            - txt - String k zakodovani.

        Returns:
            - Zakodovany string.
        """
        enc = ''
        for i in range(0, len(txt)):
            enc = enc + self.encodeChar(txt[i]) + ' '
        return enc

    def decode(self, txt):
        """Metoda dekodujici string z Morseovi abecedy do alfabeticke.

        Args:
            - txt - String k dekodovani.

        Returns:
            - Dekodovany string.
        """
        dec = ''
        w = ''
        for i in range(0, len(txt)):
            if (ord(txt[i]) == 32):
                dec = dec + self.decodeChar(w)
                w = ''
            else:
                w = w + txt[i]
        dec = dec + self.decodeChar(w)
        return dec
