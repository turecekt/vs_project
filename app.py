"""Program for simple mathematical operations.
"""
import calculator

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
    choice = input("Enter choice(1/2/3/4): ")
    """Take input from the user.

    Input are four number, representing a single mathematical operation.
    """
    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == '1':
            print(number1, "+", number2, "=", calculator.add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", calculator.subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", calculator.multiply(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", calculator.divide(number1, number2))
        break
    else:
        print("Invalid Input! Input must be one of these numbers: 1,2,3,4.")
