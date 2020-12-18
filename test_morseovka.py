import morseovka
import pytest

{
def test_TnM():
    """Sifrovani do morseova kodu.
    Funkce TnM() porovnava
    vraceny string s morseovym kodem.
    """
    assert TnM('A A') == '.- / .-'
    assert TnM('test') == '- . ... -'
    assert TnM('33 -  10 = 23') == '...-- ...-- / -....- / / .---- ----- / / ..--- ...--'
    assert TnM('/+-: .    .') == '-..-. .-.-. -....- ---...  .-.-.-     .-.-.-'
    assert TnM('1234567890') == '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'
    assert TnM('Pokud je zadán text, je přeložen do morseovky a naopak. ')
               == '.--. --- -.- ..- -.. / .--- . / --.. .- -.. -. /
                     ' - . -..- - / .--- . / .--. . .-.. --- . -. / -.. --- /
                     ' -- --- .-. ... . --- ...- -.- -.-- /
                     ' .- / -. .- --- .--. .- -.- .-.-.-'
           


def test_MnT():
    """Desifrovani morseova kodu.
    Funkce test_MnT() porovnava
    morseuv kod se stringem podle Morseovy abecedy.
    """
  
   
    assert MnT('-..-. -....- / .-.-.- / .-.-.-') == '/+-: . .'
    assert MnT('.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----') \
           == '1234567890'
    assert MnT('.--. -.-- - .... --- -. / .--- . / -. . .--- .-.. . .--. ... .. 
               '/ .--- .- --.. -.-- -.- / -. .- / ... ...- . - . .-.-.-') \
           == 'PYTHON JE NEJLEPSI JAZYK NA SVETE.'
}
        
