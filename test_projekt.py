from projekt import MorseCode

morseCode = MorseCode()

# Test funkce pro rozdělení věty podle slov
def test_get_words():
    assert morseCode.get_words("test 123 asd") == ["test", "123", "asd"]

# Test funkce pro převod do morseovy abecedy
def test_encode():
    assert morseCode.encode("test 123 asd") \
        == "- . ... - ...---... .---- ..--- ...-- ...---... .- ... -.. ...---... "

# Test funkce pro převod z morseovy abecedy
def test_decode():
    assert morseCode.decode("- . ... - ...---... .---- ..--- ...-- ...---... .- ... -..") \
        == "test 123 asd "
