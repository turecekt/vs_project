"""Main module which handles user input and prints results to the console."""

import sys
from point import Point
import triangle


def print_triangle_info(point_a, point_b, point_c):
    """Print information about a triangle to the command line.

    Parameters:
        point_a (Point): point A
        point_b (Point): point B
        point_c (Point): point C
    """
    side_a = point_b.distance(point_c)
    side_b = point_a.distance(point_c)
    side_c = point_a.distance(point_b)

    print("Délka strany a (B -> C): %.2f" % side_a)
    print("Délka strany b (A -> C): %.2f" % side_b)
    print("Délka strany c (A -> B): %.2f" % side_c)

    print()

    is_valid = triangle.is_valid(side_a, side_b, side_c)
    print("Jde sestrojit: " + ("ano" if is_valid else "ne"))

    if is_valid:
        is_right_angle = triangle.is_right_angle(side_a, side_b, side_c)
        print("Pravoúhlý: " + ("ano" if is_right_angle else "ne"))

        print()

        print("Obvod: %.2f" % (side_a + side_b + side_c))
        print("Obsah: %.2f" % (triangle.area(side_a, side_b, side_c)))


def request_point(name):
    """Prompt a user to enter point coordinates.

    Input is expected to be two numbers separated by a space (e. g. "0 10").
    If the user enters invalid data, they are promped again.

    Parameters:
        name (str): a display name for the point
    """
    while True:
        try:
            print("Zadejte souřadnice bodu " + name)
            values = input().strip().split(" ")
            if len(values) == 2:
                return Point(values[0], values[1])
            else:
                print("Nesprávný vstup")
                print("Zadejte dvě čísla oddělená mezerou")
                print()
        except ValueError as e:
            print("Nesprávný vstup")
            print(e)
            print()


def init():
    """Process command line arguments or prompt user to enter coordinates."""
    if __name__ == "__main__":
        args = sys.argv
        arg_count = len(args)
        if arg_count == 1:
            point_a = request_point("A")
            point_b = request_point("B")
            point_c = request_point("C")
            print()

            print_triangle_info(point_a, point_b, point_c)
            sys.exit(0)
        elif arg_count == 7:
            try:
                point_a = Point(args[1], args[2])
                point_b = Point(args[3], args[4])
                point_c = Point(args[5], args[6])
                print_triangle_info(point_a, point_b, point_c)
                sys.exit(0)
            except ValueError as e:
                print("Nesprávný vstup")
                print(e)
                sys.exit(1)
        else:
            print("Nesprávný počet argumentů")
            print("Očekáváno 6")
            print("Nalezeno " + str(arg_count - 1))
            sys.exit(1)


init()
