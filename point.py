import math

class Point:
    def __init__(self, x, y):
        if isinstance(x, str): x = x.replace(",", ".")
        if isinstance(y, str): y = y.replace(",", ".")

        self.x = float(x)
        self.y = float(y)

    def distance(self, point):
        return distance(self.x, self.y, point.x, point.y)

    def __str__(self):
        return "(%.2f; %.2f)" % (self.x, self.y)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
