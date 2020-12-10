"""Unit tests."""

import soubor


def test_fileExists():
    """Fileexists unit test."""
    text = "ahoj"
    actual = soubor.fileExists("ahoj.txt")
    assert(actual.read() == text)

def test_TextIntoVar():
    """textIntoVar uni test."""
    file = 'ahoj'
    actual = soubor.textIntoVar('ahoj.txt')
    assert(actual == file)

def test_CharNum():
    """cahrNum unit test"""
    assert soubor.charNum("Nikolas") == 7

def test_mostFreq():
    """mostFreq unit test."""
    assert soubor.mostFreq('Nina') == ('n',2)

def test_leastFreq():
    """leastFreq unit test."""
    assert soubor.leastFreq('Uz je to tady') == 'u'

def test_numOfEachChar():
    """numOfEachChar unit test."""
    assert soubor.numOfEachChar('Uz je to tady') == {'u': 1, 'z': 1, ' ': 3, 'j': 1, 'e': 1, 't': 2, 'o': 1, 'a': 1, 'd': 1, 'y': 1}

def test_avarage():
    """avarage unit test."""
    each = 'Nikolas';
    assert soubor.average(each) == 7