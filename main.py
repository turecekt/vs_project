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


print('Prekladac z desitkove soustavy'
      '\nVyber si do jake soustavy chces prekladat: ')
print('1) Dvojkova\n2) Osmickova\n3) Sestnactkova')
# vyber = int(input('Vyber: '))  # zakomentovano z duvodu selhani testu
# x = int(input('Zadej cislo: '))  # zakomentovano z duvodu selhani testu
vyber = 1  # Zaznamena vyber z nabidky
x = 150  # Zazamena int input do x

if vyber == 1 and x >= 0:  # Rozhoduje podle vstupu vyber
    dva(x)  # Provede fuknci dva(x)
    print('Prevod do 2 soustavy je: ', dva(x))  # Vytiskne vysledek
elif vyber == 2 and x >= 0:
    osm(x)  # Provede funkci osm(x)
    print('Prevod do 8 soustavy je: ', osm(x))
elif vyber == 3 and x >= 0:
    sest(x)  # Provede se funkce sest(x)
    print('Prevod do 16 soustavy je: ', sest(x))
else:  # Pokud neni cislo = 1, 2 nebo 3
    print('Tato moznost neexistuje')


def test_dva():
    """Test funkce dva()."""
    assert dva(10) == '1010'


def test_osm():
    """Test funkce osm()."""
    assert osm(9) == '11'


def test_sest():
    """Test funkce sest()."""
    assert sest(15) == 'F'
