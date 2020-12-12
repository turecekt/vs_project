""" Project minesweeper generator. """

import numpy

EMPTY = " "
""" Global constant for empty field in the playground. """
MINE = "*"
""" Global constant for mine in the playground. """


class Minesweeper:
    """class which represents minesweeper structure"""
    def __init__(self, rows, cols, count_of_mines):
        """count of rows of the playground, +2 means # for each side of the playground"""
        self.rows = rows + 2
        # count of cols of the playground, +2 means # for each side of the playground
        self.cols = cols + 2
        # count of mines which should be in the playground
        self.count_of_mines = count_of_mines
        # playground which is full of #
        self.playground = [["#"] * self.cols for row in range(self.rows)]
        # full playground with EMPTY constant, from 1 to rows/cols - 1, which means borders of the playground
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                self.playground[i][j] = EMPTY


def create_array_with_mines(rows, cols, count_of_mines):
    """
        input:  rows
                cols
                count of mines
        output: array with bombs on random indices
        * represents mine
    """
    array = []
    array_len = rows * cols
    for i in range(0, array_len):
        if count_of_mines == 0:
            array.append(EMPTY)
        else:
            array.append(MINE)
            count_of_mines -= 1
    numpy.random.shuffle(array)
    bombs_array = numpy.reshape(array, (rows, cols))
    return bombs_array


def put_mines_to_playground(minesweeper):
    """
        input:  minesweeper
                count of mines
        output: nothing, this function randomly put mines to the playground
        * represents mine
    """
    bombs_array = create_array_with_mines(minesweeper.rows - 2, minesweeper.cols - 2, minesweeper.count_of_mines)

    for i in range(1, minesweeper.rows - 1):
        for j in range(1, minesweeper.cols - 1):
            bombs_array_i = i - 1
            bombs_array_j = j - 1
            minesweeper.playground[i][j] = bombs_array[bombs_array_i][bombs_array_j]


def check_neighbours_of_cell(minesweeper, index_of_row, index_of_col, number_of_near_mines):
    """
        input:  minesweeper
                index_of_row is current index of row
                index_of_col is current index of column
                number_of_near_mines is count of mines that the cell touches
        output: number of near mines of the cell
    """
    for i in range(-1, 2):
        for j in range(-1, 2):
            if minesweeper.playground[index_of_row + i][index_of_col + j] == MINE:
                # increase number_of_near_mines if the cell touches mine
                number_of_near_mines += 1
    return number_of_near_mines


def put_numbers_to_playground(minesweeper):
    """
        input:  minesweeper
        output: nothing, this function put numbers that represent the number of mines that this cell touches
    """
    # from 1 to rows/columns - 1 because we do not want to change borders from #
    for i in range(1, minesweeper.rows - 1):
        for j in range(1, minesweeper.cols - 1):
            # cell does not include mine
            if minesweeper.playground[i][j] == EMPTY:
                number_of_near_mines = check_neighbours_of_cell(minesweeper, i, j, 0)
                # if number of near mines is not 0, put the number to the playground, we do not want to have 0
                if number_of_near_mines != 0:
                    minesweeper.playground[i][j] = number_of_near_mines


def print_playground(minesweeper):
    """
        input:  minesweeper
        output: printed playground
    """
    for i in range(minesweeper.rows):
        for j in range(minesweeper.cols):
            print(minesweeper.playground[i][j], end=" ")
        print()


def check_input(input_for_check):
    """
        input:  input
        output: True if input is correct else False
    """
    if not input_for_check.isnumeric():
        return False

    input_for_check = int(input_for_check)

    if input_for_check <= 0:
        return False
    return True


def load_rows_from_input():
    """
        input:  nothing
        output: number of rows if input is correct
    """
    rows = input("Enter number of rows: ")
    if not check_input(rows):
        print("Incorrect input, please try again.")
        return load_rows_from_input()
    else:
        return int(rows)


def load_cols_from_input():
    """
        input:  nothing
        output: number of columns if input is correct
    """
    cols = input("Enter number of cols: ")
    if not check_input(cols):
        print("Incorrect input, please try again.")
        return load_cols_from_input()
    else:
        return int(cols)


def load_count_of_mines():
    """
        input:  nothing
        output: number of mines if input is correct
    """
    count_of_mines = input("Enter number of mines: ")
    if not check_input(count_of_mines):
        print("Incorrect input, please try again.")
        return load_count_of_mines()
    else:
        return int(count_of_mines)


def load_data_from_input():
    """
        input:  nothing
        output: nothing
        Main function which calls every function
    """
    rows = load_rows_from_input()
    cols = load_cols_from_input()
    count_of_mines = load_count_of_mines()
    if (rows * cols) < count_of_mines:
        count_of_mines_invalid_input = True
        while count_of_mines_invalid_input:
            count_of_mines = load_count_of_mines()
            count_of_mines_invalid_input = (rows * cols) < count_of_mines

    minesweeper = Minesweeper(rows, cols, count_of_mines)
    return minesweeper


def main():
    minesweeper = load_data_from_input()
    put_mines_to_playground(minesweeper)
    put_numbers_to_playground(minesweeper)
    print_playground(minesweeper)


# main()
