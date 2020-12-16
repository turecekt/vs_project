import pytest
from projekt import MorseCode

morseCode = MorseCode()

def test_get_words():
    assert morseCode.get_words("test 123 asd") == ["test", "123", "asd"]

def test_encode():
    assert morseCode.encode("test 123 asd") == "- . ... - ...---... .---- ..--- ...-- ...---... .- ... -.. ...---... " 

def test_decode():
    assert morseCode.decode("- . ... - ...---... .---- ..--- ...-- ...---... .- ... -..") == "test 123 asd "