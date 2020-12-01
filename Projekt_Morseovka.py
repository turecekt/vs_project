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


def test_remove_diacritics() -> None:
    """Test remove_diacritics function.
    """
    assert(remove_diacritics('áčďéěíňóřšťúůýž') == 'ACDEEINORSTUUYZ')
    assert(remove_diacritics('Příliš žluťoučký kůň úpěl ďábelské ódy.') == 'PRILIS ZLUTOUCKY KUN UPEL DABELSKE ODY.')


def test_alphabet_to_morse() -> None:
    """Test alphabet_to_morse function.
    """
    assert(alphabet_to_morse('Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu.')
           == '-.|.|----|-||.---|..|--..||....|.-.|..|...|-.|.||...|.-|-..-|---|..-.|---|-.|-.--|' +
              '|-..|.-|-...|.-..|..-||.-.|---|--..|.|--..|...-|..-|-.-.|..||...|..|-.||..-|-..|.|...|-.|-.--|--|..|' +
              '|-|---|-.|-.--||.--|.-|.-..|-|--..|..-|--..--||-|.-|-.|--.|.-|' +
              '|.-||--.-|..-|..|-.-.|-.-|...|-|.|.--.|..-|.-.-.-|')


test_remove_diacritics()
test_alphabet_to_morse()
