import math


class Rectangle:

    def __init__(self):
        print("Souřadnice zadávejte ve formátu: x,y\nNapříklad: 1,1")
        ex, self.point_a = input_values(point_name="A")
        ex, self.point_b = input_values(point_name="B")
        ex, self.point_c = input_values(point_name="C")
        self.a, self.b, self.c = self.side_lenght()

    def side_lenght(self):
        sides = [(self.point_a, self.point_b), (self.point_a, self.point_c), (self.point_b, self.point_c)]
        return (math.sqrt(pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2)) for i, j in sides)

    def is_able(self):
        a, b, c = self.a, self.b, self.c

        if a + b > c and a + c > b and c + b > a:
            return True
        else:
            return False

    def is_rectangular(self):
        sides: list[float] = [self.a, self.b, self.c]
        sides.sort(reverse=True)

        if round(sides[0] * sides[0]) == sides[1] * sides[1] + sides[2] * sides[2]:
            return True
        else:
            return False


def input_values(point_name):
    point = str_list_to_int(input(f"Zadejte souřadnice bodu ${point_name}: ").split(","))
    if point:
        return point
    else:
        print("Zadejte souřadnice ve správném formátu! například: 1,1")
        input_values(point_name)


def str_list_to_int(list_to_convert):
    try:
        return True, [int(i) for i in list_to_convert]
    except ValueError:
        return False


if __name__ == '__main__':
    rectangle = Rectangle()
    print(f"Strana a: {rectangle.a}\nStrana b: {rectangle.b}\nStrana c: {rectangle.c}")

    print("Je pravouhlý" if rectangle.is_rectangular() else "Není pravouhlý")
    print("Trojuholník je zostrojiteľný" if rectangle.is_able() else "Trojuholník nie je zostrojiteľný")
