"""Library working with arrays."""


import sys
from random import randint


def inicializer(option):
    """Inicializing array via random generator / text file / user input."""
    array = []
    if len(sys.argv) == 1 or option == 1:
        for i in range(20):
            array.append(randint(-100, 100))
    elif (len(sys.argv) == 2 and
          sys.argv[1].isdigit() is False) or option == 2:
        with open(sys.argv[1], 'rt') as f:
            my_list = list(f)
        try:
            for line in my_list:
                for word in line.split():
                    array.append(int(word))
        except ValueError as exception:
            print('String contained in the file must be digits!' + exception)
    elif (len(sys.argv) >= 2 and sys.argv[1].isdigit() is True) or option == 3:
        try:
            for i in range(1, len(sys.argv)):
                array.append(int(sys.argv[i]))
        except ValueError as exception:
            print('User input must be digits!' + exception)
    return array


def bubble_sort(array):
    """Sorts elements of array."""
    for cycles in range(len(array)):
        sorted = True
        for index in range(0, len(array) - cycles - 1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                sorted = False
        if sorted is True:
            break
    return array


def insertion_sort(array):
    """Sorts elements of array."""
    for index in range(1, len(array)):
        element = array[index]
        position = index - 1
        while position >= 0 and array[position] > element:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = element
    return array


def quick_sort(array):
    """Sorts elements of array."""
    if len(array) < 2:
        return array
    lower, same, higher = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for element in array:
        if element < pivot:
            lower.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            higher.append(element)
    return quick_sort(lower) + same + quick_sort(higher)


def printer(array):
    """Print min() & max() of sorted array."""
    print(f'\nMin: {min(array)} Max: {max(array)} \nArray: {array}')


def choose_sorting_method(array, choice=0):
    """UI to choose sorting system."""
    if choice == 0:
        while choice not in [1, 2, 3]:
            try:
                choice = int(input('1: Bubble sort. \
                                \n2: Insertion sort \
                                \n3: Quick sort.\n'))
            except ValueError as exception:
                print('User input must be digits!' + exception)
    if choice == 1:
        printer(bubble_sort(array))
    elif choice == 2:
        printer(insertion_sort(array))
    elif choice == 3:
        printer(quick_sort(array))
