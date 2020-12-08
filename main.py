"""
main file for our project.

>>> 1
1
"""
import triangle as tr

if __name__ == '__main__':
    print("Souřadnice zadávejte ve formátu: x,y\nNapříklad: 1,1")
    triangle = tr.Triangle(tr.input_values(point_name="A")[1],
                           tr.input_values(point_name="B")[1],
                           tr.input_values(point_name="C")[1])
    if triangle.is_able():
        print("Trojuholník je zostrojiteľný")
        print(
            f"Strana a: {round(triangle.a, 2)}\n"
            f"Strana b: {round(triangle.b, 2)}\n"
            f"Strana c: {round(triangle.c, 2)}"
        )
        print(f"Obvod trojúhelníku je: {round(triangle.perimeter(), 2)}")
        print(f"Obsah trojúhelníku je: {round(triangle.area(), 2)}")
        print(
            "Je pravouhlý" if triangle.is_rectangular() else "Není pravouhlý")
    else:
        print("Trojuholník nie je zostrojiteľný")
