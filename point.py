"""Definition for a 2D point class"""

import math

class Point:
    """Stores an x and y coordinate."""

    def __init__(self, x, y):
        """Default constructor.
        
        Parameters:
            x (any): coordinate on the x axis
            y (any): coordinate on the y axis
        """
        if isinstance(x, str): x = x.replace(",", ".")
        if isinstance(y, str): y = y.replace(",", ".")

        self.x = float(x)
        self.y = float(y)

    def distance(self, point):
        """Calculate the distance to a different point.
        
        Parameters:
            point (Point): the other point

        Return (float):
            the distance
        """
        return distance(self.x, self.y, point.x, point.y)

    def __str__(self):
        """Return the string representation of this point.
        
        Return (str):
            a string in the format (x; y)
        """
        return "(%.2f; %.2f)" % (self.x, self.y)

def distance(x1, y1, x2, y2):
    """Calculate the distance between two points.
        
    Parameters:
        x1 (float): x coordinate of the first point
        y1 (float): y coordinate of the first point
        x2 (float): x coordinate of the second point
        y2 (float): y coordinate of the second point

    Return (float):
        the distance
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
