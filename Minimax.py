"""
Created on Sun Dec 13 13:31:54 2020

@author: Martin Danielčík
"""

# importuji funkci randint z modulu random
from random import randint
import sys

pole = [] 
  
# number of elemetns as input 

if len(sys.argv) > 1:
# iterating till the range 
    for i in range(1, len(sys.argv)): 
        pole.append(sys.argv[i])
    print ("Pole s vámi zadanými hodnotami:")
    print(pole) 
else:
    for i in range(0, 20): 
        pole.append(randint(1, 30))
    print ("Pole s 20 pseudonáhodně vygenerovanými prvky mezi čísly 1 a 30:")
    print(pole)
input("Press Enter to end...")
      
