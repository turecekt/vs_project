"""Test modules in library."""


from library import inicializer, printer, bubble_sort, \
                    insertion_sort, quick_sort, choose_sorting_method
import sys
import io


def test_inicializer():
    """Test iniciliazer of array."""
    assert len(inicializer(1)) == 20
    sys.argv[0] = 'minimax'
    if len(sys.argv) == 2:
        sys.argv[1] = 'test_text.txt'
        assert len(inicializer(2)) == 9
    elif len(sys.argv) == 1:
        sys.argv.append('test_text.txt')
        assert len(inicializer(2)) == 9
    if len(sys.argv) == 2:
        sys.argv.pop()
        for i in range(1, 10):
            sys.argv.append(f'{i}')
        assert len(inicializer(3)) == 9
        assert inicializer(3) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort():
    """Test bubble sort functionality."""
    assert bubble_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert bubble_sort([0]) == [0]
    assert bubble_sort([0, -1]) == [-1, 0]


def test_insertion_sort():
    """Test insertion sort functionality."""
    assert insertion_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert insertion_sort([0]) == [0]
    assert insertion_sort([0, -1]) == [-1, 0]


def test_quick_sort():
    """Test quick sort \
    functionality."""
    assert quick_sort([15, 9, -8, 0, 12, 5, -8, 1]) \
           == [-8, -8, 0, 1, 5, 9, 12, 15]
    assert quick_sort([0]) == [0]
    assert quick_sort([0, -1]) == [-1, 0]


def test_printer():
    """Test printer output."""
    printer_output = io.StringIO()
    sys.stdout = printer_output
    printer([-8, -8, 0, 1, 5, 9, 12, 15])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('Min: -8') != -1
    assert string.find('Max: 15') != -1
    assert string.find('[-8, -8, 0, 1, 5, 9, 12, 15]') != -1


def test_choose_sorting_method():
    """Test choice-maker for sorting systems."""
    printer_output = io.StringIO()
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 1)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 2)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1
    sys.stdout = printer_output
    choose_sorting_method([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
    printer([9, 8, 7, 6, 5, 4, 3, 2, 1])
    sys.stdout = sys.__stdout__
    string = printer_output.getvalue()
    assert string.find('[9, 8, 7, 6, 5, 4, 3, 2, 1]') != -1


test_inicializer()
test_bubble_sort()
test_insertion_sort()
test_quick_sort()
test_printer()
test_choose_sorting_method()
