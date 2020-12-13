import morseovka


def test_Text_na_Morseovku():
    """Sifrovani do morseova kodu.
    Funkce Text_na_Morseovku() porovnava
    vraceny string s morseovym kodem.
    """
    assert Text_na_Morseovku('A A') == '.- / .-'
    assert Text_na_Morseovku('test') == '- . ... -'
    assert Text_na_Morseovku('33 -  10 = 23') == \
           '...-- ...--  -....-   .---- -----  -...-  ..--- ...--'
    assert Text_na_Morseovku('/+-: .    .') == \
           '-..-. .-.-. -....- ---...  .-.-.-     .-.-.-'
    assert Text_na_Morseovku('1234567890') == \
           '.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'
    assert Text_na_Morseovku('Pokud je zadán text, '
                             'je přeložen do morseovky a naopak. ') == \
           '.--. --- -.- ..- -.. / .--- . / --.. .- -.. -. / - . -..- -'
           '.--- . / .--. . .-.. --- . -. / -.. --- / -- --- .-. ... . --- ...- -.- -.-- / .- / -. .- --- .--. .- -.- .-.-.-'
           


def test_Morseovka_na_Text():
    """Desifrovani morseova kodu.
    Funkce test_Morseovka_na_Text() porovnava
    morseuv kod se stringem podle Morseovy abecedy.
    """
  
   
    assert morseovka.Morseovka_na_Text('-..-. .-.-. -....- ---...  '
                              '.-.-.-     .-.-.-') \
           == '/+-: . .'
    assert morseovka.Morseovka_na_Text('.---- ..--- ...-- ....- ..... '
                              '-.... --... ---.. ----. -----') \
           == '1234567890'

        
