import time
import random

"""
Checks if the product of the division is a decimal number.

If it is a decimal number then function returns float otherwise int is returned.

Parameters:
a (int): Randomly generated number a <-10, 10>
b (int): Randomly generated number b <-10, 10>

Returns:
int: If a % b == 0 then the returned value is int
float: If a % b != 0 then the returned value is float

"""


def check_int(a, b):
    if a % b == 0:
        return int(a / b)
    else:
        return round(a / b, 2)


"""
Function to calculate the solution of en example.

Function switches among possible operations. Switch is done by an op argument.

Parameters:
a (int): Randomly generated number a <-10, 10>
b (int): Randomly generated number b <-10, 10>
op (int): Randomly generated number op <0, 3>

Returns:
int: For +-* operations and if a % b == 0
float: For division operation if a % b != 0

"""


def count(op, a, b):
    operation = {0: a + b, 1: a - b, 2: a * b, 3: check_int(a, b)}
    return operation.get(op)


operations = ["+", "-", "*", "/"]  # Possible operations

correct = 0  # Couter of correct answers
elapsed_time = 0  # elapsed time couter

print("Solve 5 examples. Use . in decimal numbers, round to two decimal places.")

for x in range(5):

    a = random.randint(-10, 10)  # Generates random number a <-10, 10>
    b = random.randint(-10, 10)  # Generates random number b <-10, 10>
    op = random.randint(
        0, 3
    )  # Generates random number op <0, 3>, used to switch between operations

    while b == 0:  # preventing division by 0
        b = random.randint(-10, 10)

    if b < 0:
        b_string = (
                "(" + str(b) + ")"
        )  # it is a convension to display a negative number in brackets e.g. 4+(-3)
    else:
        b_string = b  # no need for brackets in case of a positive number

    print(a, end="")
    print(operations[op], end="")
    print(b_string)

    start = time.time()  # start counting the user response time
    answer = input("Enter the result: ")
    end = time.time()  # stop counting the user response time
    elapsed_time += end - start  # update elapsed time counter

    if answer == str(count(op, a, b)):
        correct += 1  # if the user input is a correct solution, counter of correct answers is increased

print()
print("Correct answers ", end="")
print(correct, end="")
print("/5. Success rate ", end="")
print(int(correct / 5 * 100), end="")  # print relative success rate
print("%.")
print("Average response time: ", end="")
print(
    round(elapsed_time / 5, 2), end=""
)  # print average elapsed time rounded to two decimal places
print(" seconds.")
