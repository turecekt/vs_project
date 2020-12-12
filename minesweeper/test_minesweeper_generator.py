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


class TestCheckNeighboursOfCell(TestCase):
    def setUp(self) -> None:
        self.minesweeper = minesweeper_generator.Minesweeper(3, 3, 6)
        self.minesweeper.playground = [['#', '#', '#', '#', '#'],
                                       ['#', '*', ' ', '*', '#'],
                                       ['#', ' ', '*', '*', '#'],
                                       ['#', '*', '*', ' ', '#'],
                                       ['#', '#', '#', '#', '#']]

    def test_check_neighbours_of_cell_1(self):
        number_of_neighbours = minesweeper_generator\
                .check_neighbours_of_cell(self.minesweeper, 1, 2, 0)
        self.assertEqual(number_of_neighbours, 4)

    def test_check_neighbours_of_cell_2(self):
        number_of_neighbours = minesweeper_generator\
            .check_neighbours_of_cell(self.minesweeper, 3, 3, 0)
        self.assertEqual(number_of_neighbours, 3)


class TestPutNumbersToPlayground(TestCase):
    def test_put_numbers_to_playground(self):
        minesweeper = minesweeper_generator.Minesweeper(5, 5, 6)
        expected_minesweeper = [['#', '#', '#', '#', '#', '#', '#'],
                                ['#', '*', 2, 1, 1, 1, '#'],
                                ['#', '*', 2, 1, '*', 1, '#'],
                                ['#', 1, 1, 2, 3, 3, '#'],
                                ['#', 1, 1, 1, '*', '*', '#'],
                                ['#', '*', 1, 1, 2, 2, '#'],
                                ['#', '#', '#', '#', '#', '#', '#']]
        minesweeper.playground = [['#', '#', '#', '#', '#', '#', '#'],
                                  ['#', '*', ' ', ' ', ' ', ' ', '#'],
                                  ['#', '*', ' ', ' ', '*', ' ', '#'],
                                  ['#', ' ', ' ', ' ', ' ', ' ', '#'],
                                  ['#', ' ', ' ', ' ', '*', '*', '#'],
                                  ['#', '*', ' ', ' ', ' ', ' ', '#'],
                                  ['#', '#', '#', '#', '#', '#', '#']]
        minesweeper_generator.put_numbers_to_playground(minesweeper)
        self.assertEqual(minesweeper.playground, expected_minesweeper)


class TestLoadRows(TestCase):
    def test_load_rows_from_input(self):
        with patch('builtins.input', return_value='2'):
            self.assertEqual(minesweeper_generator.load_rows_from_input(), 2)


class TestLoadCols(TestCase):
    def test_load_cols_from_input(self):
        with patch('builtins.input', return_value='5'):
            self.assertEqual(minesweeper_generator.load_cols_from_input(), 5)


class TestLoadCountOfMines(TestCase):
    def test_load_count_of_mines(self):
        with patch('builtins.input', return_value='5'):
            self.assertEqual(minesweeper_generator.load_count_of_mines(), 5)


class TestLoadDataFromInput(TestCase):
    def test_load_data_from_input(self):
        inputs_in_order = ['5', '5', '5']
        minesweeper = minesweeper_generator.Minesweeper(5, 5, 5)
        with patch('builtins.input', side_effect=inputs_in_order):
            result = minesweeper_generator.load_data_from_input()
            self.assertEqual(result.rows, minesweeper.rows)
            self.assertEqual(result.cols, minesweeper.cols)
            self.assertEqual(result.count_of_mines, minesweeper.count_of_mines)


class TestPrintPlayground(TestCase):
    def test_print_playground(self):
        minesweeper = minesweeper_generator.Minesweeper(5, 5, 6)
        minesweeper.playground = [['#', '#', '#', '#', '#', '#', '#'],
                                  ['#', '*', 2, 1, 1, 1, '#'],
                                  ['#', '*', 2, 1, '*', 1, '#'],
                                  ['#', 1, 1, 2, 3, 3, '#'],
                                  ['#', 1, 1, 1, '*', '*', '#'],
                                  ['#', '*', 1, 1, 2, 2, '#'],
                                  ['#', '#', '#', '#', '#', '#', '#']]
        with patch('builtins.print') as fake_stdout:
            minesweeper_generator.print_playground(minesweeper)

            fake_stdout.assert_has_calls([call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call('*', end=' '),
                                         call(2, end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call('*', end=' '),
                                         call(2, end=' '),
                                         call(1, end=' '),
                                         call('*', end=' '),
                                         call(1, end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call(2, end=' '),
                                         call(3, end=' '),
                                         call(3, end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call('*', end=' '),
                                         call('*', end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call('*', end=' '),
                                         call(1, end=' '),
                                         call(1, end=' '),
                                         call(2, end=' '),
                                         call(2, end=' '),
                                         call('#', end=' '),
                                         call(),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call('#', end=' '),
                                         call()])
