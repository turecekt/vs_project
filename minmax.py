#! /usr/bin/python
import sys
import os
import random


def get_input():
    ret_val = []
    for string in sys.argv[1:]:
        if os.path.isfile(string):
            with open(string, 'r') as file:
                for line in file:
                    for word in line.split():
                        ret_val.append(int(word))
        else:
            ret_val.append(int(string))
    return ret_val


def get_random_input():
    return [random.randint(-9000, 9000) for x in range(0, 20)]


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == '__main__':
    if len(sys.argv) > 1:
       y = get_input()
    else:
        y = get_random_input()
    sort_dict={"bubble":bubbleSort,"cocktail":cocktailSort,"insertion":insertionSort}
    print("minimum: {}".format(min(y)))
    print("maximum: {}".format(max(y)))

    sort_str = input("{}\nzvolte jeden radici algoritmus:".format([x for x in sort_dict]))
    sort_dict[sort_str](y)
    print(y)