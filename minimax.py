import random

# funkce pro vytvoreni nahodneho pole 20ti cisel v rozsahu -100 : 100
def createRandomArray():
   
    random_array = random.sample(range(-100,100), 20)

    return random_array

def findMinValue(array):
    
    min_value = min(array)

    return min_value

array = createRandomArray()
min_value = findMinValue(array)

# print for testing purposes
print("Random array: ", array)    
print("Minimal value of array: ", min_value)