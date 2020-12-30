
import pytest
import morseovka

test = morseovka()
def test_prevodDoMorseovky():
    assert morseovka.test_prevodDoMorseovky("RADIM13578") == ".-. .- -.. .. -- .---- ...-- ..... --... ---.."

def test_prevodZMorseovky():
    assert morseovka.test_prevodZMorseovky().decode(".-. .- -.. .. -- .---- ...-- ..... --... ---..") == "RADIM13578"