import random
import time


OPERATIONS = ["+", "-", "*", "/"]  # Possible operations


def generate_equation(a=None, b=None, op=None) -> (int, int, int):
    """Generate random a, b and op for asking a question.

    If a,b and op are provided, then they wil be returned
    """
    if all((a, b, op)):
        return a, b, op
    a = random.randint(-10, 10)  # Generates random number a <-10, 10>
    b = random.randint(-10, 10)  # Generates random number b <-10, 10>
    op = random.randint(
        0, 3
    )  # Generates random number op <0, 3>, used to switch between operations

    while b == 0:  # preventing division by 0
        b = random.randint(-10, 10)
    return a, b, op


def check_int(a, b):
    """Checks if the product of the division is a decimal number.

    If it is a decimal number then function returns float otherwise int is returned.

    Parameters:
    a (int): Randomly generated number a <-10, 10>
    b (int): Randomly generated number b <-10, 10>

    Returns:
    int: If a % b == 0 then the returned value is int
    float: If a % b != 0 then the returned value is float

    """

    if a % b == 0:
        return int(a / b)
    else:
        return round(a / b, 2)


def ask_for_answer(answer=None) -> str:
    return answer or input("Enter result: ")


def calculate_equation(op, a, b):
    """Function to calculate the solution of en example.

    Function switches among possible operations. Switch is done by an op argument.

    Parameters:
    a (int): Randomly generated number a <-10, 10>
    b (int): Randomly generated number b <-10, 10>
    op (int): Randomly generated number op <0, 3>

    Returns:
    int: For +-* operations and if a % b == 0
    float: For division operation if a % b != 0

    """
    operation = {0: a + b, 1: a - b, 2: a * b, 3: check_int(a, b)}
    return operation.get(op)


def main(number_of_questions=5):
    correct = 0  # Couter of correct answers
    elapsed_time = 0  # elapsed time couter
    print(
        f"Solve {number_of_questions} examples. Use . in decimal numbers, "
        f"round to two decimal places."
    )

    for _ in range(number_of_questions):

        a, b, op = generate_equation()

        if b < 0:
            b_string = (
                "(" + str(b) + ")"
            )  # it is a convension to display a negative number in brackets e.g. 4+(-3)
        else:
            b_string = b  # no need for brackets in case of a positive number

        print(a, end="")
        print(OPERATIONS[op], end="")
        print(b_string)

        start = time.time()  # start counting the user response time
        answer = ask_for_answer()
        end = time.time()  # stop counting the user response time
        elapsed_time += end - start  # update elapsed time counter

        if answer == str(calculate_equation(op, a, b)):
            correct += 1  # if the user input is a correct solution, counter of correct answers is increased

    print()
    print("Correct answers ", end="")
    print(correct, end="")
    print(f"/{number_of_questions}. Success rate ", end="")
    print(
        int(correct / number_of_questions * 100), end=""
    )  # print relative success rate
    print("%.")
    print("Average response time: ", end="")
    print(
        round(elapsed_time / number_of_questions, 2), end=""
    )  # print average elapsed time rounded to two decimal places
    print(" seconds.")
