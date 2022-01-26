"""Ciselne soustavy."""


def dva(x):
    """Prevod do 2 soustavy.

    Vraci hodnotu x prevedenou do 2 soustavy
    """
    return bin(x)[2:]


def osm(x):
    """Prevod do 8 soustavy.

    Vraci hodnotu x prevedenou do 8 soustavy
    """
    return oct(x)[2:]


def sest(x):
    """Prevod do 16 soustavy.

    Vezme hodnotu z promenne x a prevede do 16 soustavy
    take zmeni vsechna mala pismena na velka f -> F
    """
    return hex(x)[2:].upper()


def prevod(vyber, x):
    """Vyber soustavy a overeni platnosti.

    Podle zadane hodnoty zvoli soustavu, overi zda-li je cislo
    vetsi nebo rovno nez nula a pote provede danou funkci
    """
    if vyber == 1 and x >= 0:  # Rozhoduje podle vstupu vyber
        return f'Prevod do 2 soustavy je: {dva(x)}'
    elif vyber == 2 and x >= 0:
        return f'Prevod do 8 soustavy je: {osm(x)}'
    elif vyber == 3 and x >= 0:
        return f'Prevod do 16 soustavy je: {sest(x)}'
    else:  # Pokud neni cislo = 1, 2 nebo 3
        return 'Tato moznost neexistuje'


if __name__ == '__main__':
    print('Prekladac z desitkove soustavy'
          '\nVyber si do jake soustavy chces prekladat: ')
    print('1) Dvojkova\n2) Osmickova\n3) Sestnactkova')
    vyber = int(input('Vyber: '))
    x = int(input('Zadej cislo: '))
    prevod(vyber, x)
    print(prevod(vyber, x))


def test_prevod():
    """Test funkce prevod()."""
    assert prevod(3, 20) == 'Prevod do 16 soustavy je: 14'


def test_dva():
    """Test funkce dva()."""
    assert dva(10) == '1010'


def test_osm():
    """Test funkce osm()."""
    assert osm(9) == '11'


def test_sest():
    """Test funkce sest()."""
    assert sest(15) == 'F'
