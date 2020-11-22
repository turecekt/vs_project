"""This is input reading module.

Input reading module suplies functions for reading values from stdin
and parse them to points.

"""


def parsePoint(pointInput):
    """Parse point to coordinates pair (list of two numbers).

    Args:
        pointInput (string): pointInput read from terminal

    Returns:
        list: x and y coordinates (pair)

    Raises:
        Exception: when coordinantes are in invalid format or are not numbers

    >>> parsePoint("5.2,7.6")
    [5.2, 7.6]
    >>> parsePoint("a,3")
    Traceback (most recent call last):
        ...
    ValueError: could not convert string to float: 'a'
    >>> parsePoint("1,1,1")
    Traceback (most recent call last):
        ...
    Exception: Wrong format of point. Allowed formats are \
'number, number' and '(number, number)'
    """
    unifiedPointInput = pointInput.replace("(", "")
    unifiedPointInput = pointInput.replace(")", "")
    unifiedPointInput = pointInput.replace(" ", "")
    coordinantes = unifiedPointInput.split(",")
    if (len(coordinantes) < 2 or len(coordinantes) > 2):
        raise Exception((
            "Wrong format of point. Allowed formats are "
            "'number, number' and '(number, number)'"
            ))
    return[float(coordinantes[0]), float(coordinantes[1])]


def getPoints(pointsNames, enviroment):
    """Read point from terminal.

    Args:
        pointsNames (list of strings): name of the points
            in two dimensional space
        enviroment (string): enviroment of app

    Returns:
        list: list of points

    Raises:
        Exception: Wrong format of point.

    >>> getPoints(["1","2","3"], "test")
    [[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]]
    """
    points = []
    for pointName in pointsNames:
        question = "Please enter coordinante (x,y) of point "+pointName+": "
        if enviroment == "__main__":
            point = input(question)
        else:
            point = "1,"+pointName+""
        points.append(parsePoint((point)))
    return points
