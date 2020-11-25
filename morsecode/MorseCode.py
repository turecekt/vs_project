"""Welcome to 'MorseCode' module.

This module supplies function: encode().

For example:

>>> encode("ahoj")
'.-|....|---|.---'
"""
morseCodeDictionary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                       "e": ".", "f": "..-.", "g": "--.", "h": "....",
                       "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                       "m": "--", "n": "-.", "o": "---", "p": ".--.",
                       "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                       "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                       "y": "-.--", "z": "--.."}


def encode(text):
    """Returns encoded text in morse code of argument text.
    Function encode all ASCII alphabet characters.
    Letters are separated with '|' character.

    Args:
        - text - Some text for encoding

    Returns:
        - Encrypted string
    """

    morseCodetList = []
    for letter in text:
        morseCodetList.append(morseCodeDictionary.get(letter))

    return "|".join(morseCodetList)
