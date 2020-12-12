"""MiniMax AP1VS

Zaverecny projekt v Pythonu - Adam Karas
"""
import random
import time


def createRandomArray():
    """Create an array of random integers.

    Values of an array are between -100 and 100
    Number of array elements = 20

    Returns:
        - array - an unsorted array of random integers
    """
    random_array = random.sample(range(-100, 100), 20)
    return random_array


def findMinValue(array):
    """Find a min value of array.

    Returns:
        - min_value - minimal value of array
    """
    min_value = min(array)
    return min_value


def findMaxValue(array):
    """Find a max value of array.

    Returns:
        - max_value - maximal value of array
    """
    max_value = max(array)
    return max_value


def findMinIndex(array):
    """Find an index of min value in array.

    Returns:
        - min_index - position of minimal value in array.
    """
    min_index = array.index(min_value)
    return min_index


def findMaxIndex(array):
    """Find an index of max value in array.

    Returns:
        - max_index - position of maximal value in array.
    """
    max_index = array.index(max_value)
    return max_index


def selectionSort(array):
    """Sorting algorithm: Selection Sort"""
    n = len(array)
    for i in range(n):
        #Initially, assume the first element 
        #of the unsorted part as the minimum.
        minimum = i

        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                #Update position of minimum element 
                #if a smaller element is found.
                minimum = j
        #Swap the minimum element with the first element of the unsorted part.     
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array


def bubbleSort(array):
    """Sorting algorithm: Bubble Sort"""
    n = len(array)
    #Traverse through all array elements 
    for i in range(n - 1):
        #range(n) also work but outer loop will 
        #repeat one time more than needed. 
        #Last i elements are already in place 
        for j in range(0, n - i - 1):
            #Traverse the array from 0 to n-i-1, 
            #swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insertionSort(array):
    """Sorting algorithm: Insertion Sort"""
    #traverse through 1 to len(array)
    for i in range(1, len(array)):
        key = array[i]
        #move elements of array [0..i-1], that are greater than key, 
        #to one position ahed of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#hlavni cast programu
print("*" * 50)
print("Generating 20 random numbers")
print("-" * 50)
#creating array via function
array = createRandomArray()
time.sleep(1)
print(array)
print("-" * 50)
print("Getting min/max data and their index")
print("-" * 50)
time.sleep(1)
#min value, min index
min_value = findMinValue(array)
print("Minimal value of array: ", min_value)
min_index = findMinIndex(array)
print("Index of min value is: ", min_index)
print("-" * 50)
time.sleep(1)
#max value, max index
max_value = findMaxValue(array)
print("Maximal value of array: ", max_value)
max_index = findMaxIndex(array)
print("Index of max value is: ", max_index)
print("-" * 50)
time.sleep(1)
#way of sorting data
sortingWay = int(input("Enter 1 for Selection Sort\nEnter 2 for Bubble Sort\n"
"Enter 3 for Insertion Sort\n"))
print("-" * 50)
time.sleep(1)

if sortingWay == 1:
    print("Selection Sort:")
    selectionSort(array)
    print(array)

elif sortingWay == 2:
    print("Bubble Sort:")   
    bubbleSort(array)
    print(array)

elif sortingWay == 3:
    print("Insertion Sort:")
    insertionSort(array)
    print(array)

else: 
    print("Wrong input!!")

print("*" * 50)
print("End of program.")
print("*" * 50)