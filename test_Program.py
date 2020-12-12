"""Unit testy."""
import Program as p


def test_formateError():
    """Test formatovani chyb."""
    assert p.formateError('test') == "!!! test !!!"


def test_parseAction_Encode():
    """Test parsovani akce."""
    assert p.parseAction('Z') == 1


def test_parseAction_Decode():
    """Test parsovani invalidni akce."""
    assert p.parseAction('D') == 2


def test_parseAction_End():
    """Test parsovani akce konec."""
    assert p.parseAction('K') == 3


def test_parseAction_Invalid():
    """Test parsovani invalidni akce."""
    assert p.parseAction('X') == 4


def test_checkUserInputText():
    """Test vstupu uzivatele."""
    res = 'False'
    if (p.checkUserInputText('"test"')):
        res = 'True'
    assert res == 'True'


def test_checkUserInputText_Invalid():
    """Test nevalidniho vstupu uzivatele."""
    res = 'True'
    if (not p.checkUserInputText('test')):
        res = 'False'
    assert res == 'False'


def test_encodeText_Test():
    """Test kodovani."""
    assert p.encodeText('test') == '- . ... -'


def test_decodeText_Test():
    """Test dekodovani."""
    assert p.decodeText('- . ... -') == 'TEST'


def test_encodeText_InvalidChar():
    """Test kodovani."""
    assert p.encodeText('č') == '..--..'


def test_encodeText_SpecialChars():
    """Test dekodovani."""
    assert p.decodeText('. , ? ! ; : ( ) - _ @') == '.-.-.-. .-..-. --..--' +
    ' .-..-. ..--.. .-..-. --..- .-..-. -.-.-. .-..-. ---... .-..-. --...' +
    ' .-..-. -.--.- .-..-. -....- .-..-. ..--.- .-..-. .--.-.'


def test_encodeText_SpecialChars():
    """Test dekodovani."""
    assert p.decodeText('.-.-.-. .-..-. --..--' +
    ' .-..-. ..--.. .-..-. --..- .-..-. -.-.-. .-..-. ---... .-..-. --...' +
    ' .-..-. -.--.- .-..-. -....- .-..-. ..--.- .-..-. .--.-.' ==
    '. , ? ! ; : ( ) - _ @'


def test_encodeText_Filip():
    """Test kodovani."""
    assert p.encodeText('Filip') == '..-. .. .-.. .. .--.'


def test_decodeText_Filip():
    """Test dekodovani."""
    assert p.decodeText('..-. .. .-.. .. .--.') == 'FILIP'
