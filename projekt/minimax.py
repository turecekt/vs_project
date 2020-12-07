import sys

pole = []
for x in sys.argv:
    try:
        TryParse = int(x)
        pole.append(TryParse)
    except ValueError:
        sys.exit("Všechny vstupy musí být typu int!")