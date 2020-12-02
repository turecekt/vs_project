"""VS PROJEKT"""

def getUserInput(message):
    inp = input(message + "\n")
    while len(inp.split()) != 2:
        inp = input("Invalid input. Try it again. Example input: 1 2" + "\n")
    return inp.split()

def sqrt(n):
    return n ** (1/2)

def sqr(n):
    return n * n

def calculatePerimeter(a, b, c):
    return a + b + c

def calculateArea(a, b, c):
    return a

def isConstructable(a, b, c):
    return a + b > c and a + c > b and b + c > a

def test_sqrt():
    assert sqrt(81) == 9

def test_sqr():
    assert sqr(4) == 16

def test_calculatePerimeter():
    assert calculatePerimeter(15, 20, 25) == 60

if __name__ == "__main__":
    """
    Main function
    
    First 3 steps are loading user input
    """
    a = getUserInput("Enter A coordinate in 2D grid")
    b = getUserInput("Enter B coordinate in 2D grid")
    c = getUserInput("Enter C coordinate in 2D grid")
    """
    Convert to int coordinate array
    """
    aCoord = [int(a[0]), int(a[1])]
    bCoord = [int(b[0]), int(b[1])]
    cCoord = [int(c[0]), int(c[1])]
    """
    Calculate lengths
    a - BC
    b - AC
    c - AB
    """
    al = sqrt(sqr(bCoord[0] - cCoord[0]) + sqr(bCoord[1] - cCoord[1]))
    bl = sqrt(sqr(aCoord[0] - cCoord[0]) + sqr(aCoord[1] - cCoord[1]))
    cl = sqrt(sqr(aCoord[0] - bCoord[0]) + sqr(aCoord[1] - bCoord[1]))
    print("Lengths: a =", al, ", b =", bl, ", c =", cl)

    """
    Print triangle perimeter
    """
    print("Triangle perimeter:", calculatePerimeter(al, bl, cl))
