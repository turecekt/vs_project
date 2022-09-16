"""Module will do number extractions.
Either from given file, from commandline interface or generated.
"""


from random import randrange


def ExtractNumbersFromFile(pathToFile: str):
    lines = None
    numbers = []
    with open(pathToFile) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace(' ', '').split(',')
            [numbers.append(int(charL)) for charL in line if charL != '']

    return numbers


def ExtractNumbersFromCLI(cliArg: str):
    """Extract numbers from CLI.
    Values are in quotes, comma separated, including negative values.
    Returns list of those values as integers.
    """
    ants = cliArg.split(',')
    ints = []
    for ant in ants:
        try:
            ints.append(int(ant))
        except ValueError as e:
            print(f"Exception: {e}")
            raise
    return ints


def GenerateRandomVectorLength20():
    lst = []
    for _ in range(20):
        lst.append(randrange(-100, 100))
    return lst
