"""Include files."""
from dragon import move_left, move_right, generate_dragon  # , main
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
