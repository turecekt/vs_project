#!/usr/bin/env python3
"""Run triangle program."""

from triangle import *
import inputProcessor

sides = inputProcessor.getSides()

sidea = sides[0]
sideb = sides[1]
sidec = sides[2]
"""Print results of default calculations."""

# Perimeter
perimeter = trianglePerimeter(sidea, sideb, sidec)

print(f"Perimeter of the triangle is: {perimeter}")

# Area
area = triangleArea(sidea, sideb, sidec)

print(f"Area of the triangle is: {area}")

# Orthogonality
sidesSorted = sorted(sides)
orthogonal = triangleOrthogonality(sidesSorted[0], sidesSorted[1], sidesSorted[2])
