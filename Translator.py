class Translator:        

    def __init__(self):
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
        for key, value in self.abeceda.items():
            if (value == enc):
                return str(key)        
        return '?'

    def encodeChar(self, dec):
        for key, value in self.abeceda.items():
            if (key == dec.upper()):
                return str(value)
        return '..--..'
        
    def encode(self, txt):
        enc = ''
        for i in range(0, len(txt)):
            enc = enc + self.encodeChar(txt[i]) + ' '
        return enc        

    def decode(self, txt):        
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
