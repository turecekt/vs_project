"""Function that converts decimal number to octal number."""


def convert(input_number):
    """Convert decimal number to octal."""
    text = ""
    k = []

    while input_number > 0:
        # calc
        a = int(input_number % 8)

        # a add to array
        k.append(a)

        # calc
        input_number = (input_number - a) / 8

        # load array
        text = ""

    # turn the array
    for j in k[::-1]:
        text = text + str(j)

    return text
