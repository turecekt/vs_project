from minesweeper import minesweeper_generator
from unittest import TestCase
from unittest.mock import patch, call


class TestCheckInput(TestCase):
    def test_check_input_non_numeric_input(self):
        self.assertFalse(minesweeper_generator.check_input("jrif"))

    def test_check_input_negative_value(self):
        self.assertFalse(minesweeper_generator.check_input('-2'))

    def test_check_input_float_number(self):
        self.assertFalse(minesweeper_generator.check_input("10.2"))


class TestCreateArrayWithMines(TestCase):
    def test_create_array_with_mines(self):
        bombs_array = minesweeper_generator.create_array_with_mines(10, 10, 5)
        count_of_mines = 0
        for i in range(0, 10):
            for j in range(0, 10):
                if bombs_array[i][j] == "*":
                    count_of_mines += 1
        self.assertEqual(count_of_mines, 5)


class TestPutMinesToPlayground(TestCase):
    def test_put_mines_to_playground(self):
        minesweeper = minesweeper_generator.Minesweeper(5, 5, 0)
        minesweeper_generator.put_mines_to_playground(minesweeper)
        expected_array = [['#', '#', '#', '#', '#', '#', '#'],
                          ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['#', '#', '#', '#', '#', '#', '#']]
        self.assertListEqual(minesweeper.playground, expected_array)