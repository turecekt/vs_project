"""Utesty."""
from minmax import get_input
from minmax import bubbleSort
from minmax import cocktailSort
from minmax import insertionSort
from minmax import handle_file
import sys
import pytest


try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


def test_input_1():
    """Test."""
    testargs = ["minmax.py", "4", "5", "1"]
    with patch.object(sys, 'argv', testargs):
        setup = get_input()
        assert setup == [4, 5, 1]


def test_input_2():
    """Test."""
    testargs = ["minmax.py", ""]
    with patch.object(sys, 'argv', testargs):
        with pytest.raises(SystemExit) as e:
            get_input()
            assert e.type == SystemExit
            assert e.value.code == -1


def test_input_3():
    """Test."""
    testargs = ["minmax.py", "4 5 6 7"]
    with patch.object(sys, 'argv', testargs):
        setup = get_input()
        assert setup == [4, 5, 6, 7]


def test_input_4():
    """Test."""
    testargs = ["minmax.py", "test4.txt"]
    with patch.object(sys, 'argv', testargs):
        setup = get_input()
        assert setup == [1, 2, 3]


def test_input_5():
    """Test."""
    testargs = ["minmax.py", "test5.txt"]
    with patch.object(sys, 'argv', testargs):
        setup = get_input()
        assert setup == [1, 2, 3]


def test_bubbleSort_1():
    """Test."""
    arr = [4, 8, 31, -1, 0]
    bubbleSort(arr)
    assert arr == [-1, 0, 4, 8, 31]


def test_bubbleSort_2():
    """Test."""
    arr = []
    bubbleSort(arr)
    assert arr == []


def test_bubbleSort_3():
    """Test."""
    arr = [1, 2, 3]
    bubbleSort(arr)
    assert arr == [1, 2, 3]


def test_bubbleSort_4():
    """Test."""
    arr = [3, 2, 1]
    bubbleSort(arr)
    assert arr == [1, 2, 3]


def test_bubbleSort_5():
    """Test."""
    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    bubbleSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 1, 1]


def test_bubbleSort_6():
    """Test."""
    arr = [1, 1, 1, 3, 1, 5, 1, 1]
    bubbleSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 3, 5]


def test_bubbleSort_7():
    """Test."""
    arr = [1, 2, 2, 4]
    bubbleSort(arr)
    assert arr == [1, 2, 2, 4]


def test_bubbleSort_8():
    """Test."""
    arr = [4, 2, 2, 1]
    bubbleSort(arr)
    assert arr == [1, 2, 2, 4]


def test_cocktailSort_1():
    """Test."""
    arr = [4, 8, 31, -1, 0]
    cocktailSort(arr)
    assert arr == [-1, 0, 4, 8, 31]


def test_cocktailSort_2():
    """Test."""
    arr = []
    cocktailSort(arr)
    assert arr == []


def test_cocktailSort_3():
    """Test."""
    arr = [1, 2, 3]
    cocktailSort(arr)
    assert arr == [1, 2, 3]


def test_cocktailSort_4():
    """Test."""
    arr = [3, 2, 1]
    cocktailSort(arr)
    assert arr == [1, 2, 3]


def test_cocktailSort_5():
    """Test."""
    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    cocktailSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 1, 1]


def test_cocktailSort_6():
    """Test."""
    arr = [1, 1, 1, 3, 1, 5, 1, 1]
    cocktailSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 3, 5]


def test_cocktailSort_7():
    """Test."""
    arr = [1, 2, 2, 4]
    cocktailSort(arr)
    assert arr == [1, 2, 2, 4]


def test_cocktailSort_8():
    """Test."""
    arr = [4, 2, 2, 1]
    cocktailSort(arr)
    assert arr == [1, 2, 2, 4]


def test_insertionSort_1():
    """Test."""
    arr = [4, 8, 31, -1, 0]
    insertionSort(arr)
    assert arr == [-1, 0, 4, 8, 31]


def test_insertionSort_2():
    """Test."""
    arr = []
    insertionSort(arr)
    assert arr == []


def test_insertionSort_3():
    """Test."""
    arr = [1, 2, 3]
    insertionSort(arr)
    assert arr == [1, 2, 3]


def test_insertionSort_4():
    """Test."""
    arr = [3, 2, 1]
    insertionSort(arr)
    assert arr == [1, 2, 3]


def test_insertionSort_5():
    """Test."""
    arr = [1, 1, 1, 1, 1, 1, 1, 1]
    insertionSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 1, 1]


def test_insertionSort_6():
    """Test."""
    arr = [1, 1, 1, 3, 1, 5, 1, 1]
    insertionSort(arr)
    assert arr == [1, 1, 1, 1, 1, 1, 3, 5]


def test_insertionSort_7():
    """Test."""
    arr = [1, 2, 2, 4]
    insertionSort(arr)
    assert arr == [1, 2, 2, 4]


def test_insertionSort_8():
    """Test."""
    arr = [4, 2, 2, 1]
    insertionSort(arr)
    assert arr == [1, 2, 2, 4]


def test_handle_file_1():
    """Test."""
    arr = []
    with open("test4.txt", 'r') as file:
        handle_file(arr, file)
    assert arr == [1, 2, 3]


def test_handle_file_2():
    """Test."""
    arr = []
    with open("test5.txt", 'r') as file:
        handle_file(arr, file)
    assert arr == [1, 2, 3]


def test_hadle_args_1():
    """Test."""
    arr = []
    with open("test4.txt", 'r') as file:
        handle_file(arr, file)
    assert arr == [1, 2, 3]


def test_hadle_args_2():
    """Test."""
    arr = []
    with open("test5.txt", 'r') as file:
        handle_file(arr, file)
    assert arr == [1, 2, 3]
