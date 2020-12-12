import main
import unittest.mock as mock
from point import Point

def test_print_triangle_info():
    point_a = Point(5, 10)
    point_b = Point(10, 20)
    point_c = Point(50, -10)
    main.print_triangle_info(point_a, point_b, point_c)

class InputGenerator:
    def __init__(self):
        self.iterator = 0

    def get_input(self):
        self.iterator = self.iterator + 1;
        if self.iterator == 1:
            return "0"
        if self.iterator == 2:
            return "0 abc"
        else:
           return "0 100"

def test_request_point():
    generator = InputGenerator()
    with mock.patch("builtins.input", wraps=generator.get_input):
        with mock.patch.object(main.sys, 'argv', ["main"]):
            point = main.request_point("A")
            assert point.x == 0

def test_init():
    i = 10
    with mock.patch.object(main, "__name__", "__main__"):
        with mock.patch.object(main.sys, 'exit') as mock_exit:
            with mock.patch.object(main, 'print_triangle_info'):
                with mock.patch("main.request_point", return_value=Point(50, 50)):
                    with mock.patch.object(main.sys, 'argv', ["main", 0, 0, 100, 0, 0, 100]):
                        main.init()
                        assert mock_exit.call_args[0][0] == 0
                        
                    with mock.patch.object(main.sys, 'argv', ["main", 0, 0, "abc", 0, 0, 100]):
                        main.init()
                        assert mock_exit.call_args[0][0] != 0

                    with mock.patch.object(main.sys, 'argv', ["main", 0, 0]):
                        main.init()
                        assert mock_exit.call_args[0][0] != 0

                    with mock.patch.object(main.sys, 'argv', ["main"]):
                        main.init()
                        assert mock_exit.call_args[0][0] == 0
