import sys

pole = []
sys.argv.pop(0)
for x in sys.argv:
    try:
        TryParse = int(x)
        pole.append(TryParse)
    except ValueError:
        sys.exit("Všechny vstupy musí být typu int!")