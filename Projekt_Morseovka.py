translator = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'CH': '----', 'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
              'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.',
              ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
              '?': '..--..', '!': '--...-', '-': '-....-', '/': '-..-.',
              '=': '-...-', '_': '..--.-', '(': '-.--.', ')': '-.--.-',
              '@': '.--.-.', '"': '.-..-.', ' ': ''}


def remove_diacritics(text: str) -> str:
    """Remove diacritics from text.

    Return uppercase text without diacritics
    """
    text = text.upper()
    diacritics = 'ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ'
    without = 'ACDEEINORSTUUYZ'
    for i in range(len(text)):
        if text[i] in diacritics:
            text = text.replace(text[i], without[diacritics.index(text[i])])
    return text


def alphabet_to_morse(text: str) -> str:
    """Translate text to morse code.

    Return text translated to morse code
    """
    result = ''
    text = remove_diacritics(text)
    index = 0
    while index < len(text):
        char = text[index]

        if index < len(text) - 1:
            if text[index: index + 2] == 'CH':
                char = 'CH'
                index += 1

        result += translator[char] + '|'
        index += 1

    return result


def get_key(letter: str, dictionary: dict) -> str:
    """Get key from dictionary.

    Return key from dictionary by value.
    """
    for key, value in dictionary.items():
        if letter == value:
            return key


def morse_to_alphabet(text: str) -> str:
    """Translate text from morse code.

    Return text translated from morse code.
    """
    text = text.split('||')
    code = []
    for word in text:
        code += [word.split('|')]

    result = ''
    for word in code:
        for letter in word:
            result += get_key(letter, translator)
        result += ' '
    return result.lower().capitalize()


def test_remove_diacritics() -> None:
    """Test remove_diacritics function.
    """
    assert (remove_diacritics('áčďéěíňóřšťúůýž') == 'ACDEEINORSTUUYZ')
    assert (remove_diacritics('Příliš žluťoučký kůň úpěl ďábelské ódy.') == 'PRILIS ZLUTOUCKY KUN UPEL DABELSKE ODY.')


def test_alphabet_to_morse() -> None:
    """Test alphabet_to_morse function.
    """
    assert (alphabet_to_morse('Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu.')
            == '-.|.|----|-||.---|..|--..||....|.-.|..|...|-.|.||...|.-|-..-|---|..-.|---|-.|-.--|'
               '|-..|.-|-...|.-..|..-||.-.|---|--..|.|--..|...-|..-|-.-.|..||...|..|-.||..-|-..|.|...|-.|-.--|--|..|'
               '|-|---|-.|-.--||.--|.-|.-..|-|--..|..-|--..--||-|.-|-.|--.|.-|'
               '|.-||--.-|..-|..|-.-.|-.-|...|-|.|.--.|..-|.-.-.-|')
    assert (alphabet_to_morse('My e-mail address is: stuart_little@utb.cz, but you can call me "Steve";')
            == '--|-.--||.|-....-|--|.-|..|.-..||.-|-..|-..|.-.|.|...|...||..|...|---...|'
               '|...|-|..-|.-|.-.|-|..--.-|.-..|..|-|-|.-..|.|.--.-.|..-|-|-...|.-.-.-|-.-.|--..|--..--||-...|..-|-|'
               '|-.--|---|..-||-.-.|.-|-.||-.-.|.-|.-..|.-..||--|.||.-..-.|...|-|.|...-|.|.-..-.|-.-.-.|')


def test_get_key() -> None:
    """Test get_key function.
    """
    assert (get_key('.---', translator) == 'J')
    assert (get_key('-....', translator) == '6')
    assert (get_key('.--.-.', translator) == '@')


test_remove_diacritics()
test_alphabet_to_morse()
test_get_key()
