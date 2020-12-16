class MorseCode:

    MORSE_CODE_LIST = {
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "l": ".-..",
            "k": "-.-",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
            " ": "...---...",
    }


    def encode(self, text):
        ret = ""
        words = self.get_words(text)
        for word in words:
            for letter in word:
                if letter.lower() in self.MORSE_CODE_LIST:
                    ret += self.MORSE_CODE_LIST[letter.lower()]
                    ret += " "
            ret += "...---... "
        ret.strip()
        return ret

    def decode(self, text):
        ret = ""
        words = self.get_words(text)
        for word in words:
            for i, x in self.MORSE_CODE_LIST.items():
                        if word == x:
                            ret += i
        ret += " "
        ret.strip()
        return ret

    def get_words(self, text):
        return text.split(" ")


if __name__ == '__main__':
    morseCode = MorseCode()
    print("Volby:\nKódovat: 1\nDekódovat: 2")
    opt = input()
    if opt == "1":
        print("Zadejte text pro zakódování")
        print(morseCode.encode(input()))
    else:
        print("Zadejte text pro dekódování")
        print(morseCode.decode(input()))
    



