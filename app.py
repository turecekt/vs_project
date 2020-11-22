"""This is triangle app.

Triangle app checks if triangle is constructable, counts lengt of sides etc.

"""

from input import getPoints
from triangle import checkIfconstructable, lengthOfSide, countArea, countPerimeter, checkIfRightAngled

pointsNames = ["A", "B", "C"]
points = []
distances = []

if __name__ == "__main__":
    points = getPoints(pointsNames, __name__)
else:
    points = [[1, 11], [2, 232], [23, 223]]


distances.append(lengthOfSide(points[0], points[1])) # side AB
distances.append(lengthOfSide(points[1], points[2])) # side BC
distances.append(lengthOfSide(points[2], points[0])) # side CA

if (not checkIfconstructable(points)):
    print("Triangle is not constructable")
    exit()

print("Triangle is constructable")

if (checkIfRightAngled(distances)):
    print("Triangle is right angeled")
else:
    print("Triangle isn't right angeled")

print("Triangle perimeter is", countPerimeter(distances))
print("Triangle area is", countArea(distances))
