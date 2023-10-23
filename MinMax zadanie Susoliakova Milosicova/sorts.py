"""Funkcie, ktore su na jednotlive zoradenie sortov. \
    Zdroj algoritmov: https://stackabuse.com/."""


def buble_sort(numbers):
    """Funkcia pre buble sort."""
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(numbers) - num_of_iterations - 1):
            if numbers[i] > numbers[i+1]:
                # Swap
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                has_swapped = True
        num_of_iterations += 1


def merge_sort(array, left_index, right_index):
    """Funkcia pre merge sort."""
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def insertion_sort(numbers):
    """Funkcia pre insertion sort."""
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(numbers)):
        currentValue = numbers[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and\
                numbers[currentPosition - 1] > currentValue:
            numbers[currentPosition] = numbers[currentPosition - 1]
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        numbers[currentPosition] = currentValue


def quick_sort(array, start, end):
    """Funkcia pre quick sort."""
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def partition(array, start, end):
    """Pmocna funkcia pre quick sort."""
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the
        # low pointer, since that
        # indicates we have already moved all the elements to their
        # correct side of the pivot

        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def merge(array, left_index, right_index, middle):
    """Pomocna funkcia pre merge sort."""
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and \
            right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
