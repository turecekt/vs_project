from point import Point
import triangle

def print_triangle_info(point_a, point_b, point_c):
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

if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(0, 50.8)
    c = Point(50.6668215, 0)
    print_triangle_info(a, b, c)
