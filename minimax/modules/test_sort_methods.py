"""Unit testing for sorting algorithms."""


import sort_methods


testVector = [1, 2, 3, 4, -10, -11, 22, 0, 16, -4]


def test_bubblesort__testVectorGiven__expectSortedArray():
    """Unit test will do test for bubblesort method.

    Result is sorted array.
    """
    v = sort_methods.bubble_sort(testVector)
    assert v == sorted(testVector)


def test_insertionsort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for insertionsort method.

    Result is sorted array.
    """
    v = sort_methods.insertion_sort(testVector)
    assert v == sorted(testVector)


def test_merge__leftHalfEmpty__expectsRightHalf():
    """Unit test will do test for merging arrays.

    Result is two arrays merged into one.
    """
    left = []
    right = [1, 3, 5]
    result = sort_methods._merge(left, right)
    assert result == right


def test_merge__rightHalfEmpty__expectsLeftHalf():
    """Unit test will do test for merging arrays.

    Result is two arrays merged into one.
    """
    left = [1, 3, 5]
    right = []
    result = sort_methods._merge(left, right)
    assert result == left


def test_merge__inbetweenerGiven__expectsSomeBehaviour():
    """Unit test will do test for merging arrays.

    Result is two arrays merged into one.
    """
    left = [1, 3, 5]
    right = [7, 9, 11]
    result = sort_methods._merge(left, right)
    assert result == left + right


def test_mergesort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for mergesort method.

    Result is sorted array.
    """
    v = sort_methods.merge_sort(testVector)
    assert v == sorted(v)


def test_quicksort__testVectorGiven__expectsSortedArray():
    """Unit test will do test for quicksort method.

    Result is sorted array.
    """
    v = sort_methods.quick_sort(testVector)
    assert v == sorted(testVector)
