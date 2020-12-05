import math


def valid_input(x, y):
    try:
        int(x)
        int(y)
    except ValueError:
        exit("Napište hodnoty ve správném formátu!")


def side_lenght(point_1, point_2):
    return math.sqrt(pow(int(point_1[0]) - int(point_2[0]), 2) + pow(int(point_1[1]) - int(point_2[1]), 2))


def is_able(point_a, point_b, point_c):
    if point_a == point_b or point_b == point_c or point_c == point_a:

        print("Trojuholník nie je zostrojiteľný")
    else:
        print("Trojuholník je zostrojiteľný")


def is_rectangular(point_a, point_b, point_c):
    sides = [
        side_lenght(point_a, point_b),
        side_lenght(point_b, point_c),
        side_lenght(point_a, point_c)
    ]
    sides.sort(reverse=True)

    if round(sides[0] * sides[0]) == sides[1] * sides[1] + sides[2] * sides[2]:
        print("Je pravouhlý")
    else:
        print("Nie je pravouhlý")


if __name__ == '__main__':
    print("například: 1,1")

    point_a = input("zadejte souřadnice bodu A: ").split(",")
    valid_input(point_a[0], point_a[1])

    point_b = input("zadejte souřadnice bodu B: ").split(",")
    valid_input(point_b[0], point_b[1])

    point_c = input("zadejte souřadnice bodu C: ").split(",")
    valid_input(point_c[0], point_c[1])

    is_rectangular(point_a, point_b, point_c)
    is_able(point_a, point_b, point_c)
