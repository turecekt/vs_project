import sys
import os.path
from os import path
import random

pole = []
if len(sys.argv) > 1:
    sys.argv.pop(0)
    if(path.exists(sys.argv[0])):
        file = open(sys.argv[0], "r")
        words = file.read().splitlines()
        file.close()
        data = []
        for x in words:
            data = x.split()
            for k in data:
                try:
                    TryParse = int(k)
                    pole.append(TryParse)
                except ValueError:
                    sys.exit("Všechny vstupy musí být typu int!")
    else:
        for x in sys.argv:
            try:
                TryParse = int(x)
                pole.append(TryParse)
            except ValueError:
                sys.exit("Všechny vstupy musí být typu int!")
else:
    pole = [random.randint(1,100) for _ in range(10)]

print(pole)
