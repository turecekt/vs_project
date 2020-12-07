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

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def input_values(point_name):
    point = str_list_to_int(input(f"Zadejte souřadnice bodu {point_name}: ").split(","))
    if point:
        return point
    else:
        print("Zadejte souřadnice ve správném formátu! například: 1,1")
        return input_values(point_name)


def str_list_to_int(list_to_convert):
    try:
        x = list_to_convert[0]
        x = list_to_convert[1]
        return True, [int(i) for i in list_to_convert]
    except ValueError or NameError:
        return False


if __name__ == '__main__':
    rectangle = Rectangle()
    if rectangle.is_able():
        print("Trojuholník je zostrojiteľný")
        print(
            f"Strana a: {round(rectangle.a, 2)}\n"
            f"Strana b: {round(rectangle.b, 2)}\n"
            f"Strana c: {round(rectangle.c, 2)}"
        )
        print(f"Obvod trojúhelníku je: {round(rectangle.perimeter(), 2)}")
        print(f"Obsah trojúhelníku je: {round(rectangle.area(), 2)}")
        print("Je pravouhlý" if rectangle.is_rectangular() else "Není pravouhlý")
    else:
        print("Trojuholník nie je zostrojiteľný")
