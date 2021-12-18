import math


def sides(A, B, C):
    a = math.sqrt(pow(abs(B[0] - C[0]), 2) + pow(abs(B[1] - C[1]), 2))
    b = math.sqrt(pow(abs(A[0] - C[0]), 2) + pow(abs(A[1] - C[1]), 2))
    c = math.sqrt(pow(abs(A[0] - B[0]), 2) + pow(abs(A[1] - B[1]), 2))
    return a, b, c


def assemblability(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def squarness(a, b, c):
    if round(pow(a, 2), 5) + round(pow(c, 2), 5) == round(pow(b, 2), 5):
        return True
    else:
        return False


def calculation(a, b, c):
    perimeter = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area


def triangle():
    print("""You will be prompted to enter coordinates
    for each points of triangle, enter two numbers
    with space between them""")

    try:
        A = input("A: ")
        A = tuple(map(int, A.split()))

        B = input("B: ")
        B = tuple(map(int, B.split()))

        C = input("C: ")
        C = tuple(map(int, C.split()))

        a, b, c = sides(A, B, C)
        print("Sides: a = %.2f, b = %.2f, c = %.2f" % (a, b, c))

        if assemblability(a, b, c):
            print("Triangle is assemblable")

            if squarness(a, b, c):
                print("Triangle is rectangular")
            else:
                print("Triangle is not rectangular")

            perimeter, area = calculation(a, b, c)
            print("Perimeter: %.2f  Area: %.2f" % (perimeter, area))
        else:
            print("Triangle is not assemblable")
    except Exception:
        print('You need to enter coordinates for each point')