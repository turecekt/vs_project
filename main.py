def dva(x):
    return bin(x)[2:]

def osm(x):
    return oct(x)[2:]

def sest(x):
    return hex(x)[2:].upper()

print('Prekladac z desitkove soustavy\nVyber si do jake soustavy chces prekladat: ')
print('1) Dvojkova\n2) Osmickova\n3) Sestnactkova')
vyber = int(input('Vyber z nabidky: '))
x = int(input('Zadej cislo pro prevod: '))

if vyber == 1 and x >= 0:
    dva(x)
    print('Prevod do 2 soustavy je: ', dva(x))
elif vyber == 2 and x >= 0:
    osm(x)
    print('Prevod do 8 soustavy je: ', osm(x))
elif vyber == 3 and x >= 0:
    sest(x)
    print('Prevod do 16 soustavy je: ', sest(x))
else:
    print('Tato moznost neexistuje')

def test_dva():
    assert dva(10) == '1010'

def test_osm():
    assert osm(9) == '11'

def test_sest():
    assert sest(15) == 'F'
