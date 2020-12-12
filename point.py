import math

class Point:
    def __init__(self, x, y):
        if isinstance(x, str): x = x.replace(",", ".")
        if isinstance(y, str): y = y.replace(",", ".")

        self.x = float(x)
        self.y = float(y)

    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "(%.2f; %.2f)" % (self.x, self.y)
