"""Unit testy."""
import Translator as t


def test_decodeChar():
    """Test dekodovani znaku."""
    assert t.decodeChar('.-') == 'A'


def test_encodeChar():
    """Test zakodovani znaku."""
    assert t.encodeChar('A') == '.-'


def test_encode():
    """Test zakodovani textu."""
    assert t.encode('test') == '- . ... -'


def test_decode():
    """Test zakodovani textu."""
    assert t.decode('- . ... -') == 'TEST'
