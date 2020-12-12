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

# funkce pro razeni, Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        # Initially, assume the first element of the unsorted part as the minimum.
        minimum = i
        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                # Update position of minimum element if a smaller element is found.
                minimum = j
        # Swap the minimum element with the first element of the unsorted part.     
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array

# temporary variables and prints for testing purposes
array = createRandomArray()
print("Random array: ", array)    
min_value = findMinValue(array)
print("Minimal value of array: ", min_value)
max_value = findMaxValue(array)
print("Maximal value of array: ", max_value)
min_index = findMinIndex(array)
print("Index of min_value is: ", min_index)
max_index = findMaxIndex(array)
print("Index of max_value is: ", max_index)
selectionSort(array)
print("Array after Selection Sort: ", array)