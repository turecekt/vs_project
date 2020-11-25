"""Welcome to 'MorseCode' module.

This module encode all ASCII alphabet characters,
where letters are separated with '|' character.
Module also supplies function: encode().

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
    """Returns encoding string.

    Args:
        - text - Some text for encoding

    Returns:
        - encoded string
    """
    morseCodetList = []
    for letter in text:
        morseCodetList.append(morseCodeDictionary.get(letter))

    return "|".join(morseCodetList)
