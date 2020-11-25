"""Module Triangle.

This code calculates sides of triangle from user given coordinates.
With the calculated sides, it also calculates perimeter and area
of the triangle aswell as if the triangle is constuctable and
if its rectangular.
"""


import numpy as np
# Import of numerical library,
# which is used in code for power and square root function


def getInput():
    """Users input.

    Firstly i defined function which detects users input, then i loaded the
    input into variable tmp, which is string at the moment. After that i used
    split() which splits string into array. I also check if user inputs
    correct amount of numbers. If not he is asked to input them again.
    After that i returne variable tmp.
    """
    tmp = input("Input 6 coordinates, i.e(a1 b1 a2 b2 a3 b3)")
    while len(tmp.split()) != 6:
        tmp = input("Wrong input try again, i.e(a1 b1 a2 b2 a3 b3)")
    tmp = tmp.split()
    return tmp


def ReturnSide(a, b, c):
    """Sides of triangle.

    Defined function which prints each calculated side of the
    triangle, it takes variables "a,b,c" from main.
    """
    print("Side a is:", a)
    print("Side b is:", b)
    print("Side c is:", c)


def ReturnPerimeter(a, b, c):
    """Perimeter calcuation.

    Function which calculates perimeter of triangle with values calculated in
    main, returns value of perimeter, i also use round() function which rounds
    decimal number to 2 decimal places.
    """
    perimeter = a + b + c
    perimeter = round(perimeter, 2)
    return perimeter


def ReturnArea(a, b, c, perimeter):
    """Content calculation.

    Function which calculates area of triangle with input values from main,
    firstly it calculates small s which is used in area of triangle equation
    then it calculates the area, round it to 2 decimal places and return it.
    """
    s = perimeter / 2
    S = np.sqrt(s * ((s - a) * (s - b) * (s - c)))
    S = round(S, 2)
    return S


def IsRectangular(a, b, c):
    """Rectanguar check.

    Function which calculates if triangle is rectangular or not. Firstly i
    check if the equation is correct, if it passes then it returns true,
    if not then it returns false.
    """
    if np.power(c, 2) == np.power(a, 2) + np.power(b, 2):
        return True
    else:
        return False


def IsConstucrable(a, b, c):
    """Triangle constructability.

    Function which checks if triangle is constuctable. It returns true or false
    depending on the "if" outcome.
    """
    if a + b > c or a + c > b or b + c > a:
        return True
    else:
        return False


def test_perimeter():
    """Test of perimeter.

    Test witch checks if function ReturnPerimeter works correctly. By assert we
    tell pytest what line of code it should check. It compares calculated value
    to return value from the function.
    """
    assert ReturnPerimeter(2, 3, 4) == 9


def test_area():
    """Test of perimeter.

    Test which checks if ReturnArea works. We compare already calculated
    result with return value from function ReturnArea(). It uses localy
    assigned variables as input for function
    """
    a1 = 2
    b1 = 3
    c1 = 4
    ob = 22
    assert ReturnArea(a1, b1, c1, ob) == 74.46


def test_rectangular():
    """Test of rectangular.

    Defining test which checks if IsRectangular works. It uses local variables
    which i know make rectangular triangle, so IsRectangular returns true.
    """
    a = 3
    b = 4
    c = 5
    assert IsRectangular(a, b, c)


def test_constuctable():
    """Test of constructable.

    Test witch checks if IsConstucrable works, same as tests before, it uses
    precalculated local variables in the function, so the function returns
    true.
    """
    a = 3
    b = 4
    c = 5
    assert IsConstucrable(a, b, c)


def test_getSideFromCoordinate():
    """Test of coordinate equation.

    Test witch checks if equation works properly, it compares precalculated
    result with the result from equation using local variables.
    """
    x1 = 2
    x2 = 4
    y1 = 5
    y2 = 8
    xy = 5
    assert xy == np.sqrt(np.power(x1 - y1, 2) + np.power(x2 - y2, 2))


if __name__ == '__main__':
    """Assign input.

    Here i call the getInput() and save its return values into variable tmp.
    In next 3 lines i make multidimensional arrays which contains coordinates
    for the sides equation, and convert them to int.
    """
    tmp = getInput()
    co1 = [int(tmp[0]), int(tmp[1])]
    co2 = [int(tmp[2]), int(tmp[3])]
    co3 = [int(tmp[4]), int(tmp[5])]

    a = np.sqrt(np.power(co2[0] - co3[0], 2) + np.power(co2[1] - co3[1], 2))
    b = np.sqrt(np.power(co1[0] - co3[0], 2) + np.power(co1[1] - co3[1], 2))
    c = np.sqrt(np.power(co1[0] - co2[0], 2) + np.power(co1[1] - co2[1], 2))

    """Rounding Numbers.

    Rounding numebers from user input to 2 decimal places
    """
    a = round(a, 2)
    b = round(b, 2)
    c = round(c, 2)

    """Calculated sides.

    Calling function ReturnSide which prints text defined in function on screen
    """
    ReturnSide(a, b, c)
    """Calculated perimeter.

    Calling function ReturnPerimeter, then saving its return values into
    variable perimeter, and printing the value onto screen.
    """

    ReturnPerimeter(a, b, c)
    perimeter = ReturnPerimeter(a, b, c)
    print("Perimeter of triangle is:", perimeter)

    """Displays area of triangle.

    Calling function ReturnArea which prints returned value of area,
    it uses values from input and returned value from ReturnPerimeter()
    function.
    """
    print("Area of triangle is:", ReturnArea(a, b, c, perimeter))

    """Check of rectangular.

    Calling function IsRectangular with our variables "a,b,c" from user. It
    displays text depending on the return from IsRectangular function.
    """
    IsRectangular(a, b, c)
    if(IsRectangular(a, b, c)):
        print("Triangle is rectangular")
    else:
        print("Triangle isn't rectangular")

    """Check of constructibility.

    Calling function IsConstucrable with our variables "a,b,c" from user.
    Works on the same principle as the function before. Which means print
    changes depending on return from the function.
    """
    IsConstucrable(a, b, c)
    if(IsConstucrable(a, b, c)):
        print("Triangle is constucrable")
    else:
        print("Triangle isn't constucrable")
