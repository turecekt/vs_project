#!/usr/bin/env python3
"""Run triangle program."""

from triangle import (constructability, trianglePerimeter,
                      triangleArea, triangleOrthogonality)
import inputProcessor
import sys


def main():
    """Core function of triangle program."""
    debug = False

    sides = inputProcessor.getSides(sys.argv, debug)

    sidea = sides[0]
    sideb = sides[1]
    sidec = sides[2]

    # Constructability
    if constructability(sidea, sideb, sidec):
        print("Lengths of the sides of the triangle are:\n"
              f"{sides[0]}, {sides[1]}, {sides[2]}")

        """Print results of default calculations."""

        # Perimeter
        perimeter = trianglePerimeter(sidea, sideb, sidec)

        print(f"Perimeter of the triangle is: {perimeter}")

        # Area
        area = triangleArea(sidea, sideb, sidec)

        print(f"Area of the triangle is: {area}")

        # Orthogonality
        sidesSorted = sorted(sides)
        orthogonal = triangleOrthogonality(sidesSorted[0],
                                           sidesSorted[1],
                                           sidesSorted[2])

        if orthogonal:
            print("This triangle is orthogonal")
    else:
        print("This triangle is not constructable!")


if __name__ == '__main__':
    main()
