class Number:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def valid_input(x, y):
    try:
        int(x)
        int(y)
        return True
    except ValueError:
        return "Napište hodnoty ve správném formátu!"


if __name__ == '__main__':
    A = input("zadejte souřadnice bodu A: ").split(",")
    valid_input(A[0], A[1])
    B = input("zadejte souřadnice bodu B: ").split(",")
    C = input("zadejte souřadnice bodu C: ").split(",")
