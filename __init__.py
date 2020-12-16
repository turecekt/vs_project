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
        " ": " ",
}

inp = ""

def encode(text):
    ret = ""
    words = get_words(text)
    for word in words:
        for letter in word:
            if letter.lower() in MORSE_CODE_LIST:
                ret += MORSE_CODE_LIST[letter.lower()]
                ret += " "
    return ret

def decode(text):
    ret = ""
    words = get_words(text)
    for word in words:
           for i, x in MORSE_CODE_LIST.items():
                    if word == x:
                        ret += i
                        ret += " "
    return ret

def get_words(text):
    return text.split(" ")


print("Volby:\nKódovat: 1\nDekódovat: 2")
opt = input()
if opt == "1":
    print("Zadejte text pro zakódování")
    inp = input()
    print(encode(inp))
else:
    print("Zadejte text pro dekódování")
    inp = input()
    print(decode(inp))
    



