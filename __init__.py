import math


def valid_input(x, y):
    try:
        int(x)
        int(y)
    except ValueError:
        return "Napište hodnoty ve správném formátu!"


def side_lenght(a, b):
    lenght = math.sqrt(pow(int(a[0]) - int(b[0]), 2) + pow(int(a[1]) - int(b[1]), 2))
    return lenght


def is_able(A, B, C):
    if(A == B or B == C or C == A):
        print("Trojuholník nie je zostrojiteľný")
    else:
        print("Trojuholník je zostrojiteľný")



def is_rectangular(A, B, C):
    sides = [side_lenght(A, B), side_lenght(B, C), side_lenght(A, C)]
    sides.sort(reverse=True)
    if round(sides[0] * sides[0]) == sides[1] * sides[1] + sides[2] * sides[2]:
        print("Je pravouhlý")
    else:
        print("Nie je pravouhlý")


if __name__ == '__main__':
    print("například: 1,1")
    A = input("zadejte souřadnice bodu A: ").split(",")
    valid_input(A[0], A[1])
    B = input("zadejte souřadnice bodu B: ").split(",")
    valid_input(B[0], B[1])
    C = input("zadejte souřadnice bodu C: ").split(",")
    valid_input(C[0], C[1])
    is_rectangular(A, B, C)
    is_able(A, B, C)
