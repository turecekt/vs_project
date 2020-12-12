import math

class Bod:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


def vrat_bod(bod):
    n = 'Zadej bod ' + bod 
    m = ' souradnici '
    while True:
        try:
            x = int(input(n + m + 'x: ').strip())
            break
        except:
            print('Je treba zadat ciselnou hodnotu')

    while True:
        try:
            y = int(input(n + m + 'y: ').strip())
            break
        except:
            print('Je treba zadat ciselnou hodnotu')
    
    return Bod(x,y)

def pythagorova_veta(bod):
    x = math.sqrt((bod.x*bod.x)+(bod.y*bod.y))
    return x

def secteni_souradnic(bod1, bod2):
    return Bod(abs(bod1.x - bod2.x), abs(bod1.y - bod2.y))

def delka_strany(bod1, bod2):
    return pythagorova_veta(secteni_souradnic(bod1, bod2))

def sestrojitelnost(a, b, c):
    return (a + b > c and b + c > a and a + c > b)

def obvod(a, b ,c):
    return a + b + c

def obsah(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(s * ((s - a) * (s - b) * (s - c)))

# kontrola zda je trojúhelník pravouhlý
def pravouhlost(a, b, c):
    tmp_r = c
    if(a > tmp_r):
        tmp_l1 = tmp_r
        tmp_r = a
        tmp_l2 = b
    elif(b > tmp_r):
        tmp_l1 = tmp_r
        tmp_r = b
        tmp_l2 = a

    right = math.pow(tmp_r)
    left = (math.pow(tmp_l1) + math.pow(tmp_l2))

    return right == left

bod_a = vrat_bod('A')
bod_b = vrat_bod('B')
bod_c = vrat_bod('C')


