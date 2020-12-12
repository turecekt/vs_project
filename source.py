"""Import knihovny math."""
import math


class Bod:
    """souradnice x."""

    x = 0
    """souradnice y."""
    y = 0

    def __init__(self, x, y):
        """Konstruktor.

        :param x: souradnice x
        :param y: souradnice y
        """
        self.x = x
        self.y = y


def vrat_bod(bod):
    """Zajistuje vstup od uzivatele ve forme bodu."""
    n = f'Zadej bod {bod} souradnici'
    while True:
        try:
            x = int(input(f'{n} x: ').strip())
            break
        except TypeError:
            print('Je treba zadat ciselnou hodnotu')

    while True:
        try:
            y = int(input(f'{n} y: ').strip())
            break
        except TypeError:
            print('Je treba zadat ciselnou hodnotu')

    return Bod(x, y)


def pythagorova_veta(bod):
    """Popis.

    Vypocita pythagorovu vetu na zaklade souctu
    souradnic bodu zadanych uzivatelem
    """
    x = math.sqrt((bod.x*bod.x)+(bod.y*bod.y))
    return x


def secteni_souradnic(bod1, bod2):
    """Secte souradnice bodu zadanych uzivatelem."""
    return Bod(abs(bod1.x - bod2.x), abs(bod1.y - bod2.y))


def delka_strany(bod1, bod2):
    """Spocita delku strany z bodu zadanych uzivatelem."""
    return pythagorova_veta(secteni_souradnic(bod1, bod2))


def sestrojitelny(a, b, c):
    """Overi zda je trojuhelnik sestrojitelny na zaklade delek stran."""
    return (a + b > c and b + c > a and a + c > b)


def obvod(a, b, c):
    """Spocita obvod trojuhelnik pomoci delek stran."""
    return a + b + c


def obsah(a, b, c):
    """Spocita obvod trojuhelnik pomoci delek stran."""
    s = (a + b + c)/2
    return math.sqrt(s * ((s - a) * (s - b) * (s - c)))


def pravouhly(a, b, c):
    """Overi zda je trojuhelnik pravouhly."""
    tmp_r = c
    tmp_l1 = a
    tmp_l2 = b
    if(a > tmp_r):
        tmp_r = a
        tmp_l1 = tmp_r
    elif(b > tmp_r):
        tmp_l2 = tmp_r
        tmp_r = b

    right = math.pow(tmp_r, 2)
    left = (math.pow(tmp_l1, 2) + math.pow(tmp_l2, 2))

    return right == left


if __name__ == '__main__':
    a = vrat_bod('A')
    b = vrat_bod('B')
    c = vrat_bod('C')

    ab = delka_strany(a, b)
    bc = delka_strany(b, c)
    ac = delka_strany(a, c)
    print()
    if (sestrojitelny(ab, bc, ac)):
        print("Trojuhelnik je sestrojitelny")
    else:
        print("Trojuhelnik neni sestrojitelny")
    print()
    print(f"Strana a: {bc}\n\rStrana b: {ac}\n\rStrana c: {ab}")
    print()
    print(f"Obvod: {obvod(ab,ac,bc)}\n\rObsah: {obsah(ab,ac,bc)}")
    print()
    if (pravouhly(ab, bc, ac)):
        print("Trojuhelnik je pravouhly")
    else:
        print("Trojuhelnik neni pravouhly")


def test_pythagorova_veta():
    """Test Pythagorovy vety."""
    assert pythagorova_veta(Bod(3, 4)) == 5.0


def test_secteni_souradnic():
    """Test souctu souradnic."""
    bod = secteni_souradnic(Bod(3, -2), Bod(-1, -2))
    assert bod.x == 4 and bod.y == 0.0


def test_delka_strany():
    """Test delky stran."""
    assert delka_strany(Bod(2, 2), Bod(-1, -2)) == 5.0


def test_sestrojitelny():
    """Test sestrojitelnosti."""
    assert sestrojitelny(3, 4, 5)


def test_obvod():
    """Test obvodu."""
    assert obvod(3, 4, 5) == 12.0


def test_obsah():
    """Test obsahu."""
    assert obsah(3, 4, 5) == 6.0


def test_pravouhly():
    """Test pravouhlosti."""
    assert pravouhly(3, 4, 5)
