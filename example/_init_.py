"""Převodník morseové soustavy."""

from morse import encrypt, decrypt, choice


<<<<<<< HEAD
def encrypt(zprava):
    """Vrací zadanou zprávu převedenou do morseovi abecedy.

    Arguments:
    zprava - text určený k převodu do morseovy soustavy
    Returns:
    sifra - text přeložený do morseovy soustavy
    """
    
    if not isinstance(zprava, str):
      return "parameter musí být str" 
    
    zprava = zprava.upper()
    sifra = ''

    if zprava == "":
        return "Chyba: prázdné pole"

    for pole in zprava:
        if pole != ' ':
            sifra += Znaky[pole] + ' '
        else:
            sifra += ' '
    return sifra


def decrypt(zprava):
    """Vrací přeložený text z morseovy soustavy.

    Arguments:
    zprava - morseova soustava určená k převodu do textu
    Returns:
    vystup - morseova soustava přeložená do textu
    """
    
    if not isinstance(zprava, str):
        return "parameter musí být (str)" 
    
    zprava += ' '
    vystup = ''
    znak = ''

    if zprava == " ":
        return "Chyba: prázdné pole"

    for pole in zprava:
        if(pole != '-' and pole != '.' and pole != ' '):
            vystup = 'špatný formát zadávání'
            return vystup

    for pole in zprava:
        if (pole != ' '):
            i = 0
            znak += pole
        else:
            i += 1
            if i == 2:
                vystup += ' '
            else:
                vystup += list(Znaky.keys())[list(Znaky.values()).index(znak)]
                znak = ''
    return vystup

def choice(vyber):
    """Vrací definici dle zadaného parametru.
    
    Arguments:
        vyber - hodnota určující volání definice

    Returns:
        result - vrací hodnotu zvolené definice
    """
    
    if not isinstance(vyber, int):
        return "parametr musí být (int)"
    if vyber < 0:
        return "parametr nesmí být v záporný"
    
    if vyber == 1:
        result = encrypt("TEST")

    elif vyber == 2:
        result = decrypt('- . ... -')
        
    else: result = 'špatný formát zadávání'
    
    return result

def main(): 
   
    volani = choice(1)
    print (volani) 
   
if __name__ == '__main__': 
    main() 

=======
>>>>>>> 94ee9acb8fbf9d9ab4f905ae77be625152e69639
def test_decrypt():
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... -") == "TEST"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("..--- -----") == "20"
    """Otestuje zda funkce překládá znaky mimo morseovu abecedu."""
    assert decrypt("AWEGWRHGWRh") == "Špatný formát zadávání"
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert decrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z morseovi abecedy do textu."""
    assert decrypt("- . ... - .---- ..--- .--.-.") == "TEST12@"
<<<<<<< HEAD
    """Otestuje správnost zadáváného parametru (musí být str)"""
    assert decrypt(10) == \
    "parameter musí být (str)"
   
    
=======


>>>>>>> 94ee9acb8fbf9d9ab4f905ae77be625152e69639
def test_encrypt():
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test") == "- . ... - "
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("20") == "..--- ----- "
    """Otestuje zda funkce pracuje s prázdným parametrem."""
    assert encrypt("") == "Chyba: prázdné pole"
    """Otestuje správnost převodu z textu do morseovi abecedy."""
    assert encrypt("test12@") == "- . ... - .---- ..--- .--.-. "
<<<<<<< HEAD
    """Otestuje správnost zadáváného parametru (musí být str)"""
    assert encrypt(10) == \
    "parameter musí být (str)"
    
def test_choice():
    """Otestuje správnost parametru volajícho funkce pro kódování/dekódování morseovky"""
    assert choice(0) == "špatný formát zadávání"   
    """Otestuje správnost parametru (nemsí být záporné)"""
    assert choice(-20) == \
    "parametr nesmí být v záporný"
    """Otestuje správnost parametru (nesmí být str)"""
    assert choice("TEST") == \
    "parametr musí být (int)"
         
=======


def test_choice():
    """Ověření parametru pro volání definicí."""
    assert choice(0) == "Špatný formát zadávání"
>>>>>>> 94ee9acb8fbf9d9ab4f905ae77be625152e69639
