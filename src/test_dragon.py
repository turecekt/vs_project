"""Include files."""
from dragon import move_left, move_right, \
                   generate_dragon, modify_pos, arg_decode  # , main
# import runpy as rp


def test_move_left():
    """Tests function move_left."""
    assert move_left([0], [0], 0, 0) == (0, 1)
    assert move_left([0], [0], 0, 1) == (-1, 0)
    assert move_left([0], [0], 0, 2) == (0, -1)
    assert move_left([0], [0], 0, 3) == (1, 0)


def test_move_right():
    """Tests function move_right."""
    assert move_right([0], [0], 0, 0) == (0, -1)
    assert move_right([0], [0], 0, 1) == (-1, 0)
    assert move_right([0], [0], 0, 2) == (0, 1)
    assert move_right([0], [0], 0, 3) == (1, 0)


def test_generate_dragon():
    """Tests function generate_dragon."""
    assert generate_dragon(0) == 'r'
    assert generate_dragon(1) == 'r'
    assert generate_dragon(2) == 'rrl'
    assert generate_dragon(3) == ('rrlrrll')
    assert generate_dragon(4) == ('rrlrrllrrrllrll')


def test_modify_pos():
    """Tests function for modified positions."""
    assert modify_pos([0, 0], [0, 0], 0, 0, 0, 2, ['l']) \
        == ([-1, -1], [0, 0], 1, 1, 0, ['l'])

    assert modify_pos([0, 0], [0, 0], 0, 0, 0, 2, ['r']) \
        == ([-1, -1], [0, 0], 1, 0, 1, ['r'])

    assert modify_pos([0, 0], [0, 0], 0, 0, 0, 2, ['l', 'l']) \
        == ([-1, -1], [0, 0], 1, 1, 0, ['l', 'l'])

    assert modify_pos([0, 0], [0, 0], 0, 0, 0, 2, ['r', 'r']) \
        == ([-1, -1], [0, 0], 1, 0, 1, ['r', 'r'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, 4, 0, 3, ['l', 'r']) \
        == ([0, 0, 0, 0], [0, -1, -1, 0], 2, 3, 0, ['l', 'r'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, -6, 0, 3, ['l', 'r']) \
        == ([0, 0, 0, 0], [0, -1, -1, 0], 2, 0, 0, ['l', 'r'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, -1, 3, 3, ['r', 'r']) \
        == ([0, 0, 0, 0], [0, -1, -1, 0], 2, 0, 0, ['r', 'r'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, -1, 3, 3, ['r', 'l']) \
        == ([0, 0, 0, 0], [0, 1, 1, 0], 2, 0, 3, ['r', 'l'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, 3, 3, 3, ['l', 'l']) \
        == ([0, 0, 0, 0], [0, 1, 1, 0], 2, 0, 3, ['l', 'l'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, -1, 6, 3, ['r', 'l']) \
        == ([0, 0, 0, 0], [0, 1, 1, 0], 2, 0, 0, ['r', 'l'])

    assert modify_pos([0, 0, 0, 0], [0, 0, 0, 0], 1, -1, -4, 3, ['r', 'l']) \
        == ([0, 1, 1, 0], [0, 0, 0, 0], 2, 3, 0, ['r', 'l'])


def test_arg_decode():
    """Tests input arguments."""
    assert arg_decode([]) == -1
    assert arg_decode(['dragon.py']) == (9, 'r', 'k')
    assert arg_decode(['dragon.py', 5, 'y']) == (5, 'y', 'k')
    assert arg_decode(['dragon.py', 5, 'y', 'b']) == (5, 'y', 'b')


# Problem with QT libraries linking with cloud VM
# works on local machine or VM


# def test_main():
# """Tests main function."""
# assert main(['dragon.py', 5, 'k', 'w']) == 0


# def test_init():
# """Tests init function."""
# import sys
# sys.argv = ['dragon.py', 9]
# assert rp.run_module('dragon', run_name='__main__')
