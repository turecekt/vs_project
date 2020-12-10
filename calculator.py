"""This is a program for simple mathematical operations with two numbers.

The operations are addition, subtraction, multiplication and division.

The input method is through the console.
"""


def add(x, y):
    """Find the addition of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a addition of two numbers.
    """
    return x + y


def subtract(x, y):
    """Find the subtraction of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a subtraction of two numbers.
    """
    return x - y


def multiply(x, y):
    """Find the multiplication of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a multiplication of two numbers.
    """
    return x * y


def divide(x, y):
    """Find the division of x,y and return the result.

    Input of the function are two numbers.

    Output of the function is a division of two numbers.

    Raise Value error when second number is 0.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


print("""
Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
""")
"""List the choices for the user.
"""

while True:
    choice = int(input("Insert your choice |1|2|3|4| > "))
    """Take input from the user.

    Input are four numbers: 1,2,3,4. Each representing a single mathematical operation.
    """
    if choice in (1, 2, 3, 4):
        first_number = float(input("Insert your first number > "))
        second_number = float(input("Insert your second number > "))

        if choice == 1:
            print(first_number, "+", second_number, "=", add(first_number, second_number))

        elif choice == 2:
            print(first_number, "-",second_number, "=", subtract(first_number, second_number))

        elif choice == 3:
            print(first_number, "*", second_number, "=", multiply(first_number, second_number))

        elif choice == 4:
            print(first_number, "/", second_number, "=", divide(first_number,second_number))
        break
    else:
        print("Invalid Input! Input must be one of these numbers: 1,2,3,4.")
