"""This is a program for simple mathematical operations with two numbers.
The operations are addition, subtraction, multiplication and division.
The functions are defined in "calculator".

Input is from the console.

Output is from the console.

Example:

Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide

Insert choice |1|2|3|4| -> 1

Insert your first number -> 20
Insert your second number -> 15

20.0 + 15.0 = 35
"""

# Import necessary functions.
import calculator

# List the choices for the user.
print("""
Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
""")

while True:

    # Take input from the user.
    choice = int(input("Insert choice |1|2|3|4| -> "))

    # Check the user input.
    if choice in (1, 2, 3, 4):

        # Get input numbers from the user for the calculation.
        n1 = float(input("Insert your first number -> "))
        n2 = float(input("Insert your second number -> "))

        # Use the add function and print the result.
        if choice == 1:
            print(n1, "+", n2, "=", calculator.add(n1, n2))

        # Use the subtract function and print the result.
        elif choice == 2:
            print(n1, "-", n2, "=", calculator.subtract(n1, n2))

        # Use the multiply function and print the result.
        elif choice == 3:
            print(n1, "*", n2, "=", calculator.multiply(n1, n2))

        # Use the divide function and print the result.
        elif choice == 4:
            print(n1, "/", n2, "=", calculator.divide(n1, n2))
        break
    else:
        print("Invalid Input! Input must be one of these numbers: 1,2,3,4.")
