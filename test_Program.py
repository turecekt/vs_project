"""Unit testy."""
import Program as p

def test_formateError():
    """Test formatovani chyb."""
    assert(p.formateError('test') == "!!! test !!!")


def test_parseAction():
    """Test parsovani akce."""
    assert(p.parseAction('Z') == 1)


def test_checkUserInputText():
    """Test vstupu uzivatele."""
    assert(p.checkUserInputText('"test"') == True)


def test_encodeText():
    """Test kodovani."""
    assert(p.encodeText('test') == '- . ... -')


def test_decodeText():
    """Test dekodovani."""
    assert(p.decodeText('- . ... -') == 'TEST')
