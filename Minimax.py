"""
Created on Sun Dec 13 13:31:54 2020

@author: Martin Danielčík
"""

# importuji funkci randint z modulu random
from random import randint

pole = [] 
  
# number of elemetns as input 
n = int(input("Zadej počet hodnot v poli : ")) 

if n > 0:
# iterating till the range 
    for i in range(0, n): 
        s = f"Zadej {i+1}. hodnotu:"
        tmp = int(input(s)) 
        pole.append(tmp)
    print(pole) 
else:
    for i in range(0, 20): 
        pole.append(randint(1, 30))
    print ("Pole s 20 pseudonáhodně vygenerovanými prvky mezi čísly 1 a 30:")
    print(pole) 

