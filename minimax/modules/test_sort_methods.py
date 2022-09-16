"""Unit testing for sorting algorithms."""


import sort_methods


testVector = [1, 2, 3, 4, -10, -11, 22, 0, 16, -4]


def test_bubblesort__testVectorGiven__expectSortedArray():
    """Unit test will do test for bubblesort method."""
    v = sort_methods.bubble_sort(testVector)
    assert v == sorted(testVector)


def test_insertionsort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for insertionsort method."""
    v = sort_methods.insertion_sort(testVector)
    assert v == sorted(testVector)


def test_mergesort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for mergesort method."""
    v = sort_methods.merge_sort(testVector)
    assert v == sorted(v)


def test_quicksort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for quicksort method."""
    v = sort_methods.quick_sort(testVector)
    assert v == sorted(testVector)
