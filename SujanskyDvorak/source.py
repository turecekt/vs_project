import math

# Třída představující bod
class Bod:
    x = 0 # souřadnice x
    y = 0 # souřadnice z
    
    # konstruktor
    def __init__(self, x, y):
        """ :param x: souřadnice x 
            :param y: souřadnice y
        """
        self.x = x
        self.y = y

# Zajišťuje vstup od uživatele ve formě bodů
def vrat_bod(bod):
    n = f'Zadej bod {bod} souradnici'
    while True:
        try:
            x = int(input(f'{n} x: ').strip())
            break
        except:
            print('Je treba zadat ciselnou hodnotu')

    while True:
        try:
            y = int(input(f'{n} y: ').strip())
            break
        except:
            print('Je treba zadat ciselnou hodnotu')
    
    return Bod(x,y)


# Vypočítá pythagorovu větu na základě součtu souřadnic bodů zadaných uživatelem
def pythagorova_veta(bod):
    x = math.sqrt((bod.x*bod.x)+(bod.y*bod.y))
    return x

# Sečte souřadnice bodů zadaných uživatelem
def secteni_souradnic(bod1, bod2):
    return Bod(abs(bod1.x - bod2.x), abs(bod1.y - bod2.y))

# Spočítá délku strany z bodů zadaných uživatelem
def delka_strany(bod1, bod2):
    return pythagorova_veta(secteni_souradnic(bod1, bod2))

# Ověří zda je trojúhelník sestrojitelný na základě délek stran
def sestrojitelny(a, b, c):
    return (a + b > c and b + c > a and a + c > b)

# Spočítá obvod trojúhelníku pomocí délek stran
def obvod(a, b ,c):
    return a + b + c

# Spočítá obvod trojúhelníku pomocí délek stran
def obsah(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(s * ((s - a) * (s - b) * (s - c)))

# Ověří zda je trojúhelník pravouhlý
def pravouhly(a, b, c):
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

    ab = delka_strany(a,b)
    bc = delka_strany(b,c)
    ac = delka_strany(a,c)
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
    if (pravouhly(ab,bc,ac)):
        print("Trojuhelnik je pravouhly")
    else:
         print("Trojuhelnik neni pravouhly")
    

# Testy

def test_pythagorova_veta():
    assert pythagorova_veta(Bod(3,4)) == 5.0

def test_secteni_souradnic():
    bod = secteni_souradnic(Bod(3,-2),Bod(-1,-2))
    assert bod.x == 4 and bod.y == 0.0

def test_delka_strany():
    assert delka_strany(Bod(2,2),Bod(-1,-2)) == 5.0

def test_sestrojitelny():
    assert sestrojitelny(3,4,5)

def test_obvod():
    assert obvod(3,4,5) == 12.0

def test_obsah():
    assert obsah(3,4,5) == 6.0

def test_pravouhly():
    assert pravouhly(3,4,5)
