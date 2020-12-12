import random

# funkce pro vytvoreni nahodneho pole 20ti cisel v rozsahu -100 : 100
def createRandomArray():
   
    random_array = random.sample(range(-100,100), 20)

    return random_array

# funkce pro vyhledani minimalni hodnoty elementu v poli
def findMinValue(array):
    
    min_value = min(array)

    return min_value

# funkce pro vyhledalni maximalni hodnoty elementu v poli
def findMaxValue(array):
    
    max_value = max(array)

    return max_value

# funkce pro vyhledani indexu min_value
def findMinIndex(array):
     
     min_index = array.index(min_value)

     return min_index

# funkce pro vyhledani indexu max_value
def findMaxIndex(array):

    max_index = array.index(max_value)

    return max_index


# temporary variables for testing purposes
array = createRandomArray()
min_value = findMinValue(array)
max_value = findMaxValue(array)
min_index = findMinIndex(array)
max_index = findMaxIndex(array)

# print for testing purposes
print("Random array: ", array)    
print("Minimal value of array: ", min_value)
print("Maximal value of array: ", max_value)
print("Index of min_value is: ", min_index)
print("Index of max_value is: ", max_index)