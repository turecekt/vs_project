"""Module (file) descrption."""


def sqrt(x):
    """Square root calc.

    Returns calculated value of x. Operator "**" works as power would in
    numpy.
    """
    return x**(1/2)


def pwr(x):
    """Power calculation.

    Returns calculated value of x. As in sqrt, i use operator "**"
    """
    return x**(2)


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
    triangle, it takes variables "a,b,c" from main. Return is
    for testing purposes
    """
    print("Side a is:", a)
    print("Side b is:", b)
    print("Side c is:", c)
    return a


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
    S = sqrt((s * ((s - a) * (s - b) * (s - c))))
    S = round(S, 2)
    return S


def IsRectangular(a, b, c):
    """Rectanguar check.

    Function which calculates if triangle is rectangular or not. Firstly i
    check if the pythagoras equation is correct, if it passes then it
    returns true,
    if not then it returns false.
    """
    if pwr(c) == pwr(a) + pwr(b):
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


def test_sqrt():
    """Square root check.

    Tests if square root function works, using local variable and
    precalculated result
    """
    x = 25
    assert sqrt(x) == 5
    assert sqrt(36) == 6


def test_sqrt_mdArray():
    """Square root with multi array.

    Testing if sqrt() function works with multidimensional array
    by comparint it to precalculated result
    """
    tmp = [5, 8, 2, 4]
    co1 = [tmp[0], tmp[1]]
    co2 = [tmp[2], tmp[3]]
    a = sqrt(pwr(co1[0] - co2[0]) + pwr(co1[1] - co2[1]))
    assert a == 5


def test_pwr():
    """Power check.

    Tests if power function works, using local variable and
    precalculated result
    """
    x = 5
    assert pwr(x) == 25
    assert pwr(3) == 9


def test_round():
    """Round test.

    Tests if round function works properly, using local variable
    and precounted result, we check if the build in function can
    properly round numbers, in my case to 2 decimal places.
    """
    x = 2.126324345
    assert round(x, 2) == 2.13


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


def test_returnSide():
    """Return test.

    Tests if returned value of a is correct for printing.
    """
    a = 2
    b = 4
    c = 7
    assert ReturnSide(a, b, c) == 2


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
    assert xy == sqrt((pwr(x1 - y1)) + (pwr(x2 - y2)))


def test_convertToInt():
    """Conversiom.

    Tests if function split(), and conversion of int work properly by
    comparing to int value of stringValue which was previously of type
    string.
    """
    stringValue = "1 2"
    stringValue = stringValue.split()
    tmp = [int(stringValue[0]), int(stringValue[1])]
    assert tmp[0] == 1
    assert tmp[1] == 2


def test_ofInt():
    """Int value.

    Testing if int() function rounds decimal places with result from
    round() function.
    """
    k = 1.1232345
    z = 1.1445765476
    k = round(k, 0)
    z = int(z)
    assert k == z


def test_Assign():
    """Asign check.

    This test checks if out user input stored in array is geting correctly
    asigned to variable co1 which is multidimensional array
    """
    tmp = [1, 2, 3, 4, 5, 6]
    int(tmp[0])
    int(tmp[1])
    co1 = [tmp[0], tmp[1]]
    assert co1[0] == tmp[0]


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

    a = sqrt(pwr(co2[0] - co3[0]) + pwr(co2[1] - co3[1]))
    b = sqrt(pwr(co1[0] - co3[0]) + pwr(co1[1] - co3[1]))
    c = sqrt(pwr(co1[0] - co2[0]) + pwr(co1[1] - co2[1]))

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
