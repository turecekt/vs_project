import operator
import random
import sys
import time

from typing import Callable, Iterable, List, Optional, Tuple, TypeVar


T = TypeVar("T")

NUMBER_OF_EXAMPLES = 5
KNOWN_OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
RAND_RANGE = (-10, 10)


def interact_with_user(
    q: str,
    type_converter: Callable[[str], T],
    exp_answer_to_continue: Optional[Iterable[str]] = None,
    exp_answer_to_quit: Optional[Iterable[str]] = None,
    number_of_trials: int = 3,
    unvalidated_answer: str = None,
) -> T:
    """Utility function to get a value from user.

    q is a question and will be prompted to the user.
    type_converter is a single arg function to convert the q str into needed type.
    You can define expected answers to define what are correct answers to convert
        and return a value.
    It is also possible to provide answers for quiting the application. In this
    case a sys.exit(0) will be called.
    number_of_trials defines the number of times the script will try to get proper
        answer from user. sys.exit(1) if not success.
    """
    if number_of_trials <= 0:
        print_to_stdout("Bad input. Exiting.")
        sys.exit(1)
    print_to_stdout(q)
    unvalidated_answer = unvalidated_answer or input()
    if exp_answer_to_quit and unvalidated_answer in exp_answer_to_quit:
        print_to_stdout("Exiting...")
        sys.exit(0)
    try:
        if (
            exp_answer_to_continue
            and unvalidated_answer not in exp_answer_to_continue
        ):
            raise ValueError()
        answer = type_converter(unvalidated_answer)
    except (ValueError, TypeError):
        print_to_stdout("Bad input. Try one more time...\n")
        return interact_with_user(
            q,
            type_converter,
            exp_answer_to_continue,
            exp_answer_to_quit,
            number_of_trials - 1,
        )
    else:
        return answer


def generate_question() -> str:
    """Generate an equation string, i.e. 1 + 1."""
    num_1, num_2 = (
        random.randint(*RAND_RANGE),  # nosec
        random.randint(*RAND_RANGE),  # nosec
    )
    op = random.choice(tuple(KNOWN_OPERATIONS))  # nosec
    if num_2 == 0 and op == "/":
        return generate_question()
    return f"{num_1} {op} {num_2}"


def evaluate_answer(q: str, answer: float) -> Tuple[bool, float]:
    """Evaluates an answer to the question.

    Question should have the following form: 1 + 1.
    Available operators defined in KNOWN_OPERATIONS.
    """
    try:
        num_1, operation, num_2 = q.split()
        expected_result = KNOWN_OPERATIONS[operation](
            float(num_1), float(num_2)
        )
    except (ValueError, KeyError, AttributeError) as err:
        raise ValueError(
            f"Question {q} is bad. It should be a form of `1 + 1`. "
            f"Known operations are {', '.join(KNOWN_OPERATIONS)}"
        ) from err
    return answer == expected_result, expected_result


def print_to_stdout(s: str) -> None:
    """Print a message to stdout."""
    print(s, file=sys.stdout)


def ask_a_question() -> bool:
    """Ask a single question, i.e. 1 + 1, and evaluates the answer.

    A question is generated with generate_question.
    """
    q = generate_question()
    correct, proper_res = evaluate_answer(
        q,
        interact_with_user(
            f"Solve equation: {q}. Your answer is: ",
            type_converter=float,
        ),
    )
    if not correct:
        print_to_stdout(f"Wrong. Correct result is {proper_res}")
        return False
    else:
        print_to_stdout("Good job!")
        return True


def evaluate_results(
    results: List[bool], time_spent: float
) -> Tuple[float, float]:
    """Evaluates the series of results.

    Returns success rate and total time spent on a series of tasks.
    """
    try:
        success_rate = sum(results) / len(results)
        time_spent = round(time_spent, 0)
    except (ZeroDivisionError, TypeError) as err:
        raise ValueError(
            f"Expecting results as [True, False...], received {results}.\n"
            f"Expecting time_spent as 15s, received {time_spent}"
        ) from err
    return success_rate, time_spent


def main() -> None:
    interact_with_user(
        f"Solve {NUMBER_OF_EXAMPLES} examples. Your results will be measured.\n"
        f"Do you want to continue? (yes/no)",
        type_converter=bool,
        exp_answer_to_continue=("Yes", "yes"),
        exp_answer_to_quit=("No", "no"),
    )
    start = time.monotonic()
    results = [ask_a_question() for _ in range(NUMBER_OF_EXAMPLES)]
    success_rate, time_spent = evaluate_results(
        results, time.monotonic() - start
    )
    print_to_stdout(f"Success rate is: {success_rate}")
    print_to_stdout(
        f"For {NUMBER_OF_EXAMPLES} tasks you've spent {time_spent} sec."
    )
