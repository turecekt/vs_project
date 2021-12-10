import sys
from random import randint


def min_max(numbers):
    """Funkce na zjisteni nejmensiho a nejvetsiho cisla a jeho indexu."""
    min_n = f"Min number:{min(numbers)}, Index:{numbers.index(min(numbers))}"
    max_n = f"Max number:{max(numbers)}, Index:{numbers.index(max(numbers))}"

    return f"{min_n}\n{max_n}"